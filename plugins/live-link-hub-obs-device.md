---
layout: default
title: Live Link Hub OBS 设备 / Live Link Hub OBS Device
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">L</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Live Link Hub OBS Device</div>
      <div class="hero-title-cn">Live Link Hub OBS 设备 · Live Link Hub 设备，用于通过 OBS WebSoc</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/LiveLinkOBSDevice/LiveLinkOBSDevice.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Live Link Hub 设备，用于通过 OBS WebSocket v5 协议控制 OBS Studio 录制和以单声道形式摄取录制的视频。</div><div class="lang-content">Live Link Hub device for controlling OBS Studio recording and ingesting recorded video as mono takes via the OBS WebSocket v5 protocol.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Live Link 把外部设备的实时数据（动捕、摄像机、灯光、面捕）流进编辑器或运行时，驱动骨骼、摄像机、Control Rig。虚拟制片和 MetaHuman 面捕的主干。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：LiveLinkOBSDevice。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine</a></p></div><div class="lang-content"><p>Live Link streams live data from mocap, cameras, lights, and facial capture into the editor or runtime to drive skeletons, cameras, and Control Rig. It is the backbone of virtual production and MetaHuman face capture.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: LiveLinkOBSDevice. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/live-link-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Live Link Hub OBS Device</code>（模块 <code class="usage-code">LiveLinkOBSDevice</code>），属 Virtual Production。</li><li>通过 OBS WebSocket v5 协议控制 OBS Studio 录制，并把录制视频以单声道 take 摄取。</li><li>在 Live Link Hub 里配置 OBS 连接，触发录制并接收录好的 take。</li><li>需 Live Link Hub 与 OBS Studio（启用 WebSocket v5）。</li></ol><p class="usage-note">通过 OBS WebSocket v5 控制 OBS 录制并摄取的 Hub 设备。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Live Link Hub OBS Device</code> (module <code class="usage-code">LiveLinkOBSDevice</code>), part of Virtual Production.</li><li>Control OBS Studio recording over the OBS WebSocket v5 protocol and ingest recorded video as mono takes.</li><li>Configure the OBS connection in Live Link Hub, trigger recording, and receive the recorded takes.</li><li>Requires Live Link Hub and OBS Studio with WebSocket v5 enabled.</li></ol><p class="usage-note">A Hub device that controls OBS recording via WebSocket v5 and ingests takes.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">LiveLinkOBSDevice</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/LiveLinkOBSDevice/LiveLinkOBSDevice.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
