---
layout: default
title: WebTests
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>W</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">WebTests</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">TestModuleRules</span></span>
        <span class="chip">10 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">TestModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">10</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Programs/WebTests/WebTests.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于其他 10 个模块：ApplicationCore、Core、EventLoop、HTTP、HTTPServer、Json、SSL、Sockets、WebSockets、XMPP。</div><div class="lang-content">This module depends on 10 other module(s): ApplicationCore, Core, EventLoop, HTTP, HTTPServer, Json, SSL, Sockets, WebSockets, XMPP.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：该模块依赖于其他 10 个模块：ApplicationCore、Core、EventLoop、HTTP、HTTPServer、Json、SSL、Sockets、WebSockets、XMPP。</p><p>这是开发者工具或独立程序模块，给 Insights、UBT、命令行用。</p><p>UBT 声明它还依赖：ApplicationCore, Core, EventLoop, HTTP, HTTPServer, Json, SSL, Sockets。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: This module depends on 10 other module(s): ApplicationCore, Core, EventLoop, HTTP, HTTPServer, Json, SSL, Sockets, WebSockets, XMPP.</p><p>This is a developer tool or program module for Insights, UBT, or command-line apps.</p><p>UBT also lists dependencies on: ApplicationCore, Core, EventLoop, HTTP, HTTPServer, Json, SSL, Sockets. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">WebTests</code>（Web Tests）：它是构建/工具/独立程序（UBT、Horde、Insights、Automation、命令行 Program）。位于 <code class="usage-code">Programs</code>，构建规则 <code class="usage-code">Programs/WebTests/WebTests.Build.cs</code>。直接依赖 8 个模块：<code class="usage-code">ApplicationCore</code>、<code class="usage-code">Core</code>、<code class="usage-code">EventLoop</code>、<code class="usage-code">HTTP</code>、<code class="usage-code">HTTPServer</code> 等。</li><li>部署：<code class="usage-code">WebTests</code> 独立程序(Programs)，给命令行/工具用，不进游戏运行时。</li><li>怎么用：作为独立程序或命令行工具运行，不进游戏运行时；用于构建、CI、性能分析等。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;WebTests&quot; });</code>；对外暴露 <code class="usage-code">WebTests</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：作为独立程序/命令运行，或在工具代码里 include 其 Public 头。</li></ol><p class="usage-note">`WebTests`：它是构建/工具/独立程序（UBT、Horde、Insights、Automation、命令行 Program）；构建规则 `Programs/WebTests/WebTests.Build.cs`，直接依赖 8 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">WebTests</code> (Web Tests): it is a build/tool/standalone Program (UBT, Horde, Insights, Automation, CLI). Located under <code class="usage-code">Programs</code>; build rule <code class="usage-code">Programs/WebTests/WebTests.Build.cs</code>. It directly depends on 8 modules: <code class="usage-code">ApplicationCore</code>, <code class="usage-code">Core</code>, <code class="usage-code">EventLoop</code>, <code class="usage-code">HTTP</code>, <code class="usage-code">HTTPServer</code> etc.</li><li>Placement: <code class="usage-code">WebTests</code> is a standalone Program; used by CLI/tools, not game runtime.</li><li>How to use: run it as a standalone program/CLI; it does not ship in the game — used for builds, CI, profiling.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;WebTests&quot; });</code>. Use Public when exposing <code class="usage-code">WebTests</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: run it as a standalone program/command, or include its Public headers from tool code.</li></ol><p class="usage-note">`WebTests`: it is a build/tool/standalone Program (UBT, Horde, Insights, Automation, CLI); build rule `Programs/WebTests/WebTests.Build.cs`; depends on 8 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (10)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">ApplicationCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EventLoop</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HTTP</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HTTPServer</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Json</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SSL</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Sockets</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WebSockets</span></div><div class="module-item"><span class="dot"></span><span class="name mono">XMPP</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Programs/WebTests/WebTests.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
