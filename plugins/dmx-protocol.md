---
layout: default
title: DMX协议 / DMX Protocol
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">DMX Protocol</div>
      <div class="hero-title-cn">DMX协议 · DMX 协议实施</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">5</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/DMX/DMXProtocol/DMXProtocol.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">DMX 协议实施</div><div class="lang-content">DMX Protocols implementation</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：DMX 协议实施</p><p>DMX 家族：舞台灯光协议、灯具、像素映射，把引擎接到真实灯光台。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：DMXProtocol, DMXProtocolArtNet, DMXProtocolSACN, DMXProtocolEditor, DMXProtocolBlueprintGraph。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: DMX Protocols implementation</p><p>DMX family: lighting protocols, fixtures, and pixel mapping from the engine to a lighting desk.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: DMXProtocol, DMXProtocolArtNet, DMXProtocolSACN, DMXProtocolEditor, DMXProtocolBlueprintGraph. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">DMX Protocol</code>（<code class="usage-code">DMXProtocol</code>、<code class="usage-code">DMXProtocolArtNet</code>、<code class="usage-code">DMXProtocolSACN</code>；编辑器 <code class="usage-code">DMXProtocolEditor</code>）。</li><li>打开 <code class="usage-code">Project Settings &gt; Plugins &gt; DMX</code>，添加 Input/Output Port：选 Art-Net 或 sACN，填网卡、Universe、单播/广播地址。</li><li>同一台机器上用 Wireshark 或灯光软件看 <code class="usage-code">DMXProtocolArtNet</code> / <code class="usage-code">DMXProtocolSACN</code> 是否在发 512 通道；防火墙要放行 UDP 6454（Art-Net）或 5568（sACN）。</li><li>蓝图通过 <code class="usage-code">DMXProtocolBlueprintGraph</code> 监听端口字节（原始 Universe），一般业务仍应走 <code class="usage-code">DMX Engine</code> 的属性层。</li><li>多网卡演播环境务必绑对 NIC，否则 DMX 会打到错误网段。</li><li><code class="usage-code">DMXProtocolEditor</code> 只进 Editor；游戏包保留 Art-Net/sACN 运行时模块即可。</li></ol><p class="usage-note">只实现 Art-Net/sACN 端口，不包含 Library 或灯具网格。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">DMX Protocol</code> (<code class="usage-code">DMXProtocol</code>, <code class="usage-code">DMXProtocolArtNet</code>, <code class="usage-code">DMXProtocolSACN</code>; editor <code class="usage-code">DMXProtocolEditor</code>).</li><li>Under <code class="usage-code">Project Settings &gt; Plugins &gt; DMX</code>, add Input/Output Ports: Art-Net or sACN, NIC, universe, unicast/broadcast.</li><li>Confirm <code class="usage-code">DMXProtocolArtNet</code> / <code class="usage-code">DMXProtocolSACN</code> emit 512-slot universes with Wireshark or a lighting app; allow UDP 6454 (Art-Net) or 5568 (sACN).</li><li>Blueprint can watch raw universe bytes via <code class="usage-code">DMXProtocolBlueprintGraph</code>; most shows should still use <code class="usage-code">DMX Engine</code> attributes.</li><li>Bind the correct NIC on multi-homed stages or DMX lands on the wrong subnet.</li><li>Keep <code class="usage-code">DMXProtocolEditor</code> on Editor targets; shipping needs the Art-Net/sACN runtime modules.</li></ol><p class="usage-note">Art-Net/sACN ports only; no Library and no fixture meshes.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (5)</div><div class="module-item"><span class="dot"></span><span class="name mono">DMXProtocol</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DMXProtocolArtNet</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DMXProtocolSACN</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DMXProtocolEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DMXProtocolBlueprintGraph</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/DMX/DMXProtocol/DMXProtocol.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
