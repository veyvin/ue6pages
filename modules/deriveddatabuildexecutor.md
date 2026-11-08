---
layout: default
title: DerivedDataBuildExecutor
---



<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>D</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">DerivedDataBuildExecutor</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">6 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">6</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Developer/DerivedDataBuildExecutor/DerivedDataBuildExecutor.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于其他 6 个模块：Core、DerivedDataCache、DesktopPlatform、Json、TraceLog、Zen。</div><div class="lang-content">This module depends on 6 other module(s): Core, DerivedDataCache, DesktopPlatform, Json, TraceLog, Zen.</div></div>
      </div>
    </div>
    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>用途：<code class="usage-code">DerivedDataBuildExecutor</code> 位于 <code class="usage-code">Developer</code>，构建规则 <code class="usage-code">Developer/DerivedDataBuildExecutor/DerivedDataBuildExecutor.Build.cs</code>。它直接依赖 6 个模块：<code class="usage-code">Core</code>、<code class="usage-code">DerivedDataCache</code>、<code class="usage-code">DesktopPlatform</code>、<code class="usage-code">Json</code>、<code class="usage-code">TraceLog</code>、<code class="usage-code">Zen</code>。</li><li>部署：它属于开发者/工具模块，用于执行派生数据(DDC)构建，供编辑器/命令行工具链使用，不要当游戏运行时依赖。</li><li>依赖：只有当你在编写构建/DDC 相关工具时才在对应模块的 <code class="usage-code">Build.cs</code> 里加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;DerivedDataBuildExecutor&quot; });</code>。</li><li>调用：#include 其 Public 头（常见 <code class="usage-code">DerivedDataBuildExecutor.h</code>），通过派生数据构建执行器 API 触发构建。</li><li>传递依赖：<code class="usage-code">DerivedDataBuildExecutor</code> 还依赖 <code class="usage-code">DerivedDataCache</code>、<code class="usage-code">DesktopPlatform</code>、<code class="usage-code">Json</code>、<code class="usage-code">TraceLog</code>、<code class="usage-code">Zen</code>；不必在游戏模块重复填写，除非你要直接 include 那些头文件。</li></ol><p class="usage-note">`DerivedDataBuildExecutor` 的构建规则位于 `Developer/DerivedDataBuildExecutor/DerivedDataBuildExecutor.Build.cs`，直接依赖 6 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li>Purpose: <code class="usage-code">DerivedDataBuildExecutor</code> lives under <code class="usage-code">Developer</code>; build rule <code class="usage-code">Developer/DerivedDataBuildExecutor/DerivedDataBuildExecutor.Build.cs</code>. It depends on 6 modules: <code class="usage-code">Core</code>, <code class="usage-code">DerivedDataCache</code>, <code class="usage-code">DesktopPlatform</code>, <code class="usage-code">Json</code>, <code class="usage-code">TraceLog</code>, <code class="usage-code">Zen</code>.</li><li>Placement: a developer/tool module that executes derived-data (DDC) builds for the editor/CLI toolchain; not a game runtime dependency.</li><li>Depend: only when building build/DDC tooling, add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;DerivedDataBuildExecutor&quot; });</code> to the relevant Build.cs.</li><li>Call: include its Public header (often <code class="usage-code">DerivedDataBuildExecutor.h</code>) and trigger builds through the derived-data build executor API.</li><li>Transitive deps: <code class="usage-code">DerivedDataBuildExecutor</code> also needs <code class="usage-code">DerivedDataCache</code>, <code class="usage-code">DesktopPlatform</code>, <code class="usage-code">Json</code>, <code class="usage-code">TraceLog</code>, <code class="usage-code">Zen</code>; do not re-list them unless you include their headers.</li></ol><p class="usage-note">`DerivedDataBuildExecutor` build rule is `Developer/DerivedDataBuildExecutor/DerivedDataBuildExecutor.Build.cs`; depends on 6 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (6)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DerivedDataCache</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DesktopPlatform</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Json</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TraceLog</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Zen</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Developer/DerivedDataBuildExecutor/DerivedDataBuildExecutor.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
