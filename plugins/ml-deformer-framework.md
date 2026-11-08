---
layout: default
title: ML变形器框架 / ML Deformer Framework
---

<h1>ML变形器框架 / ML Deformer Framework</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/MLDeformer/MLDeformerFramework/MLDeformerFramework.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MLDeformerFramework, MLDeformerFrameworkEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">ML Deformer Framework</code>（运行时 <code class="usage-code">MLDeformerFramework</code>，编辑器 <code class="usage-code">MLDeformerFrameworkEditor</code>）。</li><li>它是机器学习网格变形器框架：用训练模型驱动骨骼网格的变形细节。</li><li>创建 ML Deformer 资产、选模型、训练并应用到角色，PIE 验证变形。</li><li>Game 模块依赖 <code class="usage-code">MLDeformerFramework</code>；<code class="usage-code">MLDeformerFrameworkEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">机器学习网格变形器框架（基础），模型是可插拔的。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">ML Deformer Framework</code> (runtime <code class="usage-code">MLDeformerFramework</code>, editor <code class="usage-code">MLDeformerFrameworkEditor</code>).</li><li>It is the machine-learning mesh deformer framework: trained models drive skeletal mesh deformation detail.</li><li>Create an ML Deformer asset, pick a model, train, apply to the character, and verify in PIE.</li><li>Game modules depend on <code class="usage-code">MLDeformerFramework</code>; <code class="usage-code">MLDeformerFrameworkEditor</code> is Editor-target only.</li></ol><p class="usage-note">The ML mesh deformer framework (base); models are pluggable.</p></div></div></div>
    </div>

