---
layout: default
title: 套接字子系统 Steam (IP) / Socket Subsystem Steam (IP)
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">S</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Socket Subsystem Steam (IP)</div>
      <div class="hero-title-cn">套接字子系统 Steam (IP) · 负责用户之间的 Steam 网络连接。不使用 NAT 穿透，使用</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Online Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Online/SocketSubsystemSteamIP/SocketSubsystemSteamIP.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">负责用户之间的 Steam 网络连接。不使用 NAT 穿透，使用 SteamSockets 插件来支持 P2P</div><div class="lang-content">Responsible for Steam net connections between users. Does NOT use NAT punchthrough, use the SteamSockets plugin for P2P support</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：负责用户之间的 Steam 网络连接。不使用 NAT 穿透，使用 SteamSockets 插件来支持 P2P</p><p>属于在线子系统 / 平台服务。</p><p>它打包的模块包括：SocketSubsystemSteamIP。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Responsible for Steam net connections between users. Does NOT use NAT punchthrough, use the SteamSockets plugin for P2P support</p><p>Part of Online Subsystem / platform services.</p><p>It ships these modules: SocketSubsystemSteamIP. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Socket Subsystem Steam (IP)</code>（模块 <code class="usage-code">SocketSubsystemSteamIP</code>）。</li><li>它负责用户之间的 Steam 网络连接（基于 IP，不做 NAT 穿透）。</li><li>P2P 能力配合 <code class="usage-code">SteamSockets</code> 插件使用。</li><li>属平台网络传输；需 Steam 配置。</li></ol><p class="usage-note">Steam 用户间网络连接（IP，无 NAT 穿透）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Socket Subsystem Steam (IP)</code> (module <code class="usage-code">SocketSubsystemSteamIP</code>).</li><li>It handles Steam network connections between users (IP-based, no NAT punch-through).</li><li>For P2P, pair it with the <code class="usage-code">SteamSockets</code> plugin.</li><li>It is a platform network transport; requires Steam config.</li></ol><p class="usage-note">Steam user-to-user network connections (IP, no NAT punch-through).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">SocketSubsystemSteamIP</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Online/SocketSubsystemSteamIP/SocketSubsystemSteamIP.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
