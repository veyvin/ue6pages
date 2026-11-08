---
layout: default
title: 交换编辑器 / Interchange Editor
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">I</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Interchange Editor</div>
      <div class="hero-title-cn">交换编辑器 · Interchange Editor 插件向虚幻编辑器公开 In</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Importers</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Interchange/Editor/InterchangeEditor.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Interchange Editor 插件向虚幻编辑器公开 Interchange 导入框架和管道。</div><div class="lang-content">The Interchange Editor plugin exposes the Interchange import framework and pipelines to Unreal Editor.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Interchange Editor 插件向虚幻编辑器公开 Interchange 导入框架和管道。</p><p>导入管线：把 DCC/CAD/USD 资产转成引擎网格、材质与关卡。</p><p>编辑器或开发者插件，服务制作流程，默认不进 Shipping。</p><p>它打包的模块包括：InterchangeEditor, InterchangeEditorPipelines, InterchangeEditorUtilities。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: The Interchange Editor plugin exposes the Interchange import framework and pipelines to Unreal Editor.</p><p>Import pipeline: converts DCC/CAD/USD assets into engine meshes, materials, and levels.</p><p>An editor/developer plugin for the authoring pipeline; it does not ship by default.</p><p>It ships these modules: InterchangeEditor, InterchangeEditorPipelines, InterchangeEditorUtilities. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Interchange Editor</code>（模块 <code class="usage-code">InterchangeEditor</code>、<code class="usage-code">InterchangeEditorPipelines</code>、<code class="usage-code">InterchangeEditorUtilities</code>）。</li><li>它向编辑器公开 Interchange 导入框架与管道：在编辑器里编辑/选择导入管道和导入选项。</li><li>用它在导入前配置 pipeline stack，决定资产如何被转换。</li><li>这是编辑器侧模块，只进 Editor Target。</li></ol><p class="usage-note">Interchange 的编辑器 UI 与管道配置，纯编辑器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Interchange Editor</code> (modules <code class="usage-code">InterchangeEditor</code>, <code class="usage-code">InterchangeEditorPipelines</code>, <code class="usage-code">InterchangeEditorUtilities</code>).</li><li>It exposes the Interchange import framework and pipelines to the editor for editing/selecting import pipelines and options.</li><li>Use it to configure the pipeline stack before import and control how assets are converted.</li><li>It is editor-side; Editor targets only.</li></ol><p class="usage-note">Editor UI and pipeline config for Interchange, editor-only.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeEditorPipelines</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InterchangeEditorUtilities</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Interchange/Editor/InterchangeEditor.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
