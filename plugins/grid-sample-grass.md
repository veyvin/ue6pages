---
layout: default
title: 网格样本草 / Grid Sample Grass
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Grid Sample Grass</div>
      <div class="hero-title-cn">网格样本草 · 网格样本草地渲染技术：距离环中的程序叶片丛（完整、廉价和合并的丛</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Rendering</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/GridSampleGrass/GridSampleGrass.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">网格样本草地渲染技术：距离环中的程序叶片丛（完整、廉价和合并的丛，面向相机的冒名顶替卡），样条覆盖整形，排除和变形，在平面或景观地形上。</div><div class="lang-content">Grid sample grass rendering technique: procedural blade clumps in distance rings (full, cheap and merged clumps, camera-facing impostor cards), spline coverage shaping, exclusions and deformation, on flat planes or Landscape terrain.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：网格样本草地渲染技术：距离环中的程序叶片丛（完整、廉价和合并的丛，面向相机的冒名顶替卡），样条覆盖整形，排除和变形，在平面或景观地形上。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：GridSampleGrass。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Grid sample grass rendering technique: procedural blade clumps in distance rings (full, cheap and merged clumps, camera-facing impostor cards), spline coverage shaping, exclusions and deformation, on flat planes or Landscape terrain.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: GridSampleGrass. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Grid Sample Grass</code>（模块 <code class="usage-code">GridSampleGrass</code>）。</li><li>在草地表面配置网格样本草地渲染：距离环中的程序叶片丛（完整/廉价/合并丛、面向相机 impostor）。</li><li>用样条覆盖整形、排除与变形控制草地范围与形态，铺设到平面或景观地形。</li><li>这是渲染技术插件，关注性能与视觉；按项目渲染管线验证效果。</li></ol><p class="usage-note">网格样本草地渲染技术，程序叶片丛 + impostor，偏性能。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Grid Sample Grass</code> (module <code class="usage-code">GridSampleGrass</code>).</li><li>Configure grid-sample grass on surfaces: procedural blade clumps in distance rings (full/cheap/merged clumps, camera-facing impostors).</li><li>Use spline coverage shaping, exclusions, and deformation to control grass extent and form on flat or landscape terrain.</li><li>It is a rendering technique plugin; verify visuals and performance against your project&#x27;s render pipeline.</li></ol><p class="usage-note">A grid-sample grass rendering technique (procedural clumps + impostors), performance-focused.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">GridSampleGrass</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/GridSampleGrass/GridSampleGrass.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
