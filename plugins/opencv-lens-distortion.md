---
layout: default
title: OpenCV 镜头畸变 / OpenCV Lens Distortion
---

<h1>OpenCV 镜头畸变 / OpenCV Lens Distortion</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Compositing/OpenCVLensDistortion/OpenCVLensDistortion.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">合成</div><div class="lang-content">Compositing</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">OpenCVLensCalibration, OpenCVLensDistortion</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">OpenCV Lens Distortion</code>（模块 <code class="usage-code">OpenCVLensCalibration</code>、<code class="usage-code">OpenCVLensDistortion</code>）。</li><li>它用 OpenCV 做相机校准，并生成镜头畸变/不畸变的位移图。</li><li>在校准流程里用其工具处理镜头畸变（替代旧的 LensDistortion 插件）。</li><li>属合成/相机校准工具；需 OpenCV 插件。</li></ol><p class="usage-note">用 OpenCV 做相机校准与镜头畸变位移图。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">OpenCV Lens Distortion</code> (modules <code class="usage-code">OpenCVLensCalibration</code>, <code class="usage-code">OpenCVLensDistortion</code>).</li><li>It uses OpenCV for camera calibration and to generate lens distortion/undistortion displacement maps.</li><li>Use its tools in the calibration flow to handle lens distortion (replacing the old LensDistortion plugin).</li><li>It is a compositing/camera-calibration tool; requires the OpenCV plugin.</li></ol><p class="usage-note">Camera calibration and lens distortion maps via OpenCV.</p></div></div></div>
    </div>

