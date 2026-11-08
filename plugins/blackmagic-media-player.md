---
layout: default
title: Blackmagic媒体播放器 / Blackmagic Media Player
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">B</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Blackmagic Media Player</div>
      <div class="hero-title-cn">Blackmagic媒体播放器 · 使用 Blackmagic 采集卡实现输入和输出。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">2.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">6</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/BlackmagicMedia/BlackmagicMedia.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用 Blackmagic 采集卡实现输入和输出。</div><div class="lang-content">Implements input and output using Blackmagic Capture cards.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用 Blackmagic 采集卡实现输入和输出。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：BlackmagicCore, BlackmagicMedia, BlackmagicMediaOutput, BlackmagicMediaFactory, BlackmagicMediaFactory, BlackmagicMediaEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements input and output using Blackmagic Capture cards.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: BlackmagicCore, BlackmagicMedia, BlackmagicMediaOutput, BlackmagicMediaFactory, BlackmagicMediaFactory, BlackmagicMediaEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>安装 Blackmagic Desktop Video 驱动，再启用 <code class="usage-code">Blackmagic Media Player</code>（<code class="usage-code">BlackmagicMedia.uplugin</code>）。无卡/无驱动时 <code class="usage-code">BlackmagicMediaFactory</code> 枚举不到设备。</li><li>采集：新建 <code class="usage-code">Blackmagic Media Source</code>（<code class="usage-code">UBlackmagicMediaSource</code>），选设备、输入口、分辨率、帧率、色彩/HDR、音频声道与时码。用 <code class="usage-code">Media Player</code> + <code class="usage-code">Media Texture</code> <code class="usage-code">Open</code> 该 Source。</li><li>输出：新建 <code class="usage-code">Blackmagic Media Output</code>（<code class="usage-code">UBlackmagicMediaOutput</code>），配置填满输出标准。用 <code class="usage-code">Media Capture</code>（<code class="usage-code">UMediaCapture</code>）从视口、Composure 或渲染目标捕获并送 SDI/HDMI。</li><li>虚拟制片时在 <code class="usage-code">Project Settings</code> 对齐 <code class="usage-code">Timecode Provider</code> / 帧率，与卡上参考信号一致；nDisplay 或媒体 IO 面板里确认 Drop Frame 与信号格式。</li><li>运行时依赖 <code class="usage-code">BlackmagicCore</code>、<code class="usage-code">BlackmagicMedia</code>、<code class="usage-code">BlackmagicMediaOutput</code>、<code class="usage-code">BlackmagicMediaFactory</code>。<code class="usage-code">BlackmagicMediaEditor</code> 只进 <code class="usage-code">*Editor.Build.cs</code>。现场用 <code class="usage-code">stat Media</code> / 设备指示灯查锁定，不要只看编辑器预览窗。</li></ol><p class="usage-note">Blackmagic 采集卡的 `UBlackmagicMediaSource` / `UBlackmagicMediaOutput`。必须有 Desktop Video 驱动。</p></div><div class="lang-content"><ol class="usage-steps"><li>Install Blackmagic Desktop Video drivers, then enable <code class="usage-code">Blackmagic Media Player</code> (<code class="usage-code">BlackmagicMedia.uplugin</code>). Without a card/driver, <code class="usage-code">BlackmagicMediaFactory</code> enumerates nothing.</li><li>Ingest: create a <code class="usage-code">Blackmagic Media Source</code> (<code class="usage-code">UBlackmagicMediaSource</code>), set device, input, resolution, frame rate, color/HDR, audio, and timecode. <code class="usage-code">Open</code> it on a <code class="usage-code">Media Player</code> + <code class="usage-code">Media Texture</code>.</li><li>Egress: create a <code class="usage-code">Blackmagic Media Output</code> (<code class="usage-code">UBlackmagicMediaOutput</code>) that matches the fill standard. Drive <code class="usage-code">Media Capture</code> (<code class="usage-code">UMediaCapture</code>) from a viewport, Composure, or render target out to SDI/HDMI.</li><li>For virtual production, match <code class="usage-code">Timecode Provider</code> / frame rate in <code class="usage-code">Project Settings</code> to the card’s reference. Confirm drop-frame and signal format in nDisplay or Media IO.</li><li>Runtime modules: <code class="usage-code">BlackmagicCore</code>, <code class="usage-code">BlackmagicMedia</code>, <code class="usage-code">BlackmagicMediaOutput</code>, <code class="usage-code">BlackmagicMediaFactory</code>. <code class="usage-code">BlackmagicMediaEditor</code> belongs in <code class="usage-code">*Editor.Build.cs</code> only. Check lock with <code class="usage-code">stat Media</code> and the hardware LEDs, not only the editor preview.</li></ol><p class="usage-note">Blackmagic ingest/egress via `UBlackmagicMediaSource` / `UBlackmagicMediaOutput`. Desktop Video drivers are required.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (6)</div><div class="module-item"><span class="dot"></span><span class="name mono">BlackmagicCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">BlackmagicMedia</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">BlackmagicMediaOutput</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">BlackmagicMediaFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">BlackmagicMediaFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">BlackmagicMediaEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/BlackmagicMedia/BlackmagicMedia.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
