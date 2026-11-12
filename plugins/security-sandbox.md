---
layout: default
title: 安全沙箱 / Security Sandbox
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">S</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Security Sandbox</div>
      <div class="hero-title-cn">安全沙箱 · 提供有助于减少游戏客户端运行的操作系统权限的功能，从而减少攻击者</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Security</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/SecuritySandbox/SecuritySandbox.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">提供有助于减少游戏客户端运行的操作系统权限的功能，从而减少攻击者通过漏洞控制游戏客户端时对玩家的影响。</div><div class="lang-content">Provides features to help reduce the operating system permissions your game client runs with and therefore reduce the impact to players if an attacker takes control of it through a vulnerability.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：提供有助于减少游戏客户端运行的操作系统权限的功能，从而减少攻击者通过漏洞控制游戏客户端时对玩家的影响。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：SecuritySandbox。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Provides features to help reduce the operating system permissions your game client runs with and therefore reduce the impact to players if an attacker takes control of it through a vulnerability.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: SecuritySandbox. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Security Sandbox</code>（模块 <code class="usage-code">SecuritySandbox</code>）。</li><li>它帮助降低游戏客户端运行时的操作系统权限，从而减小被漏洞控制后对玩家的影响。</li><li>在 Windows 等目标上启用沙箱，按平台文档配置受限令牌/作业对象。</li><li>属客户端安全加固；按目标平台验证兼容性。</li></ol><p class="usage-note">降低游戏客户端 OS 权限的安全沙箱。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Security Sandbox</code> (module <code class="usage-code">SecuritySandbox</code>).</li><li>It helps reduce OS permissions the game client runs with, limiting impact if an attacker takes control via a vulnerability.</li><li>Enable the sandbox on Windows (and similar) targets and configure restricted tokens/job objects per platform docs.</li><li>It is client security hardening; validate compatibility per target platform.</li></ol><p class="usage-note">Security sandbox to reduce the game client&#x27;s OS permissions.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">SecuritySandbox</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/SecuritySandbox/SecuritySandbox.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
