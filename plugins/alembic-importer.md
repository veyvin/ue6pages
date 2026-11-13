---
layout: default
title: 蒸馏器进口商 / Alembic Importer
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Alembic Importer</div>
      <div class="hero-title-cn">蒸馏器进口商 · 支持导入 Alembic 文件</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Importers</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Importers/AlembicImporter/AlembicImporter.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持导入 Alembic 文件</div><div class="lang-content">Support importing Alembic files</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：支持导入 Alembic 文件</p><p>导入管线：把 DCC/CAD/USD 资产转成引擎网格、材质与关卡。</p><p>属于资产导入管线。</p><p>它打包的模块包括：AlembicImporter, AlembicLibrary。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Support importing Alembic files</p><p>Import pipeline: converts DCC/CAD/USD assets into engine meshes, materials, and levels.</p><p>Part of the asset-import pipeline.</p><p>It ships these modules: AlembicImporter, AlembicLibrary. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Alembic Importer</code>（编辑器导入 <code class="usage-code">AlembicImporter</code>，第三方库 <code class="usage-code">AlembicLibrary</code>）。</li><li>内容浏览器 Import <code class="usage-code">.abc</code>，在 Alembic 导入对话框选择目标：<code class="usage-code">Static Mesh</code>、<code class="usage-code">Skeletal Mesh</code> 或 <code class="usage-code">Geometry Cache</code>（<code class="usage-code">UAbcImportSettings</code>）。</li><li>Geometry Cache：导入生成 <code class="usage-code">UGeometryCache</code>，关卡放置 <code class="usage-code">GeometryCacheActor</code> / 加 <code class="usage-code">UGeometryCacheComponent</code>，指定资产与播放起止帧。</li><li>在 Sequencer 加 Geometry Cache 轨道对缓存做时间对齐；静态/骨骼网格则检查单位、轴、材质槽。</li><li>不要把 <code class="usage-code">AlembicImporter</code> 链进 Game Target；运行时播放缓存只需引擎的 GeometryCache 组件。</li><li>发束 <code class="usage-code">.abc</code> 不要走这条管线，改用 <code class="usage-code">Alembic Groom Importer</code>。</li></ol><p class="usage-note">网格/缓存 Alembic 导入器；`AlembicLibrary` 是第三方封装，游戏不要直接依赖。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Alembic Importer</code> (import module <code class="usage-code">AlembicImporter</code>, third-party <code class="usage-code">AlembicLibrary</code>).</li><li>Import <code class="usage-code">.abc</code> in the Content Browser and pick <code class="usage-code">Static Mesh</code>, <code class="usage-code">Skeletal Mesh</code>, or <code class="usage-code">Geometry Cache</code> in the Alembic dialog (<code class="usage-code">UAbcImportSettings</code>).</li><li>For caches, you get <code class="usage-code">UGeometryCache</code>; place <code class="usage-code">GeometryCacheActor</code> or add <code class="usage-code">UGeometryCacheComponent</code> and set the asset plus start/end frames.</li><li>Add a Geometry Cache track in Sequencer for timing; for static/skeletal meshes check units, axis, and material slots.</li><li>Do not link <code class="usage-code">AlembicImporter</code> into a Game target; runtime playback uses Geometry Cache components.</li><li>Do not import hair <code class="usage-code">.abc</code> here — use <code class="usage-code">Alembic Groom Importer</code>.</li></ol><p class="usage-note">Mesh/cache Alembic importer; `AlembicLibrary` is a third-party wrapper games should not depend on directly.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AlembicImporter</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AlembicLibrary</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Importers/AlembicImporter/AlembicImporter.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
