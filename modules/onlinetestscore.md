---
layout: default
title: OnlineTestsCore
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>O</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">OnlineTestsCore</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">15 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">15</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Programs/Online/OnlineTestsCore/Source/OnlineTestsCore.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于 15 个其他模块：ApplicationCore、Core、CoreUObject、EOSSDK、EOSShared、EngineSettings、HTTP、Json、JsonUtilities、OnlineServicesCommon、OnlineServicesInterface、OnlineServicesOSSAdapter、OnlineSubsystem、Projects、SSL。</div><div class="lang-content">This module depends on 15 other module(s): ApplicationCore, Core, CoreUObject, EOSSDK, EOSShared, EngineSettings, HTTP, Json, JsonUtilities, OnlineServicesCommon, OnlineServicesInterface, OnlineServicesOSSAdapter, OnlineSubsystem, Projects, SSL.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Core 是最底层运行时：容器、字符串、模块加载、日志、委托、平台抽象。不依赖 Engine；所有其他模块最终都建立在它上面。</p><p>这是开发者工具或独立程序模块，给 Insights、UBT、命令行用。</p><p>UBT 声明它还依赖：ApplicationCore, Core, CoreUObject, EOSSDK, EOSShared, EngineSettings, HTTP, Json。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Core is the lowest runtime layer: containers, strings, module loading, logging, delegates, and platform abstraction. It does not depend on Engine; everything else sits on it.</p><p>This is a developer tool or program module for Insights, UBT, or command-line apps.</p><p>UBT also lists dependencies on: ApplicationCore, Core, CoreUObject, EOSSDK, EOSShared, EngineSettings, HTTP, Json. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>用途：<code class="usage-code">OnlineTestsCore</code> 位于 <code class="usage-code">Programs</code>，构建规则 <code class="usage-code">Programs/Online/OnlineTestsCore/Source/OnlineTestsCore.Build.cs</code>。它直接依赖 8 个模块：<code class="usage-code">ApplicationCore</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">EOSSDK</code>, <code class="usage-code">EOSShared</code>, <code class="usage-code">EngineSettings</code>, <code class="usage-code">HTTP</code>, <code class="usage-code">Json</code>。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;OnlineTestsCore&quot; });</code>；对外暴露 <code class="usage-code">OnlineTestsCore</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>部署：<code class="usage-code">OnlineTestsCore</code> 属于独立程序(Programs)，给命令行/工具用，不进游戏运行时。</li><li>调用：#include 其 Public 头（常见 <code class="usage-code">OnlineTestsCore.h</code> / <code class="usage-code">OnlineTestsCoreModule.h</code>），再用 <code class="usage-code">FModuleManager::LoadModulePtr&lt;OnlineTestsCoreModule&gt;</code> 或直接使用导出类型。</li><li>传递依赖：<code class="usage-code">OnlineTestsCore</code> 还依赖 <code class="usage-code">ApplicationCore</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">EOSSDK</code>, <code class="usage-code">EOSShared</code>, <code class="usage-code">EngineSettings</code>, <code class="usage-code">HTTP</code>, <code class="usage-code">Json</code>；不必在游戏模块重复填写，除非你要直接 include 那些头文件。</li></ol><p class="usage-note">`OnlineTestsCore` 的构建规则位于 `Programs/Online/OnlineTestsCore/Source/OnlineTestsCore.Build.cs`，直接依赖 8 个模块，分类 Module。</p></div><div class="lang-content"><ol class="usage-steps"><li>Purpose: <code class="usage-code">OnlineTestsCore</code> lives under <code class="usage-code">Programs</code>; build rule <code class="usage-code">Programs/Online/OnlineTestsCore/Source/OnlineTestsCore.Build.cs</code>.It directly depends on 8 modules: <code class="usage-code">ApplicationCore</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">EOSSDK</code>, <code class="usage-code">EOSShared</code>, <code class="usage-code">EngineSettings</code>, <code class="usage-code">HTTP</code>, <code class="usage-code">Json</code>.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;OnlineTestsCore&quot; });</code>. Use Public when exposing <code class="usage-code">OnlineTestsCore</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Placement: <code class="usage-code">OnlineTestsCore</code> belongs to a standalone Program; used by CLI/tools, not game runtime.</li><li>Call: include Public headers (often <code class="usage-code">OnlineTestsCore.h</code> / <code class="usage-code">OnlineTestsCoreModule.h</code>), then use <code class="usage-code">FModuleManager::LoadModulePtr&lt;OnlineTestsCoreModule&gt;</code> or the exported types directly.</li><li>Transitive deps: <code class="usage-code">OnlineTestsCore</code> also needs <code class="usage-code">ApplicationCore</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">EOSSDK</code>, <code class="usage-code">EOSShared</code>, <code class="usage-code">EngineSettings</code>, <code class="usage-code">HTTP</code>, <code class="usage-code">Json</code>; do not re-list them unless you include their headers.</li></ol><p class="usage-note">`OnlineTestsCore` build rule is `Programs/Online/OnlineTestsCore/Source/OnlineTestsCore.Build.cs`; depends on 8 modules; category Module.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (15)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">ApplicationCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EOSSDK</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EOSShared</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EngineSettings</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HTTP</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Json</span></div><div class="module-item"><span class="dot"></span><span class="name mono">JsonUtilities</span></div><div class="module-item"><span class="dot"></span><span class="name mono">OnlineServicesCommon</span></div><div class="module-item"><span class="dot"></span><span class="name mono">OnlineServicesInterface</span></div><div class="module-item"><span class="dot"></span><span class="name mono">OnlineServicesOSSAdapter</span></div><div class="module-item"><span class="dot"></span><span class="name mono">OnlineSubsystem</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Projects</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SSL</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Programs/Online/OnlineTestsCore/Source/OnlineTestsCore.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
