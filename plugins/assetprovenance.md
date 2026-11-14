---
layout: default
title: 资产来源 / AssetProvenance
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AssetProvenance</div>
      <div class="hero-title-cn">资产来源 · 读取和写入记录资产来源和编辑历史的来源数据。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Provenance</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Developer/Provenance/AssetProvenance/AssetProvenance.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">读取和写入记录资产来源和编辑历史的来源数据。</div><div class="lang-content">Reads and writes provenance data recording the origin and edit history of assets.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：读取和写入记录资产来源和编辑历史的来源数据。</p><p>编辑器或开发者插件，服务制作流程，默认不进 Shipping。</p><p>它打包的模块包括：AssetProvenance, AssetProvenanceUI, AssetProvenanceEditorWorkflows。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Reads and writes provenance data recording the origin and edit history of assets.</p><p>An editor/developer plugin for the authoring pipeline; it does not ship by default.</p><p>It ships these modules: AssetProvenance, AssetProvenanceUI, AssetProvenanceEditorWorkflows. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Developer 插件 <code class="usage-code">AssetProvenance</code>（<code class="usage-code">AssetProvenance</code>、<code class="usage-code">AssetProvenanceUI</code>、<code class="usage-code">AssetProvenanceEditorWorkflows</code>）并重启。</li><li>按项目管线导入或保存资产（FBX/USD/再导入）；<code class="usage-code">AssetProvenanceEditorWorkflows</code> 在编辑器导入/保存时写入来源与编辑历史。</li><li>选中资产，用 <code class="usage-code">AssetProvenanceUI</code> 提供的来源面板查看原始路径、工具和后续编辑记录。</li><li>需要程序读取时，只让编辑器工具模块依赖 <code class="usage-code">AssetProvenance</code> 读写来源数据，不要把 UI/Workflows 当游戏组件挂到 Actor。</li><li><code class="usage-code">AssetProvenanceEditorWorkflows</code> 与 <code class="usage-code">AssetProvenanceUI</code> 仅进 Editor Target；Shipping 不要依赖它们。</li></ol><p class="usage-note">记录资产从哪来、谁改过，服务制作审计，不是 Gameplay Tag，也不是内容浏览器 Collection。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the Developer plugin <code class="usage-code">AssetProvenance</code> (<code class="usage-code">AssetProvenance</code>, <code class="usage-code">AssetProvenanceUI</code>, <code class="usage-code">AssetProvenanceEditorWorkflows</code>) and restart.</li><li>Import or save assets through your pipeline (FBX/USD/reimport); <code class="usage-code">AssetProvenanceEditorWorkflows</code> writes origin and edit history on editor import/save.</li><li>Select an asset and inspect original path, tool, and later edits in the provenance UI from <code class="usage-code">AssetProvenanceUI</code>.</li><li>For code access, depend on <code class="usage-code">AssetProvenance</code> from editor tooling only — do not add UI/workflow types as actor components.</li><li>Keep <code class="usage-code">AssetProvenanceEditorWorkflows</code> and <code class="usage-code">AssetProvenanceUI</code> on Editor targets; do not ship them.</li></ol><p class="usage-note">Origin/edit-history records for authoring audit — not Gameplay Tags and not Content Browser Collections.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">AssetProvenance</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AssetProvenanceUI</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AssetProvenanceEditorWorkflows</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Developer/Provenance/AssetProvenance/AssetProvenance.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
