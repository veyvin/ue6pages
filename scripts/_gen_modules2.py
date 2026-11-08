#!/usr/bin/env python3
"""Regenerate per-module AI usage with domain-aware, module-specific content.

Unlike the old one-size template, this classifies each module into a functional
domain (rendering, audio, networking, AI, physics, platform, editor, third-party,
program/toolchain, data, tests, core infra, ...) and writes domain-specific
"what it is / how to use it" text, while still using that module's real name,
folder and dependency list.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODS = json.loads((ROOT / "scripts" / "catalog" / "modules.json").read_text(encoding="utf-8"))
OUT = ROOT / "scripts" / "ai_usage"


def humanize(name: str) -> str:
    s = re.sub(r"[_\-]+", " ", name)
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", s)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def folder_of(path: str) -> str:
    return path.split("/")[0] if path else "Engine"


def placement_kind(path: str, name: str) -> str:
    p = path.replace("\\", "/")
    folder = folder_of(p)
    if "ThirdParty" in p:
        return "thirdparty"
    if folder == "Programs" or p.startswith("Programs/"):
        return "program"
    if folder == "Developer":
        return "developer"
    if folder == "Editor" or name.endswith("Editor") or "/Editor/" in p:
        return "editor"
    return "runtime"


# Functional-domain classification (name tokens + path + deps).
def domain_of(name: str, path: str, deps: list[str]) -> str:
    n = name.lower()
    p = path.replace("\\", "/").lower()

    if "thirdparty" in p or folder_of(path) == "ThirdParty":
        return "thirdparty"
    if folder_of(path) == "Programs":
        return "toolchain"
    # online/networking by path
    if "/online/" in p or n.startswith("online") or "onlinesubsystem" in n:
        return "networking"
    # platform / device
    if re.search(r"(targetplatform|platformeditor|platformsettings|platformfeatures|devicedetection|deviceprofile|android|ios\b|linux|mac\b|macos|windows|gdk|xb1|ps4|ps5|switch|hololens|tvos|devicemanager|hardwaresurvey|marketplacekit)", n):
        return "platform"
    # XR / VR
    if re.search(r"(openxr|\bxr\b|hmd|headmounted|\bvr\b|mixedreality|handtracking|eyetracker)", n):
        return "xr"
    # audio
    if re.search(r"(audio|sound|metasound|dsp|mixer|reverb|synth|adpcm|vorbis|resampl|opus|radiomagus|waves|wasapi|xaudio|coreaudio|audiolink|audioformat|radaudio|binkaudio)", n):
        return "audio"
    # media / video
    if re.search(r"(media|movie|electra|decoder|encoder|avf|wmf|bink|avi\b|libav|video|codecs)", n):
        return "media"
    # ML / neural inference
    if re.search(r"(\bnne\b|neural|onnx|inference|torch)", n):
        return "ml"
    # rendering / RHI / compute / shader
    if re.search(r"(rhi|render|shader|hlsl|nanite|lumen|d3d|vulkan|metal|opengl|dx1[12]|virtualshadow|raytrac|tracer|tonemap|virtualtexture|texture|postprocess|material|cuda|compute|gpudirect)", n):
        return "rhi_rendering"
    # geometry / mesh / world building
    if re.search(r"(mesh|geometry|landscape|foliage|ispool|\bbsp\b|bsputil|cadkernel|cad\b|hierarchicallod)", n):
        return "geometry"
    # image / color
    if re.search(r"(image|iesfile|colorio|opencolorio)", n):
        return "image"
    # physics / chaos
    if re.search(r"(chaos|physics|apex|destruction|vehicle|cloth|collision|rigidbody|implicit|fracture|fieldnotification|fieldsystem|physicsfield)", n):
        return "physics"
    # animation
    if re.search(r"(anim|skeletalmesh|persona|controlrig|\bik\b|ikrig|poser|blend|groom|metahuman|\bdna\b|morph|livelink|constraint)", n):
        return "animation"
    # AI / navigation
    if re.search(r"(aimodule|navigation|navmesh|recast|mass|behavior.?tree|statetree|smartobject|zonegraph|perception|aigraph|aisupport|gameplaybehaviors|envquery)", n):
        return "ai_nav"
    # UI
    if re.search(r"(slate|umg|widget|overlay|commonui|appframework|desktopwidgets|advancedwidgets|friends|andchat|menubuilder|game.?menu)", n):
        return "ui"
    # input
    if re.search(r"(inputcore|inputdevice|xinput|rawinput|\bhid\b|gamepad|steamcontroller)", n):
        return "input"
    # networking / online (name based)
    if re.search(r"(\bnet|iris|socket|http|websocket|replication|messag|packet|steam|\beos\b|playfab|\boss\b|rpc|mcp|nats|cares|dtls|quic|bandwidth|icmp|eventloop)", n):
        return "networking"
    # analytics / telemetry
    if re.search(r"(analytic|telemetry|swrve)", n):
        return "analytics"
    # asset pipeline / cook / exchange
    if re.search(r"(assetregistry|assettools|interchange|datasmith|importer|\busd\b|deriveddata|cook|pakfile|\bpak\b|package|buildpatch|\bzen\b|dataflow|directlink|installbundle)", n):
        return "asset_pipeline"
    # localization
    if re.search(r"(localization|locres|internationalization)", n):
        return "localization"
    # data / serialization
    if re.search(r"(json|xml|cbor|serial|config|\bini\b|msgpack|uobject|structuredlog|trace.?log|fmt|rapidjson|\bcsv\b|mathcore|oodledata)", n):
        return "data"
    # verse
    if n.startswith("verse") or n in ("verseengine", "versevm"):
        return "verse"
    # tests / automation framework
    if re.search(r"(test|suite|mock|gauntlet|automation|clientpilot)", n):
        return "tests"
    # build / dev toolchain
    if re.search(r"(horde|livecoding|hotreload|crash|crashreport|unrealinsights|toolchain|unrealbuild|\bubt\b|benchmark|deriveddataexecutor)", n):
        return "toolchain"
    # misc refinements
    if re.search(r"(unrealgame)", n):
        return "gameplay"
    if re.search(r"(webbrowser|cef3|cef)", n):
        return "ui"
    if re.search(r"(ulang)", n):
        return "toolchain"
    if re.search(r"(iostore|storage|s3client|streamingfile|assetcache|virtualization|zenoplog)", n):
        return "asset_pipeline"
    if re.search(r"(sourcecontrol|submittool|turnkey|sessionservices|sessionfrontend|preloadscreen)", n):
        return "toolchain"
    if re.search(r"(^ios(?!tore))", n):
        return "platform"
    # editor (path based)
    if placement_kind(path, name) == "editor" or folder_of(path) == "Editor":
        return "editor"
    # core infra
    if re.search(r"(^core$|coreuobject|applicationcore|trace|logging|memory|containers|misc\b|\bhal\b|fileutilities|modules|^build|platformmisc|engine$|launch|cookmetadata|\bipc\b|instrumentation|asyncfunctionresult|nulldrv|eventloop)", n):
        return "core_infra"
    # gameplay
    if re.search(r"(gameplay|ability|kismet|blueprint|engine|world|actor|pawn|player|camera|\bgame\b|level|foliage)", n):
        return "gameplay"
    return "core_infra" if folder_of(path) == "Engine" else "general"


# Per-domain (what_cn, how_cn, what_en, how_en)
DOMAIN = {
    "thirdparty": (
        "它是对一个第三方库的 UBT 封装，向引擎暴露该库的功能",
        "一般不要直接依赖它；优先用引擎里已封装好该库的上层模块。确需使用时把本模块加进 Build.cs，并包含其第三方头文件",
        "it wraps a third-party library and exposes its functionality to the engine",
        "usually do not depend on it directly; prefer the engine module that already wraps it. If truly needed, add it to Build.cs and include the third-party headers",
    ),
    "platform": (
        "它提供某个目标平台/设备的支持（平台识别、设置、打包、设备探测）",
        "平台能力会在切换目标平台或打包时自动带出，通常不需要在游戏模块里显式依赖；只有写平台相关原生代码时才直接 include",
        "it provides support for a target platform/device (detection, settings, packaging, device probing)",
        "platform support is pulled in automatically when targeting/packaging for that platform; you rarely depend on it directly — only include it for platform-specific native code",
    ),
    "xr": (
        "它提供 XR/VR/AR 能力（OpenXR、HMD 与手柄追踪、手势等）",
        "在 XR/VR 项目里启用对应 XR 插件，通过 XR 子系统读取头显/手柄姿态与输入",
        "it provides XR/VR/AR capability (OpenXR, HMD and controller tracking, hands, etc.)",
        "in XR/VR projects enable the matching XR plugin and read headset/controller pose and input through the XR subsystem",
    ),
    "audio": (
        "它属于音频系统（混音、解码、合成、DSP、空间音频、编解码）",
        "创建 Sound/MetaSound 或用音频组件播放时会用到；在 项目设置 > Audio 里配置子混音与编解码器",
        "it is part of the audio system (mixing, decoding, synthesis, DSP, spatial audio, codecs)",
        "used when authoring Sound/MetaSound or playing through audio components; configure submixes and codecs in Project Settings > Audio",
    ),
    "media": (
        "它属于媒体/视频框架（播放器、解码/编码器、Movie、Electra、编解码）",
        "建 Media Player + Media Source，用 Media Texture 把视频贴到材质/Media Plate 上播放；解码器会接到 Electra/Media Framework",
        "it is part of the media/video framework (players, decoders/encoders, Movie, Electra, codecs)",
        "create a Media Player + Media Source and play via Media Texture on a material/Media Plate; decoders plug into Electra/Media Framework",
    ),
    "rhi_rendering": (
        "它属于渲染/RHI 层（图形后端、着色器、渲染管线、纹理/后处理）",
        "在渲染线程/材质/后处理相关代码里使用；不要从游戏线程直接改 RHI 资源，需遵守渲染线程约束",
        "it is part of the rendering/RHI layer (graphics backend, shaders, pipeline, textures/post-process)",
        "use it from render-thread/material/post-process code; never mutate RHI resources from the game thread — respect render-thread rules",
    ),
    "physics": (
        "它属于物理/Chaos（刚体、碰撞、破坏、车辆、布料、物理场）",
        "给网格开启物理/Chaos，放置字段或破坏资产；运行时由物理系统模拟，代码里查询碰撞与物理状态",
        "it is part of physics/Chaos (rigid bodies, collisions, destruction, vehicles, cloth, fields)",
        "enable physics/Chaos on meshes and place fields or destruction assets; the physics system simulates at runtime and you query collisions/state from code",
    ),
    "animation": (
        "它属于动画系统（骨架、动画图、Control Rig、IK、姿态、MetaHuman/DNA）",
        "把资产挂到骨架网格体、在动画蓝图或 Sequencer 轨道采样；动画逻辑放在 AnimGraph 或 C++ AnimNode",
        "it is part of the animation system (skeleton, anim graph, Control Rig, IK, pose, MetaHuman/DNA)",
        "attach assets to a skeletal mesh and sample in AnimBP or Sequencer; animation logic lives in AnimGraph or C++ AnimNodes",
    ),
    "ai_nav": (
        "它属于 AI/导航（行为树、StateTree、寻路、Mass、感知、Smart Object、ZoneGraph）",
        "给角色加 AI 组件、放 NavMesh/Volume 或 Smart Object，在行为树/StateTree/Mass 里驱动行为",
        "it is part of AI/navigation (Behavior Tree, StateTree, pathing, Mass, perception, Smart Objects, ZoneGraph)",
        "add AI components to characters and place NavMesh/volumes or Smart Objects; drive behavior via Behavior Tree/StateTree/Mass",
    ),
    "ui": (
        "它属于 UI 层（Slate/UMG/Widget/Overlay/CommonUI/AppFramework）",
        "在 Widget Blueprint 或 Slate C++ 里使用；把它们和 Slate/SlateCore/UMG 一起加入依赖",
        "it is part of the UI layer (Slate/UMG/Widget/Overlay/CommonUI/AppFramework)",
        "use it from Widget Blueprints or Slate C++; list it alongside Slate/SlateCore/UMG",
    ),
    "input": (
        "它属于输入设备/输入系统（手柄、键鼠、触控、HID、RawInput）",
        "在 项目设置 > 输入 里映射动作，运行时通过 Enhanced Input 或 InputDevice 读取",
        "it is part of the input devices/system (gamepads, keyboard/mouse, touch, HID, RawInput)",
        "map actions in Project Settings > Input and read them via Enhanced Input or the InputDevice at runtime",
    ),
    "networking": (
        "它属于网络/在线（复制、Iris、Sockets、HTTP/RPC、Online 子系统、消息总线、MCP）",
        "联网代码要在 client 与 server Target 都列出；在线服务在 DefaultEngine.ini 指定实现并配置凭证",
        "it is part of networking/online (replication, Iris, Sockets, HTTP/RPC, Online subsystem, message bus, MCP)",
        "list it on both client and server targets; point DefaultEngine.ini at the Online implementation and add credentials",
    ),
    "asset_pipeline": (
        "它属于资产管线（导入/交换、Datasmith/USD、DDC、Cook、Pak、资产注册）",
        "通过内容浏览器导入或 Datasmith/USD 菜单走此管线；Cook/打包会自动参与，注意单位、材质、碰撞",
        "it is part of the asset pipeline (import/interchange, Datasmith/USD, DDC, Cook, Pak, asset registry)",
        "import via Content Browser or Datasmith/USD menus; Cook/packaging uses it automatically — watch units, materials, collision",
    ),
    "toolchain": (
        "它是构建/工具/独立程序（UBT、Horde、Insights、Automation、命令行 Program）",
        "作为独立程序或命令行工具运行，不进游戏运行时；用于构建、CI、性能分析等",
        "it is a build/tool/standalone Program (UBT, Horde, Insights, Automation, CLI)",
        "run it as a standalone program/CLI; it does not ship in the game — used for builds, CI, profiling",
    ),
    "data": (
        "它属于数据/序列化（JSON/XML/Config/结构体序列化/日志）",
        "在需要读写结构化数据或配置的代码里 include 其头文件，直接调用其序列化/解析 API",
        "it is part of data/serialization (JSON/XML/Config/struct serialization/logging)",
        "include its headers where you read/write structured data or config and call its serialization/parse API",
    ),
    "verse": (
        "它属于 Verse 脚本运行时（面向 UEFN/Fortnite 体验）",
        "在 Verse 项目/设备里调用其 API；改完 Verse 代码后编译并推到会话",
        "it is part of the Verse scripting runtime (for UEFN/Fortnite experiences)",
        "call its API from Verse projects/devices; compile Verse and push to the session after edits",
    ),
    "tests": (
        "它是测试模块/测试套件（自动化、Gauntlet、Mock）",
        "在 Session Frontend/自动化里运行，或由 CI 触发对应自动化目标；不要打进发行版本",
        "it is a test module/suite (automation, Gauntlet, mocks)",
        "run it from Session Frontend/automation or trigger the matching target from CI; do not ship it",
    ),
    "core_infra": (
        "它属于核心基础设施（容器、日志、内存、平台抽象、模块加载、构建元数据）",
        "几乎被所有模块间接依赖；一般无需显式添加，除非你在写底层插件或工具",
        "it is core infrastructure (containers, logging, memory, platform abstraction, module loading, build metadata)",
        "almost every module depends on it transitively; you rarely add it explicitly unless writing low-level plugins/tools",
    ),
    "editor": (
        "它是编辑器侧工具模块（编辑器 UI、面板、细节定制、资产编辑器）",
        "仅编辑器使用，写进 *Editor.Build.cs；重启后在 Window/Tools 菜单或资产编辑器里找对应面板",
        "it is an editor-side tool module (editor UI, panels, detail customization, asset editors)",
        "editor-only; put it in *Editor.Build.cs. After restart, find the panel under Window/Tools or in the relevant asset editor",
    ),
    "gameplay": (
        "它属于玩法/引擎框架（Actor、Pawn、World、Blueprint 运行时、Gameplay 系统）",
        "游戏逻辑主体；在 C++/蓝图里直接用其类型或相关子系统",
        "it is part of the gameplay/engine framework (Actor, Pawn, World, Blueprint runtime, Gameplay systems)",
        "core game logic; use its types or related subsystems directly from C++/Blueprint",
    ),
    "analytics": (
        "它属于遥测/分析（Analytics Provider，把事件上报到后端）",
        "通过项目的 AnalyticsProvider 配置后端（如 ET/Swrve/Horde），业务侧调用 RecordEvent 上报事件",
        "it is part of telemetry/analytics (Analytics Provider reporting events to a backend)",
        "configure the backend via the project's AnalyticsProvider (e.g. ET/Swrve/Horde) and report events from gameplay via RecordEvent",
    ),
    "image": (
        "它属于图像处理/编解码（像素格式、图像读写、颜色管理）",
        "在导入/导出纹理、运行时读写像素或做色彩空间转换时用；常与 ImageCore/ImageWrapper 配合",
        "it is part of image processing/codecs (pixel formats, image read/write, color management)",
        "used when importing/exporting textures, reading pixels at runtime, or converting color space; often paired with ImageCore/ImageWrapper",
    ),
    "geometry": (
        "它属于几何/网格/世界构建（Mesh、Geometry、Landscape、Foliage、CAD、BSP）",
        "在建模模式、几何脚本、Landscape/Foliage 编辑或 CAD 导入时用；几何算法多在 GeometryScript/MeshDescription 之上",
        "it is part of geometry/mesh/world building (Mesh, Geometry, Landscape, Foliage, CAD, BSP)",
        "used in Modeling mode, geometry scripts, Landscape/Foliage editing, or CAD import; geometry algorithms sit atop GeometryScript/MeshDescription",
    ),
    "localization": (
        "它属于本地化（翻译、文化、.locres/.po 资源）",
        "在 Localization Dashboard 管理翻译与文化，运行时文本用 FText/LOCTEXT 标记以支持切换语言",
        "it is part of localization (translations, cultures, .locres/.po assets)",
        "manage translations/cultures in the Localization Dashboard and mark runtime text with FText/LOCTEXT to support language switching",
    ),
    "ml": (
        "它是神经网络/推理模块（NNE 等模型部署与推理）",
        "把训练好的模型部署进项目，通过 NNE/推理接口在运行时做前向计算",
        "it is a neural-network/inference module (NNE model deployment and inference)",
        "deploy a trained model into the project and run forward inference at runtime through the NNE/inference interface",
    ),
    "general": (
        "它向其他模块提供 C++ API/功能",
        "在需要其类型或函数的模块里声明依赖，然后包含其 Public 头文件",
        "it exposes C++ API/functionality to other modules",
        "declare a dependency from the module that needs its types and include its Public headers",
    ),
}

PLACEMENT = {
    "editor": ("编辑器模块，只能写进 *Editor.Build.cs 或编辑器插件，加进 Game Target 会链接失败", "editor-only; put it in *Editor.Build.cs or an editor plugin — never a Game target"),
    "developer": ("开发者/工具模块，供编辑器或命令行使用，不要当游戏运行时依赖", "developer/tool module for editor or CLI use; not a game runtime dependency"),
    "program": ("独立程序(Programs)，给命令行/工具用，不进游戏运行时", "standalone Program; used by CLI/tools, not game runtime"),
    "thirdparty": ("第三方库封装，优先依赖引擎已包好的上层模块", "third-party library wrapper; prefer the engine module that wraps it"),
    "runtime": ("运行时模块，可进游戏包；只在真正调用其 API 的模块里声明依赖", "runtime module and can ship; depend on it only where you call its API"),
}


def make(m: dict) -> dict:
    name = m["name"]
    path = m["path"]
    slug = m["slug"]
    deps = m.get("modules") or []
    folder = folder_of(path)
    human = humanize(name)
    dk = domain_of(name, path, deps)
    pk = placement_kind(path, name)
    what_cn, how_cn, what_en, how_en = DOMAIN[dk]
    place_cn, place_en = PLACEMENT[pk]
    dep_n = len(deps)
    dep_preview = "、".join(f"`{d}`" for d in deps[:5])
    dep_preview_en = ", ".join(f"`{d}`" for d in deps[:5])
    ident = "".join(c for c in name if c.isalnum()) or name
    snippet = f'PublicDependencyModuleNames.AddRange(new string[] {{ "{name}" }});'

    human_suffix = "" if human.lower() == name.lower() else f"（{human}）"
    human_en = "" if human.lower() == name.lower() else f" ({human})"
    p1_cn = f"`{name}`{human_suffix}：{what_cn}。位于 `{folder}`，构建规则 `{path}`。"
    p1_en = f"`{name}`{human_en}: {what_en}. Located under `{folder}`; build rule `{path}`."
    dep_more = " 等" if dep_n > 5 else ""
    dep_more_en = " etc" if dep_n > 5 else ""
    if dep_n:
        p1_cn += f"直接依赖 {dep_n} 个模块：{dep_preview}{dep_more}。"
        p1_en += f" It directly depends on {dep_n} modules: {dep_preview_en}{dep_more_en}."
    else:
        p1_cn += "描述符未声明依赖。"
        p1_en += " The descriptor declares no dependencies."

    how_cn_full = f"怎么用：{how_cn}。"
    how_en_full = f"How to use: {how_en}."
    if dk == "thirdparty":
        call_cn = "调用：不要 include 引擎模块头去用它；优先用引擎里封装该库的上层模块，仅必要时包含 ThirdParty 目录下的第三方头文件。"
        call_en = "Call: do not include engine module headers to use it; use the engine module that wraps this library, and only include its ThirdParty headers when truly needed."
    elif dk == "toolchain" or pk == "program":
        call_cn = "调用：作为独立程序/命令运行，或在工具代码里 include 其 Public 头。"
        call_en = "Call: run it as a standalone program/command, or include its Public headers from tool code."
    else:
        call_cn = "调用：包含其 `Public/` 头文件以使用导出类型；模块由引擎/插件系统自动加载，通常无需手动 `LoadModulePtr`（仅懒加载时才用 `FModuleManager::LoadModuleChecked`）。"
        call_en = "Call: include its `Public/` headers to use exported types; the engine/plugin system loads the module automatically — no manual `LoadModulePtr` needed (use `FModuleManager::LoadModuleChecked` only for lazy loading)."

    rec = {
        "slug": slug,
        "kind": "module",
        "cn_steps": [
            p1_cn,
            f"部署：`{name}` {place_cn}。",
            how_cn_full,
            f"依赖：在 `YourModule.Build.cs` 加入 `{snippet}`；对外暴露 `{name}` 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。",
            call_cn,
        ],
        "en_steps": [
            p1_en,
            f"Placement: `{name}` is a {place_en}.",
            how_en_full,
            f"Depend: in `YourModule.Build.cs` add `{snippet}`. Use Public when exposing `{name}` types, Private if only calling it; then Generate Project Files and rebuild.",
            call_en,
        ],
        "note_cn": f"`{name}`：{what_cn}；构建规则 `{path}`，直接依赖 {dep_n} 个模块。",
        "note_en": f"`{name}`: {what_en}; build rule `{path}`; depends on {dep_n} modules.",
    }
    return rec


def main() -> int:
    # Remove old generated module chunk files to avoid stale/duplicate records.
    for old in OUT.glob("modules_*.json"):
        old.unlink()
    records = [make(m) for m in MODS]
    n = len(records)
    step = 15
    files = 0
    for start in range(0, n, step):
        batch = records[start:start + step]
        end = start + len(batch) - 1
        (OUT / f"modules_{start:04d}_{end:04d}.json").write_text(
            json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        files += 1
    # Domain distribution for reporting.
    from collections import Counter
    dist = Counter(domain_of(m["name"], m["path"], m.get("modules") or []) for m in MODS)
    print(f"wrote {n} module records in {files} files")
    print("domain distribution:", dict(dist))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())