---
layout: default
title: Electra Player 内容解密模块 / Electra Player Content Decryption Module
---

<h1>Electra Player 内容解密模块 / Electra Player Content Decryption Module</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Media/ElectraCDM/ElectraCDM.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">媒体播放器</div><div class="lang-content">Media Players</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ElectraCDM</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">ElectraCDM</code> 并重启。</li><li>在项目设置为 Electra 配置 DRM（如 Widevine/PlayReady）及许可证服务器地址。</li><li>打开受保护的 Media Source，通过 Electra 播放触发许可证请求。</li><li>由 <code class="usage-code">ElectraCDM</code> 处理许可证与解密。</li><li>通过 Media Player 回调确认解密成功后正常出画。</li></ol><p class="usage-note">内容解密模块，只负责 DRM/许可证解密；需要有效许可证服务器与密钥配置才能出画。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">ElectraCDM</code> and restart.</li><li>In Project Settings, configure DRM for Electra (e.g. Widevine/PlayReady) and the license server URL.</li><li>Open the protected Media Source and play through Electra to trigger license acquisition.</li><li>Let <code class="usage-code">ElectraCDM</code> handle the license and decryption.</li><li>Confirm via Media Player callbacks that decryption succeeds and video renders.</li></ol><p class="usage-note">The content decryption module handles DRM/license decryption only; you need a valid license server and keys for video to render.</p></div></div></div>
    </div>

