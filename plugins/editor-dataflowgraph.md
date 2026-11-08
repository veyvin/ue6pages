---
layout: default
title: 编辑数据流图 / Editor DataflowGraph
---

<h1>编辑数据流图 / Editor DataflowGraph</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Dataflow/Dataflow.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编辑</div><div class="lang-content">Editor</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DataflowEditor, DataflowEnginePlugin, DataflowNodes</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Dataflow</code> 插件并重启；在内容浏览器右键新建 Dataflow 资产，或从几何集合的 Dataflow 入口进入。</li><li>在 Dataflow 编辑器节点面板拖入输入节点（几何 / Actor 输入），建立图的起点。</li><li>用 <code class="usage-code">DataflowNodes</code> 里的处理节点（采样、变换、生成）按「输入→处理→输出」连线成链。</li><li>选中输出节点点 <code class="usage-code">Evaluate</code>（或 Re-evaluate），在视口查看生成或变形结果。</li><li>把这张图绑定到目标资产，改参数后重新求值。</li><li>在编辑器预览确认运行时模块 <code class="usage-code">DataflowEnginePlugin</code> 也能重算结果。</li></ol><p class="usage-note">`DataflowEditor` 只在编辑器侧；运行时重算由 `DataflowEnginePlugin` 与 `DataflowNodes` 承担，别把编辑器模块加进 Game Target。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the <code class="usage-code">Dataflow</code> plugin and restart; right-click in the Content Browser to create a Dataflow asset, or enter from a Geometry Collection&#x27;s Dataflow entry.</li><li>In the Dataflow editor, drag an input node (geometry / Actor input) from the palette to seed the graph.</li><li>Wire <code class="usage-code">DataflowNodes</code> processing nodes (sample, transform, generate) into an input → process → output chain.</li><li>Select the output node and click <code class="usage-code">Evaluate</code> (or Re-evaluate) to see the generated or deformed result in the viewport.</li><li>Bind the graph to the target asset and re-evaluate after changing parameters.</li><li>Preview in the editor to confirm the runtime module <code class="usage-code">DataflowEnginePlugin</code> recomputes the result too.</li></ol><p class="usage-note">`DataflowEditor` is editor-only; runtime recompute comes from `DataflowEnginePlugin` and `DataflowNodes` — never put the editor module in a Game target.</p></div></div></div>
    </div>

