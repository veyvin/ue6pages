import json
from pathlib import Path

cat = json.loads(Path("scripts/catalog/plugins.json").read_text(encoding="utf-8"))
folder = Path("plugins")
not_ai = []
ai_n = 0
for i, p in enumerate(cat):
    md = folder / f"{p['slug']}.md"
    text = md.read_text(encoding="utf-8") if md.exists() else ""
    src = "missing" if not text else ("ai" if 'data-usage-source="ai"' in text else "generic")
    if src == "ai":
        ai_n += 1
    else:
        not_ai.append((i, p["slug"], src))
print("ai_pages", ai_n, "not_ai", len(not_ai), "first", not_ai[:6])
print("810-854 not_ai", [x for x in not_ai if 810 <= x[0] <= 854])
