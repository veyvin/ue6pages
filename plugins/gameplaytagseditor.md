---
layout: default
title: 游戏标签编辑器 / GameplayTagsEditor
---

<h1>游戏标签编辑器 / GameplayTagsEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Editor/GameplayTagsEditor/GameplayTagsEditor.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">编辑</div><div class="lang-content">Editor</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">GameplayTagsEditor</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用编辑器插件 <code class="usage-code">GameplayTagsEditor</code>（模块 <code class="usage-code">GameplayTagsEditor</code>）并重启。</li><li>在 <code class="usage-code">Project Settings &gt; Gameplay Tags</code> 或细节面板里用它提供的编辑器 UI 增删、重命名 Gameplay Tags。</li><li>用其蓝图节点/编辑器支持给资产和对象打标签；改完记得保存标签列表。</li><li>它是编辑器工具，只能进 Editor Target，不要写进 Game <code class="usage-code">Build.cs</code>。</li></ol><p class="usage-note">Gameplay Tags 的编辑器 UI/节点，运行时标签在别的模块。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the editor plugin <code class="usage-code">GameplayTagsEditor</code> (module <code class="usage-code">GameplayTagsEditor</code>) and restart.</li><li>Use its editor UI in <code class="usage-code">Project Settings &gt; Gameplay Tags</code> or Details to add, rename, and remove Gameplay Tags.</li><li>Use its Blueprint nodes/editor support to tag assets and objects; save the tag list after edits.</li><li>It is an editor tool for Editor targets only; never add it to a game <code class="usage-code">Build.cs</code>.</li></ol><p class="usage-note">Editor UI/nodes for Gameplay Tags; the runtime tag system lives elsewhere.</p></div></div></div>
    </div>

