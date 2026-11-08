---
layout: default
title: 浮动属性 / Floating Properties
---

<h1>浮动属性 / Floating Properties</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/FloatingProperties/FloatingProperties.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">实验性的</div><div class="lang-content">Experimental</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">FloatingProperties</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">Floating Properties</code>（模块 <code class="usage-code">FloatingProperties</code>）并重启。它把 Details 里钉住的属性画在活动视口上，不是新的属性编辑器。</li><li>选中关卡 Actor，在 Details 属性旁使用钉到视口 / floating 控件（插件提供的 pin）。视口应出现可拖动的浮动行，改数值应与 Details 双向同步并可撤销。</li><li>切到正交/透视视口验证 overlay 跟的是「活动视口」；切换所选 Actor 时浮动条应换成新对象属性，而不是残留上一个。</li><li>适合调灯光强度、变换、VP 场景参数时不离开视口。不要把 <code class="usage-code">FloatingProperties</code> 加进游戏 <code class="usage-code">Build.cs</code>。</li><li>Experimental：钉住状态可能不进版本控制；Shipping 包没有视口 overlay。</li></ol><p class="usage-note">视口上的 Details 钉钉条，不是 Runtime 调试 HUD。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">Floating Properties</code> (module <code class="usage-code">FloatingProperties</code>) and restart. It draws pinned Details rows on the active viewport — it is not a second property editor.</li><li>Select a level actor and pin a Details property to the viewport via the plugin’s pin control. A draggable overlay row should appear; edits sync both ways with Details and undo.</li><li>Confirm the overlay follows the *active* viewport (ortho vs. perspective). Changing selection should swap the floating rows, not leave the previous object’s properties.</li><li>Use it to tweak light intensity, transforms, or VP scene values without leaving the viewport. Do not add <code class="usage-code">FloatingProperties</code> to a game <code class="usage-code">Build.cs</code>.</li><li>Experimental: pin state may not be source-controlled. Shipping builds have no viewport overlay.</li></ol><p class="usage-note">Pinned Details rows on the viewport, not a runtime debug HUD.</p></div></div></div>
    </div>

