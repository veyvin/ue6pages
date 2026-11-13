---
layout: default
title: 美元进口商 / USD Importer
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">U</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">USD Importer</div>
      <div class="hero-title-cn">美元进口商 · 添加了将 USD 文件格式导入虚幻引擎的支持</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Importers</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">9</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Importers/USDImporter/USDImporter.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">添加了将 USD 文件格式导入虚幻引擎的支持</div><div class="lang-content">Adds support for importing the USD file format into Unreal Engine</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：添加了将 USD 文件格式导入虚幻引擎的支持</p><p>导入管线：把 DCC/CAD/USD 资产转成引擎网格、材质与关卡。</p><p>属于资产导入管线。</p><p>它打包的模块包括：USDSchemas, USDStage, USDStageEditor, USDStageImporter, USDStageEditorViewModels, USDExporter, USDClassesEditor, GeometryCacheUSD 等。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Adds support for importing the USD file format into Unreal Engine</p><p>Import pipeline: converts DCC/CAD/USD assets into engine meshes, materials, and levels.</p><p>Part of the asset-import pipeline.</p><p>It ships these modules: USDSchemas, USDStage, USDStageEditor, USDStageImporter, USDStageEditorViewModels, USDExporter, USDClassesEditor, GeometryCacheUSD 等. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">USD Importer</code>（模块 <code class="usage-code">USDSchemas</code>、<code class="usage-code">USDStage</code>、<code class="usage-code">USDStageImporter</code>、<code class="usage-code">USDExporter</code>、<code class="usage-code">GeometryCacheUSD</code>，编辑器 <code class="usage-code">USDStageEditor</code> 等）。</li><li>它添加把 USD 文件格式导入引擎的支持（USD Stage Actor、导入/导出）。</li><li>用 USD Stage Actor 加载 .usd/.usda/.usdc，或经导入管线转成引擎资产。</li><li>Game 模块依赖运行时模块；<code class="usage-code">USDStageEditor</code> 等只进 Editor Target。</li></ol><p class="usage-note">把 USD 文件格式导入引擎（USD Stage/导入导出）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">USD Importer</code> (modules <code class="usage-code">USDSchemas</code>, <code class="usage-code">USDStage</code>, <code class="usage-code">USDStageImporter</code>, <code class="usage-code">USDExporter</code>, <code class="usage-code">GeometryCacheUSD</code>, editor <code class="usage-code">USDStageEditor</code>, etc.).</li><li>It adds support for importing the USD file format into the engine (USD Stage Actor, import/export).</li><li>Load .usd/.usda/.usdc via a USD Stage Actor, or convert through the import pipeline into engine assets.</li><li>Game modules depend on runtime modules; <code class="usage-code">USDStageEditor</code> etc. go to Editor targets only.</li></ol><p class="usage-note">Imports the USD file format into the engine (USD Stage/import-export).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (9)</div><div class="module-item"><span class="dot"></span><span class="name mono">USDSchemas</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">USDStage</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">USDStageEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">USDStageImporter</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">USDStageEditorViewModels</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">USDExporter</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">USDClassesEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GeometryCacheUSD</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">USDTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Importers/USDImporter/USDImporter.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
