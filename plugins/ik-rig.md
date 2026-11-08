---
layout: default
title: 我的装备 / IK Rig
---

<h1>我的装备 / IK Rig</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/IKRig/IKRig.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">IKRig, IKRigDeveloper, IKRigEditor, IKRigUAF</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">IK Rig</code>（运行时 <code class="usage-code">IKRig</code>，编辑器 <code class="usage-code">IKRigEditor</code>、<code class="usage-code">IKRigDeveloper</code>，另有 <code class="usage-code">IKRigUAF</code>）。</li><li>创建 IK Rig 资产，定义骨骼链、IK Goal 与 Retarget 设置。</li><li>用 IK Retargeter 在角色间重定向动画，或运行时通过 IK Rig 节点求解（如 Full Body IK）。</li><li>Game 模块依赖 <code class="usage-code">IKRig</code>；<code class="usage-code">IKRigEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">IK Rig 与动画重定向的基础资产与求解，常与 Control Rig/Full Body IK 搭配。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">IK Rig</code> (runtime <code class="usage-code">IKRig</code>, editor <code class="usage-code">IKRigEditor</code>, <code class="usage-code">IKRigDeveloper</code>, plus <code class="usage-code">IKRigUAF</code>).</li><li>Create an IK Rig asset defining bone chains, IK goals, and retarget settings.</li><li>Use an IK Retargeter to retarget animation across characters, or solve at runtime via IK Rig nodes (e.g. Full Body IK).</li><li>Game modules depend on <code class="usage-code">IKRig</code>; <code class="usage-code">IKRigEditor</code> is Editor-target only.</li></ol><p class="usage-note">The IK Rig and retargeting base assets/solver, often used with Control Rig / Full Body IK.</p></div></div></div>
    </div>

