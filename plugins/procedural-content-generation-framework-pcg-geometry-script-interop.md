---
layout: default
title: 程序内容生成框架 (PCG) 几何脚本互操作 / Procedural Content Generation Framework (PCG) Geometry Script Interop
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">P</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Procedural Content Generation Framework (PCG) Geometry Script Interop</div>
      <div class="hero-title-cn">程序内容生成框架 (PCG) 几何脚本互操作 · 用于与几何脚本交互的程序内容生成框架的额外插件。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Editor</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.2</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/PCGInterops/PCGGeometryScriptInterop/PCGGeometryScriptInterop.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于与几何脚本交互的程序内容生成框架的额外插件。</div><div class="lang-content">Extra plugin for Procedural Content Generation Framework interacting with Geometry Scripts.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>PCG 用节点图在编辑器或运行时程序化生成关卡内容：点云、变换、网格、植被与生成规则，可和景观、HLOD、Nanite 配合。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：PCGGeometryScriptInterop。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview</a></p></div><div class="lang-content"><p>PCG is a node graph for procedural level content in editor or at runtime: point clouds, transforms, meshes, foliage, and spawn rules, working with Landscape, HLOD, and Nanite.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: PCGGeometryScriptInterop. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-overview</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Procedural Content Generation Framework (PCG) Geometry Script Interop</code>（模块 <code class="usage-code">PCGGeometryScriptInterop</code>）。</li><li>它让 PCG 与 Geometry Script 交互。</li><li>在 PCG 图里调用几何脚本节点，对生成出的网格做程序化建模。</li><li>属实验性 PCG 互操作；需启用 PCG 与 Geometry Script。</li></ol><p class="usage-note">PCG 与 Geometry Script 的互操作。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Procedural Content Generation Framework (PCG) Geometry Script Interop</code> (module <code class="usage-code">PCGGeometryScriptInterop</code>).</li><li>It lets PCG interact with Geometry Script.</li><li>Call Geometry Script nodes from PCG graphs to procedurally model generated meshes.</li><li>It is experimental PCG interop; requires PCG and Geometry Script.</li></ol><p class="usage-note">PCG interop with Geometry Script.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">PCGGeometryScriptInterop</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/PCGInterops/PCGGeometryScriptInterop/PCGGeometryScriptInterop.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
