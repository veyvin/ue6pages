---
layout: default
title: 移动修补实用程序 / Mobile Patching Utilities
---

<h1>移动修补实用程序 / Mobile Patching Utilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Runtime/MobilePatchingUtils/MobilePatchingUtils.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">移动的</div><div class="lang-content">Mobile</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MobilePatchingUtils</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Mobile Patching Utilities</code>（模块 <code class="usage-code">MobilePatchingUtils</code>），运行时插件。</li><li>它通过蓝图公开在移动平台下载与修补内容的能力。</li><li>在蓝图中调用其 API 下载/安装补丁内容包，处理进度。</li><li>运行时模块可进游戏包；平台/服务器方案由项目提供。</li></ol><p class="usage-note">移动平台蓝图的下载/修补内容工具。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Mobile Patching Utilities</code> (module <code class="usage-code">MobilePatchingUtils</code>), a runtime plugin.</li><li>It exposes Blueprint functionality for downloading and patching content on mobile platforms.</li><li>Call its API from Blueprint to download/install patch content packs and handle progress.</li><li>Runtime modules can ship; platform/server solutions are provided by your project.</li></ol><p class="usage-note">Blueprint download/patch content utilities for mobile.</p></div></div></div>
    </div>

