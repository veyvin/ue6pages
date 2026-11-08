---
layout: default
title: 性能捕捉核心 / Performance Capture Core
---

<h1>性能捕捉核心 / Performance Capture Core</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/PerformanceCaptureCore/PerformanceCaptureCore.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏</div><div class="lang-content">Epic Games</div></div></span></li><li><span class="label">模块</span><span class="value">PerformanceCaptureCore, PerformanceCaptureCoreEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Performance Capture Core</code>（运行时 <code class="usage-code">PerformanceCaptureCore</code>，编辑器 <code class="usage-code">PerformanceCaptureCoreEditor</code>）。</li><li>它是性能捕捉（Performance Capture）的核心层：处理动捕/面捕数据的基础设施。</li><li>通常作为上层 Performance Capture 工具/工作流的底层依赖。</li><li>Game 模块依赖运行时模块；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">性能捕捉(动捕/面捕)的核心基础设施层。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Performance Capture Core</code> (runtime <code class="usage-code">PerformanceCaptureCore</code>, editor <code class="usage-code">PerformanceCaptureCoreEditor</code>).</li><li>It is the core layer of performance capture: infrastructure for handling mocap/facial data.</li><li>Usually a low-level dependency for upper performance-capture tools/workflows.</li><li>Game modules depend on runtime modules; editor modules go to Editor targets only.</li></ol><p class="usage-note">The core infrastructure layer for performance capture (mocap/facial).</p></div></div></div>
    </div>

