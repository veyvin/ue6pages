---
layout: default
title: ChaosSolverEngine
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>C</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">ChaosSolverEngine</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">13 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">13</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Runtime/Experimental/ChaosSolverEngine/ChaosSolverEngine.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于其他 13 个模块：ChaosVDRuntime、Core、CoreUObject、DataflowCore、DataflowEngine、DataflowSimulation、DeveloperSettings、Engine、Messaging、RHI、RenderCore、RigidPhysics、TraceBasedDebuggers。</div><div class="lang-content">This module depends on 13 other module(s): ChaosVDRuntime, Core, CoreUObject, DataflowCore, DataflowEngine, DataflowSimulation, DeveloperSettings, Engine, Messaging, RHI, RenderCore, RigidPhysics, TraceBasedDebuggers.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Engine 模块是游戏框架核心：Actor、Pawn、PlayerController、World、组件、材质与关卡流送的运行时实现。绝大多数游戏模块都会直接或间接依赖它。</p><p>这是 Runtime 模块，随游戏一起发布，给运行时 C++ 用。</p><p>UBT 声明它还依赖：ChaosVDRuntime, Core, CoreUObject, DataflowCore, DataflowEngine, DataflowSimulation, DeveloperSettings, Engine。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>The Engine module is the gameplay-framework core: Actor, Pawn, PlayerController, World, components, materials, and streaming at runtime. Almost every game module depends on it, directly or not.</p><p>This is a Runtime module that ships with the game and is for runtime C++.</p><p>UBT also lists dependencies on: ChaosVDRuntime, Core, CoreUObject, DataflowCore, DataflowEngine, DataflowSimulation, DeveloperSettings, Engine. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">ChaosSolverEngine</code>（Chaos Solver Engine）：它属于物理/Chaos（刚体、碰撞、破坏、车辆、布料、物理场）。位于 <code class="usage-code">Runtime</code>，构建规则 <code class="usage-code">Runtime/Experimental/ChaosSolverEngine/ChaosSolverEngine.Build.cs</code>。直接依赖 8 个模块：<code class="usage-code">ChaosVDRuntime</code>、<code class="usage-code">Core</code>、<code class="usage-code">CoreUObject</code>、<code class="usage-code">DataflowCore</code>、<code class="usage-code">DataflowEngine</code> 等。</li><li>部署：<code class="usage-code">ChaosSolverEngine</code> 运行时模块，可进游戏包；只在真正调用其 API 的模块里声明依赖。</li><li>怎么用：给网格开启物理/Chaos，放置字段或破坏资产；运行时由物理系统模拟，代码里查询碰撞与物理状态。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;ChaosSolverEngine&quot; });</code>；对外暴露 <code class="usage-code">ChaosSolverEngine</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：包含其 <code class="usage-code">Public/</code> 头文件以使用导出类型；模块由引擎/插件系统自动加载，通常无需手动 <code class="usage-code">LoadModulePtr</code>（仅懒加载时才用 <code class="usage-code">FModuleManager::LoadModuleChecked</code>）。</li></ol><p class="usage-note">`ChaosSolverEngine`：它属于物理/Chaos（刚体、碰撞、破坏、车辆、布料、物理场）；构建规则 `Runtime/Experimental/ChaosSolverEngine/ChaosSolverEngine.Build.cs`，直接依赖 8 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">ChaosSolverEngine</code> (Chaos Solver Engine): it is part of physics/Chaos (rigid bodies, collisions, destruction, vehicles, cloth, fields). Located under <code class="usage-code">Runtime</code>; build rule <code class="usage-code">Runtime/Experimental/ChaosSolverEngine/ChaosSolverEngine.Build.cs</code>. It directly depends on 8 modules: <code class="usage-code">ChaosVDRuntime</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">DataflowCore</code>, <code class="usage-code">DataflowEngine</code> etc.</li><li>Placement: <code class="usage-code">ChaosSolverEngine</code> is a runtime module and can ship; depend on it only where you call its API.</li><li>How to use: enable physics/Chaos on meshes and place fields or destruction assets; the physics system simulates at runtime and you query collisions/state from code.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;ChaosSolverEngine&quot; });</code>. Use Public when exposing <code class="usage-code">ChaosSolverEngine</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: include its <code class="usage-code">Public/</code> headers to use exported types; the engine/plugin system loads the module automatically — no manual <code class="usage-code">LoadModulePtr</code> needed (use <code class="usage-code">FModuleManager::LoadModuleChecked</code> only for lazy loading).</li></ol><p class="usage-note">`ChaosSolverEngine`: it is part of physics/Chaos (rigid bodies, collisions, destruction, vehicles, cloth, fields); build rule `Runtime/Experimental/ChaosSolverEngine/ChaosSolverEngine.Build.cs`; depends on 8 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (13)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">ChaosVDRuntime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataflowCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataflowEngine</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataflowSimulation</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DeveloperSettings</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Engine</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Messaging</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RHI</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RenderCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RigidPhysics</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TraceBasedDebuggers</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Runtime/Experimental/ChaosSolverEngine/ChaosSolverEngine.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
