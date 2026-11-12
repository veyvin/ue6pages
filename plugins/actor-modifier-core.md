---
layout: default
title: Actor 修改器核心 / Actor Modifier Core
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Actor Modifier Core</div>
      <div class="hero-title-cn">Actor 修改器核心 · 在 actor 上使用修饰符对象来应用自定义行为</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/ActorModifierCore/ActorModifierCore.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">在 actor 上使用修饰符对象来应用自定义行为</div><div class="lang-content">Use modifier objects on actors to apply a custom behavior</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Core 是最底层运行时：容器、字符串、模块加载、日志、委托、平台抽象。不依赖 Engine；所有其他模块最终都建立在它上面。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：ActorModifierCore, ActorModifierCoreBlueprint, ActorModifierCoreEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Core is the lowest runtime layer: containers, strings, module loading, logging, delegates, and platform abstraction. It does not depend on Engine; everything else sits on it.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: ActorModifierCore, ActorModifierCoreBlueprint, ActorModifierCoreEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Actor Modifier Core</code>（<code class="usage-code">ActorModifierCore</code>、<code class="usage-code">ActorModifierCoreBlueprint</code>、<code class="usage-code">ActorModifierCoreEditor</code>）；要真正的布局/渲染修改器还需同时启用 <code class="usage-code">Actor Modifier</code>。</li><li>在关卡中选中 Actor，打开 Details 里由 <code class="usage-code">ActorModifierCoreEditor</code> 绘制的 Modifier 栈（不是 Sequencer 也不是 nDisplay 面板）。</li><li>用 Add Modifier 往栈上挂修改器对象，由 Core 按栈顺序求值。</li><li>蓝图侧通过 <code class="usage-code">ActorModifierCoreBlueprint</code> 启用/禁用或刷新栈，不要把它当摄像机追踪插件。</li><li>自定义修改器应继承 Core 的 Modifier 基类并放在项目模块；<code class="usage-code">ActorModifierCoreEditor</code> 仅 Editor Target。</li></ol><p class="usage-note">Core 只提供修改器栈框架，单独启用看不到布局/渲染成品修改器。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Actor Modifier Core</code> (<code class="usage-code">ActorModifierCore</code>, <code class="usage-code">ActorModifierCoreBlueprint</code>, <code class="usage-code">ActorModifierCoreEditor</code>); turn on <code class="usage-code">Actor Modifier</code> as well if you need stock layout/rendering modifiers.</li><li>Select a level actor and use the Modifier stack in Details (drawn by <code class="usage-code">ActorModifierCoreEditor</code>) — not Sequencer or nDisplay.</li><li>Click Add Modifier to push modifier objects onto the stack; Core evaluates them in stack order.</li><li>From Blueprint, use <code class="usage-code">ActorModifierCoreBlueprint</code> to enable, disable, or refresh the stack; this is not a camera-tracking plugin.</li><li>Subclass Core’s modifier base in your module for custom modifiers; keep <code class="usage-code">ActorModifierCoreEditor</code> on an Editor target only.</li></ol><p class="usage-note">Core is only the modifier-stack framework; stock layout/rendering modifiers live in the Actor Modifier plugin.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">ActorModifierCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ActorModifierCoreBlueprint</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ActorModifierCoreEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/ActorModifierCore/ActorModifierCore.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
