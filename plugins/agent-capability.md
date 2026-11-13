---
layout: default
title: 代理能力 / Agent Capability
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Agent Capability</div>
      <div class="hero-title-cn">代理能力 · 被动发现已配置的代理插件和工作区功能。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/AgentCapability/AgentCapability.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">被动发现已配置的代理插件和工作区功能。</div><div class="lang-content">Passive discovery of configured agent plugin and workspace capabilities.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：被动发现已配置的代理插件和工作区功能。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：AgentCapability, AgentCapabilityTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Passive discovery of configured agent plugin and workspace capabilities.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: AgentCapability, AgentCapabilityTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Agent Capability</code>（<code class="usage-code">AgentCapability</code>），通常与编辑器 AI / Toolset 插件一起开。</li><li>本插件做被动发现：扫描已配置的 agent 插件和工作区能力，没有关卡 Actor 或 Window 面板工作流。</li><li>把 Claude/Codex 等 agent 清单和工作区说明放到项目约定目录，供发现逻辑读取。</li><li>需要回归时在 <code class="usage-code">Tools &gt; Session Frontend</code> 跑 <code class="usage-code">AgentCapabilityTests</code>，不要当游戏子系统调用。</li><li>发现结果给其他 agent/toolset 消费，而不是给你一条可玩的 AI 角色。</li></ol><p class="usage-note">Experimental 编辑器发现层，不进 Shipping，接口会随夜构建变化。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Agent Capability</code> (<code class="usage-code">AgentCapability</code>), usually together with editor AI / Toolset plugins.</li><li>It performs passive discovery of configured agent plugins and workspace capabilities; there is no level-actor or Window-panel workflow.</li><li>Place Claude/Codex agent manifests and workspace instruction files where the project expects them so discovery can read them.</li><li>Run <code class="usage-code">AgentCapabilityTests</code> from <code class="usage-code">Tools &gt; Session Frontend</code> when you need a regression; do not treat this as a game subsystem.</li><li>Other agent/toolset plugins consume the results; it does not spawn a playable AI character.</li></ol><p class="usage-note">Experimental editor discovery layer; it does not ship and the contract can change nightly.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AgentCapability</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AgentCapabilityTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/AgentCapability/AgentCapability.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
