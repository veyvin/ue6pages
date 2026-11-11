---
layout: default
title: AJA媒体播放器 / AJA Media Player
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AJA Media Player</div>
      <div class="hero-title-cn">AJA媒体播放器 · 使用 AJA 采集卡实现输入和输出。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">2.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">6</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/AjaMedia/AjaMedia.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用 AJA 采集卡实现输入和输出。</div><div class="lang-content">Implements input and output using AJA Capture cards.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用 AJA 采集卡实现输入和输出。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：AjaCore, AjaMedia, AjaMediaOutput, AjaMediaFactory, AjaMediaFactory, AjaMediaEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements input and output using AJA Capture cards.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: AjaCore, AjaMedia, AjaMediaOutput, AjaMediaFactory, AjaMediaFactory, AjaMediaEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>安装 AJA 板卡驱动后，启用 <code class="usage-code">AJA Media Player</code>（<code class="usage-code">AjaCore</code>、<code class="usage-code">AjaMedia</code>、<code class="usage-code">AjaMediaOutput</code>、<code class="usage-code">AjaMediaFactory</code>，编辑器 <code class="usage-code">AjaMediaEditor</code>）。</li><li>内容浏览器新建 <code class="usage-code">Aja Media Source</code>（<code class="usage-code">UAjaMediaSource</code>），在 Details 选择设备、SDI 输入、视频格式/色空间。</li><li>建 <code class="usage-code">Media Player</code> 与 <code class="usage-code">Media Texture</code>，Open 该 Source，把纹理赋给材质或 <code class="usage-code">Media Plate</code>，确认视口出现采集画面。</li><li>输出：新建 <code class="usage-code">Aja Media Output</code>（<code class="usage-code">UAjaMediaOutput</code>），配合 Media Capture 把视口或场景捕获送到板卡 SDI Out。</li><li>虚拟制片同步：<code class="usage-code">Project Settings &gt; Engine &gt; General</code> 把 Timecode Provider / Custom Time Step 设为 AJA（<code class="usage-code">UAjaTimecodeProvider</code> / <code class="usage-code">UAjaCustomTimeStep</code>）。</li><li><code class="usage-code">AjaMediaEditor</code> 只进 Editor Target；无板卡时 Source 设备列表为空属预期。</li></ol><p class="usage-note">这是 AJA 采集/输出与时间码，不是 Electra 软件解码器，也不是文件播放器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Install AJA card drivers, then enable <code class="usage-code">AJA Media Player</code> (<code class="usage-code">AjaCore</code>, <code class="usage-code">AjaMedia</code>, <code class="usage-code">AjaMediaOutput</code>, <code class="usage-code">AjaMediaFactory</code>, editor <code class="usage-code">AjaMediaEditor</code>).</li><li>Create an <code class="usage-code">Aja Media Source</code> (<code class="usage-code">UAjaMediaSource</code>) and pick device, SDI input, and video format/color space in Details.</li><li>Create a <code class="usage-code">Media Player</code> and <code class="usage-code">Media Texture</code>, Open that source, assign the texture to a material or <code class="usage-code">Media Plate</code>, and confirm capture in the viewport.</li><li>For output, create <code class="usage-code">Aja Media Output</code> (<code class="usage-code">UAjaMediaOutput</code>) and Media Capture the viewport or scene to the card’s SDI Out.</li><li>For VP lock, set Timecode Provider / Custom Time Step to AJA in <code class="usage-code">Project Settings &gt; Engine &gt; General</code> (<code class="usage-code">UAjaTimecodeProvider</code> / <code class="usage-code">UAjaCustomTimeStep</code>).</li><li>Keep <code class="usage-code">AjaMediaEditor</code> on an Editor target; an empty device list is expected without hardware.</li></ol><p class="usage-note">AJA capture/output and timecode, not an Electra software decoder or file player.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (6)</div><div class="module-item"><span class="dot"></span><span class="name mono">AjaCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AjaMedia</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AjaMediaOutput</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AjaMediaFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AjaMediaFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AjaMediaEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/AjaMedia/AjaMedia.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
