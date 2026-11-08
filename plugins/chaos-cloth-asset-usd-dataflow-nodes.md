---
layout: default
title: Chaos Cloth 资产 USD 数据流节点 / Chaos Cloth Asset USD Dataflow Nodes
---

<h1>Chaos Cloth 资产 USD 数据流节点 / Chaos Cloth Asset USD Dataflow Nodes</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/ChaosClothAssetUsdDataflowNodes/ChaosClothAssetUsdDataflowNodes.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChaosClothAssetUsdDataflowNodes</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Chaos Cloth Asset USD Dataflow Nodes</code>（<code class="usage-code">ChaosClothAssetUsdDataflowNodes</code>）。</li><li>在 Cloth Asset Dataflow 里加入 USD 导入/导出节点，指向 <code class="usage-code">.usd</code> 服装或绑定缓存。</li><li>跑图生成或更新 Cloth Asset，再赋给骨架网格。</li><li>没有 USD 工作流就不必启用；普通布料编辑用 Cloth Asset 编辑器即可。</li></ol><p class="usage-note">只负责 Cloth Asset 图上的 USD 节点，不是通用 USD Importer。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Chaos Cloth Asset USD Dataflow Nodes</code> (<code class="usage-code">ChaosClothAssetUsdDataflowNodes</code>).</li><li>Add USD import/export nodes on the Cloth Asset Dataflow graph and point them at a <code class="usage-code">.usd</code> garment or bind cache.</li><li>Run the graph to build or refresh the Cloth Asset, then assign it to the skeletal mesh.</li><li>Skip this plugin if you are not on a USD cloth pipeline; use the Cloth Asset editor instead.</li></ol><p class="usage-note">USD nodes for Cloth Asset Dataflow, not the general USD Importer.</p></div></div></div>
    </div>

