---
layout: default
title: 基因拼接器插件 / GeneSplicer Plugin
---

<h1>基因拼接器插件 / GeneSplicer Plugin</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/GeneSplicer/GeneSplicer.uplugin</code></span></li><li><span class="label">版本</span><span class="value">10.1.3</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GeneSplicerLib, GeneSplicerLibTest, GeneSplicerModule</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">GeneSplicer Plugin</code>（模块 <code class="usage-code">GeneSplicerLib</code>、<code class="usage-code">GeneSplicerModule</code>，测试模块 <code class="usage-code">GeneSplicerLibTest</code>）。</li><li>用于面部动画：准备 GeneSplicer 相关数据/绑定，在面部动画管线里接入该插件。</li><li>把 GeneSplicer 输出的面部驱动接到骨架/动画蓝图，PIE 看面部表情是否正确。</li><li>运行时依赖 <code class="usage-code">GeneSplicerLib</code> / <code class="usage-code">GeneSplicerModule</code>；测试模块不要进游戏包。</li></ol><p class="usage-note">面部动画专用的 GeneSplicer 插件，不是通用骨骼动画系统。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">GeneSplicer Plugin</code> (modules <code class="usage-code">GeneSplicerLib</code>, <code class="usage-code">GeneSplicerModule</code>; test module <code class="usage-code">GeneSplicerLibTest</code>).</li><li>For facial animation, prepare the GeneSplicer data/rig and hook the plugin into the facial animation pipeline.</li><li>Feed GeneSplicer output into the skeleton/AnimBP and PIE to verify facial expressions.</li><li>Runtime depends on <code class="usage-code">GeneSplicerLib</code> / <code class="usage-code">GeneSplicerModule</code>; keep the test module out of the cooked game.</li></ol><p class="usage-note">A GeneSplicer plugin for facial animation, not a general skeletal animation system.</p></div></div></div>
    </div>

