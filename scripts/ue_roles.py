"""Real role text: Epic .uplugin Description + engine-architecture knowledge (not enable-plugin templates)."""
from __future__ import annotations

# Official-doc-informed roles for well-known plugins/modules (Epic docs + engine source).
KNOWN: dict[str, dict[str, str]] = {
    "niagara": {
        "cn": "Niagara 是虚幻引擎的下一代实时特效系统，用来制作火焰、烟雾、粒子、流体等。技术美术可以在模块栈里自己扩展行为，不必每次都找程序员。发射器可复用，同一次模拟也能用 Sprite、Ribbon、Mesh 多种方式渲染。",
        "en": "Niagara is Unreal’s next-generation real-time VFX system for fire, smoke, particles, and fluids. Technical artists can add behavior in the module stack without a programmer. Emitters are reusable, and one simulation can render as sprites, ribbons, and meshes at once.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-visual-effects-system-in-unreal-engine",
    },
    "water": {
        "cn": "Water 系统用来在景观上做能互相衔接的河流、湖泊、海洋：样条工作流、统一的网格与着色、物理交互，以及脚步涟漪、船尾航迹这类玩法向流体反馈。编辑器里启用 Water 插件后，用水体 Actor 铺水面。",
        "en": "The Water system builds rivers, lakes, and oceans that work with Landscape: spline workflow, unified meshing and shading, physics, and gameplay fluids such as footstep ripples or a boat wake. Enable the Water plugin, then place Water Body actors.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/water-system-in-unreal-engine",
    },
    "paper2d": {
        "cn": "Paper2D 是引擎的 2D / 2D+3D 混合玩法与动画插件。核心资产是 Sprite；Flipbook 按序列播放 Sprite 做动画；TileSet / TileMap 用来铺 2D 关卡。和三维渲染兼容，2D 角色可以和 3D 场景同屏。",
        "en": "Paper 2D is Unreal’s 2D and 2D/3D hybrid gameplay and animation plugin. Sprites are the main asset; Flipbooks animate them; TileSets and TileMaps build 2D levels. It works with the 3D renderer, so 2D actors can sit in a 3D world.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine",
    },
    "gameplay abilities": {
        "cn": "Gameplay Ability System（GAS）给技能、冷却、消耗、Buff/Debate 一套数据驱动框架。用 GameplayAbility、GameplayEffect、AttributeSet、GameplayCue 组合出攻击、翻滚、被动等，适合需要复制的多人技能。",
        "en": "The Gameplay Ability System (GAS) is a data-driven framework for skills, cooldowns, costs, and buffs. GameplayAbility, GameplayEffect, AttributeSet, and GameplayCue compose attacks, dodges, and passives, including replicated multiplayer.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine",
    },
    "enhanced input": {
        "cn": "Enhanced Input 替代旧的轴/动作映射：Input Action + Input Mapping Context，支持触发器、修饰符、按键和弦，以及运行时切换上下文（步行/开车/UI）。新项目应优先用它而不是 DefaultInput.ini 里的老绑定。",
        "en": "Enhanced Input replaces old axis/action mappings with Input Actions and Mapping Contexts, plus triggers, modifiers, chords, and runtime context swaps (walk / drive / UI). New projects should use it instead of legacy DefaultInput.ini bindings.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine",
    },
    "control rig": {
        "cn": "Control Rig 是引擎里的绑定与程序化动画工具：在绑定图里做 FK/IK、空间切换，可在 Sequencer 里关键帧，也可在运行时驱动。常和 IK Rig、重定向一起做角色动画。",
        "en": "Control Rig is Unreal’s rigging and procedural animation toolkit: FK/IK and space switching in a rig graph, keyable in Sequencer or driven at runtime. It is often paired with IK Rig and retargeting.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine",
    },
    "massai": {
        "cn": "Mass AI 把 Mass Entity（ECS）用到大规模 AI：用碎片、处理器和状态树驱动成千上万的代理，而不是每个代理一个 Actor 的行为树。适合人群、兵团。",
        "en": "Mass AI applies the Mass Entity ECS to large-scale agents: fragments, processors, and StateTree instead of a Behavior Tree per Actor. It is meant for crowds and armies.",
    },
    "procedural content generation framework (pcg)": {
        "cn": "PCG 用节点图在编辑器或运行时程序化生成关卡内容：点云、变换、网格、植被与生成规则，可和景观、HLOD、Nanite 配合。",
        "en": "PCG is a node graph for procedural level content in editor or at runtime: point clouds, transforms, meshes, foliage, and spawn rules, working with Landscape, HLOD, and Nanite.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview",
    },
    "pixel streaming": {
        "cn": "Pixel Streaming 把引擎画面通过 WebRTC 推到浏览器：云端或本机跑游戏，薄客户端只显示与输入。用于云游戏、可视化审阅、远程演示。",
        "en": "Pixel Streaming sends the engine frame buffer to a browser over WebRTC so the game runs in the cloud or on a host while a thin client only shows video and sends input. Used for cloud gaming, reviews, and remote demos.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-streaming-in-unreal-engine",
    },
    "ndisplay": {
        "cn": "nDisplay 把一台场景渲染到多台同步的机器/窗口上，用于 LED 墙、洞穴、集群视口。和 Switchboard、Live Link、摄像机跟踪一起做虚拟制片。",
        "en": "nDisplay renders one scene across synchronized machines or windows for LED walls, CAVE, and cluster viewports. It is used in virtual production with Switchboard, Live Link, and camera tracking.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-in-unreal-engine",
    },
    "live link": {
        "cn": "Live Link 把外部设备的实时数据（动捕、摄像机、灯光、面捕）流进编辑器或运行时，驱动骨骼、摄像机、Control Rig。虚拟制片和 MetaHuman 面捕的主干。",
        "en": "Live Link streams live data from mocap, cameras, lights, and facial capture into the editor or runtime to drive skeletons, cameras, and Control Rig. It is the backbone of virtual production and MetaHuman face capture.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine",
    },
    "umg": {
        "cn": "UMG（Unreal Motion Graphics）是运行时 UI 模块：Widget Blueprint、UUserWidget、槽与动画。游戏 HUD、菜单几乎都建立在 UMG + Slate 上。",
        "en": "UMG (Unreal Motion Graphics) is the runtime UI module: Widget Blueprints, UUserWidget, slots, and widget animation. Most game HUDs and menus are UMG on top of Slate.",
    },
    "engine": {
        "cn": "Engine 模块是游戏框架核心：Actor、Pawn、PlayerController、World、组件、材质与关卡流送的运行时实现。绝大多数游戏模块都会直接或间接依赖它。",
        "en": "The Engine module is the gameplay-framework core: Actor, Pawn, PlayerController, World, components, materials, and streaming at runtime. Almost every game module depends on it, directly or not.",
    },
    "core": {
        "cn": "Core 是最底层运行时：容器、字符串、模块加载、日志、委托、平台抽象。不依赖 Engine；所有其他模块最终都建立在它上面。",
        "en": "Core is the lowest runtime layer: containers, strings, module loading, logging, delegates, and platform abstraction. It does not depend on Engine; everything else sits on it.",
    },
    "slate": {
        "cn": "Slate 是引擎的立即模式/保留模式混合 UI 工具包，编辑器几乎全部用它画。游戏 UI 通常走 UMG，UMG 再编译成 Slate 控件。",
        "en": "Slate is the engine’s UI toolkit (immediate/retained hybrid). The editor is almost entirely Slate. Game UI usually goes through UMG, which compiles down to Slate widgets.",
    },
    "openxr": {
        "cn": "OpenXR 插件让引擎走 Khronos OpenXR 运行时，对接 SteamVR、Oculus、Windows Mixed Reality 等头显，而不为每个厂商单独写插件。",
        "en": "The OpenXR plugin talks to a Khronos OpenXR runtime so Unreal can target SteamVR, Meta, WMR, and others without a vendor-specific plugin per HMD.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/developing-for-head-mounted-experiences-with-openxr-in-unreal-engine",
    },
    "metasound": {
        "cn": "MetaSound 是音频的节点图合成系统，类似 Niagara 之于粒子：在图里做振荡、滤波、调制，运行时生成声音，而不是只播 Wave 文件。",
        "en": "MetaSound is a node-graph audio synthesis system (Niagara for audio): oscillators, filters, and modulation generate sound at runtime instead of only playing waves.",
        "doc": "https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-in-unreal-engine",
    },
    "iris": {
        "cn": "Iris 是较新的复制后端，用来替代或补充旧的 Actor 复制路径，面向大规模 Actor 与更细的复制粒度。联网项目要在 DefaultEngine.ini 里显式打开。",
        "en": "Iris is the newer replication backend meant to replace or sit beside classic Actor replication, aimed at large actor counts and finer filtering. Net projects turn it on in DefaultEngine.ini.",
    },
    "chaos": {
        "cn": "Chaos 是引擎默认物理与破坏求解器（刚体、布料、破碎、字段）。相关插件把编辑器工具和运行时求解接到关卡里的几何体上。",
        "en": "Chaos is the default physics and destruction solver (rigid body, cloth, fracture, fields). Related plugins connect editor tools and the runtime solver to level geometry.",
    },
    "verse": {
        "cn": "Verse 是面向 UEFN / Fortnite 体验的脚本语言与运行时。这组插件提供编译、虚拟机、设备 API 与编辑器集成，不是传统蓝图游戏的必选项。",
        "en": "Verse is the scripting language and runtime for UEFN / Fortnite experiences. These plugins provide the compiler, VM, device APIs, and editor integration — not required for classic Blueprint games.",
    },
}

FAMILIES = [
    (("niagara",), "Niagara/VFX 家族：在 Niagara 模块栈或资产上扩展特效，而不是另起一套粒子系统。",
     "Niagara/VFX family: extend effects in the Niagara stack or assets, not a separate particle engine."),
    (("water",), "水体家族：为 Water 系统提供网格、材质、编辑器或示例，而不是通用后处理。",
     "Water family: meshing, materials, editor, or samples for the Water system — not a generic post-process."),
    (("livelink", "live link"), "Live Link 家族：把某种设备或协议的实时数据变成 Live Link 主体，供骨骼/摄像机消费。",
     "Live Link family: turns a device or protocol into a Live Link subject for skeletons or cameras."),
    (("openxr",), "OpenXR 功能插件：在 OpenXR 运行时上实现手部、眼动、控制器或交互扩展。",
     "OpenXR feature plugin: hands, eye tracking, controllers, or interaction on top of the OpenXR runtime."),
    (("onlinesubsystem", "online subsystem", "online-services", "online services"),
     "在线子系统家族：为 Steam、EOS、Google、Apple 等平台提供登录、会话、成就的 OSS / Online Services 实现。",
     "Online family: OSS / Online Services for login, sessions, and achievements on Steam, EOS, Google, Apple, etc."),
    (("electra", "decoder", "media player"), "媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。",
     "Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video."),
    (("metahuman",), "MetaHuman 家族：数字人生成、面捕、校准或运行时绑定，建立在 Control Rig / Live Link 之上。",
     "MetaHuman family: digital-human generation, face capture, calibration, or runtime, on Control Rig / Live Link."),
    (("uaf", "unreal animation framework"), "UAF 家族：新动画图框架上的一层（状态、层、Pose Search、Control Rig 桥）。",
     "UAF family: a layer on the Unreal Animation Framework (state, layering, Pose Search, Control Rig bridge)."),
    (("pcg", "procedural content"), "PCG 家族：给程序化内容生成图提供节点、互操作或编辑器工具。",
     "PCG family: nodes, interop, or editor tools for the Procedural Content Generation graph."),
    (("mass",), "Mass 家族：ECS 风格的大规模实体（碎片、处理器、可视化或 AI）。不要按普通 Actor 组件去理解。",
     "Mass family: ECS-style mass entities (fragments, processors, debug, or AI) — not a typical Actor component."),
    (("concert", "multi-user"), "Concert/多人编辑：在多台编辑器之间同步关卡与资产更改。",
     "Concert / multi-user: syncs level and asset edits across editor machines."),
    (("ndisplay", "switchboard", "icvfx"), "虚拟制片显示家族：集群视口、同步、LED 墙或舞台控制。",
     "Virtual-production display family: cluster views, sync, LED walls, or stage control."),
    (("dmx",), "DMX 家族：舞台灯光协议、灯具、像素映射，把引擎接到真实灯光台。",
     "DMX family: lighting protocols, fixtures, and pixel mapping from the engine to a lighting desk."),
    (("insights", "trace"), "Insights/Trace 家族：采集或可视化一类性能数据（CPU、渲染、IO、网络），在 Unreal Insights 里看。",
     "Insights/Trace family: records or visualizes a class of perf data (CPU, GPU, IO, net) in Unreal Insights."),
    (("toolset",), "Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。",
     "Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature."),
    (("controller keys", "controller-keys", " fkeys"), "输入键定义：只声明该手柄的 FKey，让非 OpenXR 模块也能绑定按键。",
     "Input key plugin: declares FKeys for that controller so non-OpenXR modules can bind them."),
    (("usd", "datasmith", "interchange", "alembic"), "导入管线：把 DCC/CAD/USD 资产转成引擎网格、材质与关卡。",
     "Import pipeline: converts DCC/CAD/USD assets into engine meshes, materials, and levels."),
    (("verse",), "Verse 语言/运行时的一块：编译、VM、设备或编辑器支持，服务 UEFN 体验。",
     "A slice of the Verse language/runtime: compiler, VM, devices, or editor support for UEFN."),
    (("pixel streaming", "pixelstreaming"), "把引擎画面推到网页客户端，并回收浏览器输入。",
     "Pushes engine video to a web client and returns browser input."),
    (("gameplay abilit", "gas"), "技能系统相关：GAS 的能力、效果或编辑器扩展。",
     "Gameplay Ability System: abilities, effects, or editor extensions."),
]


def _key(name: str) -> str:
    return (name or "").strip().lower()


def lookup_known(name: str) -> dict[str, str] | None:
    k = _key(name)
    if k in KNOWN:
        return KNOWN[k]
    for key, val in KNOWN.items():
        if key in k or k in key:
            return val
    return None


def family_blurb(blob: str) -> tuple[str, str] | None:
    b = blob.lower()
    for needles, cn, en in FAMILIES:
        if any(n in b for n in needles):
            return cn, en
    return None


def area_blurb(path: str, kind: str) -> tuple[str, str]:
    p = (path or "").replace("\\", "/").lower()
    if kind == "module":
        if p.startswith("runtime/") or "/runtime/" in p:
            return "这是 Runtime 模块，随游戏一起发布，给运行时 C++ 用。", "This is a Runtime module that ships with the game and is for runtime C++."
        if "editor" in p or p.startswith("editor/"):
            return "这是 Editor 模块，只在编辑器进程加载，不能链进 Game Target。", "This is an Editor module, loaded only in the editor process — do not link it into a Game target."
        if "thirdparty" in p:
            return "这是第三方库的 UBT 封装，通常由上层引擎模块使用，而不是游戏直接依赖。", "This is a UBT wrapper around a third-party library; engine modules consume it, games rarely depend on it directly."
        if p.startswith("developer/") or p.startswith("programs/"):
            return "这是开发者工具或独立程序模块，给 Insights、UBT、命令行用。", "This is a developer tool or program module for Insights, UBT, or command-line apps."
        return "这是引擎源码里的一个 UBT 模块，通过 Build.cs 被其他模块依赖。", "This is a UBT module in engine source that other modules depend on via Build.cs."
    # plugin
    if "experimental" in p:
        return "Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。", "Epic ships this under Experimental: usable, but the contract may change on nightly builds."
    if "/virtualproduction/" in p:
        return "属于虚拟制片工具链（摄像机、舞台、同步、LED）。", "Part of the virtual-production toolchain (cameras, stage, sync, LED)."
    if "/fx/" in p:
        return "属于特效/Niagara 工具链。", "Part of the FX / Niagara toolchain."
    if "/media/" in p:
        return "属于 Media Framework / Electra 播流与解码。", "Part of Media Framework / Electra playback and decode."
    if "/ai/" in p:
        return "属于人工智能与导航工具链。", "Part of the AI and navigation toolchain."
    if "/runtime/" in p:
        return "运行时插件，启用后可进游戏包。", "A runtime plugin that can ship in a cooked game."
    if "/editor/" in p or "/developer/" in p:
        return "编辑器或开发者插件，服务制作流程，默认不进 Shipping。", "An editor/developer plugin for the authoring pipeline; it does not ship by default."
    if "/online/" in p:
        return "属于在线子系统 / 平台服务。", "Part of Online Subsystem / platform services."
    if "/importers/" in p:
        return "属于资产导入管线。", "Part of the asset-import pipeline."
    return "这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。", "This is an engine plugin under Plugins/; its .uplugin states its job."


def compose_role(info: dict) -> tuple[str, str, str]:
    """Return (cn_html, en_html, doc_url)."""
    name = info.get("name") or ""
    desc_cn = (info.get("desc_cn") or "").strip()
    desc_en = (info.get("desc_en") or "").strip()
    path = info.get("file_path") or ""
    kind = info.get("kind") or "plugin"
    blob = " ".join([name, path, desc_en, desc_cn, info.get("category") or ""])

    known = lookup_known(name)
    fam = family_blurb(blob)
    area_cn, area_en = area_blurb(path, kind)

    cn_parts, en_parts = [], []
    doc = ""

    if known:
        cn_parts.append(known["cn"])
        en_parts.append(known["en"])
        doc = known.get("doc") or ""
    elif desc_cn or desc_en:
        # Epic's own Description is the canonical one-liner; expand with family/area.
        if desc_cn:
            cn_parts.append(f"Epic 在插件/模块描述里写的职责是：{desc_cn}")
        if desc_en:
            en_parts.append(f"Epic’s own description of its job: {desc_en}")
        if fam:
            cn_parts.append(fam[0])
            en_parts.append(fam[1])
    elif fam:
        cn_parts.append(fam[0])
        en_parts.append(fam[1])
    else:
        cn_parts.append(f"{name} 是引擎源码中的{('插件' if kind == 'plugin' else '模块')}，具体职责以描述符和源码为准。")
        en_parts.append(f"{name} is an engine {kind} whose job is defined by its descriptor and source.")

    cn_parts.append(area_cn)
    en_parts.append(area_en)

    mods = info.get("modules") or []
    if kind == "plugin" and mods:
        shown = ", ".join(mods[:8])
        extra = " 等" if len(mods) > 8 else ""
        cn_parts.append(f"它打包的模块包括：{shown}{extra}。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。")
        en_parts.append(f"It ships these modules: {shown}{extra}. Runtime lives in non-Editor modules; UI in *Editor modules.")
    if kind == "module" and mods:
        shown = ", ".join(mods[:8])
        cn_parts.append(f"UBT 声明它还依赖：{shown}。这些依赖暗示了它和哪些子系统协作。")
        en_parts.append(f"UBT also lists dependencies on: {shown}. Those names show which subsystems it talks to.")

    cn = "</p><p>".join(cn_parts)
    en = "</p><p>".join(en_parts)
    return f"<p>{cn}</p>", f"<p>{en}</p>", doc
