---
layout: default
title: QUIC 消息传递 / QUIC Messaging
---

<h1>QUIC 消息传递 / QUIC Messaging</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/QuicMessaging/QuicMessaging.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">消息传递</div><div class="lang-content">Messaging</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">QuicMessaging, QuicMessagingTransport</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">QUIC Messaging</code>（模块 <code class="usage-code">QuicMessaging</code>、<code class="usage-code">QuicMessagingTransport</code>）。</li><li>它给消息子系统加上基于 QUIC 的传输层，用于在联网计算机和设备之间收发消息。</li><li>在需要低延迟/多路复用消息通道时，把消息传输换成 QUIC。</li><li>属实验性消息传输；接口可能随版本变化。</li></ol><p class="usage-note">消息子系统的 QUIC 传输层。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">QUIC Messaging</code> (modules <code class="usage-code">QuicMessaging</code>, <code class="usage-code">QuicMessagingTransport</code>).</li><li>It adds a QUIC-based transport to the messaging subsystem for sending/receiving messages between networked computers and devices.</li><li>Switch messaging transport to QUIC when you need a low-latency, multiplexed message channel.</li><li>It is an experimental messaging transport; the contract may change across versions.</li></ol><p class="usage-note">QUIC transport layer for the messaging subsystem.</p></div></div></div>
    </div>

