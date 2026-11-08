---
layout: default
title: Electra 的 NVDEC 硬件解码器支持 / NVDEC hardware decoder support for Electra
---

<h1>Electra 的 NVDEC 硬件解码器支持 / NVDEC hardware decoder support for Electra</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Media/NVDECElectra/NVDECElectra.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">媒体播放器</div><div class="lang-content">Media Players</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">NVDECElectra</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">NVDEC hardware decoder support for Electra</code>（模块 <code class="usage-code">NVDECElectra</code>）。</li><li>它为 Electra 播放器加入来自 NVIDIA Media Codec SDK 的硬件解码（NVDEC）。</li><li>在 Media Player 选 Electra 后端播放视频，由 NVDEC 硬解；支持的编解码取决于 GPU。</li><li>需 D3D12 与 NVIDIA GPU；属 Media Framework 解码扩展。</li></ol><p class="usage-note">Electra 的 NVDEC 硬件解码（需 D3D12/NVIDIA GPU）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">NVDEC hardware decoder support for Electra</code> (module <code class="usage-code">NVDECElectra</code>).</li><li>It adds hardware decoding (NVDEC) from the NVIDIA Media Codec SDK to the Electra player.</li><li>Play video via a Media Player with the Electra backend, hardware-decoded by NVDEC; supported codecs depend on the GPU.</li><li>Requires D3D12 and an NVIDIA GPU; it is a Media Framework decode extension.</li></ol><p class="usage-note">NVDEC hardware decoding for Electra (needs D3D12/NVIDIA GPU).</p></div></div></div>
    </div>

