---
layout: default
title: Electra 的 FLAC 音频解码器 / FLAC audio decoder for Electra
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">FLAC audio decoder for Electra</div>
      <div class="hero-title-cn">Electra 的 FLAC 音频解码器 · 使用 Electra 媒体播放器实现 FLAC 音频播放</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/FlacDecoderElectra/FlacDecoderElectra.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用 Electra 媒体播放器实现 FLAC 音频播放</div><div class="lang-content">Implements FLAC audio playback with the Electra media player</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用 Electra 媒体播放器实现 FLAC 音频播放</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：FlacDecoderElectra。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements FLAC audio playback with the Electra media player</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: FlacDecoderElectra. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>同时启用 <code class="usage-code">Electra Player</code> 与 <code class="usage-code">FLAC audio decoder for Electra</code>（模块 <code class="usage-code">FlacDecoderElectra</code>）后重启。本插件只向 Electra 注册 FLAC 解码器，不新建播放器窗口。</li><li>准备 <code class="usage-code">.flac</code>（或容器内 FLAC 音轨）。创建 <code class="usage-code">File Media Source</code> 指向该文件，再创建 <code class="usage-code">Media Player</code>，播放器后端选 Electra 而不是 WMF/<code class="usage-code">Android Media</code>。</li><li>把 <code class="usage-code">Media Texture</code> 可省略（纯音频）；用 <code class="usage-code">Media Sound Component</code> 或 Media Player 的音轨输出监听。蓝图 <code class="usage-code">Open Source</code> → <code class="usage-code">Play</code>。</li><li>Output Log 应出现 Electra 挂上 <code class="usage-code">FlacDecoderElectra</code>；若提示 codec 不支持，确认 Player 不是 WMF，且文件确实是 FLAC 而非 ALAC/Opus。</li><li>游戏 <code class="usage-code">Build.cs</code> 通常不必直接依赖 <code class="usage-code">FlacDecoderElectra</code>；插件启用后 Electra 工厂会加载它。不要把它当成 <code class="usage-code">Audio Mixer</code> 的解码器去播 <code class="usage-code">USoundWave</code>。</li></ol><p class="usage-note">Electra 的 FLAC 编解码后端，不是 Sound Cue / MetaSound 解码器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable both <code class="usage-code">Electra Player</code> and <code class="usage-code">FLAC audio decoder for Electra</code> (module <code class="usage-code">FlacDecoderElectra</code>) and restart. The plugin only registers a FLAC decoder with Electra — no new player UI.</li><li>Point a <code class="usage-code">File Media Source</code> at a <code class="usage-code">.flac</code> (or a container with a FLAC track). Create a <code class="usage-code">Media Player</code> and select Electra, not WMF/<code class="usage-code">Android Media</code>.</li><li>Skip <code class="usage-code">Media Texture</code> for audio-only; listen via <code class="usage-code">Media Sound Component</code> or the player’s audio bus. Blueprint: <code class="usage-code">Open Source</code> then <code class="usage-code">Play</code>.</li><li>Output Log should show Electra attaching <code class="usage-code">FlacDecoderElectra</code>. If the codec is unsupported, the player is probably WMF, or the file is ALAC/Opus rather than FLAC.</li><li>Game <code class="usage-code">Build.cs</code> usually need not list <code class="usage-code">FlacDecoderElectra</code>; Electra’s factory loads it when the plugin is on. It does not decode <code class="usage-code">USoundWave</code> through Audio Mixer.</li></ol><p class="usage-note">Electra FLAC codec backend, not a Sound Cue / MetaSound decoder.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">FlacDecoderElectra</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/FlacDecoderElectra/FlacDecoderElectra.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
