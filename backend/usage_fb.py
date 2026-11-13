"""《使用方法》文档的 FlatBuffers 打包（与 gh-pages 的 assets/usage.fb 同一套 schema）。

Wire 布局（见 scripts/usage.fbs，file identifier "UEUG"）：

    UsageBundle: version(int32) generated_at(string) docs([UsageDoc])
    UsageDoc:    kind slug name category cn_steps([string]) en_steps([string]) note_cn note_en

这里只做后端侧的序列化 + 自检。前端 frontend/src/api/usageFb.js 用同样的槽位手写解析，
所以改 schema 必须两边一起改。

产物：<site.usage_fb_root>/usage.fb 与同字节的 usage.bin（部分静态托管不认 .fb 的 MIME）。
"""
from __future__ import annotations

import datetime as _dt
import re
import struct
from pathlib import Path
from typing import Any

import flatbuffers

from .config import CONFIG
from . import usage_docs

IDENT = b"UEUG"
SCHEMA_VERSION = 1
NOTE_MAX_CHARS = 4000

_MD_HEADING = re.compile(r"^#{1,6}\s+(.*)$")
_MD_BULLET = re.compile(r"^(?:[-*+]|\d+[.)])\s+(.*)$")


def output_root() -> Path:
    root = Path(CONFIG.site.usage_fb_root)
    if not root.is_absolute():
        root = Path(__file__).parent / root
    return root


# ---------- Markdown → 要点/摘要 ----------
def derive_steps(markdown: str) -> tuple[list[str], str]:
    """模型只给整篇 Markdown 时，抽出标题/列表作为要点，首段作为一句话摘要。"""
    steps: list[str] = []
    note_parts: list[str] = []
    in_fence = False
    for raw in markdown.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not line:
            continue
        heading = _MD_HEADING.match(line)
        if heading:
            steps.append(heading.group(1).strip())
            continue
        bullet = _MD_BULLET.match(line)
        if bullet:
            steps.append(bullet.group(1).strip())
            continue
        if len(note_parts) < 2:
            note_parts.append(line)
    return steps[:16], " ".join(note_parts)[:NOTE_MAX_CHARS]


def fields_for(markdown: str, structured: dict[str, Any] | None = None) -> dict[str, Any]:
    """中英文共用一份要点，避免前端拿到空数组。

    structured 是 usage_docs.read_structured() 的结果（JSON 侧车文件），
    有则优先，没有就从 Markdown 推导。
    """
    if structured:
        cn = [str(x).strip() for x in (structured.get("cn_steps") or []) if str(x).strip()]
        en = [str(x).strip() for x in (structured.get("en_steps") or []) if str(x).strip()]
        note_cn = str(structured.get("note_cn") or "").strip()
        note_en = str(structured.get("note_en") or "").strip()
        if cn or en or note_cn or note_en:
            return {
                "cn_steps": cn[:16],
                "en_steps": en[:16],
                "note_cn": note_cn or note_en,
                "note_en": note_en or note_cn,
            }

    steps, note = derive_steps(markdown)
    return {"cn_steps": steps, "en_steps": steps, "note_cn": note, "note_en": note}


# ---------- 序列化 ----------
def _str(b: flatbuffers.Builder, s: str) -> int:
    return b.CreateString(s or "")


def _str_vec(b: flatbuffers.Builder, items: list[str]) -> int:
    offs = [_str(b, x) for x in items]
    b.StartVector(4, len(offs), 4)
    for o in reversed(offs):
        b.PrependUOffsetTRelative(o)
    return b.EndVector()


def _doc_table(b: flatbuffers.Builder, rec: dict[str, Any]) -> int:
    s_kind = _str(b, rec["kind"])
    s_slug = _str(b, rec["slug"])
    s_name = _str(b, rec["name"])
    s_cat = _str(b, rec["category"])
    vec_cn = _str_vec(b, rec["cn_steps"])
    vec_en = _str_vec(b, rec["en_steps"])
    s_note_cn = _str(b, rec["note_cn"])
    s_note_en = _str(b, rec["note_en"])

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


def _catalog_meta() -> dict[tuple[str, str], tuple[str, str]]:
    """(kind, slug) → (name, category)，用于补全二进制里的展示名。"""
    meta: dict[tuple[str, str], tuple[str, str]] = {}
    try:
        from .scanner import scan_all

        plugins, modules = scan_all()
        for p in plugins:
            meta[("plugin", p.slug)] = (p.name, p.category)
        for m in modules:
            meta[("module", m.slug)] = (m.name, "")
    except Exception:  # noqa: BLE001 —— engine_root 不可用时仍打包已有文档
        pass
    return meta


def build_payload() -> tuple[bytes, int, str]:
    """把磁盘上全部《使用方法》序列化为一个二进制，返回 (bytes, docs, generated_at)。"""
    root = usage_docs.usage_root()
    meta = _catalog_meta()

    records: list[dict[str, Any]] = []
    for kind, dirname in (("plugin", "plugins"), ("module", "modules")):
        d = root / dirname
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.md")):
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            name, category = meta.get((kind, f.stem), (f.stem, ""))
            records.append({
                "kind": kind,
                "slug": f.stem,
                "name": name,
                "category": category,
                **fields_for(text, usage_docs.read_structured(kind, f.stem)),
            })

    b = flatbuffers.Builder(1024 * 1024)
    offsets = [_doc_table(b, r) for r in records]
    b.StartVector(4, len(offsets), 4)
    for o in reversed(offsets):
        b.PrependUOffsetTRelative(o)
    vec_docs = b.EndVector()

    generated_at = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    s_gen = _str(b, generated_at)
    b.StartObject(3)
    b.PrependInt32Slot(0, SCHEMA_VERSION, 0)
    b.PrependUOffsetTRelativeSlot(1, s_gen, 0)
    b.PrependUOffsetTRelativeSlot(2, vec_docs, 0)
    bundle = b.EndObject()
    b.Finish(bundle, IDENT)
    return bytes(b.Output()), len(records), generated_at


# ---------- 自检（与前端同一套偏移规则） ----------
def _u16(buf: bytes, p: int) -> int:
    return struct.unpack_from("<H", buf, p)[0]


def _u32(buf: bytes, p: int) -> int:
    return struct.unpack_from("<I", buf, p)[0]


def _i32(buf: bytes, p: int) -> int:
    return struct.unpack_from("<i", buf, p)[0]


def _field(buf: bytes, tbl: int, slot: int) -> int:
    vt = tbl - _i32(buf, tbl)
    if 4 + slot * 2 >= _u16(buf, vt):
        return 0
    return _u16(buf, vt + 4 + slot * 2)


def _vec_table(buf: bytes, tbl: int, slot: int) -> list[int]:
    off = _field(buf, tbl, slot)
    if not off:
        return []
    pos = tbl + off
    vec = pos + _u32(buf, pos)
    n = _u32(buf, vec)
    out = []
    for i in range(n):
        ep = vec + 4 + i * 4
        out.append(ep + _u32(buf, ep))
    return out


def verify(payload: bytes) -> int:
    """回读二进制，返回文档条数；格式不符抛 ValueError。"""
    if len(payload) < 12:
        raise ValueError("usage.fb 太短")
    if payload[4:8] != IDENT:
        raise ValueError(f"usage.fb identifier 不符：{payload[4:8]!r}")
    return len(_vec_table(payload, _u32(payload, 0), 2))


# ---------- 缓存 / 落盘 ----------
_CACHE: dict[str, Any] = {"payload": None, "docs": 0, "generated_at": "", "signature": None}


def _source_files() -> list[Path]:
    root = usage_docs.usage_root()
    out: list[Path] = []
    for dirname in ("plugins", "modules"):
        d = root / dirname
        if d.is_dir():
            out.extend(sorted(d.glob("*.md")))
    return out


def _signature() -> tuple[int, float]:
    files = _source_files()
    return len(files), max((f.stat().st_mtime for f in files), default=0.0)


def invalidate() -> None:
    """文档被写入/删除后调用，下次请求强制重建。"""
    _CACHE.update(payload=None, signature=None)


def get_payload(force: bool = False) -> dict[str, Any]:
    """返回 {payload, docs, generated_at, etag, sig}；源文件未变更时走内存缓存。"""
    sig = _signature()
    if not force and _CACHE["payload"] is not None and _CACHE["signature"] == sig:
        return _CACHE

    payload, docs, generated_at = build_payload()
    verify(payload)
    _CACHE.update(
        payload=payload,
        docs=docs,
        generated_at=generated_at,
        signature=sig,
        etag=f'W/"{docs}-{int(sig[1])}"',
    )
    return _CACHE


def _frontend_assets() -> Path | None:
    """开发时同步一份到 frontend/public/assets，让 Vite 不经代理也能读。"""
    public = Path(__file__).resolve().parent.parent / "frontend" / "public" / "assets"
    if public.parent.is_dir():
        public.mkdir(parents=True, exist_ok=True)
        return public
    return None


def write_files(force: bool = True) -> dict[str, Any]:
    """写入 usage.fb / usage.bin，返回状态摘要（设置页展示 / 部署时预生成）。"""
    root = output_root()
    main = root / "usage.fb"
    info = get_payload(force=force)
    root.mkdir(parents=True, exist_ok=True)
    tmp = main.with_suffix(".fb.tmp")
    tmp.write_bytes(info["payload"])
    tmp.replace(main)
    bin_path = root / "usage.bin"
    bin_path.write_bytes(info["payload"])
    copies = [str(main), str(bin_path)]
    frontend_assets = _frontend_assets()
    if frontend_assets is not None:
        for name in ("usage.fb", "usage.bin"):
            dest = frontend_assets / name
            dest.write_bytes(info["payload"])
            copies.append(str(dest))
    return {
        "root": str(root),
        "path": str(main),
        "bin_path": str(bin_path),
        "copies": copies,
        "bytes": main.stat().st_size,
        "docs": info["docs"],
        "generated_at": info["generated_at"],
    }


def disk_status() -> dict[str, Any]:
    """磁盘上已有产物的情况（不触发重建）。"""
    root = output_root()
    main = root / "usage.fb"
    exists = main.is_file()
    stale = exists and any(f.stat().st_mtime > main.stat().st_mtime for f in _source_files())
    return {
        "root": str(root),
        "path": str(main),
        "bin_path": str(root / "usage.bin"),
        "exists": exists,
        "stale": bool(stale),
        "bytes": main.stat().st_size if exists else 0,
        "docs": len(_source_files()),
    }
