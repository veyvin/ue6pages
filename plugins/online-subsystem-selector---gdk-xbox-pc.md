---
layout: default
title: 在线子系统选择器 - GDK (Xbox PC) / Online Subsystem Selector - GDK (Xbox PC)
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">O</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Online Subsystem Selector - GDK (Xbox PC)</div>
      <div class="hero-title-cn">在线子系统选择器 - GDK (Xbox PC) · 通过 Xbox PC 应用程序安装游戏时，自动切换到 Onlin</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Windows/MSGameOSSSelector/MSGameOSSSelector.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">通过 Xbox PC 应用程序安装游戏时，自动切换到 OnlineSubsystemGDK。</div><div class="lang-content">Automatically switches to OnlineSubsystemGDK when the game is installed via the Xbox PC App.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：通过 Xbox PC 应用程序安装游戏时，自动切换到 OnlineSubsystemGDK。</p><p>在线子系统家族：为 Steam、EOS、Google、Apple 等平台提供登录、会话、成就的 OSS / Online Services 实现。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：MSGameOSSSelector。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Automatically switches to OnlineSubsystemGDK when the game is installed via the Xbox PC App.</p><p>Online family: OSS / Online Services for login, sessions, and achievements on Steam, EOS, Google, Apple, etc.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: MSGameOSSSelector. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Online Subsystem Selector - GDK (Xbox PC)</code>（模块 <code class="usage-code">MSGameOSSSelector</code>）。</li><li>当游戏通过 Xbox PC 应用程序安装时，它自动切换到 <code class="usage-code">OnlineSubsystemGDK</code>。</li><li>随 GDK 打包使用，让同一构建在不同安装渠道选对 OSS。</li><li>属平台选择器；配合 OnlineSubsystemGDK 使用。</li></ol><p class="usage-note">通过 Xbox PC 应用安装时自动切到 OnlineSubsystemGDK。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Online Subsystem Selector - GDK (Xbox PC)</code> (module <code class="usage-code">MSGameOSSSelector</code>).</li><li>When the game is installed via the Xbox PC App, it automatically switches to <code class="usage-code">OnlineSubsystemGDK</code>.</li><li>Use it with GDK packaging so the same build picks the right OSS per install channel.</li><li>It is a platform selector; used with OnlineSubsystemGDK.</li></ol><p class="usage-note">Auto-switches to OnlineSubsystemGDK when installed via the Xbox PC App.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">MSGameOSSSelector</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Windows/MSGameOSSSelector/MSGameOSSSelector.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
