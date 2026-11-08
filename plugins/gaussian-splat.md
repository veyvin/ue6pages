---
layout: default
title: 高斯分布 / Gaussian Splat
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Gaussian Splat</div>
      <div class="hero-title-cn">高斯分布 · Gaussian Splat 资源和 ES3.1+ 渲染。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Rendering</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">8</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/GaussianSplat/GaussianSplat.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Gaussian Splat 资源和 ES3.1+ 渲染。</div><div class="lang-content">Gaussian Splat asset and ES3.1+ rendering.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Gaussian Splat 资源和 ES3.1+ 渲染。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：GaussianSplat, GaussianSplatShader, GaussianSplatSceneViewExtension, GaussianSplatEditor, GaussianSplatNiagara, GaussianSplatNiagaraShader, GaussianSplatNiagaraEditor, GaussianSplatTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Gaussian Splat asset and ES3.1+ rendering.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: GaussianSplat, GaussianSplatShader, GaussianSplatSceneViewExtension, GaussianSplatEditor, GaussianSplatNiagara, GaussianSplatNiagaraShader, GaussianSplatNiagaraEditor, GaussianSplatTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Gaussian Splat</code>（运行时 <code class="usage-code">GaussianSplat</code>，另有 <code class="usage-code">GaussianSplatShader</code>、<code class="usage-code">GaussianSplatSceneViewExtension</code> 与 <code class="usage-code">GaussianSplatEditor</code>、Niagara 相关模块）。</li><li>导入或创建 Gaussian Splat 资产，把它放进关卡（或用 Niagara 版本驱动）。</li><li>确认目标平台支持 ES3.1+ 的渲染路径，PIE 里查看 splat 的显示效果。</li><li>游戏运行时依赖 <code class="usage-code">GaussianSplat</code>；<code class="usage-code">GaussianSplatEditor</code> 只用于编辑器。</li></ol><p class="usage-note">Gaussian Splat 资产与 ES3.1+ 渲染，需要相应 RHI/移动端支持。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Gaussian Splat</code> (runtime <code class="usage-code">GaussianSplat</code>, plus <code class="usage-code">GaussianSplatShader</code>, <code class="usage-code">GaussianSplatSceneViewExtension</code>, <code class="usage-code">GaussianSplatEditor</code>, and Niagara modules).</li><li>Import or create a Gaussian Splat asset and place it in the level (or drive the Niagara variant).</li><li>Confirm the target platform supports the ES3.1+ rendering path and check the splat in PIE.</li><li>Game runtime depends on <code class="usage-code">GaussianSplat</code>; <code class="usage-code">GaussianSplatEditor</code> is editor-only.</li></ol><p class="usage-note">Gaussian Splat assets and ES3.1+ rendering; requires the matching RHI/mobile support.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (8)</div><div class="module-item"><span class="dot"></span><span class="name mono">GaussianSplat</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GaussianSplatShader</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GaussianSplatSceneViewExtension</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GaussianSplatEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GaussianSplatNiagara</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GaussianSplatNiagaraShader</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GaussianSplatNiagaraEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GaussianSplatTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/GaussianSplat/GaussianSplat.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
