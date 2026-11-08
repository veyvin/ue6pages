---
layout: default
title: 发动机摄像机 / Engine Cameras
---

<h1>发动机摄像机 / Engine Cameras</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Cameras/EngineCameras/EngineCameras.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">相机</div><div class="lang-content">Cameras</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">EngineCameras</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Engine Cameras</code>，它提供引擎自带的默认相机抖动和相机动画资产。</li><li>做受击/爆炸抖屏时，调用 <code class="usage-code">PlayerCameraManager</code> 的 <code class="usage-code">StartCameraShake</code>，传入该插件提供的默认相机抖动类（或其子类）。</li><li>做运镜动画时，在 <code class="usage-code">Level Sequence</code> 里加 <code class="usage-code">Camera Cut</code> 轨道与相机动画轨道，选用默认相机动画资产。</li><li>停止或切换用 <code class="usage-code">StopCameraShake</code>，或反向播放相机动画。</li><li>要自定义就继承默认抖动/动画资产改参数，别直接改引擎资产。</li></ol><p class="usage-note">这些是模板级默认资源，适合快速搭手感；正式项目一般基于它们派生自己的抖动/动画资产。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Engine Cameras</code>; it ships the engine&#x27;s default camera shakes and camera animation assets.</li><li>For hit/explosion shake, call <code class="usage-code">StartCameraShake</code> on the <code class="usage-code">PlayerCameraManager</code> with the plugin&#x27;s default shake class (or a subclass).</li><li>For cinematic moves, add a <code class="usage-code">Camera Cut</code> track plus a camera animation track in a <code class="usage-code">Level Sequence</code> and pick a default camera animation asset.</li><li>Stop or switch with <code class="usage-code">StopCameraShake</code>, or play the camera animation back.</li><li>To customize, subclass the default shake/animation assets and tweak parameters instead of editing engine assets in place.</li></ol><p class="usage-note">These are template-level defaults for quick feel; shipping projects usually derive their own shake/animation assets from them.</p></div></div></div>
    </div>

