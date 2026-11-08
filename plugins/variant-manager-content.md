---
layout: default
title: 变体管理器内容 / Variant Manager Content
---

<h1>变体管理器内容 / Variant Manager Content</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Enterprise/VariantManagerContent/VariantManagerContent.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编辑</div><div class="lang-content">Editor</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">VariantManagerContent, VariantManagerContentEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Variant Manager Content</code>（运行时 <code class="usage-code">VariantManagerContent</code>，编辑器 <code class="usage-code">VariantManagerContentEditor</code>）。</li><li>它是 Variant Manager 插件的数据类与资源（变体、属性捕获的数据层）。</li><li>作为 Variant Manager 的底层数据依赖，随其启用。</li><li>Game 模块依赖运行时模块；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">Variant Manager 的数据类与资源层。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Variant Manager Content</code> (runtime <code class="usage-code">VariantManagerContent</code>, editor <code class="usage-code">VariantManagerContentEditor</code>).</li><li>It holds the data classes and assets for the Variant Manager plugin (variants, property-capture data layer).</li><li>A low-level data dependency for Variant Manager; enabled with it.</li><li>Game modules depend on runtime modules; editor modules go to Editor targets only.</li></ol><p class="usage-note">The data classes/assets layer for Variant Manager.</p></div></div></div>
    </div>

