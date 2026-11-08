---
layout: default
title: 音乐会洞察核心 / ConcertInsightsCore
---

<h1>音乐会洞察核心 / ConcertInsightsCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Developer/Concert/ConcertInsights/ConcertInsightsCore/ConcertInsightsCore.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">联网</div><div class="lang-content">Networking</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ConcertInsightsCore</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">ConcertInsightsCore</code>（模块 <code class="usage-code">ConcertInsightsCore</code>）。它实现“同步开 Trace”的共享命令与通道，没有状态栏按钮。</li><li>客户端点状态栏时走 <code class="usage-code">ConcertInsightsClient</code>，服务器接请求时走 <code class="usage-code">ConcertInsightsServer</code>，两边都链到 Core。</li><li>扩展自定义 Concert 端点（例如工具进程也要被同步录）时，依赖 <code class="usage-code">ConcertInsightsCore</code> 发/收同一套 start-trace 消息。</li><li>不要在 Core 里找 Insights 时间轴控件——可视化在 <code class="usage-code">ConcertInsightsVisualizer</code>。</li><li>开发者插件，勿加入 Shipping 游戏。</li></ol><p class="usage-note">同步 Trace 协议层；按钮在 Client，监听在 Server，图表在 Visualizer。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">ConcertInsightsCore</code> (module <code class="usage-code">ConcertInsightsCore</code>). It is the shared start-trace command/channel, with no status-bar button.</li><li><code class="usage-code">ConcertInsightsClient</code> fires from the client status bar; <code class="usage-code">ConcertInsightsServer</code> accepts on the server; both link Core.</li><li>If a custom Concert endpoint (tool process) must join sync recording, depend on <code class="usage-code">ConcertInsightsCore</code> and speak the same start-trace messages.</li><li>Do not look in Core for Insights timeline widgets — those live in <code class="usage-code">ConcertInsightsVisualizer</code>.</li><li>Developer plugin; keep it out of Shipping games.</li></ol><p class="usage-note">Sync-trace protocol only: button on Client, listener on Server, charts in Visualizer.</p></div></div></div>
    </div>

