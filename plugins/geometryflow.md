---
layout: default
title: 几何流 / GeometryFlow
---

<h1>几何流 / GeometryFlow</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/GeometryFlow/GeometryFlow.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">几何学</div><div class="lang-content">Geometry</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GeometryFlowCore, GeometryFlowMeshProcessing, GeometryFlowMeshProcessingEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">GeometryFlow</code>（模块 <code class="usage-code">GeometryFlowCore</code>、<code class="usage-code">GeometryFlowMeshProcessing</code>、<code class="usage-code">GeometryFlowMeshProcessingEditor</code>）。</li><li>搭建几何数据流图，对网格做流式处理（生成、变换、合并等）。</li><li>Graph 编译运行后输出网格结果；编辑器节点用 <code class="usage-code">GeometryFlowMeshProcessingEditor</code>。</li><li>Experimental：接口可能变动；核心模块可运行时用，Editor 模块只进 Editor Target。</li></ol><p class="usage-note">几何数据流图，思路类似 Dataflow 但聚焦网格流处理。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">GeometryFlow</code> (modules <code class="usage-code">GeometryFlowCore</code>, <code class="usage-code">GeometryFlowMeshProcessing</code>, <code class="usage-code">GeometryFlowMeshProcessingEditor</code>).</li><li>Build geometry dataflow graphs to stream-process meshes (generate, transform, merge, etc.).</li><li>Compile and run the graph to output mesh results; editor nodes use <code class="usage-code">GeometryFlowMeshProcessingEditor</code>.</li><li>Experimental: contract may change; core modules can run at runtime, editor modules go to Editor targets.</li></ol><p class="usage-note">A geometry dataflow graph, Dataflow-like but focused on mesh stream processing.</p></div></div></div>
    </div>

