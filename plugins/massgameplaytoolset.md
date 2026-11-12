---
layout: default
title: MassGameplay工具集 / MassGameplayToolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">MassGameplayToolset</div>
      <div class="hero-title-cn">MassGameplay工具集 · 用于通过 AI 工具集注册表导航质量实体配置资产及其特征的工具集</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span><span class="chip">Epic Games</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/MassGameplayToolset/MassGameplayToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于通过 AI 工具集注册表导航质量实体配置资产及其特征的工具集。</div><div class="lang-content">Toolset for navigating Mass entity config assets and their traits via the AI Toolset Registry.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于通过 AI 工具集注册表导航质量实体配置资产及其特征的工具集。</p><p>Mass 家族：ECS 风格的大规模实体（碎片、处理器、可视化或 AI）。不要按普通 Actor 组件去理解。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：MassGameplayToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Toolset for navigating Mass entity config assets and their traits via the AI Toolset Registry.</p><p>Mass family: ECS-style mass entities (fragments, processors, debug, or AI) — not a typical Actor component.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: MassGameplayToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">MassGameplayToolset</code>（模块 <code class="usage-code">MassGameplayToolset</code>），面向 AI Toolset Registry。</li><li>让 AI 助手通过 Toolset Registry 导航 Mass 实体配置资产及其特征（traits）。</li><li>在已启用 Mass 的项目里使用，辅助检索/理解 Mass 配置。</li><li>这是开发期工具集，不是运行时功能；Experimental。</li></ol><p class="usage-note">给 AI 工具链用的 Mass 配置导航工具集。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">MassGameplayToolset</code> (module <code class="usage-code">MassGameplayToolset</code>); it targets the AI Toolset Registry.</li><li>Let AI assistants navigate Mass entity config assets and their traits through the Toolset Registry.</li><li>Use it in Mass-enabled projects to help inspect/understand Mass config.</li><li>It is a development-time toolset, not a runtime feature; Experimental.</li></ol><p class="usage-note">A Mass config navigation toolset for the AI toolchain.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">MassGameplayToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/MassGameplayToolset/MassGameplayToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
