---
layout: default
title: 捕获管理器设备 / Capture Manager Devices
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Capture Manager Devices</div>
      <div class="hero-title-cn">捕获管理器设备 · 捕获管理器设备包含可从 LiveLink Hub 的捕获管理器布</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/CaptureManager/CaptureManagerDevices/CaptureManagerDevices.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">捕获管理器设备包含可从 LiveLink Hub 的捕获管理器布局中使用的设备</div><div class="lang-content">The Capture Manager Devices contains devices that can be used from the Capture Manager layout of the LiveLink Hub</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：捕获管理器设备包含可从 LiveLink Hub 的捕获管理器布局中使用的设备</p><p>Live Link 家族：把某种设备或协议的实时数据变成 Live Link 主体，供骨骼/摄像机消费。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：MonoVideoIngestDevice, CPSLiveLinkDevice, TakeArchiveIngestDevice, StereoVideoIngestDevice, VideoLiveLinkDeviceCommon。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: The Capture Manager Devices contains devices that can be used from the Capture Manager layout of the LiveLink Hub</p><p>Live Link family: turns a device or protocol into a Live Link subject for skeletons or cameras.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: MonoVideoIngestDevice, CPSLiveLinkDevice, TakeArchiveIngestDevice, StereoVideoIngestDevice, VideoLiveLinkDeviceCommon. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 Live Link Hub 与编辑器两侧都启用 <code class="usage-code">Capture Manager Devices</code>（<code class="usage-code">MonoVideoIngestDevice</code>、<code class="usage-code">StereoVideoIngestDevice</code>、<code class="usage-code">TakeArchiveIngestDevice</code>、<code class="usage-code">CPSLiveLinkDevice</code>、<code class="usage-code">VideoLiveLinkDeviceCommon</code>）。</li><li>打开 Hub 的 <code class="usage-code">Capture Manager</code> 布局，添加设备：文件夹里的 <code class="usage-code">.mp4</code>/<code class="usage-code">.mov</code> 用 <code class="usage-code">Mono Video Ingest</code>；左右眼成对素材用 <code class="usage-code">Stereo Video Ingest</code>；<code class="usage-code">.cptake</code> 目录用 <code class="usage-code">Take Archive Ingest</code>。</li><li><code class="usage-code">TakeArchiveIngestDevice</code> 读取 <code class="usage-code">.cptake</code> 与旧版 Capture Manager 归档；先 <code class="usage-code">Connect</code>，再 <code class="usage-code">UpdateTakeList</code> 浏览 slate/take。</li><li>需要协议栈上的 Live Link 主题时加 <code class="usage-code">CPSLiveLinkDevice</code>，与文件夹监视器分开，避免同一 take 被扫两遍。</li><li>选中 take 后配置 <code class="usage-code">UIngestCapability_Options</code>：<code class="usage-code">WorkingDirectory</code>、<code class="usage-code">DownloadDirectory</code>、视频/音频命名，以及指向编辑器的 <code class="usage-code">UploadHostName</code>。</li><li>跑 <code class="usage-code">RunIngestProcess</code>，在 UE 内容目录确认生成的 <code class="usage-code">FootageCaptureData</code>；失败先看设备 <code class="usage-code">Connection Status</code>，再查 Core 管线日志。</li></ol><p class="usage-note">设备只出现在 Hub 的 Capture Manager 布局。Live Link Face 等能力由对应设备类提供，不在本插件的五个模块名之外假造入口。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Capture Manager Devices</code> on both Live Link Hub and the editor (<code class="usage-code">MonoVideoIngestDevice</code>, <code class="usage-code">StereoVideoIngestDevice</code>, <code class="usage-code">TakeArchiveIngestDevice</code>, <code class="usage-code">CPSLiveLinkDevice</code>, <code class="usage-code">VideoLiveLinkDeviceCommon</code>).</li><li>In the Hub <code class="usage-code">Capture Manager</code> layout add a device: <code class="usage-code">Mono Video Ingest</code> for a folder of <code class="usage-code">.mp4</code>/<code class="usage-code">.mov</code>, <code class="usage-code">Stereo Video Ingest</code> for paired eyes, <code class="usage-code">Take Archive Ingest</code> for <code class="usage-code">.cptake</code> folders.</li><li><code class="usage-code">TakeArchiveIngestDevice</code> reads <code class="usage-code">.cptake</code> and legacy Capture Manager archives. <code class="usage-code">Connect</code>, then <code class="usage-code">UpdateTakeList</code> to browse slate/take ids.</li><li>Add <code class="usage-code">CPSLiveLinkDevice</code> when takes arrive as protocol-stack Live Link subjects. Do not also watch the same folder or you ingest twice.</li><li>Configure <code class="usage-code">UIngestCapability_Options</code>: <code class="usage-code">WorkingDirectory</code>, <code class="usage-code">DownloadDirectory</code>, video/audio naming, and <code class="usage-code">UploadHostName</code> for the editor.</li><li>Run <code class="usage-code">RunIngestProcess</code> and confirm <code class="usage-code">FootageCaptureData</code> in the UE project. On failure check device <code class="usage-code">Connection Status</code>, then Core pipeline logs.</li></ol><p class="usage-note">Devices appear in the Hub Capture Manager layout. Live Link Face and similar capabilities come from their device classes — do not invent extra module entry points.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">MonoVideoIngestDevice</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CPSLiveLinkDevice</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TakeArchiveIngestDevice</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">StereoVideoIngestDevice</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">VideoLiveLinkDeviceCommon</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/CaptureManager/CaptureManagerDevices/CaptureManagerDevices.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
