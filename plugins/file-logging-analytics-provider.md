---
layout: default
title: 文件记录分析提供商 / File Logging Analytics Provider
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">File Logging Analytics Provider</div>
      <div class="hero-title-cn">文件记录分析提供商 · 将分析 API 调用写入本地磁盘以供调试或本地使用</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Analytics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Analytics/FileLogging/FileLogging.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">将分析 API 调用写入本地磁盘以供调试或本地使用</div><div class="lang-content">Writes analytic API calls to local disk for debugging or local use</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：将分析 API 调用写入本地磁盘以供调试或本地使用</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：FileLogging。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Writes analytic API calls to local disk for debugging or local use</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: FileLogging. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">File Logging Analytics Provider</code>（模块 <code class="usage-code">FileLogging</code>）。它实现 <code class="usage-code">IAnalyticsProvider</code>，把 <code class="usage-code">RecordEvent</code> 写到本机文件，不连 Adjust / ET / Swrve。</li><li>在 <code class="usage-code">Config/DefaultEngine.ini</code> 的 <code class="usage-code">[Analytics]</code> 设置 <code class="usage-code">ProviderModuleName=FileLogging</code>（可再配 <code class="usage-code">FileLogging</code> 段指定目录）。未写 Provider 时 <code class="usage-code">UAnalyticsBlueprintLibrary</code> 的调用会 silently 丢掉。</li><li>开局调用 <code class="usage-code">Start Session</code>，玩法处 <code class="usage-code">Record Event</code> / <code class="usage-code">Record Event with Attributes</code>，退出 <code class="usage-code">End Session</code> 并 <code class="usage-code">Flush Events</code>。C++ 走 <code class="usage-code">FAnalytics::Get().GetDefaultConfiguredProvider()</code>。</li><li>PIE 后打开项目 <code class="usage-code">Saved/Analytics</code>（或配置的路径）核对 JSON/日志行是否带上事件名与属性；多会话应生成新文件或追加，而不是空目录。</li><li>Shipping 前换成真实 Provider；本模块可进包但只适合本地调试。游戏 <code class="usage-code">Build.cs</code> 一般只依赖 <code class="usage-code">Analytics</code> / <code class="usage-code">AnalyticsBlueprintLibrary</code>，不必直接链 <code class="usage-code">FileLogging</code>。</li></ol><p class="usage-note">磁盘落盘的 Analytics 后端，不是通用日志 `UE_LOG`。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">File Logging Analytics Provider</code> (module <code class="usage-code">FileLogging</code>). It implements <code class="usage-code">IAnalyticsProvider</code> and writes <code class="usage-code">RecordEvent</code> to disk — not Adjust, ET, or Swrve.</li><li>In <code class="usage-code">Config/DefaultEngine.ini</code> under <code class="usage-code">[Analytics]</code> set <code class="usage-code">ProviderModuleName=FileLogging</code> (optional <code class="usage-code">[FileLogging]</code> path). Without a Provider, <code class="usage-code">UAnalyticsBlueprintLibrary</code> calls drop silently.</li><li>Call <code class="usage-code">Start Session</code> at boot, <code class="usage-code">Record Event</code> / <code class="usage-code">Record Event with Attributes</code> in gameplay, then <code class="usage-code">End Session</code> and <code class="usage-code">Flush Events</code>. C++ uses <code class="usage-code">FAnalytics::Get().GetDefaultConfiguredProvider()</code>.</li><li>After PIE, inspect <code class="usage-code">Saved/Analytics</code> (or your configured folder) for JSON/log lines with event names and attributes. New sessions should create or append files, not leave the folder empty.</li><li>Swap to a real provider before shipping. This module can cook but is for local debug. Game <code class="usage-code">Build.cs</code> usually depends on <code class="usage-code">Analytics</code> / <code class="usage-code">AnalyticsBlueprintLibrary</code>, not <code class="usage-code">FileLogging</code> directly.</li></ol><p class="usage-note">Disk-backed Analytics provider, not a general `UE_LOG` logger.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">FileLogging</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Analytics/FileLogging/FileLogging.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
