---
layout: default
title: UnrealInsightsMCP
---



<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>U</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">UnrealInsightsMCP</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">11 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">11</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Programs/UnrealInsightsMCP/UnrealInsightsMCP.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于其他 11 个模块：Core、CoreUObject、Json、JsonUtilities、Messaging、Projects、SessionServices、Sockets、TraceAnalysis、TraceServices、UdpMessaging。</div><div class="lang-content">This module depends on 11 other module(s): Core, CoreUObject, Json, JsonUtilities, Messaging, Projects, SessionServices, Sockets, TraceAnalysis, TraceServices, UdpMessaging.</div></div>
      </div>
    </div>
    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>用途：<code class="usage-code">UnrealInsightsMCP</code> 位于 <code class="usage-code">Programs</code>，构建规则 <code class="usage-code">Programs/UnrealInsightsMCP/UnrealInsightsMCP.Build.cs</code>。它直接依赖 8 个模块：<code class="usage-code">Core</code>、<code class="usage-code">CoreUObject</code>、<code class="usage-code">Json</code>、<code class="usage-code">JsonUtilities</code>、<code class="usage-code">Messaging</code>、<code class="usage-code">Projects</code>、<code class="usage-code">SessionServices</code>、<code class="usage-code">Sockets</code>。</li><li>部署：它属于独立程序(Programs)，是为 Unreal Insights 提供 MCP(Model Context Protocol) 服务的命令行/工具程序，不进游戏运行时。</li><li>依赖：一般无需在自己的模块里依赖它；它作为独立程序构建运行。若确实要复用其代码，再在 Build.cs 加 <code class="usage-code">PublicDependencyModuleNames</code> 声明。</li><li>调用：作为程序运行入口启动 MCP 服务，通过 <code class="usage-code">Messaging</code>/<code class="usage-code">SessionServices</code> 与 Insights 会话交互。</li><li>传递依赖：<code class="usage-code">UnrealInsightsMCP</code> 还依赖 <code class="usage-code">Json</code>、<code class="usage-code">JsonUtilities</code>、<code class="usage-code">Messaging</code>、<code class="usage-code">SessionServices</code>、<code class="usage-code">Sockets</code> 等；不必在游戏模块重复填写，除非你要直接 include 那些头文件。</li></ol><p class="usage-note">`UnrealInsightsMCP` 的构建规则位于 `Programs/UnrealInsightsMCP/UnrealInsightsMCP.Build.cs`，直接依赖 8 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li>Purpose: <code class="usage-code">UnrealInsightsMCP</code> lives under <code class="usage-code">Programs</code>; build rule <code class="usage-code">Programs/UnrealInsightsMCP/UnrealInsightsMCP.Build.cs</code>. It depends on 8 modules: <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">Json</code>, <code class="usage-code">JsonUtilities</code>, <code class="usage-code">Messaging</code>, <code class="usage-code">Projects</code>, <code class="usage-code">SessionServices</code>, <code class="usage-code">Sockets</code>.</li><li>Placement: a standalone Program that serves MCP (Model Context Protocol) for Unreal Insights via CLI/tool; it does not run in the game.</li><li>Depend: usually you do not depend on it from your own modules; it builds/runs as a standalone program. Only if you truly reuse its code, add it to your Build.cs.</li><li>Call: run it as a program entry to start the MCP service and interact with Insights sessions via <code class="usage-code">Messaging</code>/<code class="usage-code">SessionServices</code>.</li><li>Transitive deps: <code class="usage-code">UnrealInsightsMCP</code> also needs <code class="usage-code">Json</code>, <code class="usage-code">JsonUtilities</code>, <code class="usage-code">Messaging</code>, <code class="usage-code">SessionServices</code>, <code class="usage-code">Sockets</code>, etc.; do not re-list them unless you include their headers.</li></ol><p class="usage-note">`UnrealInsightsMCP` build rule is `Programs/UnrealInsightsMCP/UnrealInsightsMCP.Build.cs`; depends on 8 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (11)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Json</span></div><div class="module-item"><span class="dot"></span><span class="name mono">JsonUtilities</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Messaging</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Projects</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SessionServices</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Sockets</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TraceAnalysis</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TraceServices</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UdpMessaging</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Programs/UnrealInsightsMCP/UnrealInsightsMCP.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
