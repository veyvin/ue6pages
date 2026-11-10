---
layout: default
title: 动画预算分配器 / Animation Budget Allocator
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Animation Budget Allocator</div>
      <div class="hero-title-cn">动画预算分配器 · 通过动态限制骨架网格物体组件滴答来限制动画运行所需的时间。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Animation</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AnimationBudgetAllocator/AnimationBudgetAllocator.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">通过动态限制骨架网格物体组件滴答来限制动画运行所需的时间。</div><div class="lang-content">Constrains the time taken for animation to run by dynamically throttling skeletal mesh component ticking.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：通过动态限制骨架网格物体组件滴答来限制动画运行所需的时间。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AnimationBudgetAllocator。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Constrains the time taken for animation to run by dynamically throttling skeletal mesh component ticking.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AnimationBudgetAllocator. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Animation Budget Allocator</code>（模块 <code class="usage-code">AnimationBudgetAllocator</code>）。</li><li>把需要限预算的角色骨骼网格从 <code class="usage-code">USkeletalMeshComponent</code> 换成 <code class="usage-code">USkeletalMeshComponentBudgeted</code>（蓝图组件列表里的 Skeletal Mesh Component Budgeted）。</li><li>开局用 <code class="usage-code">UAnimationBudgetBlueprintLibrary::EnableAnimationBudget</code>（或控制台 <code class="usage-code">a.Budget.Enabled 1</code>）打开世界子系统 <code class="usage-code">UAnimationBudgetAllocator</code>。</li><li>在 <code class="usage-code">DefaultEngine.ini</code> 的动画预算参数（<code class="usage-code">UAnimationBudgetAllocatorParameters</code> / <code class="usage-code">a.Budget.BudgetMs</code>）里设每帧毫秒预算，并按距离/重要性调 <code class="usage-code">USkeletalMeshComponentBudgeted</code> 的 Significance。</li><li>用 <code class="usage-code">stat Animation</code> / Insights 看骨骼网格 Tick 是否被节流；预算耗尽时低重要性网格会降 tick 或停更。</li><li>不要把普通 <code class="usage-code">USkeletalMeshComponent</code> 期望自动进预算——只有 Budgeted 组件会向分配器注册。</li></ol><p class="usage-note">用 Budgeted 组件限动画 Tick，不是压缩 AnimSequence，也不是 Animation Sharing。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Animation Budget Allocator</code> (module <code class="usage-code">AnimationBudgetAllocator</code>).</li><li>Replace throttled meshes’ <code class="usage-code">USkeletalMeshComponent</code> with <code class="usage-code">USkeletalMeshComponentBudgeted</code> (Skeletal Mesh Component Budgeted in the component list).</li><li>Turn on world subsystem <code class="usage-code">UAnimationBudgetAllocator</code> via <code class="usage-code">UAnimationBudgetBlueprintLibrary::EnableAnimationBudget</code> (or <code class="usage-code">a.Budget.Enabled 1</code>).</li><li>Set the per-frame millisecond budget in <code class="usage-code">DefaultEngine.ini</code> (<code class="usage-code">UAnimationBudgetAllocatorParameters</code> / <code class="usage-code">a.Budget.BudgetMs</code>) and scale <code class="usage-code">USkeletalMeshComponentBudgeted</code> Significance by distance/importance.</li><li>Use <code class="usage-code">stat Animation</code> / Insights to confirm skeletal tick is throttled; low-significance meshes drop or skip ticks when the budget is spent.</li><li>A plain <code class="usage-code">USkeletalMeshComponent</code> is not registered — only budgeted components join the allocator.</li></ol><p class="usage-note">Throttles animation ticks on budgeted components; it is not AnimSequence compression or Animation Sharing.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AnimationBudgetAllocator</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AnimationBudgetAllocator/AnimationBudgetAllocator.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
