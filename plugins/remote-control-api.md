---
layout: default
title: 远程控制API / Remote Control API
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">R</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Remote Control API</div>
      <div class="hero-title-cn">远程控制API · 一套用于在编辑器中或通过网络服务器在运行时控制虚幻引擎的工具。这</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Messaging</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">8</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/RemoteControl/RemoteControl.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">一套用于在编辑器中或通过网络服务器在运行时控制虚幻引擎的工具。这允许用户通过 HTTP 或 WebSockets 请求远程控制虚幻引擎。此功能允许开发人员通过第 3 方应用程序和 Web 服务控制 Unreal。</div><div class="lang-content">A suite of tools for controlling the Unreal Engine, both in Editor or at Runtime via a webserver. This allows users to control Unreal Engine remotely through HTTP or WebSockets requests. This functionality allows developers to control Unreal through 3rd party applications and web services.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：一套用于在编辑器中或通过网络服务器在运行时控制虚幻引擎的工具。这允许用户通过 HTTP 或 WebSockets 请求远程控制虚幻引擎。此功能允许开发人员通过第 3 方应用程序和 Web 服务控制 Unreal。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：RemoteControl, RemoteControlLogic, WebRemoteControl, RemoteControlCommon, RemoteControlUI, RemoteControlProtocol, RemoteControlProtocolWidgets, RemoteControlMultiUser。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A suite of tools for controlling the Unreal Engine, both in Editor or at Runtime via a webserver. This allows users to control Unreal Engine remotely through HTTP or WebSockets requests. This functionality allows developers to control Unreal through 3rd party applications and web services.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: RemoteControl, RemoteControlLogic, WebRemoteControl, RemoteControlCommon, RemoteControlUI, RemoteControlProtocol, RemoteControlProtocolWidgets, RemoteControlMultiUser. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Remote Control API</code>（模块 <code class="usage-code">RemoteControl</code>、<code class="usage-code">RemoteControlLogic</code>、<code class="usage-code">WebRemoteControl</code>、<code class="usage-code">RemoteControlCommon</code>、<code class="usage-code">RemoteControlUI</code>、<code class="usage-code">RemoteControlProtocol</code>、<code class="usage-code">RemoteControlProtocolWidgets</code>、<code class="usage-code">RemoteControlMultiUser</code>）。</li><li>它是一套在编辑器或通过网络服务器在运行时控制引擎的工具，走 HTTP 或 WebSockets。</li><li>创建 Remote Control Preset，暴露属性/函数，再用第三方应用或 Web 服务远程驱动。</li><li>属虚拟制片/远程操控核心；按协议再启用 DMX/MIDI/OSC 等扩展。</li></ol><p class="usage-note">经 HTTP/WebSocket 远程控制引擎（编辑器或运行时）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Remote Control API</code> (modules <code class="usage-code">RemoteControl</code>, <code class="usage-code">RemoteControlLogic</code>, <code class="usage-code">WebRemoteControl</code>, <code class="usage-code">RemoteControlCommon</code>, <code class="usage-code">RemoteControlUI</code>, <code class="usage-code">RemoteControlProtocol</code>, <code class="usage-code">RemoteControlProtocolWidgets</code>, <code class="usage-code">RemoteControlMultiUser</code>).</li><li>It is a suite of tools for controlling Unreal in editor or at runtime via a web server, over HTTP or WebSockets.</li><li>Create a Remote Control Preset, expose properties/functions, then drive them from a third-party app or web service.</li><li>It is the VP/remote-control core; enable DMX/MIDI/OSC protocol plugins as needed.</li></ol><p class="usage-note">Control Unreal remotely over HTTP/WebSocket (editor or runtime).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (8)</div><div class="module-item"><span class="dot"></span><span class="name mono">RemoteControl</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RemoteControlLogic</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">WebRemoteControl</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RemoteControlCommon</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RemoteControlUI</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RemoteControlProtocol</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RemoteControlProtocolWidgets</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RemoteControlMultiUser</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/RemoteControl/RemoteControl.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
