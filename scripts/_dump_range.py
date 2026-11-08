import json
from pathlib import Path

p = json.loads(Path("scripts/catalog/plugins.json").read_text(encoding="utf-8"))
for i, x in enumerate(p[840:855], start=840):
    mods = x.get("modules") or []
    names = []
    for m in mods[:12]:
        names.append(m.get("name") if isinstance(m, dict) else str(m))
    print(f"{i}\t{x.get('slug')}\t{x.get('name')}\tmods={len(mods)}\t{', '.join(names)}")
    print("  CN:", (x.get("desc_cn") or "")[:180])
