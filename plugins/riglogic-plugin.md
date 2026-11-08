---
layout: default
title: RigLogic 插件 / RigLogic Plugin
---

<h1>RigLogic 插件 / RigLogic Plugin</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/RigLogic/RigLogic.uplugin</code></span></li><li><span class="label">版本</span><span class="value">13.2.5</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">RigLogicLib, RigLogicLibTest, RigLogicModule, RigLogicDeveloper, RigLogicEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">RigLogic Plugin</code>（模块 <code class="usage-code">RigLogicLib</code>、<code class="usage-code">RigLogicLibTest</code>、<code class="usage-code">RigLogicModule</code>、<code class="usage-code">RigLogicDeveloper</code>、<code class="usage-code">RigLogicEditor</code>）。</li><li>它是面部动画的 RigLogic 运行时（DNA 驱动的面部解算，常用于 MetaHuman）。</li><li>把 DNA 资产接到骨骼网格，运行时由 RigLogic 解算面部。</li><li>Game 模块依赖 <code class="usage-code">RigLogicModule</code>；编辑器/测试模块只进对应 Target。</li></ol><p class="usage-note">面部动画 RigLogic 运行时（DNA/MetaHuman）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">RigLogic Plugin</code> (modules <code class="usage-code">RigLogicLib</code>, <code class="usage-code">RigLogicLibTest</code>, <code class="usage-code">RigLogicModule</code>, <code class="usage-code">RigLogicDeveloper</code>, <code class="usage-code">RigLogicEditor</code>).</li><li>It is the RigLogic runtime for facial animation (DNA-driven face eval, commonly MetaHuman).</li><li>Attach a DNA asset to a skeletal mesh; RigLogic evaluates the face at runtime.</li><li>Game modules depend on <code class="usage-code">RigLogicModule</code>; editor/test modules go to matching targets only.</li></ol><p class="usage-note">RigLogic runtime for facial animation (DNA/MetaHuman).</p></div></div></div>
    </div>

