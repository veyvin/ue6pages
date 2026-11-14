---
layout: default
title: RenderCore
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>R</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">RenderCore</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">14 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">14</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Runtime/RenderCore/RenderCore.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于 14 个其他模块：ApplicationCore、BuildSettings、Core、CoreUObject、DerivedDataCache、FileUtilities、ImageWrapper、Json、OodleDataCompression、Projects、RHI、ShaderRuntime、StateStream、TraceLog。</div><div class="lang-content">This module depends on 14 other module(s): ApplicationCore, BuildSettings, Core, CoreUObject, DerivedDataCache, FileUtilities, ImageWrapper, Json, OodleDataCompression, Projects, RHI, ShaderRuntime, StateStream, TraceLog.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Core 是最底层运行时：容器、字符串、模块加载、日志、委托、平台抽象。不依赖 Engine；所有其他模块最终都建立在它上面。</p><p>这是 Runtime 模块，随游戏一起发布，给运行时 C++ 用。</p><p>UBT 声明它还依赖：ApplicationCore, BuildSettings, Core, CoreUObject, DerivedDataCache, FileUtilities, ImageWrapper, Json。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Core is the lowest runtime layer: containers, strings, module loading, logging, delegates, and platform abstraction. It does not depend on Engine; everything else sits on it.</p><p>This is a Runtime module that ships with the game and is for runtime C++.</p><p>UBT also lists dependencies on: ApplicationCore, BuildSettings, Core, CoreUObject, DerivedDataCache, FileUtilities, ImageWrapper, Json. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">RenderCore</code>（Render Core）：它属于渲染/RHI 层（图形后端、着色器、渲染管线、纹理/后处理）。位于 <code class="usage-code">Runtime</code>，构建规则 <code class="usage-code">Runtime/RenderCore/RenderCore.Build.cs</code>。直接依赖 8 个模块：<code class="usage-code">ApplicationCore</code>、<code class="usage-code">BuildSettings</code>、<code class="usage-code">Core</code>、<code class="usage-code">CoreUObject</code>、<code class="usage-code">DerivedDataCache</code> 等。</li><li>部署：<code class="usage-code">RenderCore</code> 运行时模块，可进游戏包；只在真正调用其 API 的模块里声明依赖。</li><li>怎么用：在渲染线程/材质/后处理相关代码里使用；不要从游戏线程直接改 RHI 资源，需遵守渲染线程约束。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;RenderCore&quot; });</code>；对外暴露 <code class="usage-code">RenderCore</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：包含其 <code class="usage-code">Public/</code> 头文件以使用导出类型；模块由引擎/插件系统自动加载，通常无需手动 <code class="usage-code">LoadModulePtr</code>（仅懒加载时才用 <code class="usage-code">FModuleManager::LoadModuleChecked</code>）。</li></ol><p class="usage-note">`RenderCore`：它属于渲染/RHI 层（图形后端、着色器、渲染管线、纹理/后处理）；构建规则 `Runtime/RenderCore/RenderCore.Build.cs`，直接依赖 8 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">RenderCore</code> (Render Core): it is part of the rendering/RHI layer (graphics backend, shaders, pipeline, textures/post-process). Located under <code class="usage-code">Runtime</code>; build rule <code class="usage-code">Runtime/RenderCore/RenderCore.Build.cs</code>. It directly depends on 8 modules: <code class="usage-code">ApplicationCore</code>, <code class="usage-code">BuildSettings</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">DerivedDataCache</code> etc.</li><li>Placement: <code class="usage-code">RenderCore</code> is a runtime module and can ship; depend on it only where you call its API.</li><li>How to use: use it from render-thread/material/post-process code; never mutate RHI resources from the game thread — respect render-thread rules.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;RenderCore&quot; });</code>. Use Public when exposing <code class="usage-code">RenderCore</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: include its <code class="usage-code">Public/</code> headers to use exported types; the engine/plugin system loads the module automatically — no manual <code class="usage-code">LoadModulePtr</code> needed (use <code class="usage-code">FModuleManager::LoadModuleChecked</code> only for lazy loading).</li></ol><p class="usage-note">`RenderCore`: it is part of the rendering/RHI layer (graphics backend, shaders, pipeline, textures/post-process); build rule `Runtime/RenderCore/RenderCore.Build.cs`; depends on 8 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (14)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">ApplicationCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">BuildSettings</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DerivedDataCache</span></div><div class="module-item"><span class="dot"></span><span class="name mono">FileUtilities</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ImageWrapper</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Json</span></div><div class="module-item"><span class="dot"></span><span class="name mono">OodleDataCompression</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Projects</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RHI</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ShaderRuntime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">StateStream</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TraceLog</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Runtime/RenderCore/RenderCore.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
