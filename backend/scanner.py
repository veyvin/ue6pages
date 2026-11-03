"""扫描 UE 源码树，抽取插件 & 模块元数据。

逻辑从 scripts/generate_docs.py 的 discover_uplugins / discover_build_cs 提取出来，
改为直接返回结构化 dict，不写 Markdown。
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .config import CONFIG
from .schemas import PluginInfo, PluginModule, ModuleInfo


# ---------- 工具 ----------
def slugify(name: str) -> str:
    name = re.sub(r"[^\w\- ]+", "", name)
    name = re.sub(r"\s+", "-", name.strip().lower())
    return name or "item"


def assign_slugs(items: list[dict], name_key: str = "name") -> None:
    seen: dict[str, int] = {}
    for it in items:
        base = slugify(it.get(name_key, ""))
        if base in seen:
            seen[base] += 1
            it["slug"] = f"{base}-{seen[base]}"
        else:
            seen[base] = 0
            it["slug"] = base


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
            "path": str(uplugin.relative_to(engine_root)),
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

    # public deps
    deps: list[str] = []
    for m in re.finditer(
        r'PublicDependencyModuleNames\s*(?:\.Add|\.AddRange\s*\(\s*new\s+string\[\]\s*\{)([^}]*)\}',
        text, re.DOTALL,
    ):
        deps.extend(re.findall(r'"([^"]+)"', m.group(1)))
    # private deps
    priv_deps: list[str] = []
    for m in re.finditer(
        r'PrivateDependencyModuleNames\s*(?:\.Add|\.AddRange\s*\(\s*new\s+string\[\]\s*\{)([^}]*)\}',
        text, re.DOTALL,
    ):
        priv_deps.extend(re.findall(r'"([^"]+)"', m.group(1)))

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
            info["path"] = str(cs.relative_to(engine_root))
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
