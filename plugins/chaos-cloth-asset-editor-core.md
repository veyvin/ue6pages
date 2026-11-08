---
layout: default
title: 混沌布料资产编辑器核心 / Chaos Cloth Asset Editor Core
---

<h1>混沌布料资产编辑器核心 / Chaos Cloth Asset Editor Core</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/ChaosClothAssetEditorCore/ChaosClothAssetEditorCore.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">物理</div><div class="lang-content">Physics</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">ChaosClothAssetEditor, ChaosClothAssetEditorTools</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Chaos Cloth Asset Editor Core</code>（<code class="usage-code">ChaosClothAssetEditor</code>、<code class="usage-code">ChaosClothAssetEditorTools</code>）。</li><li>内容浏览器双击 <code class="usage-code">Cloth Asset</code>，用该核心编辑器改面板、视口和工具，而不是 Cascade 或旧 Clothing 窗口。</li><li>在编辑器里绑定骨架、碰撞体和模拟参数，保存后再把资产挂到角色。</li><li><code class="usage-code">ChaosClothAssetEditor*</code> 只能进 Editor Target。</li></ol><p class="usage-note">新 Cloth Asset 编辑器的核心 UI，不含具体 USD/Dataflow 节点。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Chaos Cloth Asset Editor Core</code> (<code class="usage-code">ChaosClothAssetEditor</code>, <code class="usage-code">ChaosClothAssetEditorTools</code>).</li><li>Double-click a <code class="usage-code">Cloth Asset</code> and author it in this editor, not Cascade or the legacy Clothing window.</li><li>Bind skeleton, colliders, and sim settings, save, then assign the asset on the character.</li><li>Keep <code class="usage-code">ChaosClothAssetEditor*</code> on Editor targets only.</li></ol><p class="usage-note">Core UI for the new Cloth Asset editor; USD/Dataflow nodes live in sibling plugins.</p></div></div></div>
    </div>

