---
layout: default
title: ML Deformer 顶点增量模型 / ML Deformer Vertex Delta Model
---

<h1>ML Deformer 顶点增量模型 / ML Deformer Vertex Delta Model</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/MLDeformer/VertexDeltaModel/VertexDeltaModel.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.3</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">VertexDeltaModel, VertexDeltaModelEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">ML Deformer Vertex Delta Model</code>（运行时 <code class="usage-code">VertexDeltaModel</code>，编辑器 <code class="usage-code">VertexDeltaModelEditor</code>）。</li><li>它是 ML Deformer 框架的“顶点增量模型”，学习逐顶点偏移来表现变形细节。</li><li>在 ML Deformer 资产里选 Vertex Delta Model，训练后应用到角色。</li><li>Game 模块依赖 <code class="usage-code">VertexDeltaModel</code>；<code class="usage-code">VertexDeltaModelEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">ML Deformer 的顶点增量模型（逐顶点偏移）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">ML Deformer Vertex Delta Model</code> (runtime <code class="usage-code">VertexDeltaModel</code>, editor <code class="usage-code">VertexDeltaModelEditor</code>).</li><li>It is the Vertex Delta Model for the ML Deformer framework, learning per-vertex offsets for deformation detail.</li><li>Select Vertex Delta Model in an ML Deformer asset, train it, and apply to the character.</li><li>Game modules depend on <code class="usage-code">VertexDeltaModel</code>; <code class="usage-code">VertexDeltaModelEditor</code> is Editor-target only.</li></ol><p class="usage-note">The ML Deformer Vertex Delta Model (per-vertex offsets).</p></div></div></div>
    </div>

