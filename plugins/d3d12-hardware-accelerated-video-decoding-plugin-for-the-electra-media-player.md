---
layout: default
title: 用于 Electra 媒体播放器的 D3D12 硬件加速视频解码插件 / D3D12 Hardware accelerated video decoding plugin for the Electra media player
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">D3D12 Hardware accelerated video decoding plugin for the Electra media player</div>
      <div class="hero-title-cn">用于 Electra 媒体播放器的 D3D12 硬件加速视频解码插件 · 在 Direct3D 12 视频下使用 GPU 供应商提供的加速</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/D3D12VideoDecodersElectra/D3D12VideoDecodersElectra.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">在 Direct3D 12 视频下使用 GPU 供应商提供的加速器</div><div class="lang-content">Uses GPU vendor provided accelerators under Direct3D 12 Video</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：在 Direct3D 12 视频下使用 GPU 供应商提供的加速器</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：D3D12VideoDecodersElectra。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Uses GPU vendor provided accelerators under Direct3D 12 Video</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: D3D12VideoDecodersElectra. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>同时启用 <code class="usage-code">Electra Player</code> 与 <code class="usage-code">D3D12 Hardware accelerated video decoding plugin for the Electra media player</code>（模块 <code class="usage-code">D3D12VideoDecodersElectra</code>）。</li><li>在 <code class="usage-code">Project Settings &gt; Engine &gt; Rendering</code> 把 Default RHI 设为 <code class="usage-code">DirectX 12</code>；该解码器走 D3D12 Video，D3D11/Vulkan 不会走这条路径。</li><li>导入或指向 H.264/H.265 等 GPU 可硬解的封装，创建 <code class="usage-code">File Media Source</code>（或 Stream Media Source）和 <code class="usage-code">Media Player</code>，Player 选 Electra 而非 WMF。</li><li>把 <code class="usage-code">Media Texture</code> 接到材质或 <code class="usage-code">Media Plate</code>，蓝图调用 <code class="usage-code">Open Source</code> → <code class="usage-code">Play</code>。</li><li>看 Output Log 是否出现 <code class="usage-code">D3D12VideoDecodersElectra</code> 硬件解码成功；若回落到软件解码，检查 GPU 驱动、编解码器配置文件和 DXGI 适配器。</li><li>打包 Windows D3D12 目标时保留该插件；不要把它当独立 Media Component 加到 Actor 上。</li></ol><p class="usage-note">Electra 的 D3D12 硬解后端，不是新的播放器 UI。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable both <code class="usage-code">Electra Player</code> and <code class="usage-code">D3D12 Hardware accelerated video decoding plugin for the Electra media player</code> (module <code class="usage-code">D3D12VideoDecodersElectra</code>).</li><li>Set Default RHI to <code class="usage-code">DirectX 12</code> in <code class="usage-code">Project Settings &gt; Engine &gt; Rendering</code>; this decoder uses D3D12 Video and will not run on D3D11/Vulkan.</li><li>Point a <code class="usage-code">File Media Source</code> (or stream source) at an H.264/H.265 file the GPU can decode, create a <code class="usage-code">Media Player</code>, and select Electra rather than WMF.</li><li>Assign the <code class="usage-code">Media Texture</code> to a material or <code class="usage-code">Media Plate</code> and Blueprint <code class="usage-code">Open Source</code> → <code class="usage-code">Play</code>.</li><li>Confirm <code class="usage-code">D3D12VideoDecodersElectra</code> hardware decode in the Output Log; if it falls back to software, check the GPU driver, codec profile, and DXGI adapter.</li><li>Keep the plugin on Windows D3D12 packaged targets. Do not add it as a Media Component on an actor.</li></ol><p class="usage-note">Electra’s D3D12 hardware-decode backend, not a new player UI.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">D3D12VideoDecodersElectra</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/D3D12VideoDecodersElectra/D3D12VideoDecodersElectra.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
