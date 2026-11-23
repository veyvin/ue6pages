"""扫描 UE 源码树，抽取插件 & 模块元数据。

逻辑从 scripts/generate_docs.py 的 discover_uplugins / discover_build_cs 提取出来，
改为直接返回结构化 dict，不写 Markdown。
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .config import CONFIG
from .schemas import PluginInfo, PluginModule, ModuleInfo


# ---------- 工具 ----------
def slugify(name: str) -> str:
    """与 scripts/generate_docs.py 保持完全一致，否则后端与 gh-pages 目录对不上。"""
    s = re.sub(r"[^A-Za-z0-9._-]+", "-", (name or "").strip()).strip("-").lower()
    return s or "unknown"


def assign_slugs(items: list[dict], name_key: str = "name", path_key: str = "path") -> None:
    """重名条目用路径 hash 后缀，与 generate_docs.assign_slugs 规则相同。"""
    base = {i: slugify(str(it.get(name_key, ""))) for i, it in enumerate(items)}
    counts: dict[str, int] = {}
    for s in base.values():
        counts[s] = counts.get(s, 0) + 1
    for i, s in base.items():
        if counts[s] > 1:
            raw = str(items[i].get(path_key, "")).replace("\\", "/")
            h = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:6]
            items[i]["slug"] = f"{s}-{h}"
        else:
            items[i]["slug"] = s


# ---------- 插件 ----------
def discover_uplugins(engine_root: Path) -> list[PluginInfo]:
    results: list[dict] = []
    plugins_root = engine_root / CONFIG.scan.plugins_dir
    if not plugins_root.exists():
        return []

    for uplugin in sorted(plugins_root.rglob("*.uplugin")):
        try:
            data: dict[str, Any] = json.loads(uplugin.read_text(encoding="utf-8"))
        except Exception:
            continue

        modules = [
            PluginModule(
                name=m.get("Name", ""),
                type=m.get("Type", "Runtime"),
            )
            for m in data.get("Modules", [])
        ]

        info: dict[str, Any] = {
            "slug": "",
            "name": data.get("FriendlyName") or uplugin.parent.name,
            "version": str(data.get("Version", "")),
            "version_name": data.get("VersionName", ""),
            "category": data.get("Category", ""),
            "author": data.get("CreatedBy", ""),
            "engine_version": data.get("EngineVersion", ""),
            "description": data.get("Description", ""),
            "path": uplugin.relative_to(engine_root).as_posix(),
            "modules": [m.model_dump() for m in modules],
        }
        results.append(info)

    assign_slugs(results, "name")
    return [PluginInfo(**r) for r in results]


# ---------- 模块 ----------
def _parse_module_type(text: str) -> str:
    for kw in ("ModuleType.Runtime", "ModuleType.Editor",
               "ModuleType.Developer", "ModuleType.Game"):
        if kw in text:
            return kw.split(".")[-1]
    return "Runtime"


def parse_build_cs(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    name = path.stem
    m = re.search(r"class\s+(\w+)\s*:\s*ModuleRules", text)
    if m:
        name = m.group(1)

    mtype = _parse_module_type(text)

    # public / private deps：AddRange(new[]{...}) 与逐个 Add("X") 两种写法都要覆盖
    def _deps(prefix: str) -> list[str]:
        out: list[str] = []
        pat_range = re.compile(
            rf"{prefix}DependencyModuleNames\.AddRange\s*\(\s*new\s*(?:string)?\[\]\s*\{{([^}}]*)\}}",
            re.DOTALL,
        )
        pat_add = re.compile(
            rf'{prefix}DependencyModuleNames\.Add\s*\(\s*"([A-Za-z0-9_.]+)"\s*\)'
        )
        for m in pat_range.finditer(text):
            out.extend(re.findall(r'"([A-Za-z0-9_.]+)"', m.group(1)))
        for m in pat_add.finditer(text):
            out.append(m.group(1))
        return list(dict.fromkeys(out))

    deps = _deps("Public")
    priv_deps = _deps("Private")

    base_match = re.search(r'\b(\w+)\s*\(\s*ReadOnlyTargetRules', text)
    base = base_match.group(1) if base_match else "ModuleRules"

    # platform = 第一行 `public class X : ModuleRules` 之后是否有 Target.PlatformType check
    plat = ""
    if any(k in text for k in ("Win64", "bBuildEditor")):
        plat = "Win64"

    return {
        "name": name,
        "type": mtype,
        "path": str(path),
        "description": "",
        "base": base,
        "public_deps": deps,
        "private_deps": priv_deps,
        "platform": plat,
    }


def discover_build_cs(engine_root: Path) -> list[ModuleInfo]:
    results: list[dict] = []
    source_root = engine_root / CONFIG.scan.source_dir
    if not source_root.exists():
        return []
    for cs in sorted(source_root.rglob("*.Build.cs")):
        info = parse_build_cs(cs)
        info["slug"] = ""
        # 归一化 path 为相对
        try:
            info["path"] = cs.relative_to(engine_root).as_posix()
        except ValueError:
            pass
        results.append(info)

    assign_slugs(results, "name")
    return [ModuleInfo(**r) for r in results]


# ---------- 缓存层 ----------
_CACHE: dict[str, Any] = {"plugins": None, "modules": None}


def scan_all(force: bool = False) -> tuple[list[PluginInfo], list[ModuleInfo]]:
    """扫描全部；force=True 强制重扫。"""
    if not force and _CACHE["plugins"] is not None:
        return _CACHE["plugins"], _CACHE["modules"]

    root = Path(CONFIG.engine_root)
    plugins = discover_uplugins(root)
    modules = discover_build_cs(root)
    _CACHE["plugins"] = plugins
    _CACHE["modules"] = modules
    return plugins, modules


def invalidate_cache() -> None:
    _CACHE["plugins"] = None
    _CACHE["modules"] = None
