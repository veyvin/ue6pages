#!/usr/bin/env python3
"""Serialize all AI usage guides into a single FlatBuffers binary.

Output: assets/usage.fb and assets/usage.bin (same bytes; .bin for GitHub Pages MIME).

Built with the runtime flatbuffers.Builder using manual slot layout that mirrors
the .fbs field order, so no flatc is required. Read back with a hand-written
parser (same wire layout the browser uses in assets/usage-fb.js).
"""
from __future__ import annotations

import datetime as _dt
import json
import struct
import sys
from pathlib import Path

import flatbuffers

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from inject_usage import load_ai_usage  # noqa: E402

OUT = ROOT / "assets" / "usage.fb"
OUT_BIN = ROOT / "assets" / "usage.bin"
OUT_BIN = ROOT / "assets" / "usage.bin"  # GitHub Pages serves .bin as octet-stream
IDENT = b"UEUG"


def catalog_index() -> dict:
    idx = {}
    for kind, fn in (("plugin", "plugins.json"), ("module", "modules.json")):
        p = ROOT / "scripts" / "catalog" / fn
        if not p.exists():
            continue
        for r in json.loads(p.read_text(encoding="utf-8")):
            idx[(kind, r.get("slug", ""))] = (r.get("name", ""), r.get("category", ""))
    return idx


def build_doc(b, kind, slug, name, category, cn, en, note_cn, note_en) -> int:
    s_kind = b.CreateString(kind)
    s_slug = b.CreateString(slug)
    s_name = b.CreateString(name)
    s_cat = b.CreateString(category or "")
    s_note_cn = b.CreateString(note_cn or "")
    s_note_en = b.CreateString(note_en or "")

    cn_offs = [b.CreateString(x) for x in cn]
    b.StartVector(4, len(cn_offs), 4)
    for o in reversed(cn_offs):
        b.PrependUOffsetTRelative(o)
    vec_cn = b.EndVector()

    en_offs = [b.CreateString(x) for x in en]
    b.StartVector(4, len(en_offs), 4)
    for o in reversed(en_offs):
        b.PrependUOffsetTRelative(o)
    vec_en = b.EndVector()

    b.StartObject(8)
    b.PrependUOffsetTRelativeSlot(0, s_kind, 0)
    b.PrependUOffsetTRelativeSlot(1, s_slug, 0)
    b.PrependUOffsetTRelativeSlot(2, s_name, 0)
    b.PrependUOffsetTRelativeSlot(3, s_cat, 0)
    b.PrependUOffsetTRelativeSlot(4, vec_cn, 0)
    b.PrependUOffsetTRelativeSlot(5, vec_en, 0)
    b.PrependUOffsetTRelativeSlot(6, s_note_cn, 0)
    b.PrependUOffsetTRelativeSlot(7, s_note_en, 0)
    return b.EndObject()


def build() -> tuple[int, int]:
    usage = load_ai_usage()
    cat = catalog_index()
    keys = sorted(usage.keys())
    b = flatbuffers.Builder(1024 * 1024)
    doc_offsets = []
    for key in keys:
        rec = usage[key]
        kind, slug = key
        name, category = cat.get((kind, slug), (slug, ""))
        cn = [str(x) for x in rec.get("cn_steps", [])]
        en = [str(x) for x in rec.get("en_steps", [])]
        doc_offsets.append(build_doc(
            b, kind, slug, name, category, cn, en,
            rec.get("note_cn", ""), rec.get("note_en", ""),
        ))
    b.StartVector(4, len(doc_offsets), 4)
    for o in reversed(doc_offsets):
        b.PrependUOffsetTRelative(o)
    vec_docs = b.EndVector()

    gen_at = b.CreateString(_dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    b.StartObject(3)
    b.PrependInt32Slot(0, 1, 0)
    b.PrependUOffsetTRelativeSlot(1, gen_at, 0)
    b.PrependUOffsetTRelativeSlot(2, vec_docs, 0)
    bundle = b.EndObject()
    b.Finish(bundle, IDENT)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = bytes(b.Output())
    OUT.write_bytes(payload)
    OUT_BIN.write_bytes(payload)
    return len(keys), OUT.stat().st_size


# ---- hand-written reader (mirrors assets/usage-fb.js) ----
def _u8(b, p): return b[p]
def _u16(b, p): return struct.unpack_from("<H", b, p)[0]
def _u32(b, p): return struct.unpack_from("<I", b, p)[0]
def _i32(b, p): return struct.unpack_from("<i", b, p)[0]


def _field(b, tbl, slot):
    vt = tbl - _i32(b, tbl)
    vtsize = _u16(b, vt)
    o = 4 + slot * 2
    if o >= vtsize:
        return 0
    return _u16(b, vt + o)


def _str(b, tbl, slot):
    fo = _field(b, tbl, slot)
    if fo == 0:
        return ""
    pos = tbl + fo
    sp = pos + _u32(b, pos)
    n = _u32(b, sp)
    return b[sp + 4:sp + 4 + n].decode("utf-8")


def _vec_str(b, tbl, slot):
    fo = _field(b, tbl, slot)
    if fo == 0:
        return []
    pos = tbl + fo
    vec = pos + _u32(b, pos)
    n = _u32(b, vec)
    out = []
    for i in range(n):
        ep = vec + 4 + i * 4
        sp = ep + _u32(b, ep)
        ln = _u32(b, sp)
        out.append(b[sp + 4:sp + 4 + ln].decode("utf-8"))
    return out


def _vec_table(b, tbl, slot):
    fo = _field(b, tbl, slot)
    if fo == 0:
        return []
    pos = tbl + fo
    vec = pos + _u32(b, pos)
    n = _u32(b, vec)
    out = []
    for i in range(n):
        ep = vec + 4 + i * 4
        out.append(ep + _u32(b, ep))
    return out


def verify() -> tuple[int, str]:
    b = OUT.read_bytes()
    assert b[4:8] == IDENT, "bad file identifier"
    root = _u32(b, 0)
    version = 0
    fo = _field(b, root, 0)
    if fo:
        version = _i32(b, root + fo)
    gen_at = _str(b, root, 1)
    docs = _vec_table(b, root, 2)
    sample = None
    for t in docs:
        if _str(b, t, 1) == "aimodule":
            sample = (t, )
            break
    return len(docs), gen_at


def main() -> int:
    n, size = build()
    count, gen_at = verify()
    print(f"wrote {OUT}  docs={n}  bytes={size}  readback={count}  generated_at={gen_at}")
    assert count == n, "readback count mismatch"
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
