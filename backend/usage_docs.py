"""《使用方法》文档（AI 批量生成）的存储读写与统计。

文件布局：<usage_docs_root>/plugins/<slug>.md 与 <usage_docs_root>/modules/<slug>.md。
usage_docs_root 支持相对路径（相对 backend 包目录）或绝对路径，可在设置页修改
（CONFIG.site.usage_docs_root，写入 backend/config.yaml）。

CI（generate-ue-docs.yml）不再调用 AI，只输出静态目录；这些文档全部由后端
用设置页配置的 OpenAI-compatible API 批量生成。
"""
from __future__ import annotations

from pathlib import Path

from .config import CONFIG


def usage_root() -> Path:
    root = Path(CONFIG.site.usage_docs_root)
    if not root.is_absolute():
        root = Path(__file__).parent / root
    return root


def doc_path(kind: str, slug: str) -> Path:
    if kind not in ("plugin", "module"):
        raise ValueError(f"kind must be 'plugin' or 'module', got {kind!r}")
    return usage_root() / ("plugins" if kind == "plugin" else "modules") / f"{slug}.md"


def read_doc(kind: str, slug: str) -> dict:
    """读取一篇文档；不存在时返回 found=False。"""
    p = doc_path(kind, slug)
    if not p.is_file():
        return {"found": False, "path": str(p), "mtime": 0.0, "content": ""}
    try:
        content = p.read_text(encoding="utf-8", errors="replace")
        mtime = p.stat().st_mtime
    except Exception as exc:  # noqa: BLE001
        return {"found": False, "path": str(p), "mtime": 0.0, "content": "", "error": str(exc)}
    return {"found": True, "path": str(p), "mtime": mtime, "content": content}


def write_doc(kind: str, slug: str, content: str) -> str:
    """写入一篇文档（覆盖），返回最终路径字符串。"""
    p = doc_path(kind, slug)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.rstrip() + "\n", encoding="utf-8")
    return str(p)


def existing_slugs() -> dict[str, set[str]]:
    """已存在文档的 slug 集合：{"plugins": {...}, "modules": {...}}。"""
    out: dict[str, set[str]] = {}
    for dirname in ("plugins", "modules"):
        d = usage_root() / dirname
        out[dirname] = {f.stem for f in d.glob("*.md")} if d.is_dir() else set()
    return out
