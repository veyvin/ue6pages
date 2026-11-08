---
layout: default
title: 空间感知重定向操作 / Spatially Aware Retarget Ops
---

<h1>空间感知重定向操作 / Spatially Aware Retarget Ops</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Animation/RelativeIKOp/RelativeIKOp.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">RelativeIKOp, RelativeBodyAnimInfo, BodyIntersectIKOp, RelativeBodyAnimUtils, PreviewPropOp, SpatialRetargetUtils, ProximityIKOp, PelvisVolumeOp, LimbTwistOp</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Spatially Aware Retarget Ops</code>（模块 <code class="usage-code">RelativeIKOp</code>、<code class="usage-code">RelativeBodyAnimInfo</code>、<code class="usage-code">BodyIntersectIKOp</code>、<code class="usage-code">SpatialRetargetUtils</code>、<code class="usage-code">ProximityIKOp</code> 等）。</li><li>它是一组重定向操作，用于在重定向动画上保留空间关系（如手与环境/物体的相对位置）。</li><li>在 IK Rig/重定向里用这些 Op 保持角色与环境的相对接触/距离。</li><li>Experimental：接口可能变动；用于高质量重定向。</li></ol><p class="usage-note">保留空间关系的重定向操作集合，实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Spatially Aware Retarget Ops</code> (modules <code class="usage-code">RelativeIKOp</code>, <code class="usage-code">RelativeBodyAnimInfo</code>, <code class="usage-code">BodyIntersectIKOp</code>, <code class="usage-code">SpatialRetargetUtils</code>, <code class="usage-code">ProximityIKOp</code>, etc.).</li><li>It is a set of retarget operations that preserve spatial relationships on retargeted animations (e.g. hand relative to environment/objects).</li><li>Use these Ops in IK Rig/retargeting to maintain relative contact/distance with the environment.</li><li>Experimental: contract may change; for high-quality retargeting.</li></ol><p class="usage-note">Retarget operations preserving spatial relationships, experimental.</p></div></div></div>
    </div>

