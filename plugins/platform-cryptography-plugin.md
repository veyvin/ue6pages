---
layout: default
title: 平台密码学插件 / Platform Cryptography Plugin
---

<h1>平台密码学插件 / Platform Cryptography Plugin</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/PlatformCrypto/PlatformCrypto.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">杂项</div><div class="lang-content">Misc</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">PlatformCrypto, PlatformCryptoTypes, PlatformCryptoContext</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Platform Cryptography Plugin</code>（模块 <code class="usage-code">PlatformCrypto</code>、<code class="usage-code">PlatformCryptoTypes</code>、<code class="usage-code">PlatformCryptoContext</code>）。</li><li>它暴露统一加密 API：优先用平台原生加密，否则回退 OpenSSL。</li><li>在需要哈希/对称加密等能力时依赖这些模块，避免直接绑死某一库。</li><li>属实验性平台加密封装。</li></ol><p class="usage-note">统一加密 API（平台原生，否则 OpenSSL）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Platform Cryptography Plugin</code> (modules <code class="usage-code">PlatformCrypto</code>, <code class="usage-code">PlatformCryptoTypes</code>, <code class="usage-code">PlatformCryptoContext</code>).</li><li>It exposes a unified crypto API: platform-native crypto when available, otherwise OpenSSL.</li><li>Depend on these modules for hashing/symmetric crypto instead of hard-wiring one library.</li><li>It is an experimental platform-crypto wrapper.</li></ol><p class="usage-note">Unified crypto API (platform-native, else OpenSSL).</p></div></div></div>
    </div>

