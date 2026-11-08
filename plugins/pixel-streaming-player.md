---
layout: default
title: 像素流媒体播放器 / Pixel Streaming Player
---

<h1>像素流媒体播放器 / Pixel Streaming Player</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/PixelStreamingPlayer/PixelStreamingPlayer.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">图形</div><div class="lang-content">Graphics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">PixelStreamingPlayer, PixelStreamingPlayerEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Pixel Streaming Player</code>（运行时 <code class="usage-code">PixelStreamingPlayer</code>，编辑器 <code class="usage-code">PixelStreamingPlayerEditor</code>）。</li><li>它在引擎内作为 Pixel Streaming 的播放端，接收远端 WebRTC 画面。</li><li>用于在编辑器/关卡里预览或嵌入一路 Pixel Streaming 流。</li><li>属实验性播放端；需配合 Pixel Streaming 信令。</li></ol><p class="usage-note">引擎内的 Pixel Streaming 播放端（收 WebRTC 画面）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Pixel Streaming Player</code> (runtime <code class="usage-code">PixelStreamingPlayer</code>, editor <code class="usage-code">PixelStreamingPlayerEditor</code>).</li><li>It is an in-engine Pixel Streaming playback client that receives a remote WebRTC video stream.</li><li>Use it to preview or embed a Pixel Streaming feed inside the editor/level.</li><li>It is an experimental player; requires Pixel Streaming signaling.</li></ol><p class="usage-note">In-engine Pixel Streaming player (receives WebRTC video).</p></div></div></div>
    </div>

