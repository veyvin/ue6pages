---
layout: default
title: 音频捕获时间码提供程序 / Audio Capture Timecode Provider
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Audio Capture Timecode Provider</div>
      <div class="hero-title-cn">音频捕获时间码提供程序 · 对来自实时音频捕获设备（即计算机音频插孔）的 LTC 信号（线性</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/AudioCaptureTimecodeProvider/AudioCaptureTimecodeProvider.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">对来自实时音频捕获设备（即计算机音频插孔）的 LTC 信号（线性时间码）进行解码。</div><div class="lang-content">Decodes an LTC signal (linear timcode) from a live audio capture device (ie. the computer audio jack).</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：对来自实时音频捕获设备（即计算机音频插孔）的 LTC 信号（线性时间码）进行解码。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：AudioCaptureTimecodeProvider。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Decodes an LTC signal (linear timcode) from a live audio capture device (ie. the computer audio jack).</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: AudioCaptureTimecodeProvider. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Audio Capture Timecode Provider</code>，并同时启用依赖的 <code class="usage-code">Audio Capture</code> 与 <code class="usage-code">Linear Timecode</code>。</li><li>把外部 LTC 接到本机线路/麦克风输入（或 USB 音频接口的干净通道）。</li><li>新建蓝图，父类选 <code class="usage-code">AudioCaptureTimecodeProvider</code>（<code class="usage-code">UAudioCaptureTimecodeProvider</code>）。</li><li>在 Details 设置 <code class="usage-code">AudioChannel</code>（从 1 起）、<code class="usage-code">FrameRate</code>，或勾选 <code class="usage-code">Detect Frame Rate</code> / <code class="usage-code">Assume Drop Frame Format</code>。</li><li>在 <code class="usage-code">Edit &gt; Project Settings</code> 的 Timecode 里把 Timecode Provider 指到该资产；也可用 Media Profile 覆盖，并设为 Startup Media Profile。</li><li>打开 <code class="usage-code">Window &gt; Virtual Production &gt; Timecode Provider</code>，确认同步状态为 <code class="usage-code">Synchronized</code>。</li><li>Sequencer 里把 Clock Source 设为 <code class="usage-code">Timecode</code>，用 LTC 驱动时间显示。</li></ol><p class="usage-note">从音频口解 LTC，不是 Media Player 播视频；噪声线路会导致丢帧。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Audio Capture Timecode Provider</code>, plus its dependencies <code class="usage-code">Audio Capture</code> and <code class="usage-code">Linear Timecode</code>.</li><li>Route external LTC into the machine line/mic input (or a clean USB audio channel).</li><li>Create a Blueprint whose parent is <code class="usage-code">AudioCaptureTimecodeProvider</code> (<code class="usage-code">UAudioCaptureTimecodeProvider</code>).</li><li>In Details set <code class="usage-code">AudioChannel</code> (1-based), <code class="usage-code">FrameRate</code>, or enable <code class="usage-code">Detect Frame Rate</code> / <code class="usage-code">Assume Drop Frame Format</code>.</li><li>In <code class="usage-code">Edit &gt; Project Settings</code> Timecode, assign that asset as Timecode Provider; a Media Profile can override it as the Startup Media Profile.</li><li>Open <code class="usage-code">Window &gt; Virtual Production &gt; Timecode Provider</code> and wait for <code class="usage-code">Synchronized</code>.</li><li>In Sequencer set Clock Source to <code class="usage-code">Timecode</code> so playback follows LTC.</li></ol><p class="usage-note">Decodes LTC from an audio jack, not a Media Player; a noisy line will drop frames.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AudioCaptureTimecodeProvider</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/AudioCaptureTimecodeProvider/AudioCaptureTimecodeProvider.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
