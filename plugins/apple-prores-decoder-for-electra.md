---
layout: default
title: 适用于 Electra 的 Apple ProRes 解码器 / Apple ProRes Decoder for Electra
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Apple ProRes Decoder for Electra</div>
      <div class="hero-title-cn">适用于 Electra 的 Apple ProRes 解码器 · 实现 Apple ProRes 编码视频的视频播放。 Apple</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/AppleProResDecoderElectra/AppleProResDecoderElectra.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">实现 Apple ProRes 编码视频的视频播放。 Apple ProRes 是一种高品质、有损视频压缩格式。</div><div class="lang-content">Implements video playback of Apple ProRes encoded videos. Apple ProRes is a high quality, lossy video compression format.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：实现 Apple ProRes 编码视频的视频播放。 Apple ProRes 是一种高品质、有损视频压缩格式。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：AppleProResDecoderElectra。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements video playback of Apple ProRes encoded videos. Apple ProRes is a high quality, lossy video compression format.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: AppleProResDecoderElectra. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Apple ProRes Decoder for Electra</code>（<code class="usage-code">AppleProResDecoderElectra.uplugin</code> / 模块 <code class="usage-code">AppleProResDecoderElectra</code>），并保持 <code class="usage-code">Electra Player</code> 开启后重启。</li><li>准备 Apple ProRes 审查片（常见 <code class="usage-code">.mov</code>，四字符码如 <code class="usage-code">apco</code>/<code class="usage-code">apcs</code>/<code class="usage-code">apcn</code>/<code class="usage-code">apch</code>/<code class="usage-code">ap4h</code>）。本模块只给 Electra 解码，不负责 Movie Render Queue 导出。</li><li>新建 <code class="usage-code">File Media Source</code> 指向该文件；<code class="usage-code">Media Player</code> 资产首选 Electra。打开后 Electra 按 codec id 挂上 <code class="usage-code">AppleProResDecoderElectra</code>。</li><li>用 <code class="usage-code">Media Texture</code> / <code class="usage-code">Media Plate</code> 上屏，核对分辨率、帧率与 422/4444 色彩。虚拟制片回放时把引擎 <code class="usage-code">Timecode Provider</code> 与片源时码对齐。</li><li>蓝图里没有「ProRes 组件」。游戏 <code class="usage-code">Build.cs</code> 通常不用链 <code class="usage-code">AppleProResDecoderElectra</code>；只有扩展 Electra 解码器列表时才包含该模块。导出 ProRes 请改用 <code class="usage-code">Apple ProRes Media</code>。</li></ol><p class="usage-note">Electra 的 ProRes 解码插件。出片编码走 `Apple ProRes Media`；不要与启动片 `Apple Movie Player` 混用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Apple ProRes Decoder for Electra</code> (<code class="usage-code">AppleProResDecoderElectra.uplugin</code> / module <code class="usage-code">AppleProResDecoderElectra</code>), keep <code class="usage-code">Electra Player</code> on, and restart.</li><li>Stage Apple ProRes review media (typically <code class="usage-code">.mov</code>, fourCCs such as <code class="usage-code">apco</code>/<code class="usage-code">apcs</code>/<code class="usage-code">apcn</code>/<code class="usage-code">apch</code>/<code class="usage-code">ap4h</code>). This module only decodes for Electra; it does not export via Movie Render Queue.</li><li>Create a <code class="usage-code">File Media Source</code> to that file and prefer Electra on the <code class="usage-code">Media Player</code>. Electra attaches <code class="usage-code">AppleProResDecoderElectra</code> from the codec id.</li><li>Display through a <code class="usage-code">Media Texture</code> / <code class="usage-code">Media Plate</code> and check resolution, frame rate, and 422/4444 color. For virtual-production playback, align the engine <code class="usage-code">Timecode Provider</code> with the file’s timecode.</li><li>There is no Blueprint “ProRes component”. Game <code class="usage-code">Build.cs</code> files usually skip <code class="usage-code">AppleProResDecoderElectra</code>; include it only when extending Electra’s decoder list. Exporting ProRes is <code class="usage-code">Apple ProRes Media</code>.</li></ol><p class="usage-note">Electra’s ProRes decoder. Encoding/export is `Apple ProRes Media`; startup movies are `Apple Movie Player`.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AppleProResDecoderElectra</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/AppleProResDecoderElectra/AppleProResDecoderElectra.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
