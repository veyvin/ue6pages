#!/usr/bin/env python3
"""Generate a bilingual How-to-use card for every plugin/module page on gh-pages."""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
USAGE_ID = 'id="usage"'
AI_USAGE_DIR = ROOT / "scripts" / "ai_usage"


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def code(s: str) -> str:
    return f'<code class="usage-code">{esc(s)}</code>'


def format_step(text: str) -> str:
    """Turn `inline code` into usage-code spans; escape the rest."""
    parts = re.split(r"`([^`]+)`", text or "")
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(code(part))
        else:
            out.append(esc(part))
    return "".join(out)


def load_ai_usage() -> dict[tuple[str, str], dict]:
    out: dict[tuple[str, str], dict] = {}
    if not AI_USAGE_DIR.is_dir():
        return out
    for path in sorted(AI_USAGE_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "items" in data:
            data = data["items"]
        if isinstance(data, dict):
            iterable = data.values() if all(isinstance(v, dict) for v in data.values()) else []
        else:
            iterable = data
        for rec in iterable:
            if not isinstance(rec, dict):
                continue
            slug = rec.get("slug") or rec.get("id")
            kind = rec.get("kind")
            steps_cn = rec.get("cn_steps") or rec.get("steps_cn")
            steps_en = rec.get("en_steps") or rec.get("steps_en")
            if slug and kind and steps_cn and steps_en:
                out[(kind, slug)] = rec
    return out


def first(pattern: str, text: str, flags: int = 0) -> str:
    m = re.search(pattern, text, flags)
    return (m.group(1).strip() if m else "")


def parse_page(path: Path, kind: str) -> dict:
    text = path.read_text(encoding="utf-8")
    source = text
    usage_at = text.find('class="card usage-card"')
    if usage_at >= 0:
        source = text[:usage_at]
    name = first(r'<div class="hero-title(?: mono)?">([^<]+)</div>', source)
    if not name:
        name = first(r"<h1>([^<]+)</h1>", text)
    if " / " in name:
        name = name.split(" / ")[-1].strip()
    title = first(r"^title:\s*(.+)$", text, re.M) or name

    desc_cn = first(
        r'<div class="desc-body">[\s\S]*?<div class="lang-content active">([\s\S]*?)</div>',
        source,
    )
    desc_en = first(
        r'<div class="desc-body">[\s\S]*?<div class="lang-content(?: active)?">[\s\S]*?</div><div class="lang-content">([\s\S]*?)</div>',
        source,
    )
    if not desc_cn:
        desc_cn = first(
            r'<h2>Description / 描述</h2>\s*<div class="bilingual-block">[\s\S]*?<div class="lang-content active">([\s\S]*?)</div>',
            source,
        )
        desc_en = first(
            r'<h2>Description / 描述</h2>\s*<div class="bilingual-block">[\s\S]*?</div><div class="lang-content">([\s\S]*?)</div>',
            source,
        )
    desc_cn = re.sub(r"<[^>]+>", "", desc_cn or "").strip()
    desc_en = re.sub(r"<[^>]+>", "", desc_en or "").strip()

    category = first(
        r'chip chip-primary[\s\S]*?</span>\s*([^<]+)</span>',
        source,
    )
    if not category:
        category = first(
            r'<span class="label">类别</span>[\s\S]*?<div class="lang-content">([^<]+)</div>',
            source,
        )
    category = (category or "").strip()

    file_path = first(r'<div class="file-path mono">([^<]+)</div>', text)
    if not file_path:
        file_path = first(r"<code>(Engine/[^<]+)</code>", text)

    modules = re.findall(r'<span class="name mono">([^<]+)</span>', text)
    if not modules:
        raw = first(r'<span class="label">模块</span><span class="value">([^<]+)</span>', text)
        if raw:
            modules = [m.strip() for m in raw.split(",") if m.strip()]

    return {
        "kind": kind,
        "name": name or path.stem,
        "title": title,
        "desc_cn": desc_cn,
        "desc_en": desc_en,
        "category": category,
        "file_path": file_path,
        "modules": modules,
        "text": text,
        "path": path,
    }


def blob(info: dict) -> str:
    return " ".join(
        [
            info["kind"],
            info["name"],
            info["category"],
            info["file_path"],
            info["desc_en"],
            info["desc_cn"],
        ]
    ).lower()


def has_any(text: str, *needles: str) -> bool:
    for n in needles:
        if len(n) <= 3:
            if re.search(r'(^|[^a-z0-9])' + re.escape(n) + r'([^a-z0-9]|$)', text):
                return True
        elif n in text:
            return True
    return False


def path_norm(info: dict) -> str:
    return (info.get("file_path") or "").replace("\\", "/")


def plugin_place(info: dict) -> tuple[str, str]:
    p = path_norm(info).lower()
    name = info["name"]
    if "experimental" in p:
        return (
            f"{code(name)} 在 Experimental 目录，接口可能变动；先在空关卡验证再进正式内容。",
            f"{code(name)} is under Experimental and may change. Prove it in an empty map first.",
        )
    if "virtualproduction" in p or "virtualproduction" in p.replace("/", ""):
        return (
            f"启用后从 {code('Window > Virtual Production')} 打开与 {code(name)} 相关的面板或舞台工具。",
            f"After enabling, open the {code(name)} panel from {code('Window > Virtual Production')}.",
        )
    if "/media/" in p:
        return (
            f"在内容浏览器创建 Media Player / Media Source，或把 {code(name)} 提供的解码器接到 Electra / 媒体框架。",
            f"Create a Media Player / Media Source, or attach {code(name)}’s decoder to Electra / Media Framework.",
        )
    if "/fx/" in p or "niagara" in p:
        return (
            f"在内容浏览器右键 {code('FX / Niagara')}，创建 System 或把 {code(name)} 资产拖进关卡。",
            f"In Content Browser, {code('FX / Niagara')} → create a System, or drop {code(name)} assets into a level.",
        )
    if "/importers/" in p or "datasmith" in p or "interchange" in p:
        return (
            f"用内容浏览器「导入」或 Datasmith / Interchange 菜单，文件会走 {code(name)} 这条管线。",
            f"Import via Content Browser or Datasmith / Interchange — {code(name)} owns that pipeline.",
        )
    if "/ai/" in p:
        return (
            f"给角色或关卡加上 AI 组件 / Volume，并在行为树、State Tree 或 Mass 里引用 {code(name)}。",
            f"Add the AI component or volume, then reference {code(name)} from Behavior Tree, State Tree, or Mass.",
        )
    if "/runtime/" in p:
        return (
            f"{code(name)} 是运行时插件，启用后可进包装；在蓝图或 C++ 里直接调用其组件/子系统。",
            f"{code(name)} is a runtime plugin and can ship. Call its components or subsystems from Blueprint or C++.",
        )
    if "/editor/" in p or "/developer/" in p:
        return (
            f"{code(name)} 主要是编辑器工具。重启后在 {code('Window')} / {code('Tools')} / 模式工具栏找同名面板，不要加进游戏运行时依赖。",
            f"{code(name)} is editor-side. After restart, look under {code('Window')} / {code('Tools')} / mode toolbar. Do not add it as a game runtime dependency.",
        )
    if "/online/" in p or "onlinesubsystem" in p.replace(" ", ""):
        return (
            f"在 {code('DefaultEngine.ini')} 指定该 Online 实现，并配置平台凭证后，用 OSS / Online Services 调 {code(name)}。",
            f"Point {code('DefaultEngine.ini')} at this Online implementation, add credentials, then call {code(name)} through OSS / Online Services.",
        )
    return (
        f"启用 {code(name)} 后，在内容浏览器、细节面板或 Window 菜单搜索同名资产、组件、子系统。",
        f"After enabling {code(name)}, search Content Browser, Details, and Window menus for a same-named asset, component, or subsystem.",
    )


def plugin_workflow(info: dict) -> tuple[str, str]:
    b = blob(info)
    name = info["name"]
    desc_cn = info["desc_cn"] or info["desc_en"] or name
    desc_en = info["desc_en"] or info["desc_cn"] or name
    if has_any(b, "paper2d", "2d", "sprite", "tilemap"):
        return (
            f"操作：内容浏览器新建 Paper Sprite / Flipbook / Tile Map，拖进关卡；用 Paper2D 组件播动画。用途是：{esc(desc_cn)}。",
            f"Workflow: create Paper Sprite / Flipbook / Tile Map assets, drop them in a level, play via Paper2D components. Purpose: {esc(desc_en)}.",
        )
    if has_any(b, "niagara", "/fx/", "vfx"):
        return (
            f"操作：内容浏览器 {code('FX / Niagara')} 新建 System，拖进关卡，在 Niagara 编辑器调 {code(name)}。",
            f"Workflow: Content Browser {code('FX / Niagara')} → System → drop in level → tune {code(name)} in the Niagara editor.",
        )
    if has_any(b, "water"):
        return (
            "操作：放置 Water Body（Ocean / Lake / River）雕刻景观；运行时用 Water 模块查水面高度。",
            "Workflow: place Water Body (Ocean / Lake / River); query water height from the Water module at runtime.",
        )
    if has_any(b, "virtual production", "ndisplay", "live link", "livelink", "icvfx", "switchboard", "take recorder"):
        return (
            f"操作：接好摄像机/追踪，打开 Window > Virtual Production，在 Sequencer / nDisplay 里绑定 {code(name)}。",
            f"Workflow: hook up cameras/tracking, open Window > Virtual Production, bind {code(name)} in Sequencer / nDisplay.",
        )
    if has_any(b, "media player", "electra", "movie player", "decoder"):
        return (
            "操作：建 Media Player + Media Source，把 Media Texture 赋给材质或 Media Plate，蓝图 Open / Play / Pause。",
            "Workflow: Media Player + Media Source → Media Texture on a material/Media Plate → Open / Play / Pause.",
        )
    if has_any(b, "animation", "control rig", "ik rig", "pose search", "ml deformer", "metahuman", "uaf", "groom"):
        return (
            f"操作：把 {code(name)} 资产挂到骨架网格体，在动画蓝图或 Sequencer 轨道里采样。",
            f"Workflow: attach {code(name)} assets to a skeletal mesh; sample in AnimBP or Sequencer.",
        )
    if has_any(b, "rendering", "nanite", "gpu lightmass", "path tracer", "post process"):
        return (
            f"操作：项目设置或后期处理体积中打开 {code(name)}，用 Show Flag 对比，打包前确认 RHI。",
            f"Workflow: enable {code(name)} in Project Settings or a Post Process Volume; confirm RHI before packaging.",
        )
    if has_any(b, "audio", "metasound", "sound", "midi"):
        return (
            f"操作：创建 Sound / MetaSound，挂到 Sound 组件播放；项目设置 > Audio 里核对 {code(name)} 子混合。",
            f"Workflow: author Sound/MetaSound → Sound component; check {code(name)} in Project Settings > Audio.",
        )
    if has_any(b, "enhanced input", "controller", "xinput", "openxr"):
        return (
            f"操作：项目设置 > 输入映射动作，运行时用 Enhanced Input / OpenXR 读 {code(name)}。",
            f"Workflow: map actions in Project Settings > Input; read {code(name)} via Enhanced Input / OpenXR.",
        )
    if has_any(b, "online", "eos", "steam", "playfab", "replication", "iris"):
        return (
            f"操作：{code('DefaultEngine.ini')} 指定该 Online 实现并填凭证；client 与 server 都要启用 {code(name)}。",
            f"Workflow: point {code('DefaultEngine.ini')} at this Online impl, add credentials; enable {code(name)} on client and server.",
        )
    if has_any(b, "umg", "slate", "common ui", "web browser"):
        return (
            f"操作：Widget Blueprint 拖入 {code(name)} 控件，HUD / Player Controller Create Widget 后 Add to Viewport。",
            f"Workflow: drop {code(name)} widgets in a Widget Blueprint; Create Widget from HUD and Add to Viewport.",
        )
    if has_any(b, "mass", "state tree", "smart object", "navigation", "zone graph"):
        return (
            f"操作：关卡放 Volume / Smart Object，或给角色加组件，用 State Tree / Mass / 导航驱动 {code(name)}。",
            f"Workflow: place volumes/Smart Objects or add the component; drive {code(name)} with State Tree / Mass / navmesh.",
        )
    if has_any(b, "pcg", "procedural", "geometry script", "modeling"):
        return (
            f"操作：Modeling Mode 或 PCG Graph 把 {code(name)} 应用到选中 Actor；编辑器工具默认不进 Shipping。",
            f"Workflow: apply {code(name)} in Modeling Mode or a PCG Graph. Editor tools do not ship.",
        )
    if has_any(b, "importer", "datasmith", "usd", "alembic", "interchange", "gltf"):
        return (
            f"操作：内容浏览器「导入」或 Datasmith/USD 菜单走 {code(name)} 管线，再检查材质、单位、碰撞。",
            f"Workflow: Import or Datasmith/USD menus use {code(name)}; then check materials, units, collision.",
        )
    if has_any(b, "pixel streaming"):
        return (
            "操作：打包或 PIE 时启用 Pixel Streaming，用浏览器打开信令 URL，在项目设置里配 STUN/TURN。",
            "Workflow: enable Pixel Streaming for pack/PIE, open the signalling URL in a browser, set STUN/TURN.",
        )
    if has_any(b, "verse"):
        return (
            f"操作：在 Verse 设备或项目里引用 {code(name)} 的 API；改完 Verse 后编译并推到会话。",
            f"Workflow: call {code(name)} from Verse devices/code; compile Verse and push to the session.",
        )
    if has_any(b, "test", "gauntlet", "automation"):
        return (
            f"操作：Session Frontend / 自动化会话里跑 {code(name)} 相关用例，或命令行调用对应 Gauntlet/Automation 目标。",
            f"Workflow: run {code(name)} cases from Session Frontend / Automation, or the matching Gauntlet target.",
        )
    if has_any(b, "insights", "trace", "profiler"):
        return (
            f"操作：用 Unreal Insights 打开 trace，或 {code('Window > Developer Tools')} 里打开 {code(name)} 面板。",
            f"Workflow: open a trace in Unreal Insights, or {code(name)} under {code('Window > Developer Tools')}.",
        )
    if has_any(b, "chaos", "physics", "destruction"):
        return (
            f"操作：给网格开 Chaos / 物理，放置字段或破坏资产，运行时由 {code(name)} 模拟。",
            f"Workflow: enable Chaos/physics on meshes, place fields or destruction assets; {code(name)} simulates at runtime.",
        )
    place_cn, place_en = plugin_place(info)
    return (
        f"{place_cn} 围绕「{esc(desc_cn)}」来用：新建相关资产或把组件加到 Actor，在关卡里验证。",
        f"{place_en} Use it for “{esc(desc_en)}”: create the asset or add the component, then verify in a level.",
    )


def module_topic_steps(info: dict) -> tuple[list[str], list[str]]:
    b = blob(info)
    name = info["name"]
    p = path_norm(info)
    cn, en = [], []

    if "/Runtime/" in f"/{p}" or p.startswith("Runtime/"):
        cn.append(f"{code(name)} 是运行时模块，可以进游戏包；只在真正调用其 API 的模块里声明依赖。")
        en.append(f"{code(name)} is a runtime module and can ship. Depend on it only where you call its API.")
    elif p.startswith("Editor/") or "/Editor/" in p or name.endswith("Editor"):
        cn.append(f"{code(name)} 是编辑器模块，只能写进 *Editor.Build.cs 或编辑器插件，加进 Game Target 会链接失败。")
        en.append(f"{code(name)} is editor-only. Put it in *Editor.Build.cs or an editor plugin — never a Game target.")
    elif p.startswith("Developer/") or p.startswith("Programs/"):
        cn.append(f"{code(name)} 属于开发者工具或独立程序，给编辑器、Insights 或命令行用，不要当游戏运行时依赖。")
        en.append(f"{code(name)} is a developer/tool or program module (editor, Insights, CLI). Do not use it as game runtime.")
    elif "ThirdParty" in p:
        cn.append(f"{code(name)} 是第三方库的 UBT 封装。优先依赖引擎已经包好的上层模块，而不是直接依赖它。")
        en.append(f"{code(name)} wraps a third-party library. Prefer the engine module that already wraps it.")
    else:
        cn.append(f"在需要 {code(name)} 类型或函数的模块里声明依赖，然后包含其 Public 头文件。")
        en.append(f"Depend from the module that needs {code(name)} types, then include its Public headers.")

    if name.lower() in {"core", "engine"}:
        cn.append("普通游戏模块通常已间接依赖 Core/Engine，不必重复添加，除非你在写底层插件。")
        en.append("Typical game modules already pull Core/Engine transitively. Re-add them only for low-level plugins.")
    elif has_any(b, "slate", "umg"):
        cn.append(f"写 UI 时把 {code(name)} 和 Slate/SlateCore/UMG 一起加入 Public 依赖，头文件走 UUserWidget 或 SWidget。")
        en.append(f"For UI, list {code(name)} with Slate/SlateCore/UMG and include UUserWidget or SWidget headers.")
    elif has_any(b, "rendercore", "rhi", "shader"):
        cn.append(f"使用 {code(name)} 的渲染代码必须遵守渲染线程约束，不要在游戏线程直接改 RHI 资源。")
        en.append(f"Code that uses {code(name)} must respect the render thread; do not mutate RHI resources on the game thread.")
    elif has_any(b, "online", "replication", "iris", "netcore"):
        cn.append(f"{code(name)} 相关联网代码要在 client 与 server Target 同时列出。")
        en.append(f"List {code(name)} on both client and server targets for networking/replication.")

    ident = re.sub(r"[^A-Za-z0-9]", "", name)
    if ident:
        cn.append(f"头文件一般在该模块 Public 目录，常见形式 {code(ident + '.h')} 或 {code(ident + 'Module.h')}，以源码树为准。")
        en.append(f"Headers usually live in the module’s Public folder, often {code(ident + '.h')} or {code(ident + 'Module.h')}.")
    return cn, en


def plugin_caveat(info: dict) -> tuple[str, str]:
    p = path_norm(info).lower()
    name = info["name"]
    bits_cn, bits_en = [], []
    if "experimental" in p:
        bits_cn.append("Experimental，正式项目慎用")
        bits_en.append("Experimental — use with care in shipping projects")
    if "/editor/" in p or "/developer/" in p:
        bits_cn.append("编辑器插件，不要加进游戏运行时")
        bits_en.append("editor plugin, not a game runtime dependency")
    elif "/runtime/" in p:
        bits_cn.append("运行时插件，可以进包装")
        bits_en.append("runtime plugin, can ship")
    if "deprecated" in p or "deprecated" in name.lower():
        bits_cn.append("已标记 Deprecated")
        bits_en.append("marked Deprecated")
    if not bits_cn:
        bits_cn.append("具体 API 以该插件 Public 头文件为准")
        bits_en.append("treat the plugin’s Public headers as the API source of truth")
    return "注意：" + "；".join(bits_cn) + "。", "Note: " + "; ".join(bits_en) + "."


def plugin_steps(info: dict) -> tuple[list[str], list[str]]:
    name = info["name"]
    fp = info["file_path"] or "(plugin descriptor)"
    desc_cn = info["desc_cn"] or info["desc_en"] or name
    desc_en = info["desc_en"] or info["desc_cn"] or name
    cat = info["category"] or "Uncategorized"
    wf_cn, wf_en = plugin_workflow(info)
    place_cn, place_en = plugin_place(info)
    caveat_cn, caveat_en = plugin_caveat(info)
    mods = info["modules"]
    runtime = [m for m in mods if "Editor" not in m and "Test" not in m]
    editor = [m for m in mods if "Editor" in m]
    listed_rt = ", ".join(code(m) for m in runtime[:10]) or "（描述符未列出运行时模块）"
    listed_ed = ", ".join(code(m) for m in editor[:8])
    first_rt = runtime[0] if runtime else name.replace(" ", "")
    snippet = f'PublicDependencyModuleNames.AddRange(new string[] {{ "{esc(first_rt)}" }});'
    cn = [
        f"用途：「{esc(name)}」用于{esc(desc_cn)}。分类：{esc(cat)}。描述符：{code(fp)}。",
        f"启用：打开项目 → {code('编辑 > 插件')} → 搜索 {code(name)} → 勾选启用 → 重启编辑器。找不到时在 .uproject 的 Plugins 数组里写 {code(name)}。",
        f"入口：{place_cn}",
        wf_cn,
        f"蓝图：启用后在右键菜单、细节面板、组件列表搜索 {code(name)}；把组件加到 Actor 或从子系统取对象。",
        f"C++：游戏模块 {code('Build.cs')} 只加运行时模块 {listed_rt}。示例：{code(snippet)}。然后 Generate Project Files 并编译。头文件在 {code(first_rt)} 的 Public 目录。",
    ]
    en = [
        f"Purpose: {code(name)} — {esc(desc_en)}. Category: {esc(cat)}. Descriptor: {code(fp)}.",
        f"Enable: {code('Edit > Plugins')} → search {code(name)} → enable → restart. If missing, add it to the .uproject Plugins array.",
        f"Where: {place_en}",
        wf_en,
        f"Blueprint: search {code(name)} in context menus, Details, and Components; add the component or get the subsystem.",
        f"C++: in your game {code('Build.cs')} add runtime modules only: {listed_rt}. Example: {code(snippet)}. Then Generate Project Files and rebuild. Headers live under {code(first_rt)}/Public.",
    ]
    if listed_ed:
        cn.append(f"编辑器模块 {listed_ed} 只能写进 *Editor.Build.cs，加进 Game Target 会链接失败。")
        en.append(f"Editor modules {listed_ed} belong in *Editor.Build.cs only — never a Game target.")
    cn.append(caveat_cn)
    en.append(caveat_en)
    return cn, en


def module_purpose(info: dict) -> tuple[str, str]:
    name = info["name"]
    summary_cn = info["desc_cn"] or ""
    summary_en = info["desc_en"] or ""
    dep_only = summary_cn.startswith("该模块依赖") or summary_en.startswith("This module depends")
    p = path_norm(info)
    folder = p.split("/")[0] if p else "Engine"
    if dep_only or not summary_cn:
        return (
            f"用途：{code(name)} 位于 {code(folder)}，向其他模块提供 C++ API。构建规则：{code(p or name + '.Build.cs')}。",
            f"Purpose: {code(name)} lives under {code(folder)} and exposes a C++ API. Build rule: {code(p or name + '.Build.cs')}.",
        )
    return (
        f"用途：{esc(summary_cn)} 构建规则：{code(p or name + '.Build.cs')}。",
        f"Purpose: {esc(summary_en)} Build rule: {code(p or name + '.Build.cs')}.",
    )


def module_steps(info: dict) -> tuple[list[str], list[str]]:
    name = info["name"]
    fp = info["file_path"] or f"{name}.Build.cs"
    ident = re.sub(r"[^A-Za-z0-9]", "", name) or name
    snippet = f'PublicDependencyModuleNames.AddRange(new string[] {{ "{esc(name)}" }});'
    purpose_cn, purpose_en = module_purpose(info)
    extra_cn, extra_en = module_topic_steps(info)
    deps = info["modules"][:10]
    dep_txt = ", ".join(code(d) for d in deps) if deps else "无额外公开依赖"
    cn = [
        purpose_cn,
        f"依赖：打开 {code('YourModule.Build.cs')}，加入 {code(snippet)}。对外暴露 {code(name)} 类型用 Public，仅内部调用用 Private。然后 Generate Project Files 并编译。",
    ]
    en = [
        purpose_en,
        f"Depend: in {code('YourModule.Build.cs')} add {code(snippet)}. Use Public if you expose {code(name)} types, Private if you only call it. Then Generate Project Files and rebuild.",
    ]
    cn += extra_cn
    en += extra_en
    cn.append(f"调用：#include 其 Public 头（常见 {code(ident + '.h')} / {code(ident + 'Module.h')}），再用 {code('FModuleManager::LoadModulePtr<' + ident + 'Module>')} 或直接用类型。")
    en.append(f"Call: include Public headers (often {code(ident + '.h')} / {code(ident + 'Module.h')}), then use the types or {code('FModuleManager::LoadModulePtr<' + ident + 'Module>')}.")
    cn.append(f"传递依赖：{code(name)} 还依赖 {dep_txt}。不必在游戏模块重复填写，除非你要直接 include 那些头文件。")
    en.append(f"Transitive deps: {code(name)} also needs {dep_txt}. Do not re-list them unless you include their headers.")
    return cn, en


def ol(items: list[str]) -> str:
    lis = "".join(f"<li>{item}</li>" for item in items)
    return f'<ol class="usage-steps">{lis}</ol>'


def pending_steps(info: dict) -> tuple[list[str], list[str], str, str]:
    name = info["name"]
    kind_cn = "插件" if info["kind"] == "plugin" else "模块"
    kind_en = "plugin" if info["kind"] == "plugin" else "module"
    cn = [
        f"{code(name)} 的使用方法还没按这一份{kind_cn}单独写完。"
        "这里故意不再套「编辑 > 插件启用 / 在 Build.cs 加依赖」的通用模板。"
    ]
    en = [
        f"Per-item how-to for {code(name)} is not written yet."
        f" A generic enable-{kind_en} / Build.cs template is intentionally omitted."
    ]
    return (
        cn,
        en,
        "正在逐条用 AI 按该条目的真实工作流补全。",
        "Being filled one item at a time from that item’s real workflow.",
    )


def usage_card_html(info: dict, rec: dict | None = None, *, allow_template: bool = False) -> str:
    source = "pending"
    if rec:
        source = "ai"
        cn_items = [format_step(s) for s in rec.get("cn_steps") or rec.get("steps_cn") or []]
        en_items = [format_step(s) for s in rec.get("en_steps") or rec.get("steps_en") or []]
        note_cn = esc(rec.get("note_cn") or "由 AI 按该插件/模块的实际工作流逐条写出，不是按类别套模板。")
        note_en = esc(rec.get("note_en") or "Written per item from that plugin/module’s real workflow, not a category template.")
    elif allow_template:
        source = "template"
        if info["kind"] == "plugin":
            cn_items, en_items = plugin_steps(info)
            note_cn = "以上步骤根据插件类别、描述符路径和模块列表生成，便于快速上手；具体 API 以引擎头文件为准。"
            note_en = "Steps are derived from the plugin category, descriptor path, and module list. Treat engine headers as the source of truth."
        else:
            cn_items, en_items = module_steps(info)
            note_cn = "以上步骤根据 Build.cs 路径与依赖生成。把模块加进错误的 Target（例如把 Editor 模块加进 Game）会导致链接失败。"
            note_en = "Steps come from the Build.cs path and dependencies. Linking an Editor module into a Game target will fail."
    else:
        cn_items, en_items, note_cn, note_en = pending_steps(info)

    inner = (
        '<div class="bilingual-block"><div class="lang-tabs">'
        '<button class="lang-tab active" onclick="switchLang(this)">中文</button>'
        '<button class="lang-tab" onclick="switchLang(this)">English</button>'
        "</div>"
        f'<div class="lang-content active">{ol(cn_items)}<p class="usage-note">{note_cn}</p></div>'
        f'<div class="lang-content">{ol(en_items)}<p class="usage-note">{note_en}</p></div>'
        "</div>"
    )
    # Inline CSS so daily CI rewrite of assets/style.css cannot drop the section look.
    return (
        f'    <div class="card usage-card" {USAGE_ID} data-usage-source="{source}">\n'
        "      <style>"
        ".usage-steps{margin:0;padding-left:22px}"
        ".usage-steps li{margin-bottom:12px;line-height:1.7}"
        ".usage-steps li:last-child{margin-bottom:0}"
        ".usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;"
        "background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}"
        ".usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}"
        ".usage-card .desc-body .bilingual-block{margin-bottom:0}"
        "</style>\n"
        '      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>\n'
        f'      <div class="desc-body">{inner}</div>\n'
        "    </div>\n"
    )


def find_div_span(text: str, start: int) -> tuple[int, int] | None:
    i = text.find("<div", start)
    if i < 0:
        return None
    depth = 0
    pos = i
    while pos < len(text):
        nxt_open = text.find("<div", pos)
        nxt_close = text.find("</div>", pos)
        if nxt_close < 0:
            return None
        if nxt_open >= 0 and nxt_open < nxt_close:
            depth += 1
            pos = nxt_open + 4
        else:
            depth -= 1
            pos = nxt_close + 6
            if depth == 0:
                return i, pos
    return None


def strip_existing_usage(text: str) -> str:
    marker = text.find('class="card usage-card"')
    if marker < 0:
        return text
    div_start = text.rfind("<div", 0, marker + 1)
    span = find_div_span(text, div_start)
    if not span:
        return text
    start, end = span
    h2 = text.rfind("<h2", 0, start)
    if h2 >= 0 and "usage" in text[h2:start].lower():
        start = h2
    return (text[:start] + text[end:]).replace("\n\n\n", "\n\n")


def inject(text: str, card: str) -> str:
    text = strip_existing_usage(text)
    aside = text.find('  <aside class="detail-sidebar">')
    if aside != -1:
        left = text.rfind("  </div>", 0, aside)
        if left != -1:
            return text[:left] + card + "\n" + text[left:]
    legacy = card.lstrip()
    return text.rstrip() + "\n\n" + legacy + "\n"


def process_dir(kind: str, ai: dict[tuple[str, str], dict], allow_template: bool) -> tuple[int, int, int]:
    folder = ROOT / ("plugins" if kind == "plugin" else "modules")
    ok = skip = ai_n = 0
    pending_all = "--pending-missing" in sys.argv
    for path in sorted(folder.glob("*.md")):
        info = parse_page(path, kind)
        if not info["name"]:
            skip += 1
            continue
        rec = ai.get((kind, path.stem))
        if rec:
            ai_n += 1
        elif not allow_template and not pending_all:
            # Keep existing page text until this item has a per-item AI usage record.
            skip += 1
            continue
        card = usage_card_html(info, rec, allow_template=allow_template)
        new_text = inject(info["text"], card)
        if new_text != info["text"]:
            path.write_text(new_text, encoding="utf-8")
            ok += 1
        else:
            skip += 1
    return ok, skip, ai_n


def main() -> int:
    allow_template = "--templates" in sys.argv
    ai = load_ai_usage()
    print(f"ai usage records={len(ai)} templates={'on' if allow_template else 'off'}")
    p_ok, p_skip, p_ai = process_dir("plugin", ai, allow_template)
    m_ok, m_skip, m_ai = process_dir("module", ai, allow_template)
    print(f"plugins updated={p_ok} skipped={p_skip} ai={p_ai}")
    print(f"modules updated={m_ok} skipped={m_skip} ai={m_ai}")
    print(f"total updated={p_ok + m_ok}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
