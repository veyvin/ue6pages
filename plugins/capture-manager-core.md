---
layout: default
title: 捕获管理器核心 / Capture Manager Core
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Capture Manager Core</div>
      <div class="hero-title-cn">捕获管理器核心 · Capture Manager Core 插件包含在 Captu</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">12</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/CaptureManager/CaptureManagerCore/CaptureManagerCore.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Capture Manager Core 插件包含在 Capture Manager App 插件和 Capture Manager Editor 插件之间共享的实用程序模块。</div><div class="lang-content">The Capture Manager Core plugin contains utility modules that are shared between Capture Manager App plugin and Capture Manager Editor plugin.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Core 是最底层运行时：容器、字符串、模块加载、日志、委托、平台抽象。不依赖 Engine；所有其他模块最终都建立在它上面。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：CaptureUtils, CaptureProtocolStack, CaptureManagerCPSClient, CaptureManagerPipeline, CaptureManagerMediaRW, CaptureDataConverter, DataIngestCore, LiveLinkHubCaptureMessaging 等。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Core is the lowest runtime layer: containers, strings, module loading, logging, delegates, and platform abstraction. It does not depend on Engine; everything else sits on it.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: CaptureUtils, CaptureProtocolStack, CaptureManagerCPSClient, CaptureManagerPipeline, CaptureManagerMediaRW, CaptureDataConverter, DataIngestCore, LiveLinkHubCaptureMessaging 等. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Capture Manager Core</code>。它没有独立窗口，是 App 与 Editor 共用的协议/管线层，通常作为那两个插件的依赖自动加载。</li><li>扩展入库格式时，在 <code class="usage-code">CaptureProtocolStack</code> / <code class="usage-code">CaptureManagerCPSClient</code> 上对接采集协议，而不是在 Hub UI 里硬编码路径。</li><li>自定义转码或时间线切分实现 <code class="usage-code">CaptureManagerPipeline</code> 与 <code class="usage-code">CaptureManagerMediaRW</code> 的读写器，把相机原片写成图像序列+音频。</li><li>把厂商元数据映射进引擎类型时走 <code class="usage-code">CaptureDataConverter</code> 和 <code class="usage-code">DataIngestCore</code>，输出仍应是 <code class="usage-code">UFootageCaptureData</code> 能引用的媒体与标定。</li><li><code class="usage-code">LiveLinkHubCaptureMessaging</code> 只负责 Hub↔引擎消息；不要在游戏运行时 Tick 里调用这些模块。</li><li>游戏 Target 不要链接 Core 的媒体栈；仅编辑器工具或 Hub 附属进程依赖 <code class="usage-code">CaptureUtils</code> 等运行时模块。</li></ol><p class="usage-note">无 UI；现场控制在 App，导入在 Editor，设备列表在 Devices。本插件只提供 CPS/管线/媒体 IO。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Capture Manager Core</code>. It has no window; it is the shared protocol/pipeline layer, usually pulled in by the App and Editor plugins.</li><li>To support a new capture format, extend <code class="usage-code">CaptureProtocolStack</code> / <code class="usage-code">CaptureManagerCPSClient</code> instead of hard-coding paths in Hub UI.</li><li>Custom transcode or take splitting belongs in <code class="usage-code">CaptureManagerPipeline</code> and <code class="usage-code">CaptureManagerMediaRW</code> writers that emit image sequences plus audio.</li><li>Map vendor metadata through <code class="usage-code">CaptureDataConverter</code> and <code class="usage-code">DataIngestCore</code> so outputs remain media and calibration <code class="usage-code">UFootageCaptureData</code> can reference.</li><li><code class="usage-code">LiveLinkHubCaptureMessaging</code> is Hub↔engine messaging only — do not tick these modules from game runtime.</li><li>Do not link the Core media stack into a game Target. Editor tools or Hub helper processes may depend on <code class="usage-code">CaptureUtils</code>.</li></ol><p class="usage-note">No UI. App controls the set, Editor imports, Devices lists hardware. This plugin is CPS, pipeline, and media I/O only.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (12)</div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureUtils</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureProtocolStack</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureManagerCPSClient</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureManagerPipeline</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureManagerMediaRW</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureDataConverter</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataIngestCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">LiveLinkHubCaptureMessaging</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureManagerStyle</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureManagerTakeMetadata</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureMetadataExtraction</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureUtilsEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/CaptureManager/CaptureManagerCore/CaptureManagerCore.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
