---
layout: default
title: 激光雷达点云支持 / LiDAR Point Cloud Support
---

<h1>激光雷达点云支持 / LiDAR Point Cloud Support</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Enterprise/LidarPointCloud/LidarPointCloud.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">渲染</div><div class="lang-content">Rendering</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">LidarPointCloudRuntime, LidarPointCloudEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">LiDAR Point Cloud Support</code>（运行时 <code class="usage-code">LidarPointCloudRuntime</code>，编辑器 <code class="usage-code">LidarPointCloudEditor</code>）。</li><li>导入 LiDAR 点云数据（.las/.laz 等），在编辑器里处理、裁剪、着色。</li><li>把点云挂到 Actor 上渲染，用于测绘、场景参考或大世界重建。</li><li>Game 模块依赖 <code class="usage-code">LidarPointCloudRuntime</code>；<code class="usage-code">LidarPointCloudEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">LiDAR 点云的导入、处理与渲染，测绘/大世界参考用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">LiDAR Point Cloud Support</code> (runtime <code class="usage-code">LidarPointCloudRuntime</code>, editor <code class="usage-code">LidarPointCloudEditor</code>).</li><li>Import LiDAR point-cloud data (.las/.laz, etc.) and process/crop/color it in the editor.</li><li>Attach the cloud to an actor for rendering, for surveying, scene reference, or large-world reconstruction.</li><li>Game modules depend on <code class="usage-code">LidarPointCloudRuntime</code>; <code class="usage-code">LidarPointCloudEditor</code> is Editor-target only.</li></ol><p class="usage-note">LiDAR point-cloud import, processing, and rendering for surveying/large-world reference.</p></div></div></div>
    </div>

