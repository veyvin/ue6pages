---
layout: default
title: 实时链接 / Live Link
---

<h1>实时链接 / Live Link</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/LiveLink/LiveLink.uplugin</code></span></li><li><span class="label">版本</span><span class="value">2.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">LiveLink, LiveLinkComponents, LiveLinkEditor, LiveLinkGraphNode, LiveLinkMovieScene, LiveLinkSequencer, LiveLinkMultiUser</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Live Link</code>（模块 <code class="usage-code">LiveLink</code>、<code class="usage-code">LiveLinkComponents</code>、<code class="usage-code">LiveLinkGraphNode</code>、<code class="usage-code">LiveLinkSequencer</code>、<code class="usage-code">LiveLinkMovieScene</code>，编辑器 <code class="usage-code">LiveLinkEditor</code>）。</li><li>把外部设备（动捕、摄像机、面捕、灯光）的数据变成 Live Link 主体，流进编辑器或运行时。</li><li>给骨骼/摄像机/Control Rig 加 Live Link 组件消费主体数据，用于虚拟制片与 MetaHuman 面捕。</li><li>Game 模块依赖运行时模块；<code class="usage-code">LiveLinkEditor</code> 等只进 Editor Target。</li></ol><p class="usage-note">实时设备数据流的主干，虚拟制片/MetaHuman 面捕依赖它。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Live Link</code> (modules <code class="usage-code">LiveLink</code>, <code class="usage-code">LiveLinkComponents</code>, <code class="usage-code">LiveLinkGraphNode</code>, <code class="usage-code">LiveLinkSequencer</code>, <code class="usage-code">LiveLinkMovieScene</code>, editor <code class="usage-code">LiveLinkEditor</code>).</li><li>Turn external device data (mocap, cameras, facial, lights) into Live Link subjects that stream into the editor or runtime.</li><li>Add Live Link components to skeletons/cameras/Control Rig to consume subject data for virtual production and MetaHuman facial capture.</li><li>Game modules depend on runtime modules; editor ones like <code class="usage-code">LiveLinkEditor</code> go to Editor targets only.</li></ol><p class="usage-note">The backbone for real-time device data; virtual production/MetaHuman facial capture depend on it.</p></div></div></div>
    </div>

