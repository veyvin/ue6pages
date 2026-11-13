---
layout: default
title: Launch
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>L</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">Launch</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">50 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">50</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Runtime/Launch/Launch.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于 50 个其他模块：AgilitySDK、ApplicationCore、AudioMixerAndroid、AutomationWorker、BuildSettings、ClothingSystemRuntimeInterface、ClothingSystemRuntimeNv、CookOnTheFly、Core、CoreUObject、DerivedDataCache、DesktopPlatform、DeveloperToolSettings、EditorFramework、Engine、FunctionalTesting、HeadMountedDisplay、InputCore、InstallBundleManager、Json、LauncherCheck、MRMEsh、 MainFrame、MaterialShaderQualitySettings、MediaUtils、MoviePlayer、MoviePlayerProxy、NetworkFile、网络、OpenGLDrv、Overlay、PakFile、PreLoadScreen、项目、RHI、RenderCore、SandboxFile、序列化、SessionServices、设置、Slate、SlateCore、套接字、SourceControl、StorageServerClient、StorageServerClientDebug、StreamingFile、TraceLog、UnixCommonStartup、UnrealEd。</div><div class="lang-content">This module depends on 50 other module(s): AgilitySDK, ApplicationCore, AudioMixerAndroid, AutomationWorker, BuildSettings, ClothingSystemRuntimeInterface, ClothingSystemRuntimeNv, CookOnTheFly, Core, CoreUObject, DerivedDataCache, DesktopPlatform, DeveloperToolSettings, EditorFramework, Engine, FunctionalTesting, HeadMountedDisplay, InputCore, InstallBundleManager, Json, LauncherCheck, MRMesh, MainFrame, MaterialShaderQualitySettings, MediaUtils, MoviePlayer, MoviePlayerProxy, NetworkFile, Networking, OpenGLDrv, Overlay, PakFile, PreLoadScreen, Projects, RHI, RenderCore, SandboxFile, Serialization, SessionServices, Settings, Slate, SlateCore, Sockets, SourceControl, StorageServerClient, StorageServerClientDebug, StreamingFile, TraceLog, UnixCommonStartup, UnrealEd.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：该模块依赖于 50 个其他模块：AgilitySDK、ApplicationCore、AudioMixerAndroid、AutomationWorker、BuildSettings、ClothingSystemRuntimeInterface、ClothingSystemRuntimeNv、CookOnTheFly、Core、CoreUObject、DerivedDataCache、DesktopPlatform、DeveloperToolSettings、EditorFramework、Engine、FunctionalTesting、HeadMountedDisplay、InputCore、InstallBundleManager、Json、LauncherCheck、MRMEsh、 MainFrame、MaterialShaderQualitySettings、MediaUtils、MoviePlayer、MoviePlayerProxy、NetworkFile、网络、OpenGLDrv、Overlay、PakFile、PreLoadScreen、项目、RHI、RenderCore、SandboxFile、序列化、SessionServices、设置、Slate、SlateCore、套接字、SourceControl、StorageServerClient、StorageServerClientDebug、StreamingFile、TraceLog、UnixCommonStartup、UnrealEd。</p><p>Insights/Trace 家族：采集或可视化一类性能数据（CPU、渲染、IO、网络），在 Unreal Insights 里看。</p><p>这是 Runtime 模块，随游戏一起发布，给运行时 C++ 用。</p><p>UBT 声明它还依赖：AgilitySDK, ApplicationCore, AudioMixerAndroid, AutomationWorker, BuildSettings, ClothingSystemRuntimeInterface, ClothingSystemRuntimeNv, CookOnTheFly。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: This module depends on 50 other module(s): AgilitySDK, ApplicationCore, AudioMixerAndroid, AutomationWorker, BuildSettings, ClothingSystemRuntimeInterface, ClothingSystemRuntimeNv, CookOnTheFly, Core, CoreUObject, DerivedDataCache, DesktopPlatform, DeveloperToolSettings, EditorFramework, Engine, FunctionalTesting, HeadMountedDisplay, InputCore, InstallBundleManager, Json, LauncherCheck, MRMesh, MainFrame, MaterialShaderQualitySettings, MediaUtils, MoviePlayer, MoviePlayerProxy, NetworkFile, Networking, OpenGLDrv, Overlay, PakFile, PreLoadScreen, Projects, RHI, RenderCore, SandboxFile, Serialization, SessionServices, Settings, Slate, SlateCore, Sockets, SourceControl, StorageServerClient, StorageServerClientDebug, StreamingFile, TraceLog, UnixCommonStartup, UnrealEd.</p><p>Insights/Trace family: records or visualizes a class of perf data (CPU, GPU, IO, net) in Unreal Insights.</p><p>This is a Runtime module that ships with the game and is for runtime C++.</p><p>UBT also lists dependencies on: AgilitySDK, ApplicationCore, AudioMixerAndroid, AutomationWorker, BuildSettings, ClothingSystemRuntimeInterface, ClothingSystemRuntimeNv, CookOnTheFly. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Launch</code>：它属于核心基础设施（容器、日志、内存、平台抽象、模块加载、构建元数据）。位于 <code class="usage-code">Runtime</code>，构建规则 <code class="usage-code">Runtime/Launch/Launch.Build.cs</code>。直接依赖 8 个模块：<code class="usage-code">AgilitySDK</code>、<code class="usage-code">ApplicationCore</code>、<code class="usage-code">AudioMixerAndroid</code>、<code class="usage-code">AutomationWorker</code>、<code class="usage-code">BuildSettings</code> 等。</li><li>部署：<code class="usage-code">Launch</code> 运行时模块，可进游戏包；只在真正调用其 API 的模块里声明依赖。</li><li>怎么用：几乎被所有模块间接依赖；一般无需显式添加，除非你在写底层插件或工具。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;Launch&quot; });</code>；对外暴露 <code class="usage-code">Launch</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：包含其 <code class="usage-code">Public/</code> 头文件以使用导出类型；模块由引擎/插件系统自动加载，通常无需手动 <code class="usage-code">LoadModulePtr</code>（仅懒加载时才用 <code class="usage-code">FModuleManager::LoadModuleChecked</code>）。</li></ol><p class="usage-note">`Launch`：它属于核心基础设施（容器、日志、内存、平台抽象、模块加载、构建元数据）；构建规则 `Runtime/Launch/Launch.Build.cs`，直接依赖 8 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Launch</code>: it is core infrastructure (containers, logging, memory, platform abstraction, module loading, build metadata). Located under <code class="usage-code">Runtime</code>; build rule <code class="usage-code">Runtime/Launch/Launch.Build.cs</code>. It directly depends on 8 modules: <code class="usage-code">AgilitySDK</code>, <code class="usage-code">ApplicationCore</code>, <code class="usage-code">AudioMixerAndroid</code>, <code class="usage-code">AutomationWorker</code>, <code class="usage-code">BuildSettings</code> etc.</li><li>Placement: <code class="usage-code">Launch</code> is a runtime module and can ship; depend on it only where you call its API.</li><li>How to use: almost every module depends on it transitively; you rarely add it explicitly unless writing low-level plugins/tools.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;Launch&quot; });</code>. Use Public when exposing <code class="usage-code">Launch</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: include its <code class="usage-code">Public/</code> headers to use exported types; the engine/plugin system loads the module automatically — no manual <code class="usage-code">LoadModulePtr</code> needed (use <code class="usage-code">FModuleManager::LoadModuleChecked</code> only for lazy loading).</li></ol><p class="usage-note">`Launch`: it is core infrastructure (containers, logging, memory, platform abstraction, module loading, build metadata); build rule `Runtime/Launch/Launch.Build.cs`; depends on 8 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (50)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">AgilitySDK</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ApplicationCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AudioMixerAndroid</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AutomationWorker</span></div><div class="module-item"><span class="dot"></span><span class="name mono">BuildSettings</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ClothingSystemRuntimeInterface</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ClothingSystemRuntimeNv</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CookOnTheFly</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DerivedDataCache</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DesktopPlatform</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DeveloperToolSettings</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditorFramework</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Engine</span></div><div class="module-item"><span class="dot"></span><span class="name mono">FunctionalTesting</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HeadMountedDisplay</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InputCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InstallBundleManager</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Json</span></div><div class="module-item"><span class="dot"></span><span class="name mono">LauncherCheck</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MRMesh</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MainFrame</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MaterialShaderQualitySettings</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MediaUtils</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MoviePlayer</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MoviePlayerProxy</span></div><div class="module-item"><span class="dot"></span><span class="name mono">NetworkFile</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Networking</span></div><div class="module-item"><span class="dot"></span><span class="name mono">OpenGLDrv</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Overlay</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PakFile</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PreLoadScreen</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Projects</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RHI</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RenderCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SandboxFile</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Serialization</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SessionServices</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Settings</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Slate</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SlateCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Sockets</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SourceControl</span></div><div class="module-item"><span class="dot"></span><span class="name mono">StorageServerClient</span></div><div class="module-item"><span class="dot"></span><span class="name mono">StorageServerClientDebug</span></div><div class="module-item"><span class="dot"></span><span class="name mono">StreamingFile</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TraceLog</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnixCommonStartup</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealEd</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Runtime/Launch/Launch.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
