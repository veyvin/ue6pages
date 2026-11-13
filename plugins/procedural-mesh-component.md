---
layout: default
title: 程序网格组件 / Procedural Mesh Component
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">P</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Procedural Mesh Component</div>
      <div class="hero-title-cn">程序网格组件 · 用于按程序创建和修改网格几何体的可渲染组件和实用程序库。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Rendering</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/ProceduralMeshComponent/ProceduralMeshComponent.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于按程序创建和修改网格几何体的可渲染组件和实用程序库。</div><div class="lang-content">A renderable component and library of utilities for creating and modifying mesh geometry procedurally.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于按程序创建和修改网格几何体的可渲染组件和实用程序库。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：ProceduralMeshComponent, ProceduralMeshComponentEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A renderable component and library of utilities for creating and modifying mesh geometry procedurally.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: ProceduralMeshComponent, ProceduralMeshComponentEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Procedural Mesh Component</code>（运行时 <code class="usage-code">ProceduralMeshComponent</code>，编辑器 <code class="usage-code">ProceduralMeshComponentEditor</code>）。</li><li>它提供可渲染组件和工具库，用于按程序创建和修改网格几何。</li><li>在 Actor 上加 Procedural Mesh Component，运行时填顶点/三角形生成网格。</li><li>Game 模块依赖运行时模块；编辑器模块只进 Editor Target。更复杂建模可考虑 Geometry Script。</li></ol><p class="usage-note">运行时程序化创建/修改网格的可渲染组件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Procedural Mesh Component</code> (runtime <code class="usage-code">ProceduralMeshComponent</code>, editor <code class="usage-code">ProceduralMeshComponentEditor</code>).</li><li>It provides a renderable component and utility library for creating and modifying mesh geometry procedurally.</li><li>Add a Procedural Mesh Component on an actor and fill vertices/triangles at runtime.</li><li>Game modules depend on runtime modules; editor modules are Editor-target only. For heavier modeling, consider Geometry Script.</li></ol><p class="usage-note">Renderable component to create/modify meshes procedurally at runtime.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">ProceduralMeshComponent</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ProceduralMeshComponentEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/ProceduralMeshComponent/ProceduralMeshComponent.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
