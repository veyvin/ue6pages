"""《使用方法》文档的 FlatBuffers 打包（与 gh-pages 的 assets/usage.fb 同一套 schema）。

Wire 布局（见 scripts/usage.fbs，file identifier "UEUG"）：

    UsageBundle: version(int32) generated_at(string) docs([UsageDoc])
    UsageDoc:    kind slug name category cn_steps([string]) en_steps([string])
                 note_cn note_en ai_usage(bool, slot8, 旧文件缺省=false)
                 in_source(bool, slot9, 旧文件缺省=true；源码已删则为 false)

这里只做后端侧的序列化 + 自检。前端 frontend/src/api/usageFb.js 用同样的槽位手写解析，
所以改 schema 必须两边一起改。

产物：<site.usage_fb_root>/usage.fb 与同字节的 usage.bin（部分静态托管不认 .fb 的 MIME）。
"""
from __future__ import annotations

import datetime as _dt
import json
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

    has_ai = has_ai_usage(rec)
    in_source = rec.get("in_source", True)
    if in_source is None:
        in_source = True
    b.StartObject(10)
    b.PrependUOffsetTRelativeSlot(0, s_kind, 0)
    b.PrependUOffsetTRelativeSlot(1, s_slug, 0)
    b.PrependUOffsetTRelativeSlot(2, s_name, 0)
    b.PrependUOffsetTRelativeSlot(3, s_cat, 0)
    b.PrependUOffsetTRelativeSlot(4, vec_cn, 0)
    b.PrependUOffsetTRelativeSlot(5, vec_en, 0)
    b.PrependUOffsetTRelativeSlot(6, s_note_cn, 0)
    b.PrependUOffsetTRelativeSlot(7, s_note_en, 0)
    b.PrependBoolSlot(8, has_ai, False)
    b.PrependBoolSlot(9, bool(in_source), True)
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


_FRONT_TITLE = re.compile(r"^title:\s*(.+)$", re.M)
_HERO_TITLE = re.compile(r'<div class="hero-title(?:\s+mono)?"[^>]*>([^<]+)</div>')
_CHIP_PRIMARY = re.compile(
    r'class="chip chip-primary"[^>]*>[\s\S]*?</span>([^<]+)</span>',
    re.I,
)
_LANG_ACTIVE = re.compile(r'<div class="lang-content active">([\s\S]*?)</div>', re.I)
_DESC_P = re.compile(r'<div class="desc-body">[\s\S]*?<p>([\s\S]*?)</p>', re.I)


def _plain(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html or "")
    return re.sub(r"\s+", " ", text).strip()


def _page_identity(text: str, stem: str) -> tuple[str, str, str]:
    """从 Jekyll 页面抽出 (name, category, note)。"""
    name = stem
    m = _FRONT_TITLE.search(text)
    if m:
        raw = m.group(1).strip().strip('"').strip("'")
        name = raw.split(" / ")[-1].strip() or name
    m = _HERO_TITLE.search(text)
    if m:
        name = _plain(m.group(1)) or name

    category = ""
    m = _CHIP_PRIMARY.search(text)
    if m:
        category = _plain(m.group(1))
        if category in {"Uncategorized", "Plugin / 插件", "Module / C++ Build Rule"}:
            category = ""

    note = ""
    m = _LANG_ACTIVE.search(text) or _DESC_P.search(text)
    if m:
        note = _plain(m.group(1))[:NOTE_MAX_CHARS]
    return name, category, note


def _structured_at(root: Path, kind: str, slug: str) -> dict[str, Any] | None:
    p = root / ("plugins" if kind == "plugin" else "modules") / f"{slug}.json"
    if not p.is_file():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None
    return data if isinstance(data, dict) else None


def _serialize(records: list[dict[str, Any]]) -> tuple[bytes, int, str]:
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


def live_keys_from_engine(engine_root: Path | str | None = None) -> set[tuple[str, str]] | None:
    """当前引擎树里仍存在的 (kind, slug)。扫不到或目录为空时返回 None，避免把全目录标成已删除。"""
    try:
        from .scanner import discover_build_cs, discover_uplugins

        root = Path(engine_root) if engine_root else Path(CONFIG.engine_root)
        if not root.is_dir():
            return None
        keys: set[tuple[str, str]] = set()
        for p in discover_uplugins(root):
            keys.add(("plugin", p.slug))
        for m in discover_build_cs(root):
            keys.add(("module", m.slug))
        return keys or None
    except Exception:  # noqa: BLE001
        return None


def stamp_in_source(
    records: list[dict[str, Any]],
    live_keys: set[tuple[str, str]] | None,
) -> list[dict[str, Any]]:
    if live_keys is None:
        for rec in records:
            rec.setdefault("in_source", True)
        return records
    for rec in records:
        rec["in_source"] = (rec.get("kind"), rec.get("slug")) in live_keys
    return records


def build_payload(
    docs_root: Path | None = None,
    live_keys: set[tuple[str, str]] | None = None,
) -> tuple[bytes, int, str]:
    """把磁盘上全部《使用方法》序列化为一个二进制，返回 (bytes, docs, generated_at)。"""
    root = Path(docs_root) if docs_root is not None else usage_docs.usage_root()
    meta = _catalog_meta() if docs_root is None else {}
    if live_keys is None and docs_root is None:
        live_keys = live_keys_from_engine()

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
            structured = (
                _structured_at(root, kind, f.stem)
                if docs_root is not None
                else usage_docs.read_structured(kind, f.stem)
            )
            if docs_root is not None:
                page_name, page_cat, page_note = _page_identity(text, f.stem)
                name, category = page_name, page_cat
                if "<div" in text and not structured:
                    fields = {
                        "cn_steps": [],
                        "en_steps": [],
                        "note_cn": page_note,
                        "note_en": page_note,
                    }
                else:
                    fields = fields_for(text, structured)
                    if not (fields["note_cn"] or fields["note_en"]) and page_note:
                        fields["note_cn"] = page_note
                        fields["note_en"] = page_note
            else:
                fields = fields_for(text, structured)
            rec = {
                "kind": kind,
                "slug": f.stem,
                "name": name,
                "category": category,
                **fields,
            }
            rec["ai_usage"] = bool(structured) or has_ai_usage(rec)
            records.append(rec)

    stamp_in_source(records, live_keys)
    return _serialize(records)


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


def _str_at(buf: bytes, tbl: int, slot: int) -> str:
    off = _field(buf, tbl, slot)
    if not off:
        return ""
    pos = tbl + off
    sp = pos + _u32(buf, pos)
    n = _u32(buf, sp)
    return buf[sp + 4 : sp + 4 + n].decode("utf-8", "replace")


def _str_vec_at(buf: bytes, tbl: int, slot: int) -> list[str]:
    off = _field(buf, tbl, slot)
    if not off:
        return []
    pos = tbl + off
    vec = pos + _u32(buf, pos)
    n = _u32(buf, vec)
    out: list[str] = []
    for i in range(n):
        ep = vec + 4 + i * 4
        sp = ep + _u32(buf, ep)
        ln = _u32(buf, sp)
        out.append(buf[sp + 4 : sp + 4 + ln].decode("utf-8", "replace"))
    return out


def verify(payload: bytes) -> int:
    """回读二进制，返回文档条数；格式不符抛 ValueError。"""
    if len(payload) < 12:
        raise ValueError("usage.fb 太短")
    if payload[4:8] != IDENT:
        raise ValueError(f"usage.fb identifier 不符：{payload[4:8]!r}")
    return len(_vec_table(payload, _u32(payload, 0), 2))


def parse_bundle(payload: bytes) -> list[dict[str, Any]]:
    """把 usage.fb 解回记录列表，供 CI 与已有二进制合并。"""
    verify(payload)
    root = _u32(payload, 0)
    docs: list[dict[str, Any]] = []
    for tbl in _vec_table(payload, root, 2):
        slug = _str_at(payload, tbl, 1)
        if not slug:
            continue
        rec = {
            "kind": _str_at(payload, tbl, 0),
            "slug": slug,
            "name": _str_at(payload, tbl, 2),
            "category": _str_at(payload, tbl, 3),
            "cn_steps": _str_vec_at(payload, tbl, 4),
            "en_steps": _str_vec_at(payload, tbl, 5),
            "note_cn": _str_at(payload, tbl, 6),
            "note_en": _str_at(payload, tbl, 7),
        }
        rec["ai_usage"] = _bool_at(payload, tbl, 8) or has_ai_usage(rec)
        rec["in_source"] = _bool_at(payload, tbl, 9, default=True)
        docs.append(rec)
    return docs


def _bool_at(buf: bytes, tbl: int, slot: int, default: bool = False) -> bool:
    off = _field(buf, tbl, slot)
    if not off:
        return default
    return buf[tbl + off] != 0


def has_ai_usage(rec: dict[str, Any]) -> bool:
    """是否已有 AI《使用方法》：显式标记，或至少有一条要点（旧 usage.fb 没有 slot8）。"""
    if rec.get("ai_usage") or rec.get("aiUsage"):
        return True
    steps = rec.get("cn_steps") or rec.get("en_steps") or rec.get("cnSteps") or rec.get("enSteps") or []
    return len(steps) > 0


_PUBLISHED_FB = (
    "https://raw.githubusercontent.com/veyvin/ue6pages/gh-pages/assets/usage.fb"
)
_AI_KEYS: set[tuple[str, str]] | None = None


def _bundle_paths() -> list[Path]:
    paths = [output_root() / "usage.fb"]
    public = Path(__file__).resolve().parent.parent / "frontend" / "public" / "assets" / "usage.fb"
    paths.append(public)
    return paths


def load_ai_usage_keys(force: bool = False) -> set[tuple[str, str]]:
    """已有 AI 用法的 (kind, slug)。批量生成时跳过这些，避免重复扫。"""
    global _AI_KEYS
    if _AI_KEYS is not None and not force:
        return _AI_KEYS
    keys: set[tuple[str, str]] = set()

    def ingest(payload: bytes) -> None:
        for rec in parse_bundle(payload):
            if has_ai_usage(rec):
                keys.add((rec["kind"], rec["slug"]))

    for path in _bundle_paths():
        if not path.is_file():
            continue
        try:
            ingest(path.read_bytes())
        except (OSError, ValueError):
            continue
    if not keys:
        try:
            import urllib.request

            with urllib.request.urlopen(_PUBLISHED_FB, timeout=60) as resp:  # noqa: S310
                ingest(resp.read())
        except Exception:  # noqa: BLE001
            pass
    _AI_KEYS = keys
    return keys


def invalidate() -> None:
    """文档被写入/删除后调用，下次请求强制重建。"""
    global _AI_KEYS
    _AI_KEYS = None
    _CACHE.update(payload=None, signature=None)


def _usage_score(rec: dict[str, Any]) -> int:
    return (
        len(rec.get("cn_steps") or [])
        + len(rec.get("en_steps") or [])
        + min(len(rec.get("note_cn") or ""), 80)
        + min(len(rec.get("note_en") or ""), 80)
    )


def merge_with_existing(
    records: list[dict[str, Any]],
    existing: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """新页面补进目录；已有条目若 usage 更完整则保留要点。"""
    by_key = {(r["kind"], r["slug"]): r for r in existing}
    out: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for rec in records:
        key = (rec["kind"], rec["slug"])
        seen.add(key)
        old = by_key.get(key)
        if old and _usage_score(old) > _usage_score(rec):
            merged = {**rec}
            for field in ("cn_steps", "en_steps", "note_cn", "note_en"):
                if old.get(field):
                    merged[field] = old[field]
            if old.get("name") and (not rec.get("name") or rec["name"] == rec["slug"]):
                merged["name"] = old["name"]
            if old.get("category") and not rec.get("category"):
                merged["category"] = old["category"]
            merged["ai_usage"] = has_ai_usage(old) or has_ai_usage(merged)
            if "in_source" in rec:
                merged["in_source"] = rec["in_source"]
            elif "in_source" in old:
                merged["in_source"] = old["in_source"]
            out.append(merged)
        else:
            out.append(rec)
    for rec in existing:
        key = (rec["kind"], rec["slug"])
        if key not in seen:
            out.append(rec)
    return out


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


def _flag_sig(records: list[dict[str, Any]]) -> set[tuple[str, str, bool, bool]]:
    return {
        (r.get("kind") or "", r.get("slug") or "", has_ai_usage(r), bool(r.get("in_source", True)))
        for r in records
    }


def write_docs_tree(
    docs_root: Path,
    existing_fb: Path | None = None,
    engine_root: Path | str | None = None,
) -> dict[str, Any]:
    """把 gh-pages 的 plugins/modules markdown 打成 assets/usage.fb。

    若已有 usage.fb，保留其中更完整的《使用方法》要点，只把新 slug 加进目录。
    源码已删的条目仍留在二进制里，并打上 in_source=false。
    目录与标记都不变时不改文件，避免每日无意义提交。
    """
    docs_root = Path(docs_root)
    out_dir = docs_root / "assets"
    out_dir.mkdir(parents=True, exist_ok=True)
    main = out_dir / "usage.fb"
    fb_path = Path(existing_fb) if existing_fb else main
    live_keys = live_keys_from_engine(engine_root)

    payload, docs, generated_at = build_payload(docs_root=docs_root, live_keys=live_keys)
    records = parse_bundle(payload)
    old: list[dict[str, Any]] = []
    if fb_path.is_file():
        try:
            old = parse_bundle(fb_path.read_bytes())
        except ValueError:
            old = []
    merged = stamp_in_source(merge_with_existing(records, old), live_keys)
    old_keys = {(r["kind"], r["slug"]) for r in old}
    new_keys = {(r["kind"], r["slug"]) for r in merged}
    if fb_path.is_file() and _flag_sig(old) == _flag_sig(merged):
        return {
            "path": str(main),
            "docs": len(old),
            "bytes": fb_path.stat().st_size,
            "changed": False,
            "generated_at": "",
        }

    payload, docs, generated_at = _serialize(merged)
    verify(payload)
    tmp = main.with_suffix(".fb.tmp")
    tmp.write_bytes(payload)
    tmp.replace(main)
    (out_dir / "usage.bin").write_bytes(payload)
    return {
        "path": str(main),
        "docs": docs,
        "bytes": main.stat().st_size,
        "changed": True,
        "added": len(new_keys - old_keys),
        "generated_at": generated_at,
    }


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


# ---------- 分片（首屏先出前 N 条，其余后台逐片补） ----------
CHUNK_SIZE = 100


def _all_records(force: bool = False) -> list[dict[str, Any]]:
    """当前全部记录（已含 in_source / ai_usage 标记），按 kind+slug 排序保证分片稳定。"""
    info = get_payload(force=force)
    records = parse_bundle(info["payload"])
    records.sort(key=lambda r: (r["kind"], r["slug"]))
    return records


def chunk_count(records: list[dict[str, Any]] | None = None) -> int:
    recs = records if records is not None else _all_records()
    return (len(recs) + CHUNK_SIZE - 1) // CHUNK_SIZE


def build_manifest(force: bool = False) -> dict[str, Any]:
    """分片清单：总条数、分片大小、分片数，以及每片的条数与字节数（前端据此排进度）。"""
    info = get_payload(force=force)
    records = _all_records(force=False)
    chunks: list[dict[str, Any]] = []
    for i in range(0, len(records), CHUNK_SIZE):
        part = records[i : i + CHUNK_SIZE]
        payload, _, _ = _serialize(part)
        chunks.append({
            "index": len(chunks),
            "docs": len(part),
            "bytes": len(payload),
            "etag": f'W/"{len(part)}-{hash(tuple((r["kind"], r["slug"]) for r in part)) & 0xFFFFFFFF:x}"',
        })
    return {
        "version": SCHEMA_VERSION,
        "generated_at": info["generated_at"],
        "total_docs": len(records),
        "chunk_size": CHUNK_SIZE,
        "chunk_count": len(chunks),
        "total_bytes": sum(c["bytes"] for c in chunks),
        "chunks": chunks,
    }


def build_chunk(index: int, force: bool = False) -> tuple[bytes, int, str] | None:
    """返回第 index 片 (bytes, docs, generated_at)；越界返回 None。"""
    records = _all_records(force=force)
    start = index * CHUNK_SIZE
    if index < 0 or start >= len(records):
        return None
    return _serialize(records[start : start + CHUNK_SIZE])