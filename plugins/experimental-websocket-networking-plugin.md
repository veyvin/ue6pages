---
layout: default
title: 实验性 WebSocket 网络插件 / Experimental WebSocket Networking Plugin
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Experimental WebSocket Networking Plugin</div>
      <div class="hero-title-cn">实验性 WebSocket 网络插件 · WebSocket 网络 - 注意：必须禁用所有其他现有的 Ne</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Misc</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/WebSocketNetworking/WebSocketNetworking.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">WebSocket 网络 - 注意：必须禁用所有其他现有的 NetDriverDefinition 才能使用 WebSocketNetDriver。另外：必须禁用 HTML5/Websockets 不支持的所有 PackHandlerComponent（例如 SteamAuthComponentModuleInterface）</div><div class="lang-content">WebSocket Networking - NOTE: MUST disable all other existing NetDriverDefinitions in order to use WebSocketNetDriver. ALSO: MUST disable all PackHandlerComponents not supported by HTML5/Websockets (e.g. SteamAuthComponentModuleInterface)</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：WebSocket 网络 - 注意：必须禁用所有其他现有的 NetDriverDefinition 才能使用 WebSocketNetDriver。另外：必须禁用 HTML5/Websockets 不支持的所有 PackHandlerComponent（例如 SteamAuthComponentModuleInterface）</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：WebSocketNetworking。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: WebSocket Networking - NOTE: MUST disable all other existing NetDriverDefinitions in order to use WebSocketNetDriver. ALSO: MUST disable all PackHandlerComponents not supported by HTML5/Websockets (e.g. SteamAuthComponentModuleInterface)</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: WebSocketNetworking. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用前先改网络配置：在 <code class="usage-code">Config/DefaultEngine.ini</code> 的 <code class="usage-code">[/Script/Engine.Engine]</code> 里，把原有 <code class="usage-code">NetDriverDefinitions</code> 全部禁用或删除，才能用 <code class="usage-code">WebSocketNetDriver</code>，否则会和 UDP 驱动冲突。</li><li>新增一条指向 <code class="usage-code">WebSocketNetDriver</code> 的 <code class="usage-code">NetDriverDefinitions</code>，把默认驱动关到只剩它。</li><li>在 <code class="usage-code">PacketHandlerComponents</code> 里禁用 HTML5/WebSocket 不支持的组件（如 <code class="usage-code">SteamAuthComponentModuleInterface</code>），否则握手阶段会失败。</li><li>服务端与客户端都要启用 <code class="usage-code">WebSocketNetworking</code>，用 <code class="usage-code">-log</code> 启动，确认连接日志里使用的是 <code class="usage-code">WebSocketNetDriver</code> 而非默认驱动。</li><li>目标为 HTML5/浏览器时，按对应平台打包，确认运行时加载的 NetDriver 名为 <code class="usage-code">WebSocketNetDriver</code>。</li><li>握手失败时先查是否仍有残留的其他 <code class="usage-code">NetDriverDefinitions</code> 或未禁用的 <code class="usage-code">PacketHandler</code>，这是最常见原因。</li><li>Experimental：正式上线前用真实延迟/负载验证稳定性与吞吐。</li></ol><p class="usage-note">核心是清空其它 NetDriver 并禁用不兼容 PacketHandler；否则 WebSocket 驱动根本接管不了连接。</p></div><div class="lang-content"><ol class="usage-steps"><li>Change networking config first: in <code class="usage-code">Config/DefaultEngine.ini</code> under <code class="usage-code">[/Script/Engine.Engine]</code>, disable or remove all existing <code class="usage-code">NetDriverDefinitions</code>, otherwise <code class="usage-code">WebSocketNetDriver</code> conflicts with the UDP driver.</li><li>Add one <code class="usage-code">NetDriverDefinitions</code> entry pointing to <code class="usage-code">WebSocketNetDriver</code>, leaving it as the only default driver.</li><li>Disable <code class="usage-code">PacketHandlerComponents</code> that HTML5/WebSocket cannot support (e.g. <code class="usage-code">SteamAuthComponentModuleInterface</code>), or the handshake will fail.</li><li>Enable <code class="usage-code">WebSocketNetworking</code> on both client and server, launch with <code class="usage-code">-log</code>, and confirm the connection log shows <code class="usage-code">WebSocketNetDriver</code>, not the default driver.</li><li>For HTML5/browser targets, package for that platform and confirm the runtime-loaded NetDriver is <code class="usage-code">WebSocketNetDriver</code>.</li><li>When the handshake fails, first check for leftover other <code class="usage-code">NetDriverDefinitions</code> or an un-disabled <code class="usage-code">PacketHandler</code> — that is the most common cause.</li><li>Experimental: validate stability and throughput with realistic latency/load before going live.</li></ol><p class="usage-note">The key is clearing other NetDrivers and disabling incompatible PacketHandlers; otherwise the WebSocket driver never takes over the connection.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">WebSocketNetworking</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/WebSocketNetworking/WebSocketNetworking.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
