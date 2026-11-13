---
layout: default
title: 网格建模工具集 / Mesh Modeling Toolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Mesh Modeling Toolset</div>
      <div class="hero-title-cn">网格建模工具集 · 一组基于交互式工具框架实现 3D 网格创建和编辑的模块</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">8</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/MeshModelingToolset/MeshModelingToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">一组基于交互式工具框架实现 3D 网格创建和编辑的模块</div><div class="lang-content">A set of modules implementing 3D mesh creation and editing based on the Interactive Tools Framework</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：一组基于交互式工具框架实现 3D 网格创建和编辑的模块</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：MeshModelingTools, MeshModelingToolsEditorOnly, MeshModelingToolsetShaders, ModelingComponents, ModelingComponentsEditorOnly, ModelingOperators, ModelingOperatorsEditorOnly, SkeletalMeshModifiers。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A set of modules implementing 3D mesh creation and editing based on the Interactive Tools Framework</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: MeshModelingTools, MeshModelingToolsEditorOnly, MeshModelingToolsetShaders, ModelingComponents, ModelingComponentsEditorOnly, ModelingOperators, ModelingOperatorsEditorOnly, SkeletalMeshModifiers. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Mesh Modeling Toolset</code>（模块 <code class="usage-code">MeshModelingTools</code>、<code class="usage-code">ModelingComponents</code>、<code class="usage-code">ModelingOperators</code>、<code class="usage-code">SkeletalMeshModifiers</code> 等，含 EditorOnly 版）。</li><li>它基于 Interactive Tools Framework 提供 3D 网格的创建与编辑工具（建模模式核心）。</li><li>在建模模式里对网格做布尔、挤出、雕刻等编辑；编辑器侧工具默认不进 Shipping。</li><li>运行时依赖非 EditorOnly 模块；<code class="usage-code">*EditorOnly</code> 只进 Editor Target。</li></ol><p class="usage-note">建模模式背后的网格编辑工具集（Interactive Tools Framework）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Mesh Modeling Toolset</code> (modules <code class="usage-code">MeshModelingTools</code>, <code class="usage-code">ModelingComponents</code>, <code class="usage-code">ModelingOperators</code>, <code class="usage-code">SkeletalMeshModifiers</code>, etc., incl. EditorOnly variants).</li><li>On the Interactive Tools Framework, it provides 3D mesh creation and editing tools (the core of Modeling Mode).</li><li>In Modeling Mode, boolean/extrude/sculpt meshes; editor-side tools do not ship by default.</li><li>Runtime depends on non-EditorOnly modules; <code class="usage-code">*EditorOnly</code> goes to Editor targets only.</li></ol><p class="usage-note">The mesh-editing toolset behind Modeling Mode (Interactive Tools Framework).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (8)</div><div class="module-item"><span class="dot"></span><span class="name mono">MeshModelingTools</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MeshModelingToolsEditorOnly</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MeshModelingToolsetShaders</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ModelingComponents</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ModelingComponentsEditorOnly</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ModelingOperators</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ModelingOperatorsEditorOnly</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SkeletalMeshModifiers</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/MeshModelingToolset/MeshModelingToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
