---
layout: default
title: 直接网格控制 / Direct Mesh Control
---

<h1>直接网格控制 / Direct Mesh Control</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Animation/DirectMeshControl/DirectMeshControl.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">DirectMeshControl, DirectMeshControlRig</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Direct Mesh Control</code> 提供在视口里单击拖动、按表面选择来直接摆姿势/做动画的交互，底层基于 Control Rig。</li><li>启用后新建 <code class="usage-code">DirectMeshControl</code> 资产，或在 Control Rig 里加入 <code class="usage-code">DirectMeshControlRig</code> 相关模块。</li><li>在视口里点击网格表面选中目标区域，拖动实现推/拉/弯曲等直接变形。</li><li>把拖动产生的姿势记录进 Control Rig 关键帧或 Sequencer 片段，形成可回放的动画。</li><li>它是 Experimental：先在测试骨架网格上验证选面精度与性能，再用于正式角色。</li></ol><p class="usage-note">选面精度依赖网格密度；低模上直接拖动会跳变，必要时先提高目标区域细分。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Direct Mesh Control</code> gives viewport click-drag, surface-select posing/animation, built on Control Rig underneath.</li><li>After enabling, create a <code class="usage-code">DirectMeshControl</code> asset or add the <code class="usage-code">DirectMeshControlRig</code> modules into a Control Rig.</li><li>Click the mesh surface in the viewport to select a region, then drag to push/pull/bend directly.</li><li>Record the resulting pose into Control Rig keys or a Sequencer section to get a replayable animation.</li><li>It is Experimental: validate surface-pick precision and performance on a test skeletal mesh before using it on production characters.</li></ol><p class="usage-note">Surface-pick precision depends on mesh density; dragging on low-poly meshes jumps, so add tessellation to the target area first.</p></div></div></div>
    </div>

