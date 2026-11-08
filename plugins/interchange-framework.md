---
layout: default
title: 交换框架 / Interchange Framework
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">I</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Interchange Framework</div>
      <div class="hero-title-cn">交换框架 · Interchange Framework 插件提供了可自定义的</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Importers</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">12</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Interchange/Runtime/Interchange.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Interchange Framework 插件提供了可自定义的导入和导出系统，以及一组可扩展的管道用于处理常见文件类型。</div><div class="lang-content">The Interchange Framework plugin offers a customizable import and export system, with an extensible set of pipelines for handling common file types.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Interchange Framework 插件提供了可自定义的导入和导出系统，以及一组可扩展的管道用于处理常见文件类型。</p><p>导入管线：把 DCC/CAD/USD 资产转成引擎网格、材质与关卡。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：GLTFCore, InterchangeNodes, InterchangeFactoryNodes, InterchangeImport, InterchangeMessages, InterchangeExport, InterchangePipelines, InterchangeDispatcher 等。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: The Interchange Framework plugin offers a customizable import and export system, with an extensible set of pipelines for handling common file types.</p><p>Import pipeline: converts DCC/CAD/USD assets into engine meshes, materials, and levels.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: GLTFCore, InterchangeNodes, InterchangeFactoryNodes, InterchangeImport, InterchangeMessages, InterchangeExport, InterchangePipelines, InterchangeDispatcher 等. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Interchange Framework</code>（模块 <code class="usage-code">InterchangeImport</code>、<code class="usage-code">InterchangeExport</code>、<code class="usage-code">InterchangePipelines</code>、<code class="usage-code">InterchangeDispatcher</code>、<code class="usage-code">InterchangeNodes</code> 等）。</li><li>用其可自定义的导入/导出系统与可扩展管道处理常见文件类型（glTF、USD、FBX 等）。</li><li>通过管道（Pipeline）决定导入步骤：解析→节点→工厂→资产。</li><li>运行时导入/导出依赖对应模块；编辑器管道配置用 Interchange Editor。</li></ol><p class="usage-note">Interchange 导入/导出的核心框架，取代旧导入器的新体系。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Interchange Framework</code> (modules <code class="usage-code">InterchangeImport</code>, <code class="usage-code">InterchangeExport</code>, <code class="usage-code">InterchangePipelines</code>, <code class="usage-code">InterchangeDispatcher</code>, <code class="usage-code">InterchangeNodes</code>, etc.).</li><li>Use its customizable import/export system and extensible pipelines to handle common file types (glTF, USD, FBX, etc.).</li><li>Pipelines drive the import steps: parse → nodes → factory → assets.</li><li>Runtime import/export depends on the relevant modules; configure pipelines with Interchange Editor.</li></ol><p class="usage-note">The core Interchange import/export framework, the newer system replacing legacy importers.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (12)</div><div class="module-item"><span class="dot"></span><span class="name mono">GLTFCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeNodes</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeFactoryNodes</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeImport</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeMessages</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeExport</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangePipelines</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeDispatcher</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeCommon</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeAnalytics</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeCommonParser</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeFbxParser</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Interchange/Runtime/Interchange.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
