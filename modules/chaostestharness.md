---
layout: default
title: ChaosTestHarness
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>C</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">ChaosTestHarness</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">TestModuleRules</span></span>
        <span class="chip">5 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">TestModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">5</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Developer/ChaosTestHarness/ChaosTestHarness.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于 5 个其他模块：Catch2、Core、CoreUObject、Engine、LowLevelTestsRunner。</div><div class="lang-content">This module depends on 5 other module(s): Catch2, Core, CoreUObject, Engine, LowLevelTestsRunner.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Chaos 是引擎默认物理与破坏求解器（刚体、布料、破碎、字段）。相关插件把编辑器工具和运行时求解接到关卡里的几何体上。</p><p>这是开发者工具或独立程序模块，给 Insights、UBT、命令行用。</p><p>UBT 声明它还依赖：Catch2, Core, CoreUObject, Engine, LowLevelTestsRunner。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Chaos is the default physics and destruction solver (rigid body, cloth, fracture, fields). Related plugins connect editor tools and the runtime solver to level geometry.</p><p>This is a developer tool or program module for Insights, UBT, or command-line apps.</p><p>UBT also lists dependencies on: Catch2, Core, CoreUObject, Engine, LowLevelTestsRunner. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">ChaosTestHarness</code>（Chaos Test Harness）：它属于物理/Chaos（刚体、碰撞、破坏、车辆、布料、物理场）。位于 <code class="usage-code">Developer</code>，构建规则 <code class="usage-code">Developer/ChaosTestHarness/ChaosTestHarness.Build.cs</code>。直接依赖 5 个模块：<code class="usage-code">Catch2</code>、<code class="usage-code">Core</code>、<code class="usage-code">CoreUObject</code>、<code class="usage-code">Engine</code>、<code class="usage-code">LowLevelTestsRunner</code>。</li><li>部署：<code class="usage-code">ChaosTestHarness</code> 开发者/工具模块，供编辑器或命令行使用，不要当游戏运行时依赖。</li><li>怎么用：给网格开启物理/Chaos，放置字段或破坏资产；运行时由物理系统模拟，代码里查询碰撞与物理状态。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;ChaosTestHarness&quot; });</code>；对外暴露 <code class="usage-code">ChaosTestHarness</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：包含其 <code class="usage-code">Public/</code> 头文件以使用导出类型；模块由引擎/插件系统自动加载，通常无需手动 <code class="usage-code">LoadModulePtr</code>（仅懒加载时才用 <code class="usage-code">FModuleManager::LoadModuleChecked</code>）。</li></ol><p class="usage-note">`ChaosTestHarness`：它属于物理/Chaos（刚体、碰撞、破坏、车辆、布料、物理场）；构建规则 `Developer/ChaosTestHarness/ChaosTestHarness.Build.cs`，直接依赖 5 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">ChaosTestHarness</code> (Chaos Test Harness): it is part of physics/Chaos (rigid bodies, collisions, destruction, vehicles, cloth, fields). Located under <code class="usage-code">Developer</code>; build rule <code class="usage-code">Developer/ChaosTestHarness/ChaosTestHarness.Build.cs</code>. It directly depends on 5 modules: <code class="usage-code">Catch2</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">Engine</code>, <code class="usage-code">LowLevelTestsRunner</code>.</li><li>Placement: <code class="usage-code">ChaosTestHarness</code> is a developer/tool module for editor or CLI use; not a game runtime dependency.</li><li>How to use: enable physics/Chaos on meshes and place fields or destruction assets; the physics system simulates at runtime and you query collisions/state from code.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;ChaosTestHarness&quot; });</code>. Use Public when exposing <code class="usage-code">ChaosTestHarness</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: include its <code class="usage-code">Public/</code> headers to use exported types; the engine/plugin system loads the module automatically — no manual <code class="usage-code">LoadModulePtr</code> needed (use <code class="usage-code">FModuleManager::LoadModuleChecked</code> only for lazy loading).</li></ol><p class="usage-note">`ChaosTestHarness`: it is part of physics/Chaos (rigid bodies, collisions, destruction, vehicles, cloth, fields); build rule `Developer/ChaosTestHarness/ChaosTestHarness.Build.cs`; depends on 5 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (5)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">Catch2</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Engine</span></div><div class="module-item"><span class="dot"></span><span class="name mono">LowLevelTestsRunner</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Developer/ChaosTestHarness/ChaosTestHarness.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
