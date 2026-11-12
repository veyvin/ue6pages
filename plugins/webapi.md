---
layout: default
title: 网络应用程序接口 / WebAPI
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">W</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">WebAPI</div>
      <div class="hero-title-cn">网络应用程序接口 · 自动生成基于 Web 的 API</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Web</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Web/WebAPI/WebAPI.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">自动生成基于 Web 的 API</div><div class="lang-content">Automated generation of web based APIs</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：自动生成基于 Web 的 API</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：WebAPI, WebAPIEditor, WebAPIBlueprintGraph, WebAPIOpenAPI, WebAPILiquidJS。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Automated generation of web based APIs</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: WebAPI, WebAPIEditor, WebAPIBlueprintGraph, WebAPIOpenAPI, WebAPILiquidJS. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">WebAPI</code>（模块 <code class="usage-code">WebAPI</code>、<code class="usage-code">WebAPILiquidJS</code>、<code class="usage-code">WebAPIOpenAPI</code>、<code class="usage-code">WebAPIBlueprintGraph</code>，编辑器 <code class="usage-code">WebAPIEditor</code>）。</li><li>它用于自动生成基于 Web 的 API（把引擎/蓝图功能暴露成 Web 接口）。</li><li>在编辑器里配置路由/OpenAPI，生成可调用的 Web API。</li><li>Game 模块依赖运行时模块；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">自动生成基于 Web 的 API。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">WebAPI</code> (modules <code class="usage-code">WebAPI</code>, <code class="usage-code">WebAPILiquidJS</code>, <code class="usage-code">WebAPIOpenAPI</code>, <code class="usage-code">WebAPIBlueprintGraph</code>, editor <code class="usage-code">WebAPIEditor</code>).</li><li>It auto-generates web-based APIs (expose engine/Blueprint functionality as web endpoints).</li><li>Configure routes/OpenAPI in the editor to generate callable web APIs.</li><li>Game modules depend on runtime modules; editor modules go to Editor targets only.</li></ol><p class="usage-note">Auto-generate web-based APIs.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">WebAPI</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WebAPIEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WebAPIBlueprintGraph</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WebAPIOpenAPI</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WebAPILiquidJS</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Web/WebAPI/WebAPI.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
