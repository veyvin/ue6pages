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
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

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

    # --- Translate key fields if requested ---
    name_zh = translate_text(info["name"]) if translate else ""
    desc = info["description"] or "(no description)"
    desc_zh = translate_text(desc) if translate else ""
    body_zh = translate_text(body) if translate else ""
    category_zh = translate_text(info["category"]) if translate and info.get("category") else ""
    author_zh = translate_text(info["created_by"]) if translate and info.get("created_by") else ""

    def field_html(label: str, value: str, value_zh: str = "") -> str:
        if not value:
            return ""
        if translate and value_zh and value_zh != value:
            val_html = (
                f'<div class="bilingual-block">'
                f'<div class="lang-tabs">'
                f'<div class="lang-tab active" onclick="switchLang(this)">中文</div>'
                f'<div class="lang-tab" onclick="switchLang(this)">English</div>'
                f"</div>"
                f'<div class="lang-content active">{value_zh}</div>'
                f'<div class="lang-content">{value}</div>'
                f"</div>"
            )
        else:
            val_html = value
        return (
            f'<li><span class="label">{label}</span>'
            f'<span class="value">{val_html}</span></li>'
        )

    # Build info card fields
    info_items = [
        field_html("插件文件", f"<code>{info['path']}</code>"),
        field_html("版本", info.get("version", "")) if info.get("version") else "",
        field_html("类别", info.get("category", ""), category_zh) if info.get("category") else "",
        field_html("作者", info.get("created_by", ""), author_zh) if info.get("created_by") else "",
        field_html("引擎版本", info.get("engine_version", "")) if info.get("engine_version") else "",
        field_html("模块", ", ".join(info["modules"])) if info.get("modules") else "",
    ]
    info_items = [i for i in info_items if i]

    # Description bilingual block
    if translate and desc_zh and desc_zh != desc:
        desc_html = (
            f'<div class="bilingual-block">'
            f'<div class="lang-tabs">'
            f'<div class="lang-tab active" onclick="switchLang(this)">中文</div>'
            f'<div class="lang-tab" onclick="switchLang(this)">English</div>'
            f"</div>"
            f'<div class="lang-content active">{desc_zh}</div>'
            f'<div class="lang-content">{desc}</div>'
            f"</div>"
        )
    else:
        desc_html = f"<p>{desc}</p>"

    title = f"{info['name']}" if not translate else f"{name_zh} / {info['name']}"

    html_content = f"""---
layout: default
title: {title}
---

{failure}
<h1>{title}</h1>

<div class="info-card">
  <ul>
    {"".join(info_items)}
  </ul>
</div>

<h2>Description / 描述</h2>
{desc_html}
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

    def field_html(label: str, value: str) -> str:
        if not value:
            return ""
        return (
            f'<li><span class="label">{label}</span>'
            f'<span class="value">{value}</span></li>'
        )

    info_items = [
        field_html("文件", f"<code>{info['rel']}</code>"),
        field_html("基类", f"<code>{info['base']}</code>"),
        field_html("模块类型", f"<code>{info['module_type']}</code>") if info.get("module_type") else "",
        field_html("依赖", ", ".join(info["deps"])) if info.get("deps") else "",
    ]
    info_items = [i for i in info_items if i]

    html_content = f"""---
layout: default
title: {info['class']}
---

{failure}
<h1>{info['class']}</h1>

<div class="info-card">
  <ul>
    {"".join(info_items)}
  </ul>
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
        "url: https://ue.veyvin.com\n",
        encoding="utf-8",
    )

    # --- default layout ---
    layout_dir = docs_root / "_layouts"
    layout_dir.mkdir(parents=True, exist_ok=True)
    (layout_dir / "default.html").write_text(
        "<!DOCTYPE html>\n"
        '<html lang="zh-CN">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "  <title>{{ page.title | default: site.title }}</title>\n"
        '  <link rel="stylesheet" href="{{ \'/assets/style.css\' | relative_url }}">\n'
        "</head>\n"
        "<body>\n"
        '  <header class="site-header">\n'
        '    <div class="container">\n'
        '      <a class="site-title" href="{{ \'/\' | relative_url }}">\n'
        "        UE 插件与模块文档\n"
        "      </a>\n"
        '      <div class="header-right">\n'
        '        <div class="search-box">\n'
        '          <input type="text" id="searchInput" placeholder="搜索插件或模块..." oninput="filterItems()">\n'
        '          <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n'
        '            <circle cx="11" cy="11" r="8"></circle>\n'
        '            <path d="m21 21-4.35-4.35"></path>\n'
        '          </svg>\n'
        '        </div>\n'
        '        <nav class="site-nav">\n'
        '          <a href="{{ \'/\' | relative_url }}#plugins">插件</a>\n'
        '          <a href="{{ \'/\' | relative_url }}#modules">模块</a>\n'
        '        </nav>\n'
        '        <button class="lang-switch" onclick="toggleGlobalLang()" id="langSwitch">\n'
        '          中文\n'
        '        </button>\n'
        "      </div>\n"
        "    </div>\n"
        "  </header>\n"
        '  <main class="container">\n'
        "    {{ content }}\n"
        "  </main>\n"
        '  <footer class="site-footer">\n'
        '    <div class="container">\n'
        "      <p>Auto-generated daily from Unreal Engine source</p>\n"
        "    </div>\n"
        "  </footer>\n"
        '  <script src="{{ \'/assets/main.js\' | relative_url }}"></script>\n'
        "</body>\n"
        "</html>\n",
        encoding="utf-8",
    )

    # --- Modern CSS ---
    assets_dir = docs_root / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    (assets_dir / "style.css").write_text(
        ":root{\n"
        "  --bg:#0d1117;\n"
        "  --surface:#161b22;\n"
        "  --surface-2:#21262d;\n"
        "  --border:#30363d;\n"
        "  --text:#e6edf3;\n"
        "  --text-muted:#8b949e;\n"
        "  --accent:#58a6ff;\n"
        "  --accent-hover:#79b8ff;\n"
        "  --success:#3fb950;\n"
        "  --warning:#d29922;\n"
        "  --radius:12px;\n"
        "  --shadow:0 4px 24px rgba(0,0,0,.3);\n"
        "}\n"
        "*{box-sizing:border-box;margin:0;padding:0}\n"
        "html{scroll-behavior:smooth}\n"
        "body{\n"
        "  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif,'Apple Color Emoji','Segoe UI Emoji';\n"
        "  background:var(--bg);\n"
        "  color:var(--text);\n"
        "  line-height:1.7;\n"
        "  font-size:15px;\n"
        "}\n"
        ".container{max-width:960px;margin:0 auto;padding:0 24px}\n"
        "\n"
        "/* Header */\n"
        ".site-header{\n"
        "  border-bottom:1px solid var(--border);\n"
        "  position:sticky;top:0;z-index:100;\n"
        "  backdrop-filter:blur(12px);\n"
        "  background:rgba(22,27,34,.85);\n"
        "}\n"
        ".site-header .container{\n"
        "  display:flex;align-items:center;justify-content:space-between;\n"
        "  height:60px;\n"
        "}\n"
        ".site-title{\n"
        "  font-size:18px;font-weight:700;color:var(--text);\n"
        "  text-decoration:none;\n"
        "}\n"
        ".site-nav a{\n"
        "  color:var(--text-muted);text-decoration:none;\n"
        "  margin-left:24px;font-size:14px;\n"
        "  transition:color .2s;\n"
        "}\n"
        ".site-nav a:hover{color:var(--accent)}\n"
        "\n"
        ".header-right{\n"
        "  display:flex;align-items:center;gap:16px;\n"
        "}\n"
        "\n"
        ".search-box{\n"
        "  position:relative;\n"
        "  flex-shrink:0;\n"
        "}\n"
        ".search-box input{\n"
        "  width:200px;\n"
        "  padding:8px 12px 8px 36px;\n"
        "  background:var(--surface-2);\n"
        "  border:1px solid var(--border);\n"
        "  border-radius:8px;\n"
        "  color:var(--text);\n"
        "  font-size:14px;\n"
        "  outline:none;\n"
        "  transition:border-color .2s,width .2s;\n"
        "}\n"
        ".search-box input:focus{\n"
        "  border-color:var(--accent);\n"
        "  width:240px;\n"
        "}\n"
        ".search-box input::placeholder{\n"
        "  color:var(--text-muted);\n"
        "}\n"
        ".search-icon{\n"
        "  position:absolute;\n"
        "  left:10px;top:50%;\n"
        "  transform:translateY(-50%);\n"
        "  width:16px;height:16px;\n"
        "  color:var(--text-muted);\n"
        "}\n"
        "\n"
        ".lang-switch{\n"
        "  padding:6px 14px;\n"
        "  background:var(--surface-2);\n"
        "  border:1px solid var(--border);\n"
        "  border-radius:8px;\n"
        "  color:var(--text);\n"
        "  font-size:13px;\n"
        "  cursor:pointer;\n"
        "  transition:all .2s;\n"
        "}\n"
        ".lang-switch:hover{\n"
        "  border-color:var(--accent);\n"
        "  color:var(--accent);\n"
        "}\n"
        "\n"
        "/* Footer */\n"
        ".site-footer{\n"
        "  border-top:1px solid var(--border);\n"
        "  padding:24px 0;\n"
        "  background:var(--surface);\n"
        "}\n"
        ".site-footer p{color:var(--text-muted);font-size:13px;margin:0}\n"
        "\n"
        "/* Main content */\n"
        "main{padding:40px 0 60px;min-height:calc(100vh - 200px)}\n"
        "h1{font-size:28px;margin-bottom:8px;font-weight:700}\n"
        "h2{font-size:22px;margin:32px 0 16px;font-weight:600;padding-bottom:8px;border-bottom:1px solid var(--border)}\n"
        "h3{font-size:18px;margin:24px 0 12px;font-weight:600}\n"
        "p{margin-bottom:16px;color:var(--text)}\n"
        "a{color:var(--accent);text-decoration:none;transition:color .2s}\n"
        "a:hover{color:var(--accent-hover);text-decoration:underline}\n"
        "ul{margin-bottom:16px;padding-left:24px}\n"
        "li{margin-bottom:6px}\n"
        "\n"
        "/* Code */\n"
        "code{\n"
        "  background:var(--surface-2);\n"
        "  padding:2px 8px;\n"
        "  border-radius:6px;\n"
        "  font-size:13px;\n"
        "  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;\n"
        "}\n"
        "pre{\n"
        "  background:var(--surface);\n"
        "  padding:16px;border-radius:var(--radius);\n"
        "  overflow-x:auto;margin-bottom:16px;\n"
        "  border:1px solid var(--border);\n"
        "}\n"
        "pre code{background:none;padding:0;font-size:13px}\n"
        "\n"
        "/* Info card */\n"
        ".info-card{\n"
        "  background:var(--surface);\n"
        "  border:1px solid var(--border);\n"
        "  border-radius:var(--radius);\n"
        "  padding:20px;\n"
        "  margin-bottom:24px;\n"
        "}\n"
        ".info-card ul{list-style:none;padding:0;margin:0}\n"
        ".info-card li{\n"
        "  padding:6px 0;\n"
        "  border-bottom:1px solid var(--border);\n"
        "  display:flex;gap:12px;\n"
        "}\n"
        ".info-card li:last-child{border-bottom:none}\n"
        ".info-card .label{\n"
        "  color:var(--text-muted);\n"
        "  min-width:100px;\n"
        "  flex-shrink:0;\n"
        "  font-size:14px;\n"
        "}\n"
        ".info-card .value{flex:1;word-break:break-all}\n"
        "\n"
        "/* Bilingual section */\n"
        ".bilingual-block{\n"
        "  background:var(--surface);\n"
        "  border:1px solid var(--border);\n"
        "  border-radius:var(--radius);\n"
        "  margin-bottom:20px;\n"
        "  overflow:hidden;\n"
        "}\n"
        ".bilingual-block .lang-tabs{\n"
        "  display:flex;\n"
        "  background:var(--surface-2);\n"
        "  border-bottom:1px solid var(--border);\n"
        "}\n"
        ".bilingual-block .lang-tab{\n"
        "  padding:8px 20px;\n"
        "  cursor:pointer;\n"
        "  font-size:13px;\n"
        "  color:var(--text-muted);\n"
        "  border-right:1px solid var(--border);\n"
        "  transition:all .2s;\n"
        "}\n"
        ".bilingual-block .lang-tab:hover{color:var(--text)}\n"
        ".bilingual-block .lang-tab.active{\n"
        "  color:var(--accent);\n"
        "  background:var(--surface);\n"
        "  font-weight:500;\n"
        "}\n"
        ".bilingual-block .lang-content{\n"
        "  padding:20px;\n"
        "  display:none;\n"
        "}\n"
        ".bilingual-block .lang-content.active{display:block}\n"
        "\n"
        "/* Plugin list on index */\n"
        ".plugin-list{\n"
        "  list-style:none;\n"
        "  padding:0;\n"
        "  display:grid;\n"
        "  grid-template-columns:repeat(auto-fill,minmax(280px,1fr));\n"
        "  gap:12px;\n"
        "}\n"
        ".plugin-list li{\n"
        "  margin:0;\n"
        "  padding:0;\n"
        "}\n"
        ".plugin-list a{\n"
        "  display:block;\n"
        "  padding:14px 16px;\n"
        "  background:var(--surface);\n"
        "  border:1px solid var(--border);\n"
        "  border-radius:10px;\n"
        "  color:var(--text);\n"
        "  font-weight:500;\n"
        "  transition:all .2s;\n"
        "}\n"
        ".plugin-list a:hover{\n"
        "  border-color:var(--accent);\n"
        "  background:var(--surface-2);\n"
        "  text-decoration:none;\n"
        "  transform:translateY(-1px);\n"
        "}\n"
        ".plugin-list .plugin-name{\n"
        "  font-weight:600;\n"
        "  font-size:14px;\n"
        "  margin-bottom:4px;\n"
        "}\n"
        ".plugin-list .plugin-desc{\n"
        "  color:var(--text-muted);\n"
        "  font-size:12px;\n"
        "  line-height:1.5;\n"
        "  display:-webkit-box;\n"
        "  -webkit-line-clamp:2;\n"
        "  -webkit-box-orient:vertical;\n"
        "  overflow:hidden;\n"
        "}\n"
        "\n"
        "/* Page subtitle */\n"
        ".page-subtitle{\n"
        "  color:var(--text-muted);\n"
        "  font-size:15px;\n"
        "  margin-bottom:24px;\n"
        "}\n"
        "\n"
        "/* Stats */\n"
        ".stats{\n"
        "  display:grid;\n"
        "  grid-template-columns:repeat(auto-fit,minmax(150px,1fr));\n"
        "  gap:16px;\n"
        "  margin:24px 0;\n"
        "}\n"
        ".stat-card{\n"
        "  background:var(--surface);\n"
        "  border:1px solid var(--border);\n"
        "  border-radius:var(--radius);\n"
        "  padding:20px;\n"
        "  text-align:center;\n"
        "}\n"
        ".stat-card .num{\n"
        "  font-size:32px;\n"
        "  font-weight:700;\n"
        "  color:var(--accent);\n"
        "}\n"
        ".stat-card .label{\n"
        "  font-size:13px;\n"
        "  color:var(--text-muted);\n"
        "  margin-top:4px;\n"
        "}\n"
        "\n"
        "/* Responsive */\n"
        "@media (max-width:768px){\n"
        "  .container{padding:0 16px}\n"
        "  h1{font-size:22px}\n"
        "  h2{font-size:18px}\n"
        "  .site-title{font-size:16px}\n"
        "  .search-box input{width:140px}\n"
        "  .search-box input:focus{width:180px}\n"
        "}\n"
        "@media (max-width:560px){\n"
        "  .header-right{\n"
        "    gap:8px;\n"
        "  }\n"
        "  .search-box{\n"
        "    display:none;\n"
        "  }\n"
        "  .site-nav a{\n"
        "    margin-left:12px;\n"
        "    font-size:13px;\n"
        "  }\n"
        "  .lang-switch{\n"
        "    padding:4px 10px;\n"
        "    font-size:12px;\n"
        "  }\n"
        "  .plugin-list{grid-template-columns:1fr}\n"
        "}\n",
        encoding="utf-8",
    )

    # --- JavaScript for language switching and search ---
    (assets_dir / "main.js").write_text(
        "// Language tab switching for individual blocks\n"
        "function switchLang(tabEl) {\n"
        "  const block = tabEl.closest('.bilingual-block');\n"
        "  if (!block) return;\n"
        "  const tabs = block.querySelectorAll('.lang-tab');\n"
        "  const contents = block.querySelectorAll('.lang-content');\n"
        "  const idx = Array.from(tabs).indexOf(tabEl);\n"
        "  tabs.forEach((t, i) => t.classList.toggle('active', i === idx));\n"
        "  contents.forEach((c, i) => c.classList.toggle('active', i === idx));\n"
        "}\n"
        "\n"
        "// Global language toggle - switches ALL bilingual blocks on the page\n"
        "let currentLang = 0; // 0 = Chinese, 1 = English\n"
        "function toggleGlobalLang() {\n"
        "  currentLang = currentLang === 0 ? 1 : 0;\n"
        "  const btn = document.getElementById('langSwitch');\n"
        "  if (btn) {\n"
        "    btn.textContent = currentLang === 0 ? '中文' : 'English';\n"
        "  }\n"
        "  document.querySelectorAll('.bilingual-block').forEach(block => {\n"
        "    const tabs = block.querySelectorAll('.lang-tab');\n"
        "    const contents = block.querySelectorAll('.lang-content');\n"
        "    tabs.forEach((t, i) => t.classList.toggle('active', i === currentLang));\n"
        "    contents.forEach((c, i) => c.classList.toggle('active', i === currentLang));\n"
        "  });\n"
        "}\n"
        "\n"
        "// Search/filter functionality for plugin/module lists\n"
        "function filterItems() {\n"
        "  const input = document.getElementById('searchInput');\n"
        "  if (!input) return;\n"
        "  const query = input.value.toLowerCase().trim();\n"
        "  const lists = document.querySelectorAll('.plugin-list');\n"
        "  lists.forEach(list => {\n"
        "    const items = list.querySelectorAll('li');\n"
        "    items.forEach(item => {\n"
        "      const name = item.querySelector('.plugin-name');\n"
        "      const desc = item.querySelector('.plugin-desc');\n"
        "      const text = (name ? name.textContent : '') + ' ' + (desc ? desc.textContent : '');\n"
        "      if (query === '' || text.toLowerCase().includes(query)) {\n"
        "        item.style.display = 'block';\n"
        "      } else {\n"
        "        item.style.display = 'none';\n"
        "      }\n"
        "    });\n"
        "  });\n"
        "}\n"
        "\n"
        "// Initialize\n"
        "document.addEventListener('DOMContentLoaded', () => {\n"
        "  filterItems();\n"
        "});\n"
        "\n"
        "// Expose globally\n"
        "window.switchLang = switchLang;\n"
        "window.toggleGlobalLang = toggleGlobalLang;\n"
        "window.filterItems = filterItems;\n",
        encoding="utf-8",
    )

    # --- Index page with card-style plugin/module lists ---
    plugin_items = []
    order_p = sorted(range(len(plugins)), key=lambda i: plugins[i]["name"].lower())
    for i in order_p:
        slug = plugin_slugs[i]
        p = plugins[i]
        desc = (p.get("description") or "").strip()
        if len(desc) > 120:
            desc = desc[:117] + "..."
        plugin_items.append(
            f'  <li><a href="plugins/{slug}.html">'
            f'<div class="plugin-name">{p["name"]}</div>'
            f'<div class="plugin-desc">{desc or "—"}</div>'
            f"</a></li>"
        )

    module_items = []
    order_m = sorted(range(len(modules)), key=lambda i: modules[i]["class"].lower())
    for i in order_m:
        slug = module_slugs[i]
        m = modules[i]
        deps = m.get("deps", [])
        dep_str = f"{len(deps)} 个依赖" if deps else "无依赖"
        module_items.append(
            f'  <li><a href="modules/{slug}.html">'
            f'<div class="plugin-name">{m["class"]}</div>'
            f'<div class="plugin-desc">{dep_str}</div>'
            f"</a></li>"
        )

    index_html = f"""---
layout: default
title: Unreal Engine 插件与模块文档
---

<h1>Unreal Engine 插件与模块文档</h1>
<p class="page-subtitle">自动生成的虚幻引擎插件和模块参考文档，中英文对照</p>

<div class="stats">
  <div class="stat-card">
    <div class="num">{len(plugins)}</div>
    <div class="label">插件 Plugins</div>
  </div>
  <div class="stat-card">
    <div class="num">{len(modules)}</div>
    <div class="label">模块 Modules</div>
  </div>
</div>

<h2 id="plugins">插件 Plugins</h2>
<ul class="plugin-list">
{"".join(plugin_items)}
</ul>

<h2 id="modules">模块 Modules</h2>
<ul class="plugin-list">
{"".join(module_items)}
</ul>
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
