#!/usr/bin/env python3
"""Apply Cursor-generated role JSON onto every detail page."""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

from inject_roles import inject_role, role_card_html
from inject_usage import parse_page

ROOT = Path(__file__).resolve().parents[1]
AI_DIR = ROOT / "scripts" / "ai_roles"


def esc(s: str) -> str:
    return html.escape(s or "", quote=False)


def paras(text: str) -> str:
    parts = [p.strip() for p in text.replace("\r", "").split("\n") if p.strip()]
    if not parts:
        return ""
    return "".join(f"<p>{esc(p)}</p>" for p in parts)


def load_ai() -> dict:
    out: dict[tuple[str, str], dict] = {}
    if not AI_DIR.is_dir():
        return out
    for path in sorted(AI_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "items" in data:
            data = data["items"]
        if isinstance(data, dict):
            iterable = data.values() if all(isinstance(v, dict) for v in data.values()) else []
            if isinstance(next(iter(data.values()), None), dict) and "slug" not in next(iter(data.values())):
                for slug, rec in data.items():
                    kind = rec.get("kind") or path.stem.split("_")[0]
                    out[(kind, slug)] = rec
                continue
            iterable = data if isinstance(data, list) else data.values()
        else:
            iterable = data
        for rec in iterable:
            if not isinstance(rec, dict):
                continue
            slug = rec.get("slug") or rec.get("id")
            kind = rec.get("kind")
            if slug and kind:
                out[(kind, slug)] = rec
    return out


def card_from_ai(info: dict, rec: dict) -> str:
    cn = rec.get("cn") or rec.get("zh") or rec.get("role_cn") or ""
    en = rec.get("en") or rec.get("role_en") or ""
    note = rec.get("note") or ""
    cn_html = paras(cn) or "<p>（暂无）</p>"
    en_html = paras(en) or "<p>(none)</p>"
    extra_cn = f'<p class="usage-note">{esc(note)}</p>' if note else '<p class="usage-note">由 Cursor 模型根据插件/模块名称、官方 Description 与引擎职责生成。</p>'
    extra_en = '<p class="usage-note">Written by the Cursor model from the item name, Epic Description, and engine role.</p>'
    inner = (
        '<div class="bilingual-block"><div class="lang-tabs">'
        '<button class="lang-tab active" onclick="switchLang(this)">中文</button>'
        '<button class="lang-tab" onclick="switchLang(this)">English</button>'
        "</div>"
        f'<div class="lang-content active">{cn_html}{extra_cn}</div>'
        f'<div class="lang-content">{en_html}{extra_en}</div>'
        "</div>"
    )
    return (
        '    <div class="card role-card" id="role">\n'
        '      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>\n'
        f'      <div class="desc-body">{inner}</div>\n'
        "    </div>\n"
    )


def main() -> int:
    ai = load_ai()
    print(f"ai records={len(ai)}")
    ok = miss = 0
    for kind, folder in (("plugin", "plugins"), ("module", "modules")):
        for path in sorted((ROOT / folder).glob("*.md")):
            info = parse_page(path, kind)
            rec = ai.get((kind, path.stem))
            if not rec:
                miss += 1
                continue
            new_text = inject_role(info["text"], card_from_ai(info, rec))
            path.write_text(new_text, encoding="utf-8")
            ok += 1
    print(f"applied={ok} missing={miss}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
