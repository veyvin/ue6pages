---
layout: default
title: NNER运行时RDG / NNERuntimeRDG
---

<h1>NNER运行时RDG / NNERuntimeRDG</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/NNERuntimeRDG/NNERuntimeRDG.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">机器学习</div><div class="lang-content">ML</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">NNEHlslShaders, NNERuntimeRDG, NNERuntimeRDGData, NNERuntimeRDGUtils</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">NNERuntimeRDG</code>（模块 <code class="usage-code">NNERuntimeRDG</code>、<code class="usage-code">NNEHlslShaders</code>、<code class="usage-code">NNERuntimeRDGData</code>、<code class="usage-code">NNERuntimeRDGUtils</code>）。</li><li>它用渲染依赖图（RDG）实现 NNE API，在 GPU 上跑神经网络推理。</li><li>在需要 GPU 推理且走渲染管线的场景里选它作为 NNE 运行时。</li><li>Experimental：接口可能变动；依赖 RDG/HLSL 着色器。</li></ol><p class="usage-note">基于 RDG 的 NNE GPU 运行时，实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">NNERuntimeRDG</code> (modules <code class="usage-code">NNERuntimeRDG</code>, <code class="usage-code">NNEHlslShaders</code>, <code class="usage-code">NNERuntimeRDGData</code>, <code class="usage-code">NNERuntimeRDGUtils</code>).</li><li>It implements the NNE API using the Render Dependency Graph (RDG) to run neural-network inference on the GPU.</li><li>Pick it as the NNE runtime for GPU inference through the render pipeline.</li><li>Experimental: contract may change; relies on RDG/HLSL shaders.</li></ol><p class="usage-note">An RDG-based NNE GPU runtime, experimental.</p></div></div></div>
    </div>

