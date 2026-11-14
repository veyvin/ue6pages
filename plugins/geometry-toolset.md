---
layout: default
title: 几何工具集 / Geometry Toolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Geometry Toolset</div>
      <div class="hero-title-cn">几何工具集 · 使 AI 助手能够创作程序几何体 - 生成 DynamicMes</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/GeometryToolset/GeometryToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使 AI 助手能够创作程序几何体 - 生成 DynamicMesh actor，附加原始形状（长方体、圆柱体、圆锥体、球体、胶囊体、圆环面），并通过布尔运算（并集、减法、相交）组合它们。设计为基础级工具集，其他工具集（BlockoutToolset、未来的车辆/植被工具集）可以与之组合。仅限编辑。</div><div class="lang-content">Gives AI assistants the ability to author procedural geometry — spawn DynamicMesh actors, append primitive shapes (boxes, cylinders, cones, spheres, capsules, tori), and compose them with boolean operations (union, subtract, intersect). Designed as a substrate-level toolset that other toolsets (BlockoutToolset, future Vehicle/Vegetation toolsets) can compose with. Editor-only.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使 AI 助手能够创作程序几何体 - 生成 DynamicMesh actor，附加原始形状（长方体、圆柱体、圆锥体、球体、胶囊体、圆环面），并通过布尔运算（并集、减法、相交）组合它们。设计为基础级工具集，其他工具集（BlockoutToolset、未来的车辆/植被工具集）可以与之组合。仅限编辑。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：GeometryToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Gives AI assistants the ability to author procedural geometry — spawn DynamicMesh actors, append primitive shapes (boxes, cylinders, cones, spheres, capsules, tori), and compose them with boolean operations (union, subtract, intersect). Designed as a substrate-level toolset that other toolsets (BlockoutToolset, future Vehicle/Vegetation toolsets) can compose with. Editor-only.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: GeometryToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Geometry Toolset</code>（模块 <code class="usage-code">GeometryToolset</code>），它面向 AI Toolset Registry，仅限编辑。</li><li>让 AI 助手生成 DynamicMesh Actor、附加原始形体（盒/柱/锥/球/胶囊/环），并用布尔运算组合。</li><li>它设计为基础工具集，可与 BlockoutToolset 等其它工具集组合使用。</li><li>仅限编辑器，不要打包进游戏；Experimental，接口可能变动。</li></ol><p class="usage-note">给 AI 助手用的程序化几何工具集，仅限编辑。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Geometry Toolset</code> (module <code class="usage-code">GeometryToolset</code>); it targets the AI Toolset Registry and is editor-only.</li><li>Let AI assistants spawn DynamicMesh actors, append primitive shapes (box/cylinder/cone/sphere/capsule/torus), and combine them with booleans.</li><li>It is designed as a base toolset that composes with others like BlockoutToolset.</li><li>Editor-only, never ship it; Experimental with a contract that may change.</li></ol><p class="usage-note">A procedural geometry toolset for AI assistants, editor-only.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">GeometryToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/GeometryToolset/GeometryToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
