---
layout: default
title: 姿势搜索 / Pose Search
---

<h1>姿势搜索 / Pose Search</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Animation/PoseSearch/PoseSearch.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">PoseSearch, PoseSearchEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Pose Search</code>（运行时 <code class="usage-code">PoseSearch</code>，编辑器 <code class="usage-code">PoseSearchEditor</code>）。</li><li>它提供姿势特征的索引与搜索框架，用于运动匹配等技术。</li><li>为动画库建 Pose Search 数据库，在动画图里按目标姿势检索片段。</li><li>Game 模块依赖 <code class="usage-code">PoseSearch</code>；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">姿势特征索引/搜索框架（运动匹配等）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Pose Search</code> (runtime <code class="usage-code">PoseSearch</code>, editor <code class="usage-code">PoseSearchEditor</code>).</li><li>It is a framework for indexing and searching pose features, used in techniques such as Motion Matching.</li><li>Build a Pose Search database for your anim set and query clips by target pose in the anim graph.</li><li>Game modules depend on <code class="usage-code">PoseSearch</code>; editor modules go to Editor targets only.</li></ol><p class="usage-note">Pose-feature index/search framework (e.g. Motion Matching).</p></div></div></div>
    </div>

