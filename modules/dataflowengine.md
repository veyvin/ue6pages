---
layout: default
title: DataflowEngine
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>D</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">DataflowEngine</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">8 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">8</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Runtime/Dataflow/Engine/DataflowEngine.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于其他 8 个模块：Chaos、Core、CoreUObject、DataflowCore、Engine、GeometryCore、ImageCore、SlateCore。</div><div class="lang-content">This module depends on 8 other module(s): Chaos, Core, CoreUObject, DataflowCore, Engine, GeometryCore, ImageCore, SlateCore.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Engine 模块是游戏框架核心：Actor、Pawn、PlayerController、World、组件、材质与关卡流送的运行时实现。绝大多数游戏模块都会直接或间接依赖它。</p><p>这是 Runtime 模块，随游戏一起发布，给运行时 C++ 用。</p><p>UBT 声明它还依赖：Chaos, Core, CoreUObject, DataflowCore, Engine, GeometryCore, ImageCore, SlateCore。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>The Engine module is the gameplay-framework core: Actor, Pawn, PlayerController, World, components, materials, and streaming at runtime. Almost every game module depends on it, directly or not.</p><p>This is a Runtime module that ships with the game and is for runtime C++.</p><p>UBT also lists dependencies on: Chaos, Core, CoreUObject, DataflowCore, Engine, GeometryCore, ImageCore, SlateCore. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">DataflowEngine</code>（Dataflow Engine）：它属于资产管线（导入/交换、Datasmith/USD、DDC、Cook、Pak、资产注册）。位于 <code class="usage-code">Runtime</code>，构建规则 <code class="usage-code">Runtime/Dataflow/Engine/DataflowEngine.Build.cs</code>。直接依赖 8 个模块：<code class="usage-code">Chaos</code>、<code class="usage-code">Core</code>、<code class="usage-code">CoreUObject</code>、<code class="usage-code">DataflowCore</code>、<code class="usage-code">Engine</code> 等。</li><li>部署：<code class="usage-code">DataflowEngine</code> 运行时模块，可进游戏包；只在真正调用其 API 的模块里声明依赖。</li><li>怎么用：通过内容浏览器导入或 Datasmith/USD 菜单走此管线；Cook/打包会自动参与，注意单位、材质、碰撞。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;DataflowEngine&quot; });</code>；对外暴露 <code class="usage-code">DataflowEngine</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：包含其 <code class="usage-code">Public/</code> 头文件以使用导出类型；模块由引擎/插件系统自动加载，通常无需手动 <code class="usage-code">LoadModulePtr</code>（仅懒加载时才用 <code class="usage-code">FModuleManager::LoadModuleChecked</code>）。</li></ol><p class="usage-note">`DataflowEngine`：它属于资产管线（导入/交换、Datasmith/USD、DDC、Cook、Pak、资产注册）；构建规则 `Runtime/Dataflow/Engine/DataflowEngine.Build.cs`，直接依赖 8 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">DataflowEngine</code> (Dataflow Engine): it is part of the asset pipeline (import/interchange, Datasmith/USD, DDC, Cook, Pak, asset registry). Located under <code class="usage-code">Runtime</code>; build rule <code class="usage-code">Runtime/Dataflow/Engine/DataflowEngine.Build.cs</code>. It directly depends on 8 modules: <code class="usage-code">Chaos</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">DataflowCore</code>, <code class="usage-code">Engine</code> etc.</li><li>Placement: <code class="usage-code">DataflowEngine</code> is a runtime module and can ship; depend on it only where you call its API.</li><li>How to use: import via Content Browser or Datasmith/USD menus; Cook/packaging uses it automatically — watch units, materials, collision.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;DataflowEngine&quot; });</code>. Use Public when exposing <code class="usage-code">DataflowEngine</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: include its <code class="usage-code">Public/</code> headers to use exported types; the engine/plugin system loads the module automatically — no manual <code class="usage-code">LoadModulePtr</code> needed (use <code class="usage-code">FModuleManager::LoadModuleChecked</code> only for lazy loading).</li></ol><p class="usage-note">`DataflowEngine`: it is part of the asset pipeline (import/interchange, Datasmith/USD, DDC, Cook, Pak, asset registry); build rule `Runtime/Dataflow/Engine/DataflowEngine.Build.cs`; depends on 8 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (8)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">Chaos</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DataflowCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Engine</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GeometryCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ImageCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SlateCore</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Runtime/Dataflow/Engine/DataflowEngine.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
