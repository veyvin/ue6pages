---
layout: default
title: 层次结构表动画 / Hierarchy Table Animation
---

<h1>层次结构表动画 / Hierarchy Table Animation</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/Animation/HierarchyTableAnimation/HierarchyTableAnimation.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">动画片</div><div class="lang-content">Animation</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">HierarchyTableAnimationRuntime, HierarchyTableAnimationEditor, HierarchyTableAnimationUncookedOnly</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Hierarchy Table Animation</code>（模块 <code class="usage-code">HierarchyTableAnimationRuntime</code>、编辑器 <code class="usage-code">HierarchyTableAnimationEditor</code>、<code class="usage-code">HierarchyTableAnimationUncookedOnly</code>）。</li><li>在 Hierarchy Table 管线里使用动画专用类型定义，承载层级化动画数据。</li><li>配合动画系统读取/驱动层级表动画；先在空关卡验证数据流。</li><li>Experimental：接口可能变动；编辑器/Uncooked 模块不进 Shipping。</li></ol><p class="usage-note">Hierarchy Table 的动画类型定义，需与基础 Hierarchy Table 搭配。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Hierarchy Table Animation</code> (modules <code class="usage-code">HierarchyTableAnimationRuntime</code>, editor <code class="usage-code">HierarchyTableAnimationEditor</code>, <code class="usage-code">HierarchyTableAnimationUncookedOnly</code>).</li><li>Use the animation-specific type definitions in the Hierarchy Table pipeline to carry hierarchical animation data.</li><li>Read/drive hierarchy-table animation alongside the animation system; prove the data flow in an empty map first.</li><li>Experimental: contract may change; editor/uncooked modules do not ship.</li></ol><p class="usage-note">Animation type definitions for Hierarchy Tables; pairs with the base Hierarchy Table plugin.</p></div></div></div>
    </div>

