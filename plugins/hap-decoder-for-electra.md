---
layout: default
title: Electra 的 HAP 解码器 / HAP Decoder for Electra
---

<h1>Electra 的 HAP 解码器 / HAP Decoder for Electra</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Media/HAPDecoderElectra/HAPDecoderElectra.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">媒体播放器</div><div class="lang-content">Media Players</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">HAPDecoderElectra</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">HAP Decoder for Electra</code>（模块 <code class="usage-code">HAPDecoderElectra</code>），属 Media Framework / Electra。</li><li>创建 Media Source 指向 HAP 编码的视频，让 Electra 走该解码器（GPU 上解码）。</li><li>把 Media Texture 接到材质或 Media Plate 播放；核对平台是否支持 HAP。</li><li>运行时模块 <code class="usage-code">HAPDecoderElectra</code>；需要 Electra 播放器支持。</li></ol><p class="usage-note">Electra 上的 HAP 解码，HAP 是高分辨率 GPU 编解码器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">HAP Decoder for Electra</code> (module <code class="usage-code">HAPDecoderElectra</code>), part of Media Framework / Electra.</li><li>Create a Media Source pointing at an HAP-encoded video so Electra uses this decoder (GPU decode).</li><li>Feed the Media Texture to a material or Media Plate; confirm the platform supports HAP.</li><li>Runtime module is <code class="usage-code">HAPDecoderElectra</code>; it relies on the Electra player.</li></ol><p class="usage-note">HAP decode on Electra; HAP is a high-resolution GPU codec.</p></div></div></div>
    </div>

