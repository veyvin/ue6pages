---
layout: default
title: 电缆组件 / Cable Component
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cable Component</div>
      <div class="hero-title-cn">电缆组件 · 模拟电缆组件。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Rendering</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/CableComponent/CableComponent.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">模拟电缆组件。</div><div class="lang-content">A simulated cable component.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：模拟电缆组件。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：CableComponent。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A simulated cable component.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: CableComponent. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 <code class="usage-code">Edit &gt; Plugins</code> 启用 <code class="usage-code">Cable Component</code>（模块 <code class="usage-code">CableComponent</code>）并重启。</li><li>从放置 Actor 面板拖 <code class="usage-code">Cable Actor</code>（<code class="usage-code">ACableActor</code>），或给已有 Actor 添加 <code class="usage-code">UCableComponent</code>。</li><li>起点默认绑在组件变换上（<code class="usage-code">Attach Start</code>）。在 Details 的 Cable 里指定 <code class="usage-code">Attach End To</code> 目标 Actor/组件，可选 <code class="usage-code">Attach End To Socket Name</code>，并用 <code class="usage-code">End Location</code> 微调。</li><li>关掉 <code class="usage-code">Attach End</code> 可让末端自由摆动；保持两端附着则变成固定悬索。用 <code class="usage-code">Set Attach End To</code> / <code class="usage-code">Set Attach End To Component</code> 可在运行时改挂点。</li><li>调节 <code class="usage-code">Cable Length</code>、<code class="usage-code">Num Segments</code>、<code class="usage-code">Solver Iterations</code>、<code class="usage-code">Cable Gravity Scale</code>、<code class="usage-code">Enable Stiffness</code>；碰撞用实验性 <code class="usage-code">Enable Collision</code>（成本高）。</li><li>渲染：<code class="usage-code">Cable Width</code>、<code class="usage-code">Num Sides</code>、<code class="usage-code">Tile Material</code>，给组件指定一条沿 U 方向平铺的材质。</li><li>C++：<code class="usage-code">PublicDependencyModuleNames</code> 加 <code class="usage-code">CableComponent</code>，<code class="usage-code">#include &quot;CableComponent.h&quot;</code>；<code class="usage-code">Num Segments</code> 是 <code class="usage-code">BlueprintReadOnly</code>，分段数在编辑器或构造时设好。</li></ol><p class="usage-note">运行时可进包装。`Get Cable Particle Locations` 可取世界空间粒子点；不要在运行时改 `Num Segments`。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Cable Component</code> in <code class="usage-code">Edit &gt; Plugins</code> (module <code class="usage-code">CableComponent</code>) and restart.</li><li>Place a <code class="usage-code">Cable Actor</code> (<code class="usage-code">ACableActor</code>) or add <code class="usage-code">UCableComponent</code> to an existing Actor.</li><li>Start is the component transform (<code class="usage-code">Attach Start</code>). In Details &gt; Cable set <code class="usage-code">Attach End To</code> (Actor/component), optional <code class="usage-code">Attach End To Socket Name</code>, and <code class="usage-code">End Location</code>.</li><li>Clear <code class="usage-code">Attach End</code> to let the tip swing; keep both ends attached for a catenary. At runtime use <code class="usage-code">Set Attach End To</code> / <code class="usage-code">Set Attach End To Component</code>.</li><li>Tune <code class="usage-code">Cable Length</code>, <code class="usage-code">Num Segments</code>, <code class="usage-code">Solver Iterations</code>, <code class="usage-code">Cable Gravity Scale</code>, <code class="usage-code">Enable Stiffness</code>. <code class="usage-code">Enable Collision</code> is experimental and expensive.</li><li>Render with <code class="usage-code">Cable Width</code>, <code class="usage-code">Num Sides</code>, <code class="usage-code">Tile Material</code>, and a material that tiles along U.</li><li>C++: add <code class="usage-code">CableComponent</code> to <code class="usage-code">PublicDependencyModuleNames</code>, <code class="usage-code">#include &quot;CableComponent.h&quot;</code>. <code class="usage-code">Num Segments</code> is <code class="usage-code">BlueprintReadOnly</code> — set it in the editor or at construction.</li></ol><p class="usage-note">Ships at runtime. `Get Cable Particle Locations` returns world-space particles. Do not change `Num Segments` at runtime.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CableComponent</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/CableComponent/CableComponent.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
