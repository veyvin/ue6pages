---
layout: default
title: 混沌血肉生成器 / Chaos Flesh Generator
---

<h1>混沌血肉生成器 / Chaos Flesh Generator</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/MLDeformer/ChaosFleshGenerator/ChaosFleshGenerator.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChaosFleshGenerator</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Chaos Flesh Generator</code>，用来从封闭三角网格生成四面体 Flesh 资产。</li><li>在 Flesh / Dataflow 工具里选网格，跑四面体化与绑定，输出 Flesh Asset。</li><li>把生成结果交给 <code class="usage-code">Chaos Flesh</code> 运行时，挂到角色或缓存网格上模拟。</li><li>生成失败时先检查网格是否封闭、法线是否统一，而不是去改 Chaos 场景重力。</li></ol><p class="usage-note">四面体生成器，不是 PIE 里的软体求解循环。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Chaos Flesh Generator</code> to tet-mesh a closed triangle mesh into a Flesh asset.</li><li>In the Flesh / Dataflow tools, pick the mesh, tetrahedralize and bind, and save a Flesh Asset.</li><li>Simulate it with the <code class="usage-code">Chaos Flesh</code> runtime on a character or cached mesh.</li><li>If generation fails, fix watertightness and normals before touching world gravity.</li></ol><p class="usage-note">Tetrahedralizer, not the soft-body tick in PIE.</p></div></div></div>
    </div>

