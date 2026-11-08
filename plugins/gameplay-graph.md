---
layout: default
title: 游戏图 / Gameplay Graph
---

<h1>游戏图 / Gameplay Graph</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/GameplayGraph/GameplayGraph.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">游戏玩法</div><div class="lang-content">Gameplay</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GameplayGraph</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Gameplay Graph</code>（模块 <code class="usage-code">GameplayGraph</code>）。</li><li>在需要图结构（节点/边、寻路、依赖关系等）的玩法逻辑里，使用插件提供的图模型与常见图算法。</li><li>从模块 <code class="usage-code">Build.cs</code> 依赖 <code class="usage-code">GameplayGraph</code>，用其类型构建图并在运行时查询。</li><li>Experimental：算法接口可能随夜构建变化，别写死未文档化类型。</li></ol><p class="usage-note">通用图模型与算法库，不是可视化的关卡工具。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Gameplay Graph</code> (module <code class="usage-code">GameplayGraph</code>).</li><li>Use the provided graph model and common graph algorithms where gameplay needs node/edge data, pathing, or dependency graphs.</li><li>Depend on <code class="usage-code">GameplayGraph</code> from your module <code class="usage-code">Build.cs</code>, build graphs with its types, and query them at runtime.</li><li>Experimental: algorithm API may shift on nightlies; do not freeze undocumented types.</li></ol><p class="usage-note">A general graph model and algorithms library, not a visual level tool.</p></div></div></div>
    </div>

