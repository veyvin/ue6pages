---
layout: default
title: 游戏相机 / Gameplay Cameras
---

<h1>游戏相机 / Gameplay Cameras</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Cameras/GameplayCameras/GameplayCameras.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">相机</div><div class="lang-content">Cameras</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GameplayCameras, GameplayCamerasUncookedOnly, GameplayCamerasEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Gameplay Cameras</code>（运行时 <code class="usage-code">GameplayCameras</code>，还有 <code class="usage-code">GameplayCamerasUncookedOnly</code> 与编辑器 <code class="usage-code">GameplayCamerasEditor</code>）。</li><li>用 <code class="usage-code">Camera Asset / Camera Rig</code> 搭建模块化相机：在 Camera Director 里选择当前激活的相机 rig。</li><li>把 Camera Director 组件挂到 Player Controller 或 Pawn，通过 Camera Node（偏移、注视、遮挡等）组合行为。</li><li>Game 模块依赖 <code class="usage-code">GameplayCameras</code>；<code class="usage-code">GameplayCamerasEditor</code> 只用于编辑器。</li></ol><p class="usage-note">模块化数据驱动相机系统（Gameplay Cameras 2.0），不是旧 Camera Component 直接挂载。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Gameplay Cameras</code> (runtime <code class="usage-code">GameplayCameras</code>, plus <code class="usage-code">GameplayCamerasUncookedOnly</code> and editor <code class="usage-code">GameplayCamerasEditor</code>).</li><li>Build cameras modularly from <code class="usage-code">Camera Asset / Camera Rig</code> and pick the active rig through the Camera Director.</li><li>Attach the Camera Director component to the Player Controller or Pawn and compose behavior via Camera Nodes (offset, look-at, occlusion, etc.).</li><li>Game modules depend on <code class="usage-code">GameplayCameras</code>; <code class="usage-code">GameplayCamerasEditor</code> is editor-only.</li></ol><p class="usage-note">The modular data-driven camera system (Gameplay Cameras 2.0), not the classic Camera Component.</p></div></div></div>
    </div>

