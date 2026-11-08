---
layout: default
title: 像素流 / Pixel Streaming
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">P</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Pixel Streaming</div>
      <div class="hero-title-cn">像素流 · 将虚幻引擎音频流式传输并渲染到 WebRTC 兼容的媒体播放器（</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Graphics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">7</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/PixelStreaming/PixelStreaming.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">将虚幻引擎音频流式传输并渲染到 WebRTC 兼容的媒体播放器（例如 Web 浏览器）。</div><div class="lang-content">Streaming of Unreal Engine audio and rendering to WebRTC-compatible media players such as a web browsers.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Pixel Streaming 把引擎画面通过 WebRTC 推到浏览器：云端或本机跑游戏，薄客户端只显示与输入。用于云游戏、可视化审阅、远程演示。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：PixelStreaming, PixelStreamingServers, PixelStreamingEditor, PixelStreamingBlueprint, PixelStreamingBlueprintEditor, PixelStreamingHMD, PixelStreamingInput。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-streaming-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-streaming-in-unreal-engine</a></p></div><div class="lang-content"><p>Pixel Streaming sends the engine frame buffer to a browser over WebRTC so the game runs in the cloud or on a host while a thin client only shows video and sends input. Used for cloud gaming, reviews, and remote demos.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: PixelStreaming, PixelStreamingServers, PixelStreamingEditor, PixelStreamingBlueprint, PixelStreamingBlueprintEditor, PixelStreamingHMD, PixelStreamingInput. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-streaming-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-streaming-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Pixel Streaming</code>（模块 <code class="usage-code">PixelStreaming</code>、<code class="usage-code">PixelStreamingServers</code>、<code class="usage-code">PixelStreamingEditor</code>、<code class="usage-code">PixelStreamingBlueprint</code>、<code class="usage-code">PixelStreamingBlueprintEditor</code>、<code class="usage-code">PixelStreamingHMD</code>、<code class="usage-code">PixelStreamingInput</code>）。</li><li>它把引擎音频与画面通过 WebRTC 推到浏览器等兼容播放器（第一代 Pixel Streaming）。</li><li>配置信令服务器，启动推流，用浏览器当薄客户端显示并回传输入。</li><li>新项目可评估 <code class="usage-code">Pixel Streaming 2</code>；本插件仍用于既有云游戏/远程审阅流程。</li></ol><p class="usage-note">第一代 Pixel Streaming：WebRTC 推送引擎音视频到浏览器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Pixel Streaming</code> (modules <code class="usage-code">PixelStreaming</code>, <code class="usage-code">PixelStreamingServers</code>, <code class="usage-code">PixelStreamingEditor</code>, <code class="usage-code">PixelStreamingBlueprint</code>, <code class="usage-code">PixelStreamingBlueprintEditor</code>, <code class="usage-code">PixelStreamingHMD</code>, <code class="usage-code">PixelStreamingInput</code>).</li><li>It streams engine audio and frames over WebRTC to compatible players such as a browser (first-gen Pixel Streaming).</li><li>Configure a signaling server, start streaming, and use a browser as a thin client for video plus input.</li><li>New projects may evaluate <code class="usage-code">Pixel Streaming 2</code>; this plugin still covers existing cloud-gaming/remote-review flows.</li></ol><p class="usage-note">First-gen Pixel Streaming: WebRTC of engine audio/video to browsers.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (7)</div><div class="module-item"><span class="dot"></span><span class="name mono">PixelStreaming</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PixelStreamingServers</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PixelStreamingEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PixelStreamingBlueprint</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PixelStreamingBlueprintEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PixelStreamingHMD</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PixelStreamingInput</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/PixelStreaming/PixelStreaming.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
