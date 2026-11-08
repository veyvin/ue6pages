#!/usr/bin/env python3
"""Apply per-item AI usage JSON onto plugin/module pages. Does not use category templates."""
from __future__ import annotations

import sys

from inject_usage import load_ai_usage, main as inject_main


def main() -> int:
    records = load_ai_usage()
    print(f"ai usage records={len(records)}")
    if "--templates" in sys.argv:
        print("refusing --templates here; use inject_usage.py --templates if you really need stubs")
        return 2
    return inject_main()


if __name__ == "__main__":
    sys.exit(main())
