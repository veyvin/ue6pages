#!/usr/bin/env python3
"""Report which plugins/modules still need per-item AI usage.

Two independent checks (both incremental, safe to run any time):

1. Catalog-driven: items in scripts/catalog/{plugins,modules}.json that have NO
   matching record in scripts/ai_usage/*.json (keyed by (kind, slug)).
2. Page-driven: existing pages whose usage card is not sourced from AI
   (data-usage-source != "ai"), e.g. "pending"/"template"/missing.

Run from anywhere:  python scripts/_pending.py
Exit code 0 always; this is a reporting tool.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "scripts" / "catalog"
USAGE_RE = re.compile(r'data-usage-source="([^"]*)"')


def load_usage_keys() -> set[tuple[str, str]]:
    sys_path_fix = str(Path(__file__).resolve().parent)
    import sys

    if sys_path_fix not in sys.path:
        sys.path.insert(0, sys_path_fix)
    from inject_usage import load_ai_usage  # local module

    return set(load_ai_usage().keys())


def catalog_items() -> list[tuple[str, str, str]]:
    """Return (kind, slug, name) from catalog files."""
    out: list[tuple[str, str, str]] = []
    for kind, fn in (("plugin", "plugins.json"), ("module", "modules.json")):
        path = CATALOG / fn
        if not path.exists():
            continue
        for rec in json.loads(path.read_text(encoding="utf-8")):
            out.append((kind, rec.get("slug", ""), rec.get("name", "")))
    return out


def page_source(kind: str, slug: str) -> str:
    folder = ROOT / ("plugins" if kind == "plugin" else "modules")
    page = folder / f"{slug}.md"
    if not page.exists():
        return "missing-page"
    text = page.read_text(encoding="utf-8", errors="replace")
    m = USAGE_RE.search(text)
    return m.group(1) if m else "no-card"


def main() -> int:
    usage_keys = load_usage_keys()
    items = catalog_items()

    missing_usage: list[tuple[str, str, str]] = []
    not_ai_pages: list[tuple[str, str, str]] = []
    for kind, slug, name in items:
        if (kind, slug) not in usage_keys:
            missing_usage.append((kind, slug, name))
        src = page_source(kind, slug)
        if src != "ai":
            not_ai_pages.append((kind, slug, src))

    print(f"catalog items: {len(items)}   ai_usage records: {len(usage_keys)}")
    print(f"[1] items with NO ai_usage record: {len(missing_usage)}")
    for kind, slug, name in missing_usage[:40]:
        print(f"    - {kind}:{slug}  ({name})")
    if len(missing_usage) > 40:
        print(f"    ... and {len(missing_usage) - 40} more")

    print(f"[2] pages not sourced from AI: {len(not_ai_pages)}")
    for kind, slug, src in not_ai_pages[:40]:
        print(f"    - {kind}:{slug}  (source={src})")
    if len(not_ai_pages) > 40:
        print(f"    ... and {len(not_ai_pages) - 40} more")

    if not missing_usage and not not_ai_pages:
        print("ALL COVERED — every catalog item has AI usage and every page is AI-sourced.")
    else:
        print("NEEDS WORK — author ai_usage chunks for the items above, then run scripts/apply_ai_usage.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
