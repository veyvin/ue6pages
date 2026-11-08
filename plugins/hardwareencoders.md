---
layout: default
title: 硬件编码器 / HardwareEncoders
---

<h1>硬件编码器 / HardwareEncoders</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Media/HardwareEncoders/HardwareEncoders.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.2</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编码器</div><div class="lang-content">Encoders</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">EncoderAMF, EncoderNVENC</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">HardwareEncoders</code>（模块 <code class="usage-code">EncoderAMF</code>、<code class="usage-code">EncoderNVENC</code>），为 AVEncoder 提供硬件编码。</li><li>在需要录制/推流的流程里（如 Media Output / 渲染出片），选择硬件编码器。</li><li>按显卡选 AMF（AMD）或 NVENC（NVIDIA），确认驱动支持。</li><li>运行时模块按平台/显卡启用；缺少对应硬件时回退到软件编码。</li></ol><p class="usage-note">AVEncoder 的硬件编码后端（AMF/NVENC），用于录制/出片。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">HardwareEncoders</code> (modules <code class="usage-code">EncoderAMF</code>, <code class="usage-code">EncoderNVENC</code>) to add hardware encoding to AVEncoder.</li><li>In recording/streaming flows (e.g. Media Output / render-out), select a hardware encoder.</li><li>Pick AMF (AMD) or NVENC (NVIDIA) per GPU and confirm driver support.</li><li>Runtime modules enable per platform/GPU; fall back to software encoding when the hardware is absent.</li></ol><p class="usage-note">Hardware encoder backends (AMF/NVENC) for AVEncoder, used for recording/render-out.</p></div></div></div>
    </div>

