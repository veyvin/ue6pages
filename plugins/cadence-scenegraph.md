---
layout: default
title: Cadence场景图 / Cadence SceneGraph
---

<!-- ai-generation-failed -->

<h1>Cadence场景图 / Cadence SceneGraph</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Cadence/CadenceSceneGraph/CadenceSceneGraph.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">CadenceSceneGraph</span></li>
  </ul>
</div>

<h2>Description / 描述</h2>
<div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">跟踪玩家在 Cadence 状态缓存中拥有的 SceneGraph 实体，因此将其复制的变换与客户端对同一帧的预测进行比较，并通过重新模拟进行纠正；将 Cadence 复制的输入提供给服务器上的 Verse 输入以及各处的 own_input_component。</div><div class="lang-content">Tracks SceneGraph entities a player possesses in the Cadence state cache, so their replicated transforms are compared against the client's prediction for the same frame and corrected by a resimulation; feeds Cadence-replicated input to Verse input on the server and to possessed_input_component everywhere.</div></div>
