---
layout: default
title: 小部件查找器 / Widget Finder
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">W</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Widget Finder</div>
      <div class="hero-title-cn">小部件查找器 · 通过查询查找实时 Slate 小部件。将正在运行的小部件树镜像到</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Editor</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/WidgetFinder/WidgetFinder.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">通过查询查找实时 Slate 小部件。将正在运行的小部件树镜像到可查询的存储中，并添加一个浏览器面板来搜索它并在屏幕上突出显示匹配项。</div><div class="lang-content">Find live Slate widgets by query. Mirrors the running widget tree into a queryable store and adds a browser panel that searches it and highlights matches on screen.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：通过查询查找实时 Slate 小部件。将正在运行的小部件树镜像到可查询的存储中，并添加一个浏览器面板来搜索它并在屏幕上突出显示匹配项。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：WidgetFinderCore, WidgetFinderSQLite, WidgetFinderTEDS, WidgetFinder, WidgetFinderEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Find live Slate widgets by query. Mirrors the running widget tree into a queryable store and adds a browser panel that searches it and highlights matches on screen.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: WidgetFinderCore, WidgetFinderSQLite, WidgetFinderTEDS, WidgetFinder, WidgetFinderEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">Widget Finder</code>（模块 <code class="usage-code">WidgetFinderCore</code>、<code class="usage-code">WidgetFinderSQLite</code>、<code class="usage-code">WidgetFinderTEDS</code>、<code class="usage-code">WidgetFinder</code>，编辑器 <code class="usage-code">WidgetFinderEditor</code>）。</li><li>它通过查询查找实时 Slate 小部件：把运行中的小部件树镜像到可查询存储，并提供浏览器面板搜索与高亮。</li><li>在 UI 调试时用浏览器面板查询小部件并在屏幕上高亮匹配项。</li><li>这是编辑器/调试工具；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">通过查询查找实时 Slate 小部件并高亮的工具。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">Widget Finder</code> (modules <code class="usage-code">WidgetFinderCore</code>, <code class="usage-code">WidgetFinderSQLite</code>, <code class="usage-code">WidgetFinderTEDS</code>, <code class="usage-code">WidgetFinder</code>, editor <code class="usage-code">WidgetFinderEditor</code>).</li><li>It finds live Slate widgets via queries: mirrors the running widget tree into a queryable store and adds a browser panel to search and highlight matches on screen.</li><li>During UI debugging, use the browser panel to query widgets and highlight matches on screen.</li><li>It is an editor/debug tool; editor modules go to Editor targets only.</li></ol><p class="usage-note">Find live Slate widgets via queries and highlight them.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">WidgetFinderCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WidgetFinderSQLite</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WidgetFinderTEDS</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WidgetFinder</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WidgetFinderEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/WidgetFinder/WidgetFinder.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
