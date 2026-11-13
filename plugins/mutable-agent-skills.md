---
layout: default
title: 可变的代理技能 / Mutable Agent Skills
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Mutable Agent Skills</div>
      <div class="hero-title-cn">可变的代理技能 · AI 代理使用 CustomizedObjectEditor.C</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Mutable</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/MutableAgentSkills/MutableAgentSkills.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">AI 代理使用 CustomizedObjectEditor.CustomizedObjectScriptingSubsystem 工具集创作可变可自定义对象的技能</div><div class="lang-content">AI agent skills for authoring Mutable Customizable Objects with the CustomizableObjectEditor.CustomizableObjectScriptingSubsystem toolset</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：AI 代理使用 CustomizedObjectEditor.CustomizedObjectScriptingSubsystem 工具集创作可变可自定义对象的技能</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：MutableAgentSkills。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: AI agent skills for authoring Mutable Customizable Objects with the CustomizableObjectEditor.CustomizableObjectScriptingSubsystem toolset</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: MutableAgentSkills. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Mutable Agent Skills</code>（模块 <code class="usage-code">MutableAgentSkills</code>）。</li><li>它让 AI 代理使用 <code class="usage-code">CustomizableObjectEditor.CustomizableObjectScriptingSubsystem</code> 工具集创作 Mutable 可自定义对象。</li><li>在 Mutable 角色/物件创作流程里用 AI 代理通过脚本子系统批量生成/编辑。</li><li>属 AI 工具链/Mutable 编辑自动化，非运行时功能。</li></ol><p class="usage-note">AI 代理创作 Mutable 可自定义对象的技能/工具集。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Mutable Agent Skills</code> (module <code class="usage-code">MutableAgentSkills</code>).</li><li>It lets AI agents author Mutable Customizable Objects using the <code class="usage-code">CustomizableObjectEditor.CustomizableObjectScriptingSubsystem</code> toolset.</li><li>In Mutable character/object authoring, use AI agents via the scripting subsystem to batch-generate/edit.</li><li>It is AI-toolchain/Mutable authoring automation, not a runtime feature.</li></ol><p class="usage-note">AI-agent skills for authoring Mutable Customizable Objects.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">MutableAgentSkills</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/MutableAgentSkills/MutableAgentSkills.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
