---
layout: default
title: 适用于 Electra 的 Avid DNxHD® 解码器 / Avid DNxHD® decoder for Electra
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Avid DNxHD® decoder for Electra</div>
      <div class="hero-title-cn">适用于 Electra 的 Avid DNxHD® 解码器 · Avid DNxHD® 视频解码器</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/AvidDNxHDDecoderElectra/AvidDNxHDDecoderElectra.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Avid DNxHD® 视频解码器</div><div class="lang-content">Avid DNxHD® video decoder</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Avid DNxHD® 视频解码器</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：AvidDNxHDDecoderElectra。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Avid DNxHD® video decoder</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: AvidDNxHDDecoderElectra. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Avid DNxHD® decoder for Electra</code>（<code class="usage-code">AvidDNxHDDecoderElectra.uplugin</code>）并确保 <code class="usage-code">Electra Player</code> 已开，重启编辑器。</li><li>准备 Avid DNxHD 编码的审查片（常见 <code class="usage-code">.mxf</code> / <code class="usage-code">.mov</code>）。本插件只解码 DNxHD 供 Electra 播放，不负责 DNxHR 导出。</li><li>创建 <code class="usage-code">File Media Source</code> 指向该文件；<code class="usage-code">Media Player</code> 首选 Electra。打开后 Electra 按 codec id 挂上 <code class="usage-code">AvidDNxHDDecoderElectra</code>。</li><li>用 <code class="usage-code">Media Texture</code> / <code class="usage-code">Media Plate</code> 上屏，核对分辨率、帧率与色彩是否与后期交付一致。虚拟制片回放时把引擎 <code class="usage-code">Timecode Provider</code> 与片源时码对齐。</li><li>不要在蓝图里查找「DNxHD 组件」。游戏 <code class="usage-code">Build.cs</code> 通常不用链接 <code class="usage-code">AvidDNxHDDecoderElectra</code>；只有扩展 Electra 解码器时才包含该模块。</li></ol><p class="usage-note">只服务 Electra 播放 DNxHD。导出 MXF/DNxHR 请用 `Avid DNxHR/DNxMXF Media Plugin`，不要混用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Avid DNxHD® decoder for Electra</code> (<code class="usage-code">AvidDNxHDDecoderElectra.uplugin</code>), keep <code class="usage-code">Electra Player</code> on, and restart the editor.</li><li>Stage Avid DNxHD review media (typically <code class="usage-code">.mxf</code> / <code class="usage-code">.mov</code>). This plugin only decodes DNxHD for Electra; it does not export DNxHR.</li><li>Create a <code class="usage-code">File Media Source</code> to that file and prefer Electra on the <code class="usage-code">Media Player</code>. Electra attaches <code class="usage-code">AvidDNxHDDecoderElectra</code> from the codec id.</li><li>Display through a <code class="usage-code">Media Texture</code> / <code class="usage-code">Media Plate</code> and check resolution, frame rate, and color against the finishing spec. For virtual-production playback, align the engine <code class="usage-code">Timecode Provider</code> with the file’s timecode.</li><li>There is no Blueprint “DNxHD component”. Game <code class="usage-code">Build.cs</code> files usually skip <code class="usage-code">AvidDNxHDDecoderElectra</code>; include it only when extending Electra’s decoder list.</li></ol><p class="usage-note">Decode-only for Electra DNxHD playback. Exporting MXF/DNxHR is the other Avid DNx plugin — do not mix the two.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AvidDNxHDDecoderElectra</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/AvidDNxHDDecoderElectra/AvidDNxHDDecoderElectra.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
