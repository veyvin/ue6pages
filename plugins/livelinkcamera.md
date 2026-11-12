---
layout: default
title: 实时连线相机 / LiveLinkCamera
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">L</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">LiveLinkCamera</div>
      <div class="hero-title-cn">实时连线相机 · Live Link 插件添加了相机处理功能</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/LiveLinkCamera/LiveLinkCamera.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Live Link 插件添加了相机处理功能</div><div class="lang-content">Live Link plugin adding functionalities for camera handling</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Live Link 插件添加了相机处理功能</p><p>Live Link 家族：把某种设备或协议的实时数据变成 Live Link 主体，供骨骼/摄像机消费。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：LiveLinkCamera, LiveLinkCameraEditor, LiveLinkCameraRecording。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Live Link plugin adding functionalities for camera handling</p><p>Live Link family: turns a device or protocol into a Live Link subject for skeletons or cameras.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: LiveLinkCamera, LiveLinkCameraEditor, LiveLinkCameraRecording. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">LiveLinkCamera</code>（运行时 <code class="usage-code">LiveLinkCamera</code>、<code class="usage-code">LiveLinkCameraRecording</code>，编辑器 <code class="usage-code">LiveLinkCameraEditor</code>），属 Virtual Production。</li><li>它给 Live Link 增加相机处理能力：接入真实摄像机的跟踪/镜头数据。</li><li>把相机数据驱动到引擎摄像机/镜头组件，用于虚拟制片取景与录制。</li><li>Game 模块依赖运行时模块；<code class="usage-code">LiveLinkCameraEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">Live Link 的相机处理（跟踪/镜头）能力，虚拟制片用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">LiveLinkCamera</code> (runtime <code class="usage-code">LiveLinkCamera</code>, <code class="usage-code">LiveLinkCameraRecording</code>, editor <code class="usage-code">LiveLinkCameraEditor</code>), part of Virtual Production.</li><li>It adds camera handling to Live Link: ingest real camera tracking/lens data.</li><li>Drive engine camera/lens components with the camera data for virtual production framing and recording.</li><li>Game modules depend on runtime modules; <code class="usage-code">LiveLinkCameraEditor</code> is Editor-target only.</li></ol><p class="usage-note">Live Link camera handling (tracking/lens) for virtual production.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">LiveLinkCamera</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">LiveLinkCameraEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">LiveLinkCameraRecording</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/LiveLinkCamera/LiveLinkCamera.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
