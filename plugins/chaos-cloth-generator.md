---
layout: default
title: 混沌布料发生器 / Chaos Cloth Generator
---

<h1>混沌布料发生器 / Chaos Cloth Generator</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/MLDeformer/ChaosClothGenerator/ChaosClothGenerator.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChaosClothGenerator</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Chaos Cloth Generator</code>，用于从网格/面板生成布料资产，而不是手绘每一条约束。</li><li>在 Cloth / Dataflow 相关编辑器里跑 Generator 节点或命令，输入服装网格，输出 Cloth Asset。</li><li>检查生成的碰撞与约束，再挂到角色上模拟。</li><li>这是制作管线工具，不要当运行时布料求解器依赖。</li></ol><p class="usage-note">生成器，不是 PIE 里驱动布料的那个 Chaos Cloth 运行时。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Chaos Cloth Generator</code> to build cloth assets from meshes/panels instead of authoring every constraint by hand.</li><li>Run its generator node or command in the Cloth / Dataflow editor: mesh in, Cloth Asset out.</li><li>Inspect generated collision and constraints, then simulate on the character.</li><li>Pipeline tool only; do not treat it as the runtime cloth solver.</li></ol><p class="usage-note">A generator, not the Chaos Cloth runtime that ticks in PIE.</p></div></div></div>
    </div>

