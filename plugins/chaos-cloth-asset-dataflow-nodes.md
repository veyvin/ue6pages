---
layout: default
title: 混沌布料资产数据流节点 / Chaos Cloth Asset Dataflow Nodes
---

<h1>混沌布料资产数据流节点 / Chaos Cloth Asset Dataflow Nodes</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/ChaosClothAssetDataflowNodes/ChaosClothAssetDataflowNodes.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChaosClothAssetDataflowNodes</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在已启用 Chaos Cloth Asset 的前提下启用 <code class="usage-code">Chaos Cloth Asset Dataflow Nodes</code>（<code class="usage-code">ChaosClothAssetDataflowNodes</code>）。</li><li>打开 Cloth Asset 的 Dataflow 图，从节点面板加入该插件提供的布料数据流节点（导入、约束、碰撞代理等）。</li><li>编译 Dataflow 后，把结果接到 Cloth Asset 再赋给骨架网格的 Clothing。</li><li>游戏运行时不要直接依赖这个节点模块；它服务于资产构建图。</li></ol><p class="usage-note">给 Cloth Asset Dataflow 用的节点包，不是旧版 Clothing 工具栏。</p></div><div class="lang-content"><ol class="usage-steps"><li>With Chaos Cloth Asset enabled, enable <code class="usage-code">Chaos Cloth Asset Dataflow Nodes</code> (<code class="usage-code">ChaosClothAssetDataflowNodes</code>).</li><li>Open the Cloth Asset Dataflow graph and add this plugin’s cloth nodes (import, constraints, collision proxies).</li><li>Compile the graph, then assign the Cloth Asset to the skeletal mesh clothing slot.</li><li>Do not depend on this node module at game runtime; it is for the asset build graph.</li></ol><p class="usage-note">Dataflow nodes for Cloth Asset authoring, not the legacy Clothing toolbar.</p></div></div></div>
    </div>

