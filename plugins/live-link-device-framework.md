---
layout: default
title: Live Link 设备框架 / Live Link Device Framework
---

<h1>Live Link 设备框架 / Live Link Device Framework</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/LiveLinkDevice/LiveLinkDevice.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">LiveLinkDevice</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Live Link Device Framework</code>（模块 <code class="usage-code">LiveLinkDevice</code>）。</li><li>它是 Live Link 设备接入的框架层，供实现/注册 Live Link 设备。</li><li>编写或接入具体设备时依赖该框架，再向上提供 Live Link 主体数据。</li><li>属 Live Link 基础框架，通常与 Live Link 主插件一起用。</li></ol><p class="usage-note">Live Link 设备接入框架，供实现具体设备。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Live Link Device Framework</code> (module <code class="usage-code">LiveLinkDevice</code>).</li><li>It is the framework layer for Live Link device integration, used to implement/register Live Link devices.</li><li>Depend on it when writing or integrating a device, then expose Live Link subject data upward.</li><li>It is Live Link base framework, usually used with the main Live Link plugin.</li></ol><p class="usage-note">The Live Link device-integration framework for implementing concrete devices.</p></div></div></div>
    </div>

