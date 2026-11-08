---
layout: default
title: 捕获数据 / Capture Data
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Capture Data</div>
      <div class="hero-title-cn">捕获数据 · 与捕获数据相关的类</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/CaptureData/CaptureData.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">与捕获数据相关的类</div><div class="lang-content">Classes releated to captured data</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：与捕获数据相关的类</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：CaptureDataCore, CaptureDataEditor, CaptureDataUtils。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Classes releated to captured data</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: CaptureDataCore, CaptureDataEditor, CaptureDataUtils. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Capture Data</code>（<code class="usage-code">CaptureDataCore</code>、<code class="usage-code">CaptureDataEditor</code>、<code class="usage-code">CaptureDataUtils</code>）。它定义入库之后的资产类型，不控制采集硬件。</li><li>用 Capture Manager 入库后，在内容浏览器打开 <code class="usage-code">FootageCaptureData</code>（<code class="usage-code">UFootageCaptureData</code>）：检查 <code class="usage-code">ImageSequences</code>（每路 RGB 的 <code class="usage-code">UImgMediaSource</code>）、可选 <code class="usage-code">DepthSequences</code>、<code class="usage-code">AudioTracks</code>、<code class="usage-code">CameraCalibrations</code>。</li><li>读 <code class="usage-code">Metadata</code>：<code class="usage-code">FrameRate</code>、<code class="usage-code">DeviceClass</code>、<code class="usage-code">DeviceModelName</code>。手机自拍需正确的设备类，后面的深度/Mesh 管线才选对模型。</li><li>核对 <code class="usage-code">CaptureExcludedFrames</code> 是否包含丢帧；MetaHuman Animator / Performance 资产会合并这份排除表。</li><li>立体或带深度的镜头必须有匹配路数的 <code class="usage-code">CameraCalibrations</code>，否则深度生成会失败。</li><li>C++/Python 只依赖 <code class="usage-code">CaptureDataCore</code> 读这些对象；导入 UI 在 <code class="usage-code">CaptureDataEditor</code>，不要把 Editor 模块链进游戏。</li></ol><p class="usage-note">这是 Capture Manager 写入引擎后的数据层；改设备、转码、上传走 App/Devices/Editor，不在本插件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Capture Data</code> (<code class="usage-code">CaptureDataCore</code>, <code class="usage-code">CaptureDataEditor</code>, <code class="usage-code">CaptureDataUtils</code>). It is the post-ingest asset layer, not device control.</li><li>After Capture Manager ingest, open <code class="usage-code">FootageCaptureData</code> (<code class="usage-code">UFootageCaptureData</code>): <code class="usage-code">ImageSequences</code> (per-view <code class="usage-code">UImgMediaSource</code>), optional <code class="usage-code">DepthSequences</code>, <code class="usage-code">AudioTracks</code>, <code class="usage-code">CameraCalibrations</code>.</li><li>Read <code class="usage-code">Metadata</code> (<code class="usage-code">FrameRate</code>, <code class="usage-code">DeviceClass</code>, <code class="usage-code">DeviceModelName</code>). Phone takes need the right device class for later depth/mesh pipelines.</li><li>Check <code class="usage-code">CaptureExcludedFrames</code> for dropped frames; MetaHuman Animator / Performance assets merge that list.</li><li>Stereo or depth takes need matching <code class="usage-code">CameraCalibrations</code> per view or depth generation fails.</li><li>C++/Python should depend on <code class="usage-code">CaptureDataCore</code> to read these objects. Import UI is <code class="usage-code">CaptureDataEditor</code> — keep it out of the game target.</li></ol><p class="usage-note">This is the data layer after Capture Manager writes into Unreal. Device control, transcode, and upload live in App/Devices/Editor.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureDataCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureDataEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureDataUtils</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/CaptureData/CaptureData.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
