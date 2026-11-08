---
layout: default
title: MsQuic 运行时插件 / MsQuic Runtime Plugin
---

<h1>MsQuic 运行时插件 / MsQuic Runtime Plugin</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Runtime/MsQuic/MsQuic.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">运行时</div><div class="lang-content">Runtime</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MsQuicRuntime</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">MsQuic Runtime Plugin</code>（模块 <code class="usage-code">MsQuicRuntime</code>），运行时插件。</li><li>它把 MsQuic 库（基于 QUIC 的传输）作为运行时依赖提供。</li><li>在需要 QUIC 传输的网络/服务集成里，基于它构建连接。</li><li>运行时模块可进游戏包；属底层传输库封装。</li></ol><p class="usage-note">MsQuic（QUIC）库的运行时封装。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">MsQuic Runtime Plugin</code> (module <code class="usage-code">MsQuicRuntime</code>), a runtime plugin.</li><li>It provides the MsQuic library (QUIC-based transport) as a runtime dependency.</li><li>Use it to build connections in network/service integrations that need QUIC transport.</li><li>Runtime modules can ship; it is a low-level transport library wrapper.</li></ol><p class="usage-note">A runtime wrapper for the MsQuic (QUIC) library.</p></div></div></div>
    </div>

