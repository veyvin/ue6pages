---
layout: default
title: 平铺 Mipmap 视频播放器 / Tiled Mipmap Video Player
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">T</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Tiled Mipmap Video Player</div>
      <div class="hero-title-cn">平铺 Mipmap 视频播放器 · 用于平铺 mipmap 视频 (TMV) 播放的框架，包括转码工</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/TmvMedia/TmvMedia.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于平铺 mipmap 视频 (TMV) 播放的框架，包括转码工具。
使用高级专业视频 (APV) 编解码器实现。</div><div class="lang-content">Framework for tiled-mipmap video (TMV) playback, includes transcoding tools.
Implemented using Advanced Professional Video (APV) codec.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于平铺 mipmap 视频 (TMV) 播放的框架，包括转码工具。
使用高级专业视频 (APV) 编解码器实现。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：TmvMedia, TmvMediaEditor, TmvMediaShaders, ApvMedia, TmvMediaMp4Utils。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Framework for tiled-mipmap video (TMV) playback, includes transcoding tools.
Implemented using Advanced Professional Video (APV) codec.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: TmvMedia, TmvMediaEditor, TmvMediaShaders, ApvMedia, TmvMediaMp4Utils. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Tiled Mipmap Video Player</code>（模块 <code class="usage-code">TmvMedia</code>、<code class="usage-code">TmvMediaShaders</code>、<code class="usage-code">ApvMedia</code>、<code class="usage-code">TmvMediaMp4Utils</code>，编辑器 <code class="usage-code">TmvMediaEditor</code>）。</li><li>它是平铺 mipmap 视频(TMV)播放框架，含转码工具，并使用 APV 编解码器实现。</li><li>把支持 TMV/APV 的视频播放到材质/Media Plate（适合大分辨率流式）。</li><li>属 Media Framework 播放扩展；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">平铺 mipmap 视频(TMV)播放框架（含转码，基于 APV）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Tiled Mipmap Video Player</code> (modules <code class="usage-code">TmvMedia</code>, <code class="usage-code">TmvMediaShaders</code>, <code class="usage-code">ApvMedia</code>, <code class="usage-code">TmvMediaMp4Utils</code>, editor <code class="usage-code">TmvMediaEditor</code>).</li><li>It is a Tiled Mipmap Video (TMV) playback framework including transcode tools, implemented with the APV codec.</li><li>Play TMV/APV video onto materials/Media Plate (good for large-resolution streaming).</li><li>It is a Media Framework playback extension; editor modules go to Editor targets only.</li></ol><p class="usage-note">A Tiled Mipmap Video (TMV) playback framework (transcode, APV-based).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">TmvMedia</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TmvMediaEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TmvMediaShaders</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ApvMedia</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TmvMediaMp4Utils</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/TmvMedia/TmvMedia.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
