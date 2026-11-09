---
layout: default
title: 游戏能力 / Gameplay Abilities
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Gameplay Abilities</div>
      <div class="hero-title-cn">游戏能力 · 添加 GameplayEffect 和 GameplayAbil</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Gameplay</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/GameplayAbilities/GameplayAbilities.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">添加 GameplayEffect 和 GameplayAbility 类来处理复杂的游戏交互。</div><div class="lang-content">Adds GameplayEffect and GameplayAbility classes to handle complicated gameplay interactions.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Gameplay Ability System（GAS）给技能、冷却、消耗、Buff/Debate 一套数据驱动框架。用 GameplayAbility、GameplayEffect、AttributeSet、GameplayCue 组合出攻击、翻滚、被动等，适合需要复制的多人技能。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：GameplayAbilities, GameplayAbilitiesEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine</a></p></div><div class="lang-content"><p>The Gameplay Ability System (GAS) is a data-driven framework for skills, cooldowns, costs, and buffs. GameplayAbility, GameplayEffect, AttributeSet, and GameplayCue compose attacks, dodges, and passives, including replicated multiplayer.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: GameplayAbilities, GameplayAbilitiesEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Gameplay Abilities</code>（运行时 <code class="usage-code">GameplayAbilities</code>，编辑器 <code class="usage-code">GameplayAbilitiesEditor</code>）。</li><li>在角色上挂 <code class="usage-code">AbilitySystemComponent</code> 与 <code class="usage-code">AttributeSet</code>，初始化属性与初始技能。</li><li>用 <code class="usage-code">GameplayAbility</code> 写攻击/翻滚等技能，用 <code class="usage-code">GameplayEffect</code> 做冷却、消耗、Buff，用 <code class="usage-code">GameplayCue</code> 加表现（特效/音效）。</li><li>多人玩法在服务器授予技能、客户端预测；Game 模块依赖 <code class="usage-code">GameplayAbilities</code>，<code class="usage-code">GameplayAbilitiesEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">GAS 数据驱动技能框架，支持复制；示例常用 Lyra 的 GAS 用法对照。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Gameplay Abilities</code> (runtime <code class="usage-code">GameplayAbilities</code>, editor <code class="usage-code">GameplayAbilitiesEditor</code>).</li><li>Add an <code class="usage-code">AbilitySystemComponent</code> and an <code class="usage-code">AttributeSet</code> to the character and initialize attributes and starting abilities.</li><li>Author attacks/dodges as <code class="usage-code">GameplayAbility</code>, use <code class="usage-code">GameplayEffect</code> for cooldowns, costs, and buffs, and <code class="usage-code">GameplayCue</code> for VFX/SFX.</li><li>For multiplayer, grant on server and predict on client; depend on <code class="usage-code">GameplayAbilities</code> from game modules and keep <code class="usage-code">GameplayAbilitiesEditor</code> on Editor targets.</li></ol><p class="usage-note">The data-driven GAS framework with replication; Lyra is a common reference implementation.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">GameplayAbilities</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GameplayAbilitiesEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/GameplayAbilities/GameplayAbilities.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
