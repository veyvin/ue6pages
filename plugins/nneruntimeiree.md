---
layout: default
title: NNER运行时IREE / NNERuntimeIREE
---

<h1>NNER运行时IREE / NNERuntimeIREE</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/NNERuntimeIREE/NNERuntimeIREE.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">机器学习</div><div class="lang-content">ML</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">IREETracing, IREEUtils, IREEDriverRDG, NNERuntimeIREE, NNERuntimeIREEEditor, NNERuntimeIREEShader</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">NNERuntimeIREE</code>（模块 <code class="usage-code">NNERuntimeIREE</code>、<code class="usage-code">IREETracing</code>、<code class="usage-code">IREEUtils</code>、<code class="usage-code">IREEDriverRDG</code>、<code class="usage-code">NNERuntimeIREEShader</code>，编辑器 <code class="usage-code">NNERuntimeIREEEditor</code>）。</li><li>它实现基于 IREE/MLIR/LLVM 的 NNE 运行时，把神经网络直接编译成游戏代码。</li><li>在需要 AOT 编译式推理/GPU 加速时选它作为 NNE 运行时。</li><li>Experimental：接口可能变动；依赖 IREE 生态。</li></ol><p class="usage-note">基于 IREE/MLIR/LLVM 的 NNE 运行时（AOT 编译推理），实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">NNERuntimeIREE</code> (modules <code class="usage-code">NNERuntimeIREE</code>, <code class="usage-code">IREETracing</code>, <code class="usage-code">IREEUtils</code>, <code class="usage-code">IREEDriverRDG</code>, <code class="usage-code">NNERuntimeIREEShader</code>, editor <code class="usage-code">NNERuntimeIREEEditor</code>).</li><li>It implements an NNE runtime on IREE/MLIR/LLVM, compiling neural networks directly into game code.</li><li>Pick it as the NNE runtime when you need AOT-compiled inference/GPU acceleration.</li><li>Experimental: contract may change; depends on the IREE ecosystem.</li></ol><p class="usage-note">An IREE/MLIR/LLVM-based NNE runtime (AOT-compiled inference), experimental.</p></div></div></div>
    </div>

