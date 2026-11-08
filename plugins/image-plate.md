---
layout: default
title: 图像板 / Image Plate
---

<h1>图像板 / Image Plate</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/ImagePlate/ImagePlate.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">渲染</div><div class="lang-content">Rendering</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ImagePlate, ImagePlateEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Image Plate</code>（运行时 <code class="usage-code">ImagePlate</code>，编辑器 <code class="usage-code">ImagePlateEditor</code>）。</li><li>在关卡放置 Image Plate Actor，指定图像，使其与相机对齐（虚拟制片的图像板）。</li><li>调整距离/朝向让图像板贴在场景正确深度，用于背景板、合成参考。</li><li>Experimental：接口可能变动；<code class="usage-code">ImagePlateEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">相机对齐的图像板 Actor/组件（虚拟制片背景）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Image Plate</code> (runtime <code class="usage-code">ImagePlate</code>, editor <code class="usage-code">ImagePlateEditor</code>).</li><li>Place an Image Plate actor in the level, assign an image, and align it to the camera (a virtual production image plate).</li><li>Adjust distance/orientation so the plate sits at the correct scene depth for backdrops and compositing.</li><li>Experimental: contract may change; <code class="usage-code">ImagePlateEditor</code> is Editor-target only.</li></ol><p class="usage-note">Camera-aligned image-plate actor/component (virtual production backdrop).</p></div></div></div>
    </div>

