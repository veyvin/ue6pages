---
layout: default
title: 在线子系统实用程序 / Online Subsystem Utils
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">O</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Online Subsystem Utils</div>
      <div class="hero-title-cn">在线子系统实用程序 · 用于交互在线服务和在线子系统实现的共享代码。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Online Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Online/OnlineSubsystemUtils/OnlineSubsystemUtils.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于交互在线服务和在线子系统实现的共享代码。</div><div class="lang-content">Shared code for interacting online service and online subsystem implementations.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于交互在线服务和在线子系统实现的共享代码。</p><p>在线子系统家族：为 Steam、EOS、Google、Apple 等平台提供登录、会话、成就的 OSS / Online Services 实现。</p><p>属于在线子系统 / 平台服务。</p><p>它打包的模块包括：OnlineSubsystemUtils, OnlineBlueprintSupport。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Shared code for interacting online service and online subsystem implementations.</p><p>Online family: OSS / Online Services for login, sessions, and achievements on Steam, EOS, Google, Apple, etc.</p><p>Part of Online Subsystem / platform services.</p><p>It ships these modules: OnlineSubsystemUtils, OnlineBlueprintSupport. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Online Subsystem Utils</code>（模块 <code class="usage-code">OnlineSubsystemUtils</code>、<code class="usage-code">OnlineBlueprintSupport</code>）。</li><li>它提供与在线服务和在线子系统实现交互的共享工具（含蓝图支持）。</li><li>常用作上层在线功能（会话/大厅）的依赖，含蓝图节点。</li><li>Game 模块可依赖；广泛用于联机项目。</li></ol><p class="usage-note">在线服务/子系统的共享工具（含蓝图支持）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Online Subsystem Utils</code> (modules <code class="usage-code">OnlineSubsystemUtils</code>, <code class="usage-code">OnlineBlueprintSupport</code>).</li><li>It provides shared utilities to interact with online services and OSS implementations (incl. Blueprint support).</li><li>Commonly a dependency for upper online features (sessions/lobby), with Blueprint nodes.</li><li>Game modules can depend on it; widely used in net projects.</li></ol><p class="usage-note">Shared utilities for online services/subsystems (incl. Blueprint support).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">OnlineSubsystemUtils</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">OnlineBlueprintSupport</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Online/OnlineSubsystemUtils/OnlineSubsystemUtils.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
