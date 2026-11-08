---
layout: default
title: 史诗舞台应用程序 / Epic Stage App
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Epic Stage App</div>
      <div class="hero-title-cn">史诗舞台应用程序 · 启用来自 Epic Stage 应用程序的远程连接</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Messaging</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/EpicStageApp/EpicStageApp.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">启用来自 Epic Stage 应用程序的远程连接</div><div class="lang-content">Enables remote connections from the Epic Stage App</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：启用来自 Epic Stage 应用程序的远程连接</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：EpicStageApp。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Enables remote connections from the Epic Stage App</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: EpicStageApp. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Epic Stage App</code>，这是让 Epic Stage 移动端应用远程连到 UE 会话的引擎侧组件（虚拟制片/现场）。</li><li>确认手机与被控 UE 主机在同一网络，并在项目/消息设置里允许 UDP 消息传递，供其发现与通信。</li><li>启动用作被控的 UE 会话（常配合 nDisplay/摄像机跟踪的虚拟制片工程）。</li><li>在 Epic Stage 应用里发现/填入该 UE 主机地址，建立连接后即可远程驱动相机与场景变换。</li><li>联调时用消息/输出日志确认连接握手；断线先查防火墙与端口。</li></ol><p class="usage-note">它不是编辑器面板工具，而是“手机 App ↔ UE 主机”的远程连接桥；连不上基本都是网络/防火墙/UDP 发现没通。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Epic Stage App</code> — the engine-side component that lets the Epic Stage mobile app connect remotely to a UE session (virtual production / on-set).</li><li>Ensure the phone and the controlled UE host share a network and that UDP messaging is allowed in project/messaging settings for discovery and comms.</li><li>Launch the UE session that will be driven (often an nDisplay/camera-tracking virtual-production project).</li><li>In the Epic Stage app, discover/enter the UE host address; once connected it drives cameras and scene transforms remotely.</li><li>During bring-up, watch the message/output logs for the handshake; if it won&#x27;t connect, check firewall and ports first.</li></ol><p class="usage-note">It&#x27;s not an editor-panel tool but the remote bridge between the phone app and the UE host; connection failures are almost always networking/firewall/UDP discovery.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">EpicStageApp</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/EpicStageApp/EpicStageApp.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
