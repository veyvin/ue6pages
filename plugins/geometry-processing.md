---
layout: default
title: 几何处理 / Geometry Processing
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Geometry Processing</div>
      <div class="hero-title-cn">几何处理 · 用于处理 2D 和 3D 几何的数据结构和算法</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Geometry</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/GeometryProcessing/GeometryProcessing.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于处理 2D 和 3D 几何的数据结构和算法</div><div class="lang-content">Data Structures and Algorithms for Processing 2D and 3D Geometry</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于处理 2D 和 3D 几何的数据结构和算法</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：GeometryAlgorithms, DynamicMesh, MeshFileUtils。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Data Structures and Algorithms for Processing 2D and 3D Geometry</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: GeometryAlgorithms, DynamicMesh, MeshFileUtils. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Geometry Processing</code>（模块 <code class="usage-code">GeometryAlgorithms</code>、<code class="usage-code">DynamicMesh</code>、<code class="usage-code">MeshFileUtils</code>）。</li><li>在 C++/蓝图里用 <code class="usage-code">DynamicMesh</code> 与 <code class="usage-code">GeometryAlgorithms</code> 对网格做切割、布尔、简化、法线等处理。</li><li>用 <code class="usage-code">MeshFileUtils</code> 做网格文件的读写/转换，把处理结果落成资产。</li><li>这是运行时几何算法库，Game 模块依赖对应模块即可。</li></ol><p class="usage-note">处理 2D/3D 几何的数据结构与算法底座，DynamicMesh 与 Geometry Script 都建立在其上。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Geometry Processing</code> (modules <code class="usage-code">GeometryAlgorithms</code>, <code class="usage-code">DynamicMesh</code>, <code class="usage-code">MeshFileUtils</code>).</li><li>In C++/Blueprint use <code class="usage-code">DynamicMesh</code> and <code class="usage-code">GeometryAlgorithms</code> to cut, boolean, simplify, and recompute normals on meshes.</li><li>Use <code class="usage-code">MeshFileUtils</code> to read/write and convert mesh files, saving results as assets.</li><li>It is a runtime geometry algorithm library; game modules depend on the relevant submodules.</li></ol><p class="usage-note">The data-structure/algorithm base for 2D/3D geometry; DynamicMesh and Geometry Script build on it.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">GeometryAlgorithms</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DynamicMesh</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MeshFileUtils</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/GeometryProcessing/GeometryProcessing.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
