---
layout: default
title: 几何数据流节点 / Geometry Dataflow Nodes
---

<h1>几何数据流节点 / Geometry Dataflow Nodes</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/GeometryDataflow/GeometryDataflow.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">几何学</div><div class="lang-content">Geometry</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GeometryDataflowNodes, DataflowMedialSkeleton</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Geometry Dataflow Nodes</code>（模块 <code class="usage-code">GeometryDataflowNodes</code>、<code class="usage-code">DataflowMedialSkeleton</code>）。</li><li>在 Dataflow 图里加入这些几何处理节点，对网格做生成/变形/处理。</li><li>编译 Dataflow 图，把结果输出到目标资产（如网格、骨架等）。</li><li>Experimental：节点接口可能变动；它是 Dataflow 图里的几何节点包。</li></ol><p class="usage-note">Dataflow 里的几何处理节点，不是运行时几何库。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Geometry Dataflow Nodes</code> (modules <code class="usage-code">GeometryDataflowNodes</code>, <code class="usage-code">DataflowMedialSkeleton</code>).</li><li>Add these geometry-processing nodes into a Dataflow graph to generate/deform/process meshes.</li><li>Compile the Dataflow graph and output the result to the target asset (mesh, skeleton, etc.).</li><li>Experimental: node contracts may change; it is a geometry node pack for Dataflow graphs.</li></ol><p class="usage-note">Geometry-processing nodes inside Dataflow, not a runtime geometry library.</p></div></div></div>
    </div>

