---
layout: default
title: 在线框架插件 / Online Framework Plugin
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">O</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Online Framework Plugin</div>
      <div class="hero-title-cn">在线框架插件 · 用于与在线游戏服务交互的共享代码。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Online Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">8</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Online/OnlineFramework/OnlineFramework.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于与在线游戏服务交互的共享代码。</div><div class="lang-content">Shared code for interacting with online gameplay services.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于与在线游戏服务交互的共享代码。</p><p>属于在线子系统 / 平台服务。</p><p>它打包的模块包括：Qos, Party, Lobby, PatchCheck, Hotfix, Rejoin, PlayTimeLimit, LoginFlow。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Shared code for interacting with online gameplay services.</p><p>Part of Online Subsystem / platform services.</p><p>It ships these modules: Qos, Party, Lobby, PatchCheck, Hotfix, Rejoin, PlayTimeLimit, LoginFlow. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Online Framework Plugin</code>（模块 <code class="usage-code">Qos</code>、<code class="usage-code">Party</code>、<code class="usage-code">Lobby</code>、<code class="usage-code">PatchCheck</code>、<code class="usage-code">Hotfix</code>、<code class="usage-code">Rejoin</code>、<code class="usage-code">PlayTimeLimit</code>、<code class="usage-code">LoginFlow</code>）。</li><li>它提供与在线游戏服务交互的共享代码（大厅、队伍、QoS、补丁检查、热更、重连、登录流程等）。</li><li>用其模块搭建大厅/组队/登录等在线功能，接入所选 OSS。</li><li>Game 模块可进包；按需启用具体子模块。</li></ol><p class="usage-note">在线游戏服务交互的共享代码（大厅/队伍/QoS/登录流程等）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Online Framework Plugin</code> (modules <code class="usage-code">Qos</code>, <code class="usage-code">Party</code>, <code class="usage-code">Lobby</code>, <code class="usage-code">PatchCheck</code>, <code class="usage-code">Hotfix</code>, <code class="usage-code">Rejoin</code>, <code class="usage-code">PlayTimeLimit</code>, <code class="usage-code">LoginFlow</code>).</li><li>It provides shared code to interact with online game services (lobby, party, QoS, patch check, hotfix, rejoin, login flow, etc.).</li><li>Build lobby/party/login features from its modules on your chosen OSS.</li><li>Game modules can ship; enable the specific submodules you need.</li></ol><p class="usage-note">Shared code to interact with online game services (lobby/party/QoS/login flow, etc.).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (8)</div><div class="module-item"><span class="dot"></span><span class="name mono">Qos</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Party</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Lobby</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PatchCheck</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Hotfix</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Rejoin</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PlayTimeLimit</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">LoginFlow</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Online/OnlineFramework/OnlineFramework.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
