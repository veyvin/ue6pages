---
layout: default
title: 多用户编辑 / Multi-User Editing
---

<h1>多用户编辑 / Multi-User Editing</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Developer/Concert/ConcertApp/MultiUserClient/MultiUserClient.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.2</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编辑</div><div class="lang-content">Editor</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">MultiUserClient, MultiUserClientLibrary, MultiUserReplicationEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">Multi-User Editing</code>（模块 <code class="usage-code">MultiUserClient</code>、<code class="usage-code">MultiUserClientLibrary</code>、<code class="usage-code">MultiUserReplicationEditor</code>）并重启。</li><li>它允许在编辑器中进行协作多用户会话（Concert），在多台编辑器间同步关卡与资产更改。</li><li>加入/创建多用户会话（session），多人同时编辑同一工程。</li><li>这是编辑器/开发者插件，只进 Editor Target，不进 Shipping。</li></ol><p class="usage-note">多用户协作编辑会话（Concert），多台编辑器同步。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">Multi-User Editing</code> (modules <code class="usage-code">MultiUserClient</code>, <code class="usage-code">MultiUserClientLibrary</code>, <code class="usage-code">MultiUserReplicationEditor</code>) and restart.</li><li>It allows collaborative multi-user sessions (Concert) in the editor, syncing level and asset edits across editor machines.</li><li>Join/create a multi-user session so several people edit the same project simultaneously.</li><li>It is an editor/developer plugin for Editor targets only; it does not ship.</li></ol><p class="usage-note">Collaborative multi-user editing sessions (Concert) syncing across editors.</p></div></div></div>
    </div>

