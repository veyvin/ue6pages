---
layout: default
title: 出处C2PA / ProvenanceC2PA
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">P</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">ProvenanceC2PA</div>
      <div class="hero-title-cn">出处C2PA · 使用 C2PA 内容凭证标准实现 AssetProvenance</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Provenance</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Developer/Provenance/ProvenanceC2PA/ProvenanceC2PA.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用 C2PA 内容凭证标准实现 AssetProvenance 的读/写来源数据。</div><div class="lang-content">Implements AssetProvenance's read/write provenance data using the C2PA content credentials standard.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用 C2PA 内容凭证标准实现 AssetProvenance 的读/写来源数据。</p><p>编辑器或开发者插件，服务制作流程，默认不进 Shipping。</p><p>它打包的模块包括：ProvenanceC2PA。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Implements AssetProvenance's read/write provenance data using the C2PA content credentials standard.</p><p>An editor/developer plugin for the authoring pipeline; it does not ship by default.</p><p>It ships these modules: ProvenanceC2PA. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">ProvenanceC2PA</code>（模块 <code class="usage-code">ProvenanceC2PA</code>）。</li><li>它用 C2PA 内容凭证标准实现 AssetProvenance 的读/写来源数据。</li><li>在需要资产出处/内容凭证的管线里启用，读写 C2PA 元数据。</li><li>属来源/凭证插件；按合规需求启用。</li></ol><p class="usage-note">用 C2PA 内容凭证读写资产来源数据。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">ProvenanceC2PA</code> (module <code class="usage-code">ProvenanceC2PA</code>).</li><li>It implements AssetProvenance read/write using the C2PA content-credentials standard.</li><li>Enable it in pipelines that need asset provenance/content credentials to read/write C2PA metadata.</li><li>It is a provenance/credentials plugin; enable per compliance need.</li></ol><p class="usage-note">Read/write asset provenance via C2PA content credentials.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ProvenanceC2PA</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Developer/Provenance/ProvenanceC2PA/ProvenanceC2PA.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
