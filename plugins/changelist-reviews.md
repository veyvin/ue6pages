---
layout: default
title: 变更列表评论 / Changelist Reviews
---

<h1>变更列表评论 / Changelist Reviews</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Editor/ChangelistReview/ChangelistReview.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">源代码控制</div><div class="lang-content">Source Control</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChangelistReview</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">Changelist Reviews</code>（模块 <code class="usage-code">ChangelistReview</code>）并重启。</li><li>先在 <code class="usage-code">Revision Control</code> 里连上 Perforce（或当前源码管理），提交或挂起一个 changelist。</li><li>打开 <code class="usage-code">Window</code> / 源码管理相关面板，用 <code class="usage-code">ChangelistReview</code> 查看该 changelist 的文件与审阅状态，而不是去 Content Browser 搜组件。</li><li>不要把 <code class="usage-code">ChangelistReview</code> 写进游戏 <code class="usage-code">Build.cs</code> 或 Shipping 包。</li></ol><p class="usage-note">仅服务编辑器源码审阅，默认不进 Shipping。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">Changelist Reviews</code> (module <code class="usage-code">ChangelistReview</code>) and restart.</li><li>Connect Perforce (or your revision control) and create or shelve a changelist.</li><li>Open the revision-control UI and inspect that changelist with <code class="usage-code">ChangelistReview</code>; this is not a gameplay component.</li><li>Do not add <code class="usage-code">ChangelistReview</code> to a game <code class="usage-code">Build.cs</code> or a shipping cook.</li></ol><p class="usage-note">Editor-only changelist review; it does not ship.</p></div></div></div>
    </div>

