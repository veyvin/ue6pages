---
layout: default
title: NV编解码器 / NVCodecs
---

<h1>NV编解码器 / NVCodecs</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/AVCodecs/NVCodecs/NVCodecs.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编解码器</div><div class="lang-content">Codecs</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">NVCodecs, NVCodecsRHI, NVDEC, NVENC</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">NVCodecs</code>（模块 <code class="usage-code">NVCodecs</code>、<code class="usage-code">NVCodecsRHI</code>、<code class="usage-code">NVDEC</code>、<code class="usage-code">NVENC</code>）。</li><li>它把 NVIDIA Media Codec SDK 的编解码器（NVDEC 解码/NVENC 编码）加入 AVCodecs。</li><li>在录制/解码流程里选 NVENC/NVDEC，享受 GPU 硬件加速。</li><li>Experimental：接口可能变动；需 NVIDIA GPU 与相应驱动。</li></ol><p class="usage-note">把 NVIDIA NVENC/NVDEC 编解码加入 AVCodecs，实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">NVCodecs</code> (modules <code class="usage-code">NVCodecs</code>, <code class="usage-code">NVCodecsRHI</code>, <code class="usage-code">NVDEC</code>, <code class="usage-code">NVENC</code>).</li><li>It adds NVIDIA Media Codec SDK codecs (NVDEC decode / NVENC encode) to AVCodecs.</li><li>Choose NVENC/NVDEC in recording/decoding flows for GPU hardware acceleration.</li><li>Experimental: contract may change; requires an NVIDIA GPU and drivers.</li></ol><p class="usage-note">Adds NVIDIA NVENC/NVDEC codecs to AVCodecs, experimental.</p></div></div></div>
    </div>

