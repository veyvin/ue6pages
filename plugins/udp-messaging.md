---
layout: default
title: UDP消息传送 / UDP Messaging
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">U</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">UDP Messaging</div>
      <div class="hero-title-cn">UDP消息传送 · 将基于 UDP 的传输和隧道层添加到消息传递子系统，用于在联网计</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Messaging</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Messaging/UdpMessaging/UdpMessaging.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">将基于 UDP 的传输和隧道层添加到消息传递子系统，用于在联网计算机和设备之间发送和接收消息。</div><div class="lang-content">Adds a UDP based transport and tunneling layer to the messaging sub-system for sending and receiving messages between networked computers and devices.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：将基于 UDP 的传输和隧道层添加到消息传递子系统，用于在联网计算机和设备之间发送和接收消息。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：UdpMessaging。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Adds a UDP based transport and tunneling layer to the messaging sub-system for sending and receiving messages between networked computers and devices.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: UdpMessaging. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">UDP Messaging</code>（模块 <code class="usage-code">UdpMessaging</code>）。</li><li>它为消息子系统添加基于 UDP 的传输与隧道层，用于联网计算机/设备间收发消息。</li><li>配置 UDP 消息端点，做跨机通信（消息总线默认常用）。</li><li>运行时模块；属消息总线传输层。</li></ol><p class="usage-note">消息子系统的 UDP 传输与隧道层。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">UDP Messaging</code> (module <code class="usage-code">UdpMessaging</code>).</li><li>It adds a UDP-based transport and tunnel layer to the message subsystem for sending/receiving messages between networked computers/devices.</li><li>Configure UDP messaging endpoints for cross-machine communication (a common default message-bus transport).</li><li>A runtime module; a message-bus transport.</li></ol><p class="usage-note">A UDP transport and tunnel layer for the message subsystem.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">UdpMessaging</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Messaging/UdpMessaging/UdpMessaging.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
