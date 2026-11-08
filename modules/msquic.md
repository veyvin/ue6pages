---
layout: default
title: MsQuic
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>M</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">MsQuic</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>External</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">0 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">External</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">0</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">ThirdParty/MsQuic/MsQuic.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块没有声明的依赖项。</div><div class="lang-content">This module has no declared dependencies.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：该模块没有声明的依赖项。</p><p>这是第三方库的 UBT 封装，通常由上层引擎模块使用，而不是游戏直接依赖。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: This module has no declared dependencies.</p><p>This is a UBT wrapper around a third-party library; engine modules consume it, games rarely depend on it directly.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>用途：<code class="usage-code">MsQuic</code> 位于 <code class="usage-code">ThirdParty</code>，构建规则 <code class="usage-code">ThirdParty/MsQuic/MsQuic.Build.cs</code>。描述符未声明依赖。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;MsQuic&quot; });</code>；对外暴露 <code class="usage-code">MsQuic</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>部署：<code class="usage-code">MsQuic</code> 是第三方库的 UBT 封装。优先依赖引擎已包好的上层模块，而不是直接依赖它。</li><li>调用：#include 其 Public 头（常见 <code class="usage-code">MsQuic.h</code> / <code class="usage-code">MsQuicModule.h</code>），再用 <code class="usage-code">FModuleManager::LoadModulePtr&lt;MsQuicModule&gt;</code> 或直接使用导出类型。</li><li>传递依赖：<code class="usage-code">MsQuic</code> 未声明额外公开依赖，通常只依赖引擎基础层。</li></ol><p class="usage-note">`MsQuic` 的构建规则位于 `ThirdParty/MsQuic/MsQuic.Build.cs`，直接依赖 0 个模块，分类 External。</p></div><div class="lang-content"><ol class="usage-steps"><li>Purpose: <code class="usage-code">MsQuic</code> lives under <code class="usage-code">ThirdParty</code>; build rule <code class="usage-code">ThirdParty/MsQuic/MsQuic.Build.cs</code>.The descriptor declares no dependencies.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;MsQuic&quot; });</code>. Use Public when exposing <code class="usage-code">MsQuic</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Placement: <code class="usage-code">MsQuic</code> wraps a third-party library. Prefer the engine module that already wraps it.</li><li>Call: include Public headers (often <code class="usage-code">MsQuic.h</code> / <code class="usage-code">MsQuicModule.h</code>), then use <code class="usage-code">FModuleManager::LoadModulePtr&lt;MsQuicModule&gt;</code> or the exported types directly.</li><li>Transitive deps: <code class="usage-code">MsQuic</code> declares no extra public deps; it typically relies on engine basics.</li></ol><p class="usage-note">`MsQuic` build rule is `ThirdParty/MsQuic/MsQuic.Build.cs`; depends on 0 modules; category External.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (0)</div>
      <div style="font-size:12px;color:var(--on-surface-variant);">None declared.</div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">ThirdParty/MsQuic/MsQuic.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
