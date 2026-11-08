---
layout: default
title: 可本地化的消息 / Localizable Message
---

<h1>可本地化的消息 / Localizable Message</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/LocalizableMessage/LocalizableMessage.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">消息传递</div><div class="lang-content">Messaging</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">LocalizableMessage, LocalizableMessageBlueprint</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Localizable Message</code>（模块 <code class="usage-code">LocalizableMessage</code>，蓝图 <code class="usage-code">LocalizableMessageBlueprint</code>）。</li><li>用它构造可复制的文本消息，并支持客户端侧参数解析（占位符替换）。</li><li>在联网场景里把本地化消息发给客户端，由客户端按本地语言解析参数显示。</li><li>Experimental：接口可能变动；服务端组消息、客户端本地化呈现。</li></ol><p class="usage-note">可复制+客户端参数解析的本地化文本消息，实验性。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Localizable Message</code> (module <code class="usage-code">LocalizableMessage</code>, Blueprint <code class="usage-code">LocalizableMessageBlueprint</code>).</li><li>Build a replicable text message that supports client-side parameter resolution (placeholder substitution).</li><li>In net scenarios, send the localizable message to clients; the client resolves parameters and displays it in its locale.</li><li>Experimental: contract may change; the server forms the message, the client localizes it.</li></ol><p class="usage-note">A replicable, client-parameter-resolved localizable text message, experimental.</p></div></div></div>
    </div>

