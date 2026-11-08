---
layout: default
title: ML Deformer 细节姿势模型 / ML Deformer Detail Pose Model
---

<h1>ML Deformer 细节姿势模型 / ML Deformer Detail Pose Model</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Animation/MLDeformer/DetailPoseModel/DetailPoseModel.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DetailPoseModel, DetailPoseModelEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">ML Deformer Detail Pose Model</code>（运行时 <code class="usage-code">DetailPoseModel</code>，编辑器 <code class="usage-code">DetailPoseModelEditor</code>）。</li><li>它是 ML Deformer 框架的“详细姿势模型”，提高变形精度。</li><li>在 ML Deformer 资产里选择 Detail Pose Model，训练后驱动网格变形。</li><li>Experimental：接口可能变动；<code class="usage-code">DetailPoseModelEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">ML Deformer 的详细姿势模型（提高精度），替代最近邻模型。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">ML Deformer Detail Pose Model</code> (runtime <code class="usage-code">DetailPoseModel</code>, editor <code class="usage-code">DetailPoseModelEditor</code>).</li><li>It is the Detail Pose Model for the ML Deformer framework, improving deformation accuracy.</li><li>Select Detail Pose Model in an ML Deformer asset; after training, drive mesh deformation.</li><li>Experimental: contract may change; <code class="usage-code">DetailPoseModelEditor</code> is Editor-target only.</li></ol><p class="usage-note">The ML Deformer Detail Pose Model (higher accuracy), replacing the nearest-neighbor model.</p></div></div></div>
    </div>

