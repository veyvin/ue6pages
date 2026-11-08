import json
import sys
from pathlib import Path

cat = json.loads(Path("scripts/catalog/plugins.json").read_text(encoding="utf-8"))
start, end = int(sys.argv[1]), int(sys.argv[2])
path = Path(sys.argv[3])
data = json.loads(path.read_text(encoding="utf-8"))
want = [p["slug"] for p in cat[start : end + 1]]
got = [r["slug"] for r in data]
ok = True
if got != want:
    print("SLUG_MISMATCH", path.name)
    print(" want", want)
    print(" got ", got)
    ok = False
if len(data) != end - start + 1:
    print("COUNT", len(data), "expected", end - start + 1)
    ok = False
for rec in data:
    cn, en = rec.get("cn_steps") or [], rec.get("en_steps") or []
    if not cn or not en or len(cn) != len(en):
        print("STEPS", rec.get("slug"), len(cn), len(en))
        ok = False
    if rec.get("kind") != "plugin":
        print("KIND", rec.get("slug"), rec.get("kind"))
        ok = False
    if not rec.get("note_cn") or not rec.get("note_en"):
        print("NOTE", rec.get("slug"))
        ok = False
print("OK" if ok else "FAIL", path.name, len(data), got[0], "...", got[-1])
sys.exit(0 if ok else 1)
