#!/usr/bin/env python3
"""Insert an AI/docs-informed Role card (作用) on every plugin/module page."""
from __future__ import annotations

import sys
from pathlib import Path

from inject_usage import USAGE_ID, find_div_span, parse_page
from ue_roles import compose_role

ROOT = Path(__file__).resolve().parents[1]
ROLE_ID = 'id="role"'


def role_card_html(info: dict) -> str:
    cn, en, doc = compose_role(info)
    doc_cn = (
        f'<p class="usage-note">参考文档：<a href="{doc}" target="_blank" rel="noopener">{doc}</a></p>'
        if doc else
        '<p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p>'
    )
    doc_en = (
        f'<p class="usage-note">Docs: <a href="{doc}" target="_blank" rel="noopener">{doc}</a></p>'
        if doc else
        '<p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p>'
    )
    inner = (
        '<div class="bilingual-block"><div class="lang-tabs">'
        '<button class="lang-tab active" onclick="switchLang(this)">中文</button>'
        '<button class="lang-tab" onclick="switchLang(this)">English</button>'
        "</div>"
        f'<div class="lang-content active">{cn}{doc_cn}</div>'
        f'<div class="lang-content">{en}{doc_en}</div>'
        "</div>"
    )
    return (
        f'    <div class="card role-card" {ROLE_ID}>\n'
        '      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>\n'
        f'      <div class="desc-body">{inner}</div>\n'
        "    </div>\n"
    )


def strip_role(text: str) -> str:
    marker = text.find('class="card role-card"')
    if marker < 0:
        return text
    div_start = text.rfind("<div", 0, marker + 1)
    span = find_div_span(text, div_start)
    if not span:
        return text
    return (text[: span[0]] + text[span[1] :]).replace("\n\n\n", "\n\n")


def inject_role(text: str, card: str) -> str:
    text = strip_role(text)
    usage = text.find('class="card usage-card"')
    if usage != -1:
        div_start = text.rfind("<div", 0, usage + 1)
        return text[:div_start] + card + "\n" + text[div_start:]
    aside = text.find('  <aside class="detail-sidebar">')
    if aside != -1:
        left = text.rfind("  </div>", 0, aside)
        if left != -1:
            return text[:left] + card + "\n" + text[left:]
    return text.rstrip() + "\n\n" + card.lstrip() + "\n"


def process_dir(kind: str) -> tuple[int, int]:
    folder = ROOT / ("plugins" if kind == "plugin" else "modules")
    ok = skip = 0
    for path in sorted(folder.glob("*.md")):
        info = parse_page(path, kind)
        if not info["name"]:
            skip += 1
            continue
        new_text = inject_role(info["text"], role_card_html(info))
        if new_text != info["text"]:
            path.write_text(new_text, encoding="utf-8")
            ok += 1
        else:
            skip += 1
    return ok, skip


def main() -> int:
    p_ok, p_skip = process_dir("plugin")
    m_ok, m_skip = process_dir("module")
    print(f"plugins role updated={p_ok} skipped={p_skip}")
    print(f"modules role updated={m_ok} skipped={m_skip}")
    print(f"total updated={p_ok + m_ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
