---
layout: default
title: ChaosVisualDebugger
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>C</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">ChaosVisualDebugger</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">27 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">27</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Programs/ChaosVisualDebugger/ChaosVisualDebugger.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于 27 个其他模块：AgilitySDK、ApplicationCore、ChaosVD、Core、CoreUObject、DerivedDataCache、EditorViewport、Engine、InputCore、InstallBundleManager、MediaUtils、Messaging、MoviePlayer、MoviePlayerProxy、PreLoadScreen、ProfileVisualizer、Projects、PropertyAccessEditor、PropertyEditor、RHI、RenderCore、Slate、SlateCore、ToolWidgets、TraceLog、 UnixCommonStartup、UnrealEd。</div><div class="lang-content">This module depends on 27 other module(s): AgilitySDK, ApplicationCore, ChaosVD, Core, CoreUObject, DerivedDataCache, EditorViewport, Engine, InputCore, InstallBundleManager, MediaUtils, Messaging, MoviePlayer, MoviePlayerProxy, PreLoadScreen, ProfileVisualizer, Projects, PropertyAccessEditor, PropertyEditor, RHI, RenderCore, Slate, SlateCore, ToolWidgets, TraceLog, UnixCommonStartup, UnrealEd.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Chaos 是引擎默认物理与破坏求解器（刚体、布料、破碎、字段）。相关插件把编辑器工具和运行时求解接到关卡里的几何体上。</p><p>这是开发者工具或独立程序模块，给 Insights、UBT、命令行用。</p><p>UBT 声明它还依赖：AgilitySDK, ApplicationCore, ChaosVD, Core, CoreUObject, DerivedDataCache, EditorViewport, Engine。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Chaos is the default physics and destruction solver (rigid body, cloth, fracture, fields). Related plugins connect editor tools and the runtime solver to level geometry.</p><p>This is a developer tool or program module for Insights, UBT, or command-line apps.</p><p>UBT also lists dependencies on: AgilitySDK, ApplicationCore, ChaosVD, Core, CoreUObject, DerivedDataCache, EditorViewport, Engine. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">ChaosVisualDebugger</code>（Chaos Visual Debugger）：它是构建/工具/独立程序（UBT、Horde、Insights、Automation、命令行 Program）。位于 <code class="usage-code">Programs</code>，构建规则 <code class="usage-code">Programs/ChaosVisualDebugger/ChaosVisualDebugger.Build.cs</code>。直接依赖 8 个模块：<code class="usage-code">AgilitySDK</code>、<code class="usage-code">ApplicationCore</code>、<code class="usage-code">ChaosVD</code>、<code class="usage-code">Core</code>、<code class="usage-code">CoreUObject</code> 等。</li><li>部署：<code class="usage-code">ChaosVisualDebugger</code> 独立程序(Programs)，给命令行/工具用，不进游戏运行时。</li><li>怎么用：作为独立程序或命令行工具运行，不进游戏运行时；用于构建、CI、性能分析等。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;ChaosVisualDebugger&quot; });</code>；对外暴露 <code class="usage-code">ChaosVisualDebugger</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：作为独立程序/命令运行，或在工具代码里 include 其 Public 头。</li></ol><p class="usage-note">`ChaosVisualDebugger`：它是构建/工具/独立程序（UBT、Horde、Insights、Automation、命令行 Program）；构建规则 `Programs/ChaosVisualDebugger/ChaosVisualDebugger.Build.cs`，直接依赖 8 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">ChaosVisualDebugger</code> (Chaos Visual Debugger): it is a build/tool/standalone Program (UBT, Horde, Insights, Automation, CLI). Located under <code class="usage-code">Programs</code>; build rule <code class="usage-code">Programs/ChaosVisualDebugger/ChaosVisualDebugger.Build.cs</code>. It directly depends on 8 modules: <code class="usage-code">AgilitySDK</code>, <code class="usage-code">ApplicationCore</code>, <code class="usage-code">ChaosVD</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code> etc.</li><li>Placement: <code class="usage-code">ChaosVisualDebugger</code> is a standalone Program; used by CLI/tools, not game runtime.</li><li>How to use: run it as a standalone program/CLI; it does not ship in the game — used for builds, CI, profiling.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;ChaosVisualDebugger&quot; });</code>. Use Public when exposing <code class="usage-code">ChaosVisualDebugger</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: run it as a standalone program/command, or include its Public headers from tool code.</li></ol><p class="usage-note">`ChaosVisualDebugger`: it is a build/tool/standalone Program (UBT, Horde, Insights, Automation, CLI); build rule `Programs/ChaosVisualDebugger/ChaosVisualDebugger.Build.cs`; depends on 8 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (27)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">AgilitySDK</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ApplicationCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ChaosVD</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DerivedDataCache</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditorViewport</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Engine</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InputCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InstallBundleManager</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MediaUtils</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Messaging</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MoviePlayer</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MoviePlayerProxy</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PreLoadScreen</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ProfileVisualizer</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Projects</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PropertyAccessEditor</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PropertyEditor</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RHI</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RenderCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Slate</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SlateCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ToolWidgets</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TraceLog</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnixCommonStartup</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealEd</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Programs/ChaosVisualDebugger/ChaosVisualDebugger.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
