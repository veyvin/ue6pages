---
layout: default
title: 交互界面 / InteractionInterface
---

<h1>交互界面 / InteractionInterface</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/InteractionInterface/InteractionInterface.uplugin</code></span></li><li><span class="label">版本</span><span class="value">1.0</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">游戏玩法</div><div class="lang-content">Gameplay</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">InteractableInterface</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Interaction Interface</code>（模块 <code class="usage-code">InteractableInterface</code>）。</li><li>让可交互的 Actor 实现该交互接口（InteractableInterface），暴露“被交互”的契约。</li><li>玩家/系统通过接口统一调用交互，而不硬编码具体 Actor 类型。</li><li>Experimental：接口可能变动；它是交互契约模块，不含具体交互玩法。</li></ol><p class="usage-note">交互接口契约，配合 GameplayInteractions 等使用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Interaction Interface</code> (module <code class="usage-code">InteractableInterface</code>).</li><li>Have interactable actors implement the interaction interface (InteractableInterface) to expose an &quot;interactable&quot; contract.</li><li>Players/systems call interaction uniformly through the interface instead of hard-coding concrete actor types.</li><li>Experimental: contract may change; it is an interaction contract module, not concrete interaction gameplay.</li></ol><p class="usage-note">An interaction contract to pair with things like GameplayInteractions.</p></div></div></div>
    </div>

