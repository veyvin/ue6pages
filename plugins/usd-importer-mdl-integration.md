---
layout: default
title: 美元进口商 MDL 整合 / USD Importer MDL integration
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">U</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">USD Importer MDL integration</div>
      <div class="hero-title-cn">美元进口商 MDL 整合 · 允许通过 USD Stage Actor 和 USD 导入导入引</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Importers</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Importers/USDImporterMDL/USDImporterMDL.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">允许通过 USD Stage Actor 和 USD 导入导入引用 MDL 文件的 USD 文件</div><div class="lang-content">Allows importing USD files that reference MDL files, via the USD Stage Actor and USD import</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：允许通过 USD Stage Actor 和 USD 导入导入引用 MDL 文件的 USD 文件</p><p>导入管线：把 DCC/CAD/USD 资产转成引擎网格、材质与关卡。</p><p>属于资产导入管线。</p><p>它打包的模块包括：USDImporterMDL。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Allows importing USD files that reference MDL files, via the USD Stage Actor and USD import</p><p>Import pipeline: converts DCC/CAD/USD assets into engine meshes, materials, and levels.</p><p>Part of the asset-import pipeline.</p><p>It ships these modules: USDImporterMDL. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">USD Importer MDL integration</code>（模块 <code class="usage-code">USDImporterMDL</code>）。</li><li>它允许通过 USD Stage Actor 与 USD 导入导入引用 MDL 文件的 USD 文件。</li><li>导入含 MDL 材质引用的 USD，自动关联 MDL。</li><li>属 USD 导入扩展；需 USD Importer。</li></ol><p class="usage-note">通过 USD Stage/USD 导入引用 MDL 文件的 USD。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">USD Importer MDL integration</code> (module <code class="usage-code">USDImporterMDL</code>).</li><li>It lets you import USD files that reference MDL files via the USD Stage Actor and USD import.</li><li>Import USD with MDL material references and link them automatically.</li><li>It is a USD import extension; requires the USD Importer.</li></ol><p class="usage-note">Imports USD files referencing MDL via USD Stage/USD import.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">USDImporterMDL</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Importers/USDImporterMDL/USDImporterMDL.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
