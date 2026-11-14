---
layout: default
title: 演员修改器 / Actor Modifier
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Actor Modifier</div>
      <div class="hero-title-cn">演员修改器 · 基于ActorModifierCore插件的actor修改器的实</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">4</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/ActorModifier/ActorModifier.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">基于ActorModifierCore插件的actor修改器的实际实现</div><div class="lang-content">Actual implementation of modifiers for actors based on ActorModifierCore plugin</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：基于ActorModifierCore插件的actor修改器的实际实现</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：ActorModifier, ActorModifierEditor, ActorModifierLayout, ActorModifierRendering。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Actual implementation of modifiers for actors based on ActorModifierCore plugin</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: ActorModifier, ActorModifierEditor, ActorModifierLayout, ActorModifierRendering. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>同时启用 <code class="usage-code">Actor Modifier Core</code> 与 <code class="usage-code">Actor Modifier</code>（<code class="usage-code">ActorModifier</code>、<code class="usage-code">ActorModifierLayout</code>、<code class="usage-code">ActorModifierRendering</code>）。</li><li>选中关卡 Actor，在 Details 的 Modifier 栈点 Add，加入 Layout（阵列/变换）或 Rendering（材质/可见性）类修改器。</li><li>改修改器参数并看视口即时结果：多实例排布走 <code class="usage-code">ActorModifierLayout</code>，外观覆盖走 <code class="usage-code">ActorModifierRendering</code>。</li><li>调整栈顺序（自上而下求值），并单独开关某一个修改器做对比。</li><li>这是虚拟制片场景布置工具，不要当成 Gameplay Ability 或关卡序列。</li><li><code class="usage-code">ActorModifierEditor</code> 只进 Editor Target。</li></ol><p class="usage-note">没有 Core 插件时，本插件的具体修改器无法挂到 Actor 栈上。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable both <code class="usage-code">Actor Modifier Core</code> and <code class="usage-code">Actor Modifier</code> (<code class="usage-code">ActorModifier</code>, <code class="usage-code">ActorModifierLayout</code>, <code class="usage-code">ActorModifierRendering</code>).</li><li>Select a level actor, open the Modifier stack in Details, and Add a Layout (array/transform) or Rendering (material/visibility) modifier.</li><li>Tweak parameters in the viewport: instance layouts come from <code class="usage-code">ActorModifierLayout</code>, look overrides from <code class="usage-code">ActorModifierRendering</code>.</li><li>Reorder the stack (top-to-bottom evaluation) and toggle individual modifiers to compare.</li><li>This is a virtual-production layout tool, not a Gameplay Ability or level sequence.</li><li>Keep <code class="usage-code">ActorModifierEditor</code> on an Editor target only.</li></ol><p class="usage-note">Without Actor Modifier Core, these concrete modifiers cannot attach to an actor stack.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (4)</div><div class="module-item"><span class="dot"></span><span class="name mono">ActorModifier</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ActorModifierEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ActorModifierLayout</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ActorModifierRendering</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/ActorModifier/ActorModifier.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
