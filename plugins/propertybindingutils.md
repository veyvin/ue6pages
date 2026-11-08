---
layout: default
title: 属性绑定实用程序 / PropertyBindingUtils
---

<h1>属性绑定实用程序 / PropertyBindingUtils</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Runtime/PropertyBindingUtils/PropertyBindingUtils.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">游戏玩法</div><div class="lang-content">Gameplay</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">PropertyBindingUtils, PropertyBindingUtilsEditor, PropertyBindingUtilsTestSuite</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">PropertyBindingUtils</code>（模块 <code class="usage-code">PropertyBindingUtils</code>、<code class="usage-code">PropertyBindingUtilsEditor</code>、<code class="usage-code">PropertyBindingUtilsTestSuite</code>）。</li><li>它提供实现属性绑定的实用代码。</li><li>写自定义绑定/动画通路时依赖这些工具，而不是从零实现路径解析。</li><li>运行时模块可进游戏包；编辑器/测试模块只进对应 Target。</li></ol><p class="usage-note">实现属性绑定的实用代码。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">PropertyBindingUtils</code> (modules <code class="usage-code">PropertyBindingUtils</code>, <code class="usage-code">PropertyBindingUtilsEditor</code>, <code class="usage-code">PropertyBindingUtilsTestSuite</code>).</li><li>It provides utility code for implementing property bindings.</li><li>Depend on these utils when writing custom binding/anim access instead of parsing paths from scratch.</li><li>Runtime modules can ship in a cooked game; editor/test modules go to matching targets only.</li></ol><p class="usage-note">Utility code for implementing property bindings.</p></div></div></div>
    </div>

