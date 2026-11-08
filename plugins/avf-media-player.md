---
layout: default
title: AVF 媒体播放器 / AVF Media Player
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AVF Media Player</div>
      <div class="hero-title-cn">AVF 媒体播放器 · 使用 Apple AV Foundation 实现媒体播放器。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">2.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/AvfMedia/AvfMedia.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用 Apple AV Foundation 实现媒体播放器。</div><div class="lang-content">Implements a media player using Apple AV Foundation.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用 Apple AV Foundation 实现媒体播放器。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：AvfMedia, AvfMediaEditor, AvfMediaFactory, AvfMediaFactory, AvfMediaCapture。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements a media player using Apple AV Foundation.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: AvfMedia, AvfMediaEditor, AvfMediaFactory, AvfMediaFactory, AvfMediaCapture. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>仅在 macOS / iOS / tvOS 工程启用 <code class="usage-code">AVF Media Player</code>（<code class="usage-code">AvfMedia.uplugin</code>）。Windows 上 <code class="usage-code">AvfMediaFactory</code> 不会注册可用播放器。</li><li>用 <code class="usage-code">AvfMediaFactory</code> 作为 Media Framework 后端：内容浏览器新建 <code class="usage-code">File Media Source</code> 或 <code class="usage-code">Stream Media Source</code>，指向 AVFoundation 能解的封装（MOV/MP4/HLS 等）。</li><li>新建 <code class="usage-code">Media Player</code> + <code class="usage-code">Media Texture</code>，打开该 Source。播放器名称应落到 AVF；<code class="usage-code">AvfMediaEditor</code> 只提供编辑器工厂/预览，不要写进 Game Target 的 <code class="usage-code">Build.cs</code>。</li><li>采集苹果摄像头或麦克风时走 <code class="usage-code">AvfMediaCapture</code>：创建对应 Capture/<code class="usage-code">Media Source</code>，选 AVFoundation 设备，再 <code class="usage-code">Open</code> 到同一个 <code class="usage-code">Media Player</code>。</li><li>把 <code class="usage-code">Media Texture</code> 接到材质或 <code class="usage-code">Media Plate</code>，蓝图 <code class="usage-code">Play</code> / <code class="usage-code">Pause</code> / <code class="usage-code">Seek</code>。真机权限在 iOS <code class="usage-code">Info.plist</code> 相机/麦克风用途说明里配置，而不是在 Windows 编辑器里测通。</li><li>运行时模块依赖 <code class="usage-code">AvfMedia</code>、<code class="usage-code">AvfMediaFactory</code>、<code class="usage-code">AvfMediaCapture</code>；编辑器扩展只放 <code class="usage-code">AvfMediaEditor</code> 到 <code class="usage-code">*Editor.Build.cs</code>。</li></ol><p class="usage-note">Apple AVFoundation 后端。不能在 Win64 上当通用解码器；采集走 `AvfMediaCapture`，不是 Electra。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">AVF Media Player</code> (<code class="usage-code">AvfMedia.uplugin</code>) only on macOS / iOS / tvOS projects. <code class="usage-code">AvfMediaFactory</code> will not register a usable player on Windows.</li><li>Use <code class="usage-code">AvfMediaFactory</code> as the Media Framework backend: create a <code class="usage-code">File Media Source</code> or <code class="usage-code">Stream Media Source</code> pointing at an AVFoundation-readable container (MOV/MP4/HLS, etc.).</li><li>Create a <code class="usage-code">Media Player</code> plus <code class="usage-code">Media Texture</code> and open that source. The player name should resolve to AVF. <code class="usage-code">AvfMediaEditor</code> is editor factory/preview only — never add it to a Game Target <code class="usage-code">Build.cs</code>.</li><li>For Apple camera or microphone capture, use <code class="usage-code">AvfMediaCapture</code>: create the capture/<code class="usage-code">Media Source</code>, pick the AVFoundation device, then <code class="usage-code">Open</code> it on the same <code class="usage-code">Media Player</code>.</li><li>Wire the <code class="usage-code">Media Texture</code> into a material or <code class="usage-code">Media Plate</code> and <code class="usage-code">Play</code> / <code class="usage-code">Pause</code> / <code class="usage-code">Seek</code> from Blueprint. iOS camera/mic usage strings belong in <code class="usage-code">Info.plist</code>; proving this on a Windows editor is not a valid test.</li><li>Runtime modules are <code class="usage-code">AvfMedia</code>, <code class="usage-code">AvfMediaFactory</code>, and <code class="usage-code">AvfMediaCapture</code>. Put <code class="usage-code">AvfMediaEditor</code> only in <code class="usage-code">*Editor.Build.cs</code>.</li></ol><p class="usage-note">Apple AVFoundation backend. It is not a Win64 decoder. Capture goes through `AvfMediaCapture`, not Electra.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">AvfMedia</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AvfMediaEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AvfMediaFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AvfMediaFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AvfMediaCapture</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/AvfMedia/AvfMedia.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
