---
layout: default
title: NNE降噪器 / NNEDenoiser
---

<h1>NNE降噪器 / NNEDenoiser</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/NNE/NNEDenoiser/NNEDenoiser.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">去噪</div><div class="lang-content">Denoising</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">NNEDenoiser, NNEDenoiserShaders</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">NNEDenoiser</code>（模块 <code class="usage-code">NNEDenoiser</code>、<code class="usage-code">NNEDenoiserShaders</code>）。</li><li>它是基于神经网络引擎（NNE）的 Path Tracer 神经降噪器。</li><li>在 Path Tracer/离线渲染里启用 NNE 降噪，降低采样保画质。</li><li>属降噪/离线渲染工具；需 NNE 运行时配合。</li></ol><p class="usage-note">基于 NNE 的 Path Tracer 神经降噪器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">NNEDenoiser</code> (modules <code class="usage-code">NNEDenoiser</code>, <code class="usage-code">NNEDenoiserShaders</code>).</li><li>It is a neural denoiser for the Path Tracer based on the Neural Network Engine (NNE).</li><li>Enable NNE denoising in Path Tracer/offline renders to cut samples while keeping quality.</li><li>It is a denoise/offline-render tool; requires an NNE runtime.</li></ol><p class="usage-note">An NNE-based neural denoiser for the Path Tracer.</p></div></div></div>
    </div>

