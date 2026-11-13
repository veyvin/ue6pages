#!/usr/bin/env python3
"""把 gh-pages 的 plugins/*.md、modules/*.md 打成 assets/usage.fb，供 Vue 站当目录用。"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from backend.usage_fb import write_docs_tree  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs-root", required=True, help="gh-pages 工作树（含 plugins/ modules/）")
    ap.add_argument(
        "--engine-root",
        default="",
        help="当前 UE 源码根目录；用来标记源码里已经删掉的插件/模块",
    )
    args = ap.parse_args()
    info = write_docs_tree(
        Path(args.docs_root),
        engine_root=Path(args.engine_root) if args.engine_root else None,
    )
    if info.get("changed"):
        print(
            f"usage.fb updated: docs={info['docs']} "
            f"added={info.get('added', 0)} bytes={info['bytes']}"
        )
    else:
        print(f"usage.fb unchanged: docs={info['docs']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
