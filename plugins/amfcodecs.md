---
layout: default
title: AMF编解码器 / AMFCodecs
---

<h1>AMF编解码器 / AMFCodecs</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/AVCodecs/AMFCodecs/AMFCodecs.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编解码器</div><div class="lang-content">Codecs</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">AMFCodecs, AMFCodecsRHI</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 AMD GPU 机器上启用 Experimental <code class="usage-code">AMFCodecs</code>（<code class="usage-code">AMFCodecs</code>、<code class="usage-code">AMFCodecsRHI</code>），它把 AMD Advanced Media Framework 编解码器挂进 <code class="usage-code">AVCodecs</code>。</li><li>同时启用使用 AVCodecs 的上层功能（例如 Pixel Streaming / 视频编码路径），不要新建 Actor 组件。</li><li>在 Pixel Streaming 或编码器设置里选择硬件编码器，确认走 AMF 而不是 NVENC/软件 x264。</li><li>C++ 不要直接依赖第三方 <code class="usage-code">Amf</code> Build.cs；编码会话由 <code class="usage-code">AMFCodecs</code> / <code class="usage-code">AMFCodecsRHI</code> 对接 RHI 纹理。</li><li>无 AMD 驱动或非 Windows 时编码器不会出现；不要把本插件当 Media Player。</li></ol><p class="usage-note">Experimental 的 AMF 硬件编解码后端，供 AVCodecs 消费者使用，不是关卡媒体源。</p></div><div class="lang-content"><ol class="usage-steps"><li>On an AMD GPU machine, enable Experimental <code class="usage-code">AMFCodecs</code> (<code class="usage-code">AMFCodecs</code>, <code class="usage-code">AMFCodecsRHI</code>) so AMF codecs register with <code class="usage-code">AVCodecs</code>.</li><li>Enable an AVCodecs consumer such as Pixel Streaming / a video encode path; do not add an actor component.</li><li>In Pixel Streaming or encoder settings pick the hardware encoder and confirm AMF, not NVENC or software x264.</li><li>Do not depend on the third-party <code class="usage-code">Amf</code> module from game code; encode sessions go through <code class="usage-code">AMFCodecs</code> / <code class="usage-code">AMFCodecsRHI</code> into RHI textures.</li><li>The encoder is absent without AMD drivers or off Windows; this is not a Media Player.</li></ol><p class="usage-note">Experimental AMF hardware codec backend for AVCodecs consumers, not a level media source.</p></div></div></div>
    </div>

