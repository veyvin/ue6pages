---
layout: default
title: 可变数据流扩展 / Mutable Dataflow Extensions
---

<h1>可变数据流扩展 / Mutable Dataflow Extensions</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/MutableDataflow/MutableDataflow.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MutableDataflowEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Mutable Dataflow Extensions</code>（模块 <code class="usage-code">MutableDataflowEditor</code>）。</li><li>它为 Mutable 添加在 Dataflow 插件里使用 Dataflow 对象的能力；注意其节点均为实验性，未来可能变更/弃用。</li><li>在 Dataflow 图里用 Mutable 节点（目前能力有限、需手动操作）。</li><li>Experimental：接口可能变动；属 Mutable + Dataflow 集成。</li></ol><p class="usage-note">Mutable 在 Dataflow 中处理对象的扩展（节点实验性、能力有限）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Mutable Dataflow Extensions</code> (module <code class="usage-code">MutableDataflowEditor</code>).</li><li>It adds Mutable functionality to work with Dataflow objects from the Dataflow plugin; note all its nodes are experimental and may change/be deprecated.</li><li>Use Mutable nodes in Dataflow graphs (currently limited and manual).</li><li>Experimental: contract may change; it is Mutable + Dataflow integration.</li></ol><p class="usage-note">Mutable + Dataflow object extensions (experimental nodes, limited).</p></div></div></div>
    </div>

