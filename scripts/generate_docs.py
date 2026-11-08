#!/usr/bin/env python3
"""
generate_docs.py — Discover Unreal Engine plugins & modules, generate AI-written
Markdown introductions, and write them to the gh-pages docs tree.

Workflow
--------
1. Walk <engine-root>/Engine/Plugins for *.uplugin files. For each, parse the JSON
   and read the "Description" field (the kind of description that looks like
   "Suite of tools to profile, debug, and monitor aspects of audio in the
   Unreal Engine.").
2. Walk <engine-root>/Engine/Source for *.Build.cs files. Parse the file for the
   class name, parent class, ModuleType, and Public/PrivateDependencyModuleNames.
3. For every item, slugify its name and check whether
       <docs-root>/plugins/<slug>.md  or  <docs-root>/modules/<slug>.md
   already exists. If it does (and --force is not set, and it does not contain
   the "AI generation failed" marker), it is skipped — i.e. things previously
   written to gh-pages are NOT regenerated.
4. For new (or failed) items, call GitHub Models
   (https://models.github.ai/inference/chat/completions) using GH_TOKEN to
   expand the description into a Markdown intro.
5. Always (re)write <docs-root>/index.md listing every discovered item.

Exit code is 0 even when the AI call fails: the placeholder doc is written and
will be retried on the next daily run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from inject_usage import load_ai_usage, usage_card_html

AI_USAGE = load_ai_usage()

DEFAULT_MODEL = "openai/gpt-4o-mini"
AI_URL = "https://models.github.ai/inference/chat/completions"
# How many AI calls to run in parallel. Keeps a ~1800-item first run within
# GitHub Actions' 6h ceiling while staying well under GitHub Models' rate limits.
DEFAULT_WORKERS = 8

# Example description used to anchor the AI on the expected style.
EXAMPLE_DESCRIPTION = (
    "Suite of tools to profile, debug, and monitor aspects of audio "
    "in the Unreal Engine."
)

FAILURE_MARKER = "<!-- ai-generation-failed -->"

# Translate endpoint (free Google Translate client endpoint, no API key needed).
TRANSLATE_URL = "https://translate.googleapis.com/translate_a/single"


def translate_text(text: str, target_lang: str = "zh-CN",
                   source_lang: str = "auto") -> str:
    """Translate text using Google's free translate endpoint.

    Returns the translated string, or the original text if translation fails.
    """
    if not text or not text.strip():
        return text
    params = (
        f"client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q="
        f"{urllib.parse.quote(text)}"
    )
    url = f"{TRANSLATE_URL}?{params}"
    req = urllib.request.Request(url, headers={
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:  # noqa: S310
            data = json.loads(r.read().decode("utf-8"))
            # data[0] is a list of [translated, original] sentence pairs.
            translated = "".join(sentence[0] for sentence in data[0] if sentence[0])
            return translated.strip()
    except Exception as e:  # noqa: BLE001
        log(f"  ! translation failed: {e}")
        return text

# Strip trailing commas UE emits inside JSON arrays/objects (e.g. `["A", ]`).
TRAILING_COMMA_RE = re.compile(r",\s*([}\]])")


def parse_lenient_json(text: str) -> dict:
    """Parse UE's .uplugin JSON which may have a UTF-8 BOM and trailing commas."""
    # utf-8-sig transparently drops a leading BOM if present.
    cleaned = text.encode("utf-8", "replace").decode("utf-8-sig", "replace")
    cleaned = TRAILING_COMMA_RE.sub(r"\1", cleaned)
    return json.loads(cleaned)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def slugify(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9._-]+", "-", name.strip()).strip("-").lower()
    return s or "unknown"


def assign_slugs(items: list[dict], name_key: str, path_key: str) -> dict:
    """Return {item_index: unique_slug}.

    When two items share the same base slug (e.g. two plugins both called
    "Editor Telemetry"), append a short hash of the item's path to the
    colliding ones so each gets its own doc file.
    """
    base = {i: slugify(it[name_key]) for i, it in enumerate(items)}
    counts: dict[str, int] = {}
    for s in base.values():
        counts[s] = counts.get(s, 0) + 1
    out: dict[int, str] = {}
    for i, s in base.items():
        if counts[s] > 1:
            # Deterministic short hash so the same plugin always maps to the
            # same slug across runs (PYTHONHASHSEED would break that).
            h = hashlib.sha1(items[i][path_key].encode("utf-8")).hexdigest()[:6]
            out[i] = f"{s}-{h}"
        else:
            out[i] = s
    return out


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #
def discover_uplugins(plugins_root: Path) -> list[dict]:
    if not plugins_root.is_dir():
        return []
    out: list[dict] = []
    for path in sorted(plugins_root.rglob("*.uplugin")):
        try:
            data = parse_lenient_json(path.read_text(encoding="utf-8", errors="replace"))
        except Exception as e:  # noqa: BLE001
            log(f"  ! could not parse {path}: {e}")
            continue
        out.append({
            "path": str(path.relative_to(plugins_root.parents[1]))
                        if len(plugins_root.parents) >= 2 else str(path),
            "name": (data.get("FriendlyName") or path.stem).strip(),
            "description": (data.get("Description") or "").strip(),
            "version": data.get("VersionName", ""),
            "category": data.get("Category", ""),
            "created_by": data.get("CreatedBy", ""),
            "engine_version": data.get("EngineVersion", ""),
            "modules": [m.get("Name") for m in data.get("Modules", []) if m.get("Name")],
        })
    return out


CLASS_RE = re.compile(
    # Matches `class Foo : ModuleRules` and `class Foo : public ModuleRules`
    r"\bclass\s+([A-Za-z0-9_]+)\s*(?::\s*(?:public\s+)?([A-Za-z0-9_]+))?",
    re.MULTILINE,
)
TYPE_RE = re.compile(r"\bType\s*=\s*ModuleType\.([A-Za-z0-9_]+)")
# AddRange(new string[] { "A", "B" })  or  AddRange(new[] { "A", "B" })
DEPS_ADDRANGE_RE = re.compile(
    r"(?:Public|Private)(?:DependencyModuleNames|IncludePaths)\.AddRange\s*\(\s*new\s*(?:string)?\[\]\s*\{([^}]*)\}",
    re.MULTILINE,
)
DEPS_ADD_RE = re.compile(
    r'(?:Public|Private)DependencyModuleNames\.Add\s*\(\s*"([A-Za-z0-9_]+)"'
)


def parse_build_cs(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    cls_match = CLASS_RE.search(text)
    type_match = TYPE_RE.search(text)
    deps: set[str] = set()
    for m in DEPS_ADDRANGE_RE.finditer(text):
        for d in re.findall(r'"([A-Za-z0-9_]+)"', m.group(1)):
            deps.add(d)
    for m in DEPS_ADD_RE.finditer(text):
        deps.add(m.group(1))
    return {
        "path": str(path),
        "class": cls_match.group(1) if cls_match else path.stem,
        "base": cls_match.group(2) if cls_match else "ModuleRules",
        "module_type": type_match.group(1) if type_match else "",
        "deps": sorted(deps),
        "snippet": text[:1500],
    }


def discover_build_cs(source_root: Path) -> list[dict]:
    if not source_root.is_dir():
        return []
    out: list[dict] = []
    for path in sorted(source_root.rglob("*.Build.cs")):
        info = parse_build_cs(path)
        info["rel"] = str(path.relative_to(source_root.parents[1]))
        out.append(info)
    return out


# --------------------------------------------------------------------------- #
# AI
# --------------------------------------------------------------------------- #
def call_ai(prompt: str, model: str, token: str, endpoint: str = AI_URL) -> str:
    if not token:
        log("  ! no GH_TOKEN set; skipping AI call")
        return ""
    body = json.dumps({
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a technical writer documenting Unreal Engine internals. "
                    "Write accurate, concise Markdown. Do not invent specific APIs, "
                    "class names, or file paths you are not confident about; keep "
                    "claims general when unsure. Output only the body of the "
                    "documentation — no wrapping code fences, no leading title."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,
        "max_tokens": 700,
    }).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as r:  # noqa: S310
            data = json.loads(r.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"].strip()
    except urllib.error.HTTPError as e:
        log(f"  ! AI HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:300]}")
    except Exception as e:  # noqa: BLE001
        log(f"  ! AI error: {e}")
    return ""


def _build_plugin_prompt(p: dict) -> str:
    return (
        "Write a 3–5 paragraph technical introduction for an Unreal Engine "
        "plugin, suitable for a developer reference site.\n\n"
        f"Plugin (FriendlyName): {p['name']}\n"
        f"Plugin file path:      {p['path']}\n"
        f"Category:              {p['category'] or '(unspecified)'}\n"
        f"Modules it contains:   "
        f"{', '.join(p['modules']) if p['modules'] else '(unknown)'}\n"
        f"Author description:    {p['description'] or '(none provided)'}\n\n"
        "For style reference, here is an example of a real author-written "
        "plugin Description (from the AudioInsights plugin):\n"
        f'    "{EXAMPLE_DESCRIPTION}"\n\n'
        "Expand on what this plugin likely does, how it fits into the wider "
        "Unreal Engine ecosystem, and any notable modules or workflows. "
        "Do not invent specific C++ APIs, class names, or file paths you are "
        "not certain about; keep claims general when uncertain."
    )


def _build_module_prompt(m: dict) -> str:
    return (
        "Write a 2–4 paragraph technical introduction for an Unreal Engine "
        "C++ build module (a *.Build.cs file), suitable for a developer "
        "reference site.\n\n"
        f"Module file:     {m['rel']}\n"
        f"Rules class:     {m['class']} (extends {m['base']})\n"
        f"Module type:     {m['module_type'] or '(unspecified)'}\n"
        f"Dependencies:    {', '.join(m['deps']) if m['deps'] else '(none)'}\n\n"
        "Below is the beginning of the Build.cs file for context:\n"
        "```\n" + m["snippet"] + "\n```\n\n"
        "Explain what this module likely provides, its role within the "
        "engine, and how its declared dependencies hint at its "
        "responsibilities. Do not invent specific C++ APIs, class names, "
        "or file paths you are not certain about; keep claims general when "
        "uncertain."
    )


def generate_concurrently(tasks: list[tuple[Path, dict, str, str]],
                          model: str, token: str, endpoint: str,
                          workers: int, writer: callable,
                          use_ai: bool = True, translate: bool = False) -> int:
    """Run AI calls in parallel and write each doc as it completes.

    `tasks` is a list of (doc_path, info, prompt, label) tuples. Returns the
    number of docs actually written.
    """
    written = 0
    if not tasks:
        return 0
    if not use_ai:
        for doc_path, info, prompt, label in tasks:
            writer(doc_path, info, "", use_ai=False, translate=translate)
            written += 1
            log(f"  + {label}")
        return written
    if not token or workers <= 1:
        for doc_path, info, prompt, label in tasks:
            body = call_ai(prompt, model, token, endpoint)
            writer(doc_path, info, body, translate=translate)
            written += 1
            log(f"  + {label}")
        return written

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(call_ai, prompt, model, token, endpoint): (doc_path, info, label)
            for doc_path, info, prompt, label in tasks
        }
        for fut in as_completed(futures):
            doc_path, info, label = futures[fut]
            try:
                body = fut.result()
            except Exception as e:  # noqa: BLE001
                log(f"  ! {label} failed: {e}")
                body = ""
            writer(doc_path, info, body, translate=translate)
            written += 1
            log(f"  + {label}")
    return written


# --------------------------------------------------------------------------- #
# Doc writers
# --------------------------------------------------------------------------- #
def write_plugin_doc(doc_path: Path, info: dict, body: str,
                     use_ai: bool = True, translate: bool = False) -> None:
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    if not use_ai:
        body = info["description"] or "_(no Description field was provided in the .uplugin file)_"
        failure = ""
    elif not body:
        body = "_AI generation unavailable for this run; it will be retried next day._"
        failure = FAILURE_MARKER + "\n"
    else:
        failure = ""

    name_zh = translate_text(info["name"]) if translate else ""
    desc = info["description"] or "(no description)"
    desc_zh = translate_text(desc) if translate else ""
    body_zh = translate_text(body) if translate else ""
    category = info.get("category") or ""
    category_zh = translate_text(category) if translate and category else ""
    author = info.get("created_by") or ""
    author_zh = translate_text(author) if translate and author else ""
    version = info.get("version") or "—"
    engine = info.get("engine_version") or "—"
    rel_path = info.get("path", "")
    show_path = rel_path.replace("Engine/", "") if rel_path else "—"

    title = info["name"]
    title_attr = f"{name_zh} / {title}" if translate else title
    badge = (title[:1] or "U").upper()
    cn_sub = f"{name_zh} · {desc_zh[:32] if desc_zh else ''}" if translate else ""

    # --- Hero meta grid ---
    meta_html = (
        f'<div class="meta-grid">'
        f'<div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">{version}</div></div>'
        f'<div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">{engine}</div></div>'
        f'<div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">{author or "—"}</div></div>'
        f'<div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">{len(info.get("modules", []))}</div></div>'
        f'<div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">{show_path}</div></div>'
        f'</div>'
    )

    # --- Modules list for sidebar ---
    modules_html = ""
    if info.get("modules"):
        mod_items = []
        for m in info["modules"]:
            mod_items.append(
                f'<div class="module-item">'
                f'<span class="dot"></span>'
                f'<span class="name mono">{m}</span>'
                f'<span class="tag runtime">Runtime</span>'
                f'</div>'
            )
        modules_html = (
            f'<div class="sidebar-card">'
            f'<div class="sidebar-card-title">Modules ({len(info["modules"])})</div>'
            f'{"".join(mod_items)}'
            f'</div>'
        )

    # --- Description bilingual block ---
    if translate and desc_zh and desc_zh != desc:
        desc_html = (
            f'<div class="bilingual-block">'
            f'<div class="lang-tabs">'
            f'<button class="lang-tab active" onclick="switchLang(this)">中文</button>'
            f'<button class="lang-tab" onclick="switchLang(this)">English</button>'
            f"</div>"
            f'<div class="lang-content active">{desc_zh}</div>'
            f'<div class="lang-content">{desc}</div>'
            f"</div>"
        )
    else:
        desc_html = f"<p>{desc}</p>"

    # --- AI body bilingual block ---
    if body and use_ai:
        if translate and body_zh and body_zh != body:
            body_html = (
                f'<div class="bilingual-block">'
                f'<div class="lang-tabs">'
                f'<button class="lang-tab active" onclick="switchLang(this)">中文</button>'
                f'<button class="lang-tab" onclick="switchLang(this)">English</button>'
                f"</div>"
                f'<div class="lang-content active">{body_zh}</div>'
                f'<div class="lang-content">{body}</div>'
                f"</div>"
            )
        else:
            body_html = f'<div class="desc-body"><p>{body}</p></div>'
    else:
        body_html = ""

    cat_chip = (
        f'<span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>'
        f'{category or "Uncategorized"}</span>'
    )
    if author:
        cat_chip += f'<span class="chip">{author}</span>'

    usage_html = usage_card_html({
        "kind": "plugin",
        "name": info["name"],
        "desc_cn": desc_zh,
        "desc_en": desc,
        "category": category,
        "file_path": show_path,
        "modules": info.get("modules", []),
    }, AI_USAGE.get(("plugin", doc_path.stem)))

    html_content = f"""---
layout: default
title: {title_attr}
---

{failure}

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">{badge}</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">{title}</div>
      {f'<div class="hero-title-cn">{cn_sub}</div>' if cn_sub else ''}
      <div class="hero-tags">{cat_chip}</div>
    </div>
  </div>
  {meta_html}
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body">{desc_html}</div>
    </div>
{usage_html}
    {f'<div class="card"><div class="card-title"><span class="card-title-sep"></span>Notes<span class="card-title-cn">补充说明</span></div>{body_html}</div>' if body_html else ''}
  </div>
  <aside class="detail-sidebar">
    {modules_html}
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">{show_path}</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
"""
    doc_path.write_text(html_content, encoding="utf-8")


def write_module_doc(doc_path: Path, info: dict, body: str,
                     use_ai: bool = True, translate: bool = False) -> None:
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    if not use_ai:
        dep_text = (
            f"This module depends on {len(info['deps'])} other module(s): "
            f"{', '.join(info['deps'])}."
            if info["deps"]
            else "This module has no declared dependencies."
        )
        body = dep_text
        failure = ""
    elif not body:
        body = "_AI generation unavailable for this run; it will be retried next day._"
        failure = FAILURE_MARKER + "\n"
    else:
        failure = ""

    body_zh = translate_text(body) if translate else ""
    cls_name = info["class"]
    rel_path = info.get("rel", "")
    show_path = rel_path.replace("Engine/Source/", "") if rel_path else "—"
    mod_type = info.get("module_type") or "Module"
    deps = info.get("deps", [])
    badge = (cls_name[:1] or "M").upper()

    title_attr = cls_name

    usage_html = usage_card_html({
        "kind": "module",
        "name": cls_name,
        "desc_cn": body_zh,
        "desc_en": body,
        "category": mod_type,
        "file_path": show_path,
        "modules": deps,
    }, AI_USAGE.get(("module", doc_path.stem)))

    html_content = f"""---
layout: default
title: {title_attr}
---

{failure}

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>{badge}</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">{cls_name}</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>{mod_type}</span>
        <span class="chip">extends <span class="mono">{info.get("base") or "ModuleRules"}</span></span>
        <span class="chip">{len(deps)} dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">{mod_type}</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">{info.get("base") or "ModuleRules"}</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">{len(deps)}</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">{show_path}</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
{f'<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">{body_zh}</div><div class="lang-content">{body}</div></div>' if body and translate and body_zh and body_zh != body else f'<p>{body}</p>' if body else ''}
      </div>
    </div>
{usage_html}
  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies ({len(deps)})</div>
      {''.join(f'<div class="module-item"><span class="dot"></span><span class="name mono">{d}</span></div>' for d in deps) if deps else '<div style="font-size:12px;color:var(--on-surface-variant);">None declared.</div>'}
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">{show_path}</span>
      </div>
    </div>
  </aside>
</div>
"""
    doc_path.write_text(html_content, encoding="utf-8")


def needs_regenerate(doc_path: Path, force: bool, translate: bool = False) -> bool:
    """True if the doc at doc_path should be (re)generated."""
    if force:
        return True
    if not doc_path.exists():
        return True
    try:
        content = doc_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return True
    # Retry on previous AI failure.
    if FAILURE_MARKER in content:
        return True
    # If translation is enabled but the existing doc has no bilingual blocks,
    # regenerate it so the zh/en toggle has content to switch.
    if translate and "bilingual-block" not in content:
        return True
    return False


def update_index(docs_root: Path,
                 plugins: list[dict], plugin_slugs: dict[int, str],
                 modules: list[dict], module_slugs: dict[int, str]) -> None:
    """Write index page + Jekyll config + layout + CSS."""
    # --- Jekyll config ---
    (docs_root / "_config.yml").write_text(
        "title: Unreal Engine 插件与模块文档\n"
        "description: 虚幻引擎插件和模块的自动生成参考文档（中英文对照）\n"
        "baseurl: \n"
        "url: https://ue.veyvin.com\n"
        "include:\n"
        "  - assets/usage.bin\n"
        "  - assets/usage.fb\n",
        encoding="utf-8",
    )

    # --- default layout (hand-authored chrome; do not overwrite existing files) ---
    layout_dir = docs_root / "_layouts"
    layout_dir.mkdir(parents=True, exist_ok=True)
    chrome_root = Path(__file__).resolve().parents[1]

    def _copy_chrome(rel: str) -> None:
        src = chrome_root / rel
        dst = docs_root / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.exists() and src.resolve() != dst.resolve():
            shutil.copy2(src, dst)

    _copy_chrome("_layouts/default.html")
    _copy_chrome("assets/style.css")
    _copy_chrome("assets/main.js")
    _copy_chrome("assets/usage-fb.js")
    _copy_chrome("assets/usage-runtime.js")
    _copy_chrome("assets/usage.bin")
    _copy_chrome("assets/usage.fb")

    def _keep_chrome(_path):
        class _W:
            def write_text(self, *args, **kwargs):
                return None
        return _W()

    _keep_chrome(layout_dir / "default.html").write_text(
        "<!DOCTYPE html>\n"
        '<html lang="zh-CN" data-theme="light">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "  <title>{{ page.title | default: site.title }}</title>\n"
        '  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n'
        '  <link rel="stylesheet" href="{{ \'/assets/style.css\' | relative_url }}">\n'
        "</head>\n"
        "<body>\n"
        "  <div class=\"app\">\n"
        "    <!-- Sidebar -->\n"
        '    <aside class="sidebar" id="sidebar">\n'
        '      <div class="brand">\n'
        '        <div class="brand-logo">UE</div>\n'
        '        <div><div class="brand-text">UE Plugin Docs</div><div class="brand-sub">ue.veyvin.com</div></div>\n'
        '      </div>\n'
        '      <div class="nav-group-title">Browse 浏览</div>\n'
        '      <a class="nav-item" href="{{ \'/\' | relative_url }}">\n'
        '        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>\n'
        '        <span>Dashboard</span>\n'
        '      </a>\n'
        '      <a class="nav-item" href="{{ \'/\' | relative_url }}#plugins">\n'
        '        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>\n'
        '        <span>Plugins <span class="nav-count mono" id="navPlugins">—</span></span>\n'
        '      </a>\n'
        '      <a class="nav-item" href="{{ \'/\' | relative_url }}#modules">\n'
        '        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 7h-3V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v3H4a2 2 0 0 0-2 2v11a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"/></svg>\n'
        '        <span>Modules <span class="nav-count mono" id="navModules">—</span></span>\n'
        '      </a>\n'
        '      <div class="nav-group-title">Actions</div>\n'
        '      <button class="nav-btn lang-btn" onclick="toggleGlobalLang()" id="langSwitch">\n'
        '        <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>\n'
        '        <span><span id="langLabel">中文</span> / EN</span>\n'
        '      </button>\n'
        '      <div class="sidebar-footer">\n'
        '        <div class="sidebar-footer-title">Auto-generated</div>\n'
        '        <div style="display:flex;align-items:center;gap:8px;">\n'
        '          <span style="width:7px;height:7px;border-radius:50%;background:var(--success);display:inline-block;"></span>\n'
        '          <span class="sidebar-footer-val mono" style="font-size:13px;">Daily run active</span>\n'
        '        </div>\n'
        '        <div class="sidebar-footer-sub">Generated from Unreal Engine source</div>\n'
        '      </div>\n'
        "    </aside>\n"
        "\n"
        "    <!-- Main -->\n"
        "    <div class=\"main-wrap\">\n"
        '      <header class="site-topbar" id="topbar">\n'
        '        <button class="sidebar-toggle" id="sidebarToggle" aria-label="Toggle sidebar">\n'
        '          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>\n'
        '        </button>\n'
        '        <div class="topbar-title">{{ page.title | default: site.title }}</div>\n'
        '        <div class="search">\n'
        '          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--on-surface-variant)"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>\n'
        '          <input type="text" id="searchInput" placeholder="Search plugins or modules…" oninput="filterItems()">\n'
        '        </div>\n'
        '        <button class="icon-btn" onclick="toggleTheme()" aria-label="Theme">\n'
        '          <svg id="theme-sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>\n'
        '          <svg id="theme-moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none;"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>\n'
        '        </button>\n'
        "      </header>\n"
        '      <main class="main">\n'
        "        {{ content }}\n"
        "      </main>\n"
        "    </div>\n"
        "  </div>\n"
        "  <script src=\"{{ '/assets/main.js' | relative_url }}\"></script>\n"
        "</body>\n"
        "</html>\n",
        encoding="utf-8",
    )

    # --- Design tokens + layout CSS (FlClash-inspired) ---
    assets_dir = docs_root / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    style_css = f"""
:root {{
  /* Light — paper-warm surface system */
  --page: #F6F4EF;
  --surface: #F6F4EF;
  --surface-bright: #FFFFFF;
  --surface-container: #EFECE4;
  --surface-container-highest: #E6E3DA;

  /* UE-blue seed */
  --primary: #2F6FEB;
  --primary-on: #FFFFFF;
  --secondary: #5C6B7A;
  --tertiary: #8A6A40;

  --on-surface: #1C1B1A;
  --on-surface-variant: #5C5A55;
  --outline: #8C8A84;

  --success: #3E8B54;
  --warning: #C5872A;
  --error: #C0463A;

  --shadow-soft: 0 1px 2px rgba(28,27,26,0.04),
                 0 8px 24px rgba(28,27,26,0.06);

  --r-card: 28px;
  --r-card-sm: 20px;
  --r-chip: 14px;
  --r-pill: 999px;
  --r-icon: 16px;
}}

[data-theme="dark"] {{
  --page: #141415;
  --surface: #141415;
  --surface-bright: #1E1E20;
  --surface-container: #252528;
  --surface-container-highest: #2E2E31;

  --primary: #6E9FFF;
  --primary-on: #141415;
  --secondary: #B3BCC6;
  --tertiary: #E0C59F;

  --on-surface: #E6E1DA;
  --on-surface-variant: #A8A49D;
  --outline: #7B7872;

  --success: #7FC890;
  --warning: #E8B065;
  --error: #F28B82;

  --shadow-soft: 0 1px 2px rgba(0,0,0,0.30),
                 0 8px 24px rgba(0,0,0,0.40);
}}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}

body {{
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'SF Pro Display', system-ui, sans-serif;
  background: var(--page);
  color: var(--on-surface);
  -webkit-font-smoothing: antialiased;
  font-feature-settings: "ss01", "cv11";
  transition: background 300ms ease, color 300ms ease;
  min-height: 100vh;
  line-height: 1.7;
  font-size: 15px;
}}

.mono {{ font-family: 'JetBrains Mono', ui-monospace, monospace; font-feature-settings: "tnum"; }}

/* ============= App shell ============= */
.app {{ display: grid; grid-template-columns: 248px 1fr; min-height: 100vh; }}

/* ============= Sidebar ============= */
.sidebar {{
  background: var(--surface);
  border-right: 1px solid rgba(140,138,132,0.12);
  padding: 24px 16px;
  position: sticky; top: 0; height: 100vh;
  display: flex; flex-direction: column; gap: 4px;
  overflow-y: auto;
}}

.brand {{ display: flex; align-items: center; gap: 12px; padding: 4px 12px 24px; text-decoration: none; color: inherit; }}
.brand-logo {{
  width: 36px; height: 36px;
  background: var(--primary);
  border-radius: var(--r-icon);
  display: grid; place-items: center;
  color: var(--primary-on);
  font-weight: 700; font-size: 14px;
  box-shadow: var(--shadow-soft);
  flex-shrink: 0;
}}
.brand-text {{ font-weight: 600; font-size: 15px; letter-spacing: -0.01em; }}
.brand-sub {{ font-size: 11px; color: var(--on-surface-variant); margin-top: 2px; }}

.nav-group-title {{
  font-size: 11px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--on-surface-variant);
  padding: 16px 12px 6px;
}}

.nav-item, .nav-btn {{
  display: flex; align-items: center; gap: 12px;
  height: 40px; padding: 0 12px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 14px; font-family: inherit;
  color: var(--on-surface);
  background: transparent; border: none;
  text-decoration: none;
  position: relative;
  transition: background 200ms ease, transform 150ms ease;
  text-align: left; width: 100%;
}}
.nav-item:hover, .nav-btn:hover {{ background: rgba(140,138,132,0.08); }}
.nav-item.active {{ background: rgba(47,111,235,0.10); color: var(--primary); font-weight: 500; }}
.nav-item.active::before {{
  content: ''; position: absolute; left: 4px; top: 12px; bottom: 12px;
  width: 3px; background: var(--primary); border-radius: 3px;
}}
.nav-icon {{ width: 20px; height: 20px; flex-shrink: 0; }}
.nav-count {{ margin-left: auto; font-size: 12px; color: var(--on-surface-variant); }}

.lang-btn {{ margin-top: 6px; }}
.lang-btn:hover {{ color: var(--primary); }}

.sidebar-footer {{ margin-top: auto; background: var(--surface-container); border-radius: var(--r-card-sm); padding: 14px 16px; }}
.sidebar-footer-title {{ font-size: 11px; font-weight: 600; color: var(--on-surface-variant); margin-bottom: 8px; letter-spacing: 0.06em; text-transform: uppercase; }}
.sidebar-footer-val {{ font-weight: 600; }}
.sidebar-footer-sub {{ font-size: 11px; color: var(--on-surface-variant); margin-top: 4px; }}

/* ============= Main ============= */
.main-wrap {{ display: flex; flex-direction: column; min-width: 0; }}

.site-topbar {{
  position: sticky; top: 0; z-index: 50;
  background: color-mix(in srgb, var(--page) 85%, transparent);
  backdrop-filter: saturate(180%) blur(16px);
  -webkit-backdrop-filter: saturate(180%) blur(16px);
  border-bottom: 1px solid rgba(140,138,132,0.10);
  padding: 14px 40px;
  display: flex; align-items: center; gap: 16px;
}}

.sidebar-toggle {{
  display: none;
  width: 40px; height: 40px;
  border-radius: var(--r-pill);
  background: var(--surface-container);
  border: none; cursor: pointer;
  color: var(--on-surface);
}}

.topbar-title {{
  font-size: 18px; font-weight: 600; letter-spacing: -0.015em;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  flex: 1; min-width: 0;
}}

.search {{
  flex: 1; max-width: 440px;
  height: 40px;
  background: var(--surface-bright);
  border-radius: var(--r-pill);
  display: flex; align-items: center; gap: 10px;
  padding: 0 16px;
  box-shadow: var(--shadow-soft);
  transition: box-shadow 200ms ease;
}}
.search:focus-within {{ box-shadow: 0 0 0 3px rgba(47,111,235,0.20), var(--shadow-soft); }}
.search input {{
  flex: 1; border: none; outline: none; background: transparent;
  font-size: 14px; color: var(--on-surface); font-family: inherit;
}}
.search input::placeholder {{ color: var(--on-surface-variant); }}

.icon-btn {{
  width: 40px; height: 40px;
  border-radius: var(--r-pill);
  background: var(--surface-bright);
  border: none; cursor: pointer;
  color: var(--on-surface);
  display: grid; place-items: center;
  box-shadow: var(--shadow-soft);
  transition: transform 150ms ease;
}}
.icon-btn:hover {{ transform: scale(1.04); }}

.main {{ padding: 32px 40px 80px; max-width: 1280px; width: 100%; margin: 0 auto; }}

/* ============= Page content ============= */
h1 {{ font-size: 34px; font-weight: 700; letter-spacing: -0.025em; margin-bottom: 8px; line-height: 1.2; }}
h2 {{ font-size: 22px; font-weight: 700; letter-spacing: -0.02em; margin: 40px 0 16px; padding-bottom: 10px; border-bottom: 1px solid rgba(140,138,132,0.12); }}
h3 {{ font-size: 16px; font-weight: 600; margin: 24px 0 10px; }}
p {{ margin-bottom: 16px; color: var(--on-surface); }}
a {{ color: var(--primary); text-decoration: none; transition: color 150ms ease; }}
a:hover {{ text-decoration: underline; }}
ul {{ margin-bottom: 16px; padding-left: 0; list-style: none; }}
ul li {{ margin-bottom: 6px; position: relative; padding-left: 18px; }}
ul li::before {{
  content: ''; position: absolute; left: 0; top: 9px;
  width: 6px; height: 6px; background: var(--primary); border-radius: 50%;
}}

code {{
  background: var(--surface-container);
  padding: 2px 7px; border-radius: 6px;
  font-size: 13px;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
}}
pre {{
  background: var(--surface-container);
  padding: 16px 20px; border-radius: var(--r-card-sm);
  overflow-x: auto; margin-bottom: 16px;
}}
pre code {{ background: none; padding: 0; font-size: 13px; }}

/* ============= Stat cards (index) ============= */
.stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 28px; }}
.stat-card {{
  background: var(--surface-bright);
  border-radius: var(--r-card);
  padding: 22px 24px;
  box-shadow: var(--shadow-soft);
  position: relative;
  overflow: hidden;
}}
.stat-card-accent-bar {{
  position: absolute; left: 0; top: 0; bottom: 0;
  width: 4px; background: var(--primary); border-radius: 4px 0 0 4px;
}}
.stat-card-label {{
  font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--on-surface-variant); margin-bottom: 8px;
}}
.stat-card-value {{
  font-size: 34px; font-weight: 700;
  letter-spacing: -0.03em; color: var(--on-surface); line-height: 1;
}}
.stat-card-sub {{ font-size: 12px; color: var(--on-surface-variant); margin-top: 6px; }}

/* ============= Filters ============= */
.filters {{ display: flex; align-items: center; gap: 12px; margin-bottom: 18px; flex-wrap: wrap; }}
.filters-spacer {{ flex: 1; }}

.segmented {{ display: inline-flex; background: var(--surface-container); border-radius: var(--r-pill); padding: 4px; gap: 2px; }}
.segmented button {{
  border: none; background: transparent;
  padding: 8px 18px; font-size: 13px; font-weight: 500;
  border-radius: var(--r-pill); cursor: pointer;
  color: var(--on-surface-variant); font-family: inherit;
  transition: background 200ms ease, color 200ms ease;
}}
.segmented button.active {{
  background: var(--surface-bright); color: var(--on-surface); box-shadow: var(--shadow-soft);
}}

/* ============= Plugin grid ============= */
.grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 16px;
}}
.grid.filter-hidden {{ display: none; }}

.plugin-card {{
  background: var(--surface-bright);
  border-radius: var(--r-card);
  padding: 22px 24px;
  box-shadow: var(--shadow-soft);
  cursor: pointer;
  transition: transform 200ms cubic-bezier(0.22, 1, 0.36, 1), box-shadow 200ms ease;
  position: relative;
  display: flex; flex-direction: column; gap: 14px;
  color: inherit; text-decoration: none;
}}
.plugin-card:hover {{
  transform: translateY(-2px);
  box-shadow: 0 1px 2px rgba(28,27,26,0.05), 0 14px 36px rgba(28,27,26,0.10);
}}

.plugin-head {{ display: flex; align-items: flex-start; gap: 14px; }}
.plugin-badge {{
  width: 46px; height: 46px;
  border-radius: var(--r-icon);
  background: var(--surface-container);
  flex-shrink: 0;
  display: grid; place-items: center;
  font-weight: 700; font-size: 16px;
  letter-spacing: -0.02em; color: var(--primary);
}}
.plugin-title-area {{ flex: 1; min-width: 0; }}
.plugin-name {{ font-size: 15px; font-weight: 600; letter-spacing: -0.01em; line-height: 1.3; }}
.plugin-desc {{
  font-size: 13px; color: var(--on-surface-variant); margin-top: 2px; line-height: 1.4;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
}}
.plugin-tags {{ display: flex; flex-wrap: wrap; gap: 6px; }}

.tag {{
  font-size: 11px; font-weight: 500;
  padding: 3px 10px; border-radius: var(--r-pill);
  background: var(--surface-container); color: var(--on-surface-variant);
}}
.tag-primary {{ background: rgba(47,111,235,0.12); color: var(--primary); }}
.tag-success {{ background: rgba(62,139,84,0.14); color: var(--success); }}
.tag-warning {{ background: rgba(197,135,42,0.14); color: var(--warning); }}

.plugin-foot {{
  display: flex; align-items: center; justify-content: space-between;
  padding-top: 12px; border-top: 1px solid rgba(140,138,132,0.12);
  font-size: 11px; color: var(--on-surface-variant);
}}
.plugin-foot .file {{
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  max-width: 240px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  font-size: 10px;
}}
.plugin-foot .ver {{
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-weight: 500; padding: 2px 10px;
  background: var(--surface-container); border-radius: var(--r-pill);
}}

/* ============= Detail Hero ============= */
.hero {{
  background: var(--surface-bright);
  border-radius: var(--r-card);
  box-shadow: var(--shadow-soft);
  padding: 32px 36px;
  margin-bottom: 24px;
  position: relative;
  overflow: hidden;
}}
.hero::before {{
  content: ''; position: absolute; top: -80px; right: -80px;
  width: 240px; height: 240px;
  background: radial-gradient(circle, rgba(47,111,235,0.14) 0%, transparent 70%);
  border-radius: 50%; pointer-events: none;
}}
.hero-top {{ display: flex; align-items: flex-start; gap: 24px; }}
.hero-badge {{
  width: 72px; height: 72px;
  border-radius: var(--r-icon);
  background: linear-gradient(135deg, #2F6FEB 0%, #5B8DF5 100%);
  display: grid; place-items: center;
  color: white; font-weight: 700; font-size: 28px; letter-spacing: -0.03em;
  flex-shrink: 0;
  box-shadow: 0 4px 16px rgba(47,111,235,0.25);
}}
.hero-info {{ flex: 1; min-width: 0; }}
.hero-subtitle {{
  font-size: 12px; font-weight: 500;
  color: var(--on-surface-variant); letter-spacing: 0.04em; text-transform: uppercase;
  margin-bottom: 4px;
}}
.hero-title {{ font-size: 28px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.25; }}
.hero-title-cn {{ font-size: 14px; font-weight: 400; color: var(--on-surface-variant); margin-top: 4px; margin-bottom: 14px; }}
.hero-tags {{ display: flex; flex-wrap: wrap; gap: 8px; }}

.chip {{
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 12px; font-weight: 500;
  padding: 5px 14px; border-radius: var(--r-pill);
  background: var(--surface-container); color: var(--on-surface-variant);
}}
.chip-primary {{ background: rgba(47,111,235,0.12); color: var(--primary); }}
.chip-success {{ background: rgba(62,139,84,0.14); color: var(--success); }}
.chip-warning {{ background: rgba(197,135,42,0.14); color: var(--warning); }}

.meta-grid {{
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;
  margin-top: 24px; padding-top: 20px;
  border-top: 1px solid rgba(140,138,132,0.12);
}}
.meta-item {{
  background: var(--surface-container);
  border-radius: var(--r-card-sm);
  padding: 12px 14px;
  grid-column: span 1;
}}
.meta-item.file-col {{ grid-column: span 4; }}
.meta-label {{
  font-size: 10px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.06em;
  color: var(--on-surface-variant); margin-bottom: 4px;
}}
.meta-value {{ font-size: 14px; font-weight: 500; color: var(--on-surface); word-break: break-all; }}

.file-path {{
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 12px; padding: 10px 14px;
  background: var(--surface-container-highest);
  border-radius: var(--r-card-sm);
  color: var(--on-surface);
  word-break: break-all; line-height: 1.55;
}}

/* ============= Content card (detail) ============= */
.content-grid {{ display: grid; grid-template-columns: 1fr 340px; gap: 24px; }}
.card {{
  background: var(--surface-bright);
  border-radius: var(--r-card);
  box-shadow: var(--shadow-soft);
  padding: 26px 30px;
  margin-bottom: 24px;
}}
.card-title {{
  font-size: 18px; font-weight: 700; letter-spacing: -0.015em;
  display: flex; align-items: baseline; gap: 10px;
  margin-bottom: 14px;
}}
.card-title-sep {{
  width: 3px; height: 18px; background: var(--primary); border-radius: 2px; flex-shrink: 0; margin-right: 4px;
}}
.card-title-cn {{ font-size: 13px; font-weight: 400; color: var(--on-surface-variant); }}

.desc-body p {{ margin-bottom: 14px; line-height: 1.75; }}
.desc-body p:last-child {{ margin-bottom: 0; }}

.usage-card .desc-body .bilingual-block {{ margin-bottom: 0; }}
.usage-steps {{ margin: 0; padding-left: 22px; }}
.usage-steps li {{ margin-bottom: 12px; line-height: 1.7; }}
.usage-steps li:last-child {{ margin-bottom: 0; }}
.usage-code {{
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 12.5px;
  background: var(--surface-container-highest);
  padding: 1px 7px;
  border-radius: 8px;
  color: var(--on-surface);
  word-break: break-all;
}}
.usage-note {{
  margin-top: 16px;
  font-size: 13px;
  color: var(--on-surface-variant);
  line-height: 1.6;
}}

.detail-sidebar {{ display: flex; flex-direction: column; gap: 16px; align-self: start; }}

.sidebar-card {{
  background: var(--surface-bright);
  border-radius: var(--r-card);
  box-shadow: var(--shadow-soft);
  padding: 20px 22px;
}}
.sidebar-card-title {{
  font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--on-surface-variant);
  margin-bottom: 14px;
  display: flex; align-items: center; gap: 8px;
}}

.module-item {{
  display: flex; align-items: center; gap: 12px;
  padding: 9px 12px; margin-bottom: 6px;
  background: var(--surface-container);
  border-radius: var(--r-card-sm);
  font-size: 13px;
}}
.module-item:last-child {{ margin-bottom: 0; }}
.module-item .dot {{ width: 7px; height: 7px; border-radius: 50%; background: var(--primary); flex-shrink: 0; }}
.module-item .name {{ flex: 1; font-family: 'JetBrains Mono', ui-monospace, monospace; font-weight: 500; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
.module-item .tag {{
  font-size: 10px; font-weight: 600; padding: 2px 8px;
  border-radius: var(--r-pill); background: var(--surface-bright); color: var(--on-surface-variant);
}}
.module-item .tag.runtime {{ color: var(--success); }}
.module-item .tag.editor {{ color: var(--warning); }}

/* ============= Bilingual ============= */
.bilingual-block {{
  background: var(--surface-container);
  border-radius: var(--r-card-sm);
  margin-bottom: 16px; overflow: hidden;
}}
.bilingual-block .lang-tabs {{
  display: flex;
  background: var(--surface-container-highest);
  border-bottom: 1px solid rgba(140,138,132,0.10);
}}
.bilingual-block .lang-tab {{
  padding: 8px 22px; cursor: pointer;
  font-size: 13px; color: var(--on-surface-variant);
  border: none; background: transparent; font-family: inherit;
  transition: color 150ms ease;
}}
.bilingual-block .lang-tab:hover {{ color: var(--on-surface); }}
.bilingual-block .lang-tab.active {{ color: var(--primary); font-weight: 600; position: relative; }}
.bilingual-block .lang-tab.active::after {{
  content: ''; position: absolute; bottom: 0; left: 18px; right: 18px;
  height: 2px; background: var(--primary); border-radius: 2px;
}}
.bilingual-block .lang-content {{ padding: 18px 22px; display: none; line-height: 1.7; font-size: 15px; color: var(--on-surface); }}
.bilingual-block .lang-content.active {{ display: block; }}

/* ============= Responsive ============= */
@media (max-width: 1100px) {{
  .app {{ grid-template-columns: 1fr; }}
  .sidebar {{ position: fixed; left: 0; top: 0; bottom: 0; z-index: 200; transform: translateX(-100%); transition: transform 250ms cubic-bezier(0.22, 1, 0.36, 1); }}
  .sidebar.open {{ transform: translateX(0); }}
  .sidebar-toggle {{ display: grid; }}
  .content-grid {{ grid-template-columns: 1fr; }}
  .stats {{ grid-template-columns: repeat(2, 1fr); }}
}}
@media (max-width: 720px) {{
  .site-topbar {{ padding: 12px 20px; }}
  .main {{ padding: 24px 20px 64px; }}
  .hero {{ padding: 24px 22px; }}
  .hero-top {{ flex-direction: column; }}
  .hero-badge {{ width: 56px; height: 56px; font-size: 22px; }}
  .hero-title {{ font-size: 24px; }}
  .meta-grid {{ grid-template-columns: 1fr 1fr; }}
  .meta-item.file-col {{ grid-column: span 2; }}
  .stats {{ grid-template-columns: 1fr 1fr; }}
  .stat-card-value {{ font-size: 28px; }}
  .grid {{ grid-template-columns: 1fr; }}
  .topbar-title {{ display: none; }}
  .card {{ padding: 20px; }}
}}

@media (prefers-reduced-motion: reduce) {{
  * {{ transition: none !important; animation: none !important; }}
}}
"""
    _keep_chrome(assets_dir / "style.css").write_text(style_css, encoding="utf-8")

    # --- JavaScript: theme, language, search, sidebar toggle ---
    main_js = """
// ===== Theme toggle (persists in localStorage) =====
(function() {
  var body = document.body;
  var stored = localStorage.getItem('ue-theme');
  var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  var initial = stored || (prefersDark ? 'dark' : 'light');
  body.setAttribute('data-theme', initial);

  function syncThemeIcons() {
    var suns = document.querySelectorAll('#theme-sun, #ft-sun');
    var moons = document.querySelectorAll('#theme-moon, #ft-moon');
    var isDark = body.getAttribute('data-theme') === 'dark';
    suns.forEach(function(el) { if (el) el.style.display = isDark ? 'none' : 'block'; });
    moons.forEach(function(el) { if (el) el.style.display = isDark ? 'block' : 'none'; });
  }
  syncThemeIcons();

  window.toggleTheme = function() {
    var isDark = body.getAttribute('data-theme') === 'dark';
    var next = isDark ? 'light' : 'dark';
    body.setAttribute('data-theme', next);
    localStorage.setItem('ue-theme', next);
    syncThemeIcons();
  };
})();

// ===== Bilingual toggle =====
function switchLang(tabEl) {
  var block = tabEl.closest('.bilingual-block');
  if (!block) return;
  var tabs = block.querySelectorAll('.lang-tab');
  var contents = block.querySelectorAll('.lang-content');
  var idx = Array.from(tabs).indexOf(tabEl);
  tabs.forEach(function(t, i) { t.classList.toggle('active', i === idx); });
  contents.forEach(function(c, i) { c.classList.toggle('active', i === idx); });
}

var currentLang = 0;
function toggleGlobalLang() {
  currentLang = currentLang === 0 ? 1 : 0;
  var label = document.getElementById('langLabel');
  if (label) label.textContent = currentLang === 0 ? '中文' : 'English';
  document.querySelectorAll('.bilingual-block').forEach(function(block) {
    var tabs = block.querySelectorAll('.lang-tab');
    var contents = block.querySelectorAll('.lang-content');
    tabs.forEach(function(t, i) { t.classList.toggle('active', i === currentLang); });
    contents.forEach(function(c, i) { c.classList.toggle('active', i === currentLang); });
  });
}

// ===== Search / filter =====
function filterItems() {
  var input = document.getElementById('searchInput');
  if (!input) return;
  var query = input.value.toLowerCase().trim();
  document.querySelectorAll('.grid').forEach(function(grid) {
    grid.querySelectorAll('.plugin-card').forEach(function(card) {
      var text = card.textContent.toLowerCase();
      card.style.display = (query === '' || text.indexOf(query) !== -1) ? '' : 'none';
    });
  });
  document.querySelectorAll('.plugin-list').forEach(function(list) {
    list.querySelectorAll('li').forEach(function(li) {
      var text = li.textContent.toLowerCase();
      li.style.display = (query === '' || text.indexOf(query) !== -1) ? '' : 'none';
    });
  });
}

// ===== Sidebar toggle (mobile) =====
(function() {
  var btn = document.getElementById('sidebarToggle');
  var sb = document.getElementById('sidebar');
  if (btn && sb) {
    btn.addEventListener('click', function() { sb.classList.toggle('open'); });
    document.addEventListener('click', function(e) {
      if (sb.classList.contains('open') && !sb.contains(e.target) && e.target !== btn) {
        sb.classList.remove('open');
      }
    });
  }
})();

// ===== Nav highlight (simple: match path) =====
(function() {
  var path = location.pathname;
  document.querySelectorAll('.nav-item').forEach(function(item) {
    var href = item.getAttribute('href');
    if (!href) return;
    if (href === './' && (path === '/' || path === '' || path.endsWith('/index.html'))) {
      item.classList.add('active');
    } else if (href !== './' && path.indexOf(href.replace('./', '/')) !== -1) {
      item.classList.add('active');
    }
  });
})();

window.switchLang = switchLang;
window.toggleGlobalLang = toggleGlobalLang;
window.filterItems = filterItems;
window.toggleTheme = window.toggleTheme || function() {};

document.addEventListener('DOMContentLoaded', function() { filterItems(); });
"""
    _keep_chrome(assets_dir / "main.js").write_text(main_js, encoding="utf-8")

    # --- Index page: stat cards + grid with filters (FlClash-inspired) ---
    # Category stats
    cat_counts: dict[str, int] = {}
    for p in plugins:
        c = (p.get("category") or "Uncategorized").strip()
        cat_counts[c] = cat_counts.get(c, 0) + 1
    categories_sorted = sorted(cat_counts.items(), key=lambda x: -x[1])

    # Plugin cards — badge, name, desc, category chip, version, filename
    plugin_cards = []
    order_p = sorted(range(len(plugins)), key=lambda i: plugins[i]["name"].lower())
    for i in order_p:
        slug = plugin_slugs[i]
        p = plugins[i]
        desc = (p.get("description") or "").strip()
        if len(desc) > 140:
            desc = desc[:137] + "…"
        badge = (p["name"][:1] or "U").upper()
        category = p.get("category") or ""
        version = p.get("version") or "—"
        rel_path = p.get("path", "")
        show_path = rel_path.replace("Engine/", "") if rel_path else "—"
        plugin_cards.append(
            f'<a class="plugin-card" href="plugins/{slug}.html" data-cat="{category}">'
            f'<div class="plugin-head">'
            f'<div class="plugin-badge">{badge}</div>'
            f'<div class="plugin-title-area">'
            f'<div class="plugin-name">{p["name"]}</div>'
            f'<div class="plugin-desc">{desc or "—"}</div>'
            f'</div></div>'
            f'<div class="plugin-tags">'
            f'<span class="tag tag-primary">{category or "Uncategorized"}</span>'
            f'</div>'
            f'<div class="plugin-foot">'
            f'<span class="file mono">{show_path}</span>'
            f'<span class="ver mono">{version}</span>'
            f'</div></a>'
        )

    # Module cards — same grid style
    module_cards = []
    order_m = sorted(range(len(modules)), key=lambda i: modules[i]["class"].lower())
    for i in order_m:
        slug = module_slugs[i]
        m = modules[i]
        badge = (m["class"][:1] or "M").upper()
        deps = m.get("deps", [])
        mod_type = m.get("module_type") or "Module"
        rel_path = m.get("rel", "")
        show_path = rel_path.replace("Engine/Source/", "") if rel_path else "—"
        module_cards.append(
            f'<a class="plugin-card" href="modules/{slug}.html">'
            f'<div class="plugin-head">'
            f'<div class="plugin-badge" style="background:rgba(138,92,246,0.12);color:#8A5CF6;">{badge}</div>'
            f'<div class="plugin-title-area">'
            f'<div class="plugin-name mono">{m["class"]}</div>'
            f'<div class="plugin-desc">{len(deps)} dependencies · {mod_type}</div>'
            f'</div></div>'
            f'<div class="plugin-foot">'
            f'<span class="file mono">{show_path}</span>'
            f'<span class="ver mono">{mod_type}</span>'
            f'</div></a>'
        )

    # Category filter chips (top 8 + "其他")
    cat_filters_html = ''.join(
        f'<button class="chip-filter" data-cat="{c}"><span class="dot"></span>{c} <span style="opacity:.65;">({n})</span></button>'
        for c, n in categories_sorted[:8]
    )

    top_cats = categories_sorted[0][0] if categories_sorted else "Plugins"

    index_html = f"""---
layout: default
title: Unreal Engine Plugin Docs / 插件与模块
---

<div class="page-title-wrap">
  <p class="page-kicker">Unreal Engine · Source catalog</p>
  <h1>插件与模块</h1>
  <p class="page-lede">从引擎源码同步的 <span class="mono">{len(plugins)}</span> 个插件 · <span class="mono">{len(modules)}</span> 个模块，按路径与类别检索。</p>
</div>

<!-- Stat cards row (4 columns) -->
<div class="stats">
  <div class="stat-card plugins">
    <div class="stat-card-accent-bar"></div>
    <div class="stat-card-label">Plugins / 插件</div>
    <div class="stat-card-value mono">{len(plugins):,}</div>
    <div class="stat-card-sub">{min(len(categories_sorted), 22)} categories · Top: {top_cats}</div>
  </div>
  <div class="stat-card modules">
    <div class="stat-card-accent-bar" style="background:#8A5CF6;"></div>
    <div class="stat-card-label">Modules / 模块</div>
    <div class="stat-card-value mono">{len(modules):,}</div>
    <div class="stat-card-sub">Build rules · C++</div>
  </div>
  <div class="stat-card categories">
    <div class="stat-card-accent-bar" style="background:#3E8B54;"></div>
    <div class="stat-card-label">Categories / 分类</div>
    <div class="stat-card-value mono">{len(categories_sorted)}</div>
    <div class="stat-card-sub">Rendering · VFX · Animation…</div>
  </div>
  <div class="stat-card engine">
    <div class="stat-card-accent-bar" style="background:#C5872A;"></div>
    <div class="stat-card-label">Engine</div>
    <div class="stat-card-value mono" style="font-size:22px;">UE nightly</div>
    <div class="stat-card-sub">Auto-synced daily</div>
  </div>
</div>

<!-- Plugins section -->
<h2 id="plugins" style="font-size:22px;margin-top:36px;">Plugins / 插件</h2>
<div class="filters">
  <div class="segmented">
    <button class="active" onclick="switchGridFilter(this, 'plugins')">All</button>
    <button onclick="switchGridFilter(this, 'plugins-rendering')">Rendering</button>
    <button onclick="switchGridFilter(this, 'plugins-vfx')">FX</button>
    <button onclick="switchGridFilter(this, 'plugins-anim')">Animation</button>
    <button onclick="switchGridFilter(this, 'plugins-vp')">Virtual Production</button>
  </div>
  <div class="filters-spacer"></div>
</div>
<div id="grid-plugins" class="grid">
{''.join(plugin_cards)}
</div>

<!-- Modules section -->
<h2 id="modules" style="font-size:22px;margin-top:48px;">Modules / 模块</h2>
<p style="color:var(--on-surface-variant);font-size:13px;margin:-4px 0 16px;">C++ Build rules discovered from <span class="mono">Engine/Source/**/*.Build.cs</span></p>
<div id="grid-modules" class="grid">
{''.join(module_cards)}
</div>

<script>
// Grid filter by category (simple: show/hide by data-cat attribute)
function switchGridFilter(btn, group) {{
  document.querySelectorAll('.segmented').forEach(function(seg) {{
    if (seg === btn.parentElement) {{
      seg.querySelectorAll('button').forEach(function(b) {{ b.classList.remove('active'); }});
      btn.classList.add('active');
    }}
  }});
  var grid = document.getElementById('grid-' + group.split('-')[0]);
  if (!grid) return;
  var targetCat = btn.getAttribute('data-cat');
  grid.querySelectorAll('.plugin-card').forEach(function(card) {{
    if (group === 'plugins' || group.startsWith('plugins-')) {{
      var cat = card.getAttribute('data-cat') || '';
      if (btn.textContent === 'All' || card.id === '__dummy__') {{ card.style.display = ''; return; }}
      // Map simplified group -> UE category substrings
      var show = false;
      if (group === 'plugins-rendering') show = cat.toLowerCase().indexOf('render') !== -1;
      else if (group === 'plugins-vfx') show = cat.toLowerCase().indexOf('fx') !== -1 || cat.toLowerCase().indexOf('vfx') !== -1;
      else if (group === 'plugins-anim') show = cat.toLowerCase().indexOf('anim') !== -1;
      else if (group === 'plugins-vp') show = cat.toLowerCase().indexOf('virtual') !== -1 || cat.toLowerCase().indexOf('production') !== -1;
      else show = true;
      card.style.display = show ? '' : 'none';
    }}
  }});
}}
// Make switchGridFilter globally accessible
window.switchGridFilter = switchGridFilter;
</script>
"""
    (docs_root / "index.md").write_text(index_html, encoding="utf-8")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--engine-root", default=".", help="Repo root containing Engine/")
    ap.add_argument("--docs-root", default="docs", help="gh-pages docs output dir")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="GitHub Models model id")
    ap.add_argument(
        "--force",
        default="false",
        help="Regenerate every doc even if it already exists (true/false).",
    )
    ap.add_argument(
        "--workers",
        type=int,
        default=DEFAULT_WORKERS,
        help="Number of parallel AI calls (default: %(default)s).",
    )
    ap.add_argument(
        "--no-ai",
        action="store_true",
        help="Skip AI generation entirely; write docs with descriptions only.",
    )
    ap.add_argument(
        "--translate",
        action="store_true",
        help="Translate descriptions to Chinese (bilingual display).",
    )
    args = ap.parse_args()

    engine_root = Path(args.engine_root).resolve()
    docs_root = Path(args.docs_root).resolve()
    docs_root.mkdir(parents=True, exist_ok=True)
    (docs_root / "plugins").mkdir(parents=True, exist_ok=True)
    (docs_root / "modules").mkdir(parents=True, exist_ok=True)

    force = str(args.force).lower() in ("1", "true", "yes", "on")
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""
    endpoint = os.environ.get("AI_ENDPOINT") or AI_URL

    plugins_root = engine_root / "Engine" / "Plugins"
    source_root = engine_root / "Engine" / "Source"

    plugins = discover_uplugins(plugins_root)
    modules = discover_build_cs(source_root)
    log(f"Discovered {len(plugins)} plugins, {len(modules)} modules")

    plugin_slugs = assign_slugs(plugins, "name", "path")
    module_slugs = assign_slugs(modules, "class", "rel")

    plugin_tasks: list[tuple[Path, dict, str, str]] = []
    for i, p in enumerate(plugins):
        slug = plugin_slugs[i]
        doc_path = docs_root / "plugins" / f"{slug}.md"
        if not needs_regenerate(doc_path, force, args.translate):
            continue
        plugin_tasks.append((doc_path, p, _build_plugin_prompt(p), f"plugin: {slug}"))
    log(f"Plugin docs to (re)generate: {len(plugin_tasks)}")

    module_tasks: list[tuple[Path, dict, str, str]] = []
    for i, m in enumerate(modules):
        slug = module_slugs[i]
        doc_path = docs_root / "modules" / f"{slug}.md"
        if not needs_regenerate(doc_path, force, args.translate):
            continue
        module_tasks.append((doc_path, m, _build_module_prompt(m), f"module: {slug}"))
    log(f"Module docs to (re)generate: {len(module_tasks)}")

    use_ai = not args.no_ai
    if use_ai:
        log(f"AI generation enabled (model: {args.model}, workers: {args.workers})")
    else:
        log("AI generation disabled — writing docs with descriptions only")

    do_translate = args.translate
    if do_translate:
        log("Translation enabled — generating bilingual (zh-CN + en) content")

    new_plugins = generate_concurrently(
        plugin_tasks, args.model, token, endpoint, args.workers, write_plugin_doc,
        use_ai=use_ai, translate=do_translate,
    )
    new_modules = generate_concurrently(
        module_tasks, args.model, token, endpoint, args.workers, write_module_doc,
        use_ai=use_ai, translate=do_translate,
    )

    update_index(docs_root, plugins, plugin_slugs, modules, module_slugs)
    log(f"Done. {new_plugins} new/updated plugin docs, "
        f"{new_modules} new/updated module docs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
