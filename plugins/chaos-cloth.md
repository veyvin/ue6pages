---
layout: default
title: 混沌布 / Chaos Cloth
---

<h1>混沌布 / Chaos Cloth</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/ChaosCloth/ChaosCloth.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChaosCloth, ChaosClothEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Chaos Cloth</code> 作为角色服装的运行时求解。</li><li>骨架网格使用 Cloth Asset（或仍支持的 Clothing 数据），确认项目物理是 Chaos。</li><li>PIE 里播放动画，看裙摆/外套；过硬或穿插时回到 Cloth Asset 调阻尼、碰撞半径、约束。</li><li>需要编辑器工具时再开 Cloth Asset Editor；本插件负责运行时模拟。</li></ol><p class="usage-note">运行时 Chaos 布料求解，需搭配 Cloth Asset 才有可调资产。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Chaos Cloth</code> as the runtime solver for character garments.</li><li>Put a Cloth Asset (or supported Clothing data) on the skeletal mesh and confirm the project uses Chaos physics.</li><li>PIE an animation; if cloth is stiff or clips, tweak damping, collision radius, and constraints on the asset.</li><li>Turn on the Cloth Asset editor plugins for authoring; this plugin is the runtime sim.</li></ol><p class="usage-note">Runtime Chaos cloth; authoring lives in the Cloth Asset editor plugins.</p></div></div></div>
    </div>

