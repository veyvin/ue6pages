---
layout: default
title: 游戏功能 游戏功能 动作 / Gameplay Abilities Game Feature Actions
---

<h1>游戏功能 游戏功能 动作 / Gameplay Abilities Game Feature Actions</h1>

<div class="info-card">
  <ul>
    <li><span class="label">插件文件</span><span class="value"><code>Engine/Plugins/Experimental/AbilitySystemGameFeatureActions/AbilitySystemGameFeatureActions.uplugin</code></span></li><li><span class="label">版本</span><span class="value">0.1</span></li><li><span class="label">类别</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">游戏玩法</div><div class="lang-content">Gameplay</div></div></span></li><li><span class="label">作者</span><span class="value"><div class="bilingual-block"><div class="lang-tabs"><div class="lang-tab active" onclick="switchLang(this)">中文</div><div class="lang-tab" onclick="switchLang(this)">English</div></div><div class="lang-content active">史诗游戏公司</div><div class="lang-content">Epic Games, Inc.</div></div></span></li><li><span class="label">模块</span><span class="value">AbilitySystemGameFeatureActions</span></li>
  </ul>
</div>

<div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Gameplay Abilities Game Feature Actions</code>（模块 <code class="usage-code">AbilitySystemGameFeatureActions</code>）。</li><li>在 Game Feature 插件里添加 GAS 相关的 Game Feature Action，用它在 Feature 激活/停用时授予或移除 GameplayAbility。</li><li>让角色的 AbilitySystemComponent 通过 GameFeature 的 Add/Remove 流程取得技能，而不是手写 GrantAbility。</li><li>Experimental：接口随夜构建可能变化，先在空关卡验证 Feature 激活顺序。</li></ol><p class="usage-note">给 GAS 用的 Game Feature Action，真正的 GAS 核心在 `Gameplay Abilities` 插件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Gameplay Abilities Game Feature Actions</code> (module <code class="usage-code">AbilitySystemGameFeatureActions</code>).</li><li>Inside a Game Feature plugin, add the GAS Game Feature Actions to grant/remove GameplayAbilities as the feature activates or deactivates.</li><li>Let the character&#x27;s AbilitySystemComponent receive abilities through the GameFeature Add/Remove flow instead of hand-calling GrantAbility.</li><li>Experimental: the contract may shift on nightlies; prove feature activation order in an empty map first.</li></ol><p class="usage-note">Game Feature Actions for GAS; the actual GAS core lives in the `Gameplay Abilities` plugin.</p></div></div></div>
    </div>

