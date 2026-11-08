---
layout: default
title: 影片渲染队列 / Movie Render Queue
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Movie Render Queue</div>
      <div class="hero-title-cn">影片渲染队列 · 高级电影渲染管道，用于创建渲染过场动画或其他多媒体创作。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Rendering</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.3</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">6</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/MovieScene/MovieRenderPipeline/MovieRenderPipeline.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">高级电影渲染管道，用于创建渲染过场动画或其他多媒体创作。</div><div class="lang-content">Advanced movie rendering pipeline for use in creating rendered cinematics or other multi-media creation.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：高级电影渲染管道，用于创建渲染过场动画或其他多媒体创作。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：MovieRenderPipelineCore, MovieRenderPipelineSettings, MovieRenderPipelineRenderPasses, MovieRenderPipelineEditor, MovieRenderPipelineMP4Encoder, UEOpenExrRTTI。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Advanced movie rendering pipeline for use in creating rendered cinematics or other multi-media creation.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: MovieRenderPipelineCore, MovieRenderPipelineSettings, MovieRenderPipelineRenderPasses, MovieRenderPipelineEditor, MovieRenderPipelineMP4Encoder, UEOpenExrRTTI. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Movie Render Queue</code>（模块 <code class="usage-code">MovieRenderPipelineCore</code>、<code class="usage-code">MovieRenderPipelineSettings</code>、<code class="usage-code">MovieRenderPipelineRenderPasses</code>、<code class="usage-code">MovieRenderPipelineMP4Encoder</code>、<code class="usage-code">UEOpenExrRTTI</code>，编辑器 <code class="usage-code">MovieRenderPipelineEditor</code>）。</li><li>它是高级电影渲染管线，用于高质量渲染过场动画/多媒体（抗锯齿、多通道、MP4/EXR 输出）。</li><li>通过 MRQ 面板排队渲染、配置设置与输出，得到最终画面。</li><li>Game 模块依赖运行时模块；<code class="usage-code">MovieRenderPipelineEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">高质量电影渲染管线（MRQ），输出 MP4/EXR/多通道。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Movie Render Queue</code> (modules <code class="usage-code">MovieRenderPipelineCore</code>, <code class="usage-code">MovieRenderPipelineSettings</code>, <code class="usage-code">MovieRenderPipelineRenderPasses</code>, <code class="usage-code">MovieRenderPipelineMP4Encoder</code>, <code class="usage-code">UEOpenExrRTTI</code>, editor <code class="usage-code">MovieRenderPipelineEditor</code>).</li><li>It is an advanced movie-render pipeline for high-quality cinematics/multimedia (AA, multi-pass, MP4/EXR output).</li><li>Queue renders in the MRQ panel, set settings and outputs, and produce final frames.</li><li>Game modules depend on runtime modules; <code class="usage-code">MovieRenderPipelineEditor</code> is Editor-target only.</li></ol><p class="usage-note">The high-quality movie-render pipeline (MRQ) with MP4/EXR/multi-pass output.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (6)</div><div class="module-item"><span class="dot"></span><span class="name mono">MovieRenderPipelineCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MovieRenderPipelineSettings</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MovieRenderPipelineRenderPasses</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MovieRenderPipelineEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MovieRenderPipelineMP4Encoder</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UEOpenExrRTTI</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/MovieScene/MovieRenderPipeline/MovieRenderPipeline.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
