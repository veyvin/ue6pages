---
layout: default
title: Avid DNxHR/DNxMXF 媒体插件 / Avid DNxHR/DNxMXF Media Plugin
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Avid DNxHR/DNxMXF Media Plugin</div>
      <div class="hero-title-cn">Avid DNxHR/DNxMXF 媒体插件 · 使用 Avid DNx 编解码器实现视频导出。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/AvidDNxMedia/AvidDNxMedia.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用 Avid DNx 编解码器实现视频导出。</div><div class="lang-content">Implements video export using Avid DNx Codecs.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用 Avid DNx 编解码器实现视频导出。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：AvidDNxMedia。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements video export using Avid DNx Codecs.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: AvidDNxMedia. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 <code class="usage-code">Edit &gt; Plugins</code> 启用 <code class="usage-code">Avid DNxHR/DNxMXF Media Plugin</code>（<code class="usage-code">AvidDNxMedia.uplugin</code>）并重启。这是导出编码器，不是 Electra 的 DNxHD 软解。</li><li>打开 <code class="usage-code">Window &gt; Cinematics &gt; Movie Render Queue</code>，把 Level Sequence 加入队列，在 Job 的 Settings 里 <code class="usage-code">+ Setting</code> 增加 <code class="usage-code">Avid DNx [8bit]</code>（名称随引擎小版本可能略有出入）。</li><li>输出容器为 <code class="usage-code">.mxf</code>。在该设置里开关 <code class="usage-code">Use Compression</code>（压缩 DNxHR vs 未压缩）、设置 <code class="usage-code">Number of Encoding Threads</code>。DNx 轨不含内嵌音频，再加一项 <code class="usage-code">WAV Audio</code> 以便后期合成。</li><li>C++ 直接写 MXF 时依赖模块 <code class="usage-code">AvidDNxMedia</code>，使用 <code class="usage-code">FAvidDNxEncoder</code>（头文件 <code class="usage-code">AvidDNxEncoder/AvidDNxEncoder.h</code>）：<code class="usage-code">Initialize</code> → 每帧 <code class="usage-code">WriteFrame</code> / <code class="usage-code">WriteFrame_16bit</code> → <code class="usage-code">Finalize</code>。当前 MXF writer 不写音频。</li><li>按 Avid 规格核对待机分辨率与帧率（例如 1920×1080 @ 24/25/30）。渲染完成用外部 NLE 打开 <code class="usage-code">.mxf</code>，不要用普通 <code class="usage-code">Media Player</code> 当验收手段。</li></ol><p class="usage-note">Movie Render Queue / `FAvidDNxEncoder` 出 `.mxf`。与 `AvidDNxHDDecoderElectra` 职责相反。音频需单独 WAV。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Avid DNxHR/DNxMXF Media Plugin</code> (<code class="usage-code">AvidDNxMedia.uplugin</code>) in <code class="usage-code">Edit &gt; Plugins</code> and restart. This is an export encoder, not Electra’s DNxHD software decoder.</li><li>Open <code class="usage-code">Window &gt; Cinematics &gt; Movie Render Queue</code>, add a Level Sequence, and in the job Settings use <code class="usage-code">+ Setting</code> to add <code class="usage-code">Avid DNx [8bit]</code> (label may vary slightly by engine version).</li><li>The container is <code class="usage-code">.mxf</code>. Toggle <code class="usage-code">Use Compression</code> (lossy DNxHR vs uncompressed) and set <code class="usage-code">Number of Encoding Threads</code>. DNx does not embed audio — add a <code class="usage-code">WAV Audio</code> setting and mux in post.</li><li>For C++ MXF writers, depend on <code class="usage-code">AvidDNxMedia</code> and <code class="usage-code">FAvidDNxEncoder</code> (<code class="usage-code">AvidDNxEncoder/AvidDNxEncoder.h</code>): <code class="usage-code">Initialize</code>, per-frame <code class="usage-code">WriteFrame</code> / <code class="usage-code">WriteFrame_16bit</code>, then <code class="usage-code">Finalize</code>. The bundled MXF writer does not write audio.</li><li>Match Avid-legal resolutions and frame rates (for example 1920×1080 at 24/25/30). Open the <code class="usage-code">.mxf</code> in an NLE; a generic <code class="usage-code">Media Player</code> is not a finishing check.</li></ol><p class="usage-note">Writes `.mxf` via Movie Render Queue / `FAvidDNxEncoder`. Opposite job from `AvidDNxHDDecoderElectra`. Audio is a separate WAV.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AvidDNxMedia</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/AvidDNxMedia/AvidDNxMedia.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
