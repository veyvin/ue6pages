#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from inject_usage import parse_page

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "scripts" / "catalog"


def items(kind: str) -> list[dict]:
    folder = ROOT / ("plugins" if kind == "plugin" else "modules")
    rows = []
    for path in sorted(folder.glob("*.md")):
        info = parse_page(path, kind)
        rows.append({
            "slug": path.stem,
            "kind": kind,
            "name": info["name"],
            "desc_en": info["desc_en"][:400],
            "desc_cn": info["desc_cn"][:400],
            "path": info["file_path"],
            "category": info["category"],
            "modules": info["modules"][:8],
        })
    return rows


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    plugins = items("plugin")
    modules = items("module")
    (OUT / "plugins.json").write_text(json.dumps(plugins, ensure_ascii=False, indent=0), encoding="utf-8")
    (OUT / "modules.json").write_text(json.dumps(modules, ensure_ascii=False, indent=0), encoding="utf-8")
    chunk = 120
    all_items = plugins + modules
    n = 0
    for i in range(0, len(all_items), chunk):
        part = all_items[i : i + chunk]
        (OUT / f"chunk_{n:02d}.json").write_text(
            json.dumps(part, ensure_ascii=False), encoding="utf-8"
        )
        n += 1
    print(f"plugins={len(plugins)} modules={len(modules)} chunks={n} chunk_size={chunk}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
