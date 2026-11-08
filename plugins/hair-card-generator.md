---
layout: default
title: 发卡生成器 / Hair Card Generator
---

<h1>发卡生成器 / Hair Card Generator</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/HairCardGenerator/HairCardGenerator.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">几何学</div><div class="lang-content">Geometry</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">HairCardGeneratorEditor, HairCardGeneratorDataflow</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Hair Card Generator</code>（模块 <code class="usage-code">HairCardGeneratorEditor</code>、<code class="usage-code">HairCardGeneratorDataflow</code>）。</li><li>在 Dataflow 或编辑工具里，从发丝（strands）程序化生成发卡（hair cards）。</li><li>检查生成发卡的数量、朝向与材质，再交给 Groom 渲染。</li><li>这是制作期生成工具（编辑器侧）；Experimental，接口可能变动。</li></ol><p class="usage-note">从发丝生成发卡的程序化工具，编辑器侧，不是运行时。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Hair Card Generator</code> (modules <code class="usage-code">HairCardGeneratorEditor</code>, <code class="usage-code">HairCardGeneratorDataflow</code>).</li><li>In Dataflow or the editor tools, procedurally generate hair cards from strands.</li><li>Inspect generated card count, orientation, and materials, then render them via Groom.</li><li>It is an authoring-time generator (editor-side); Experimental with a contract that may change.</li></ol><p class="usage-note">A procedural strands-to-cards tool, editor-side, not runtime.</p></div></div></div>
    </div>

