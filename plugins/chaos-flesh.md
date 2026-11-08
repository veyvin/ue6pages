---
layout: default
title: 混沌血肉 / Chaos Flesh
---

<h1>混沌血肉 / Chaos Flesh</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/ChaosFlesh/ChaosFlesh.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChaosFlesh, ChaosFleshEngine, ChaosFleshEditor, ChaosFleshNodes, ChaosFleshDeprecatedNodes</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Chaos Flesh</code> 做四面体软体（肌肉、脂肪、可变形体）。</li><li>准备 Flesh Asset（可用 Flesh Generator），把它赋给支持的网格/组件。</li><li>PIE 中看体积保持与碰撞；过软过硬时调 Flesh 资产上的材料与约束，而不是 Niagara。</li><li>需要缓存或影视拍屏时再接 Chaos Cache；本插件是运行时软体求解。</li></ol><p class="usage-note">Chaos 软体运行时，依赖 Deformable Base；与布料（Cloth）是另一套管线。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Chaos Flesh</code> for tetrahedral soft bodies (muscle, fat, deformables).</li><li>Author a Flesh Asset (Flesh Generator helps) and assign it to a supported mesh/component.</li><li>PIE to judge volume and collision; tune material and constraints on the Flesh asset, not Niagara.</li><li>Use Chaos Cache for takes; this plugin is the runtime soft-body solve.</li></ol><p class="usage-note">Chaos soft-body runtime on Deformable Base; cloth is a separate pipeline.</p></div></div></div>
    </div>

