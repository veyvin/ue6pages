---
layout: default
title: 代理插件工具集 / Agent Plugin Toolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Agent Plugin Toolset</div>
      <div class="hero-title-cn">代理插件工具集 · 通过 AI 工具集注册表读取 Claude 和 Codex 代理</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/AgentPluginToolset/AgentPluginToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">通过 AI 工具集注册表读取 Claude 和 Codex 代理插件以及工作目录指令文件。</div><div class="lang-content">Reads Claude and Codex agent plugins, plus working-directory instruction files, through the AI Toolset Registry.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：通过 AI 工具集注册表读取 Claude 和 Codex 代理插件以及工作目录指令文件。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：AgentPluginToolset, AgentPluginToolsetEditor, AgentPluginToolsetTests。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Reads Claude and Codex agent plugins, plus working-directory instruction files, through the AI Toolset Registry.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: AgentPluginToolset, AgentPluginToolsetEditor, AgentPluginToolsetTests. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Agent Plugin Toolset</code>（<code class="usage-code">AgentPluginToolset</code>、<code class="usage-code">AgentPluginToolsetEditor</code>），并同时打开 AI Toolset Registry。</li><li>在项目工作目录放入 Claude/Codex 代理插件清单，以及 <code class="usage-code">AGENTS.md</code> / <code class="usage-code">CLAUDE.md</code> 这类指令文件。</li><li>重启或刷新后，Registry 通过本插件枚举这些插件与工作目录指令。</li><li>在编辑器 AI 助手里确认工具已注册可用；这与 <code class="usage-code">AIModule</code> 行为树无关。</li><li><code class="usage-code">AgentPluginToolsetEditor</code> 仅 Editor Target；<code class="usage-code">AgentPluginToolsetTests</code> 用 Session Frontend 跑。</li></ol><p class="usage-note">Experimental 编辑器 Toolset，给 AI 助手读插件/指令，不进游戏包。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Agent Plugin Toolset</code> (<code class="usage-code">AgentPluginToolset</code>, <code class="usage-code">AgentPluginToolsetEditor</code>) together with the AI Toolset Registry.</li><li>Put Claude/Codex agent plugin manifests and working-directory instruction files such as <code class="usage-code">AGENTS.md</code> / <code class="usage-code">CLAUDE.md</code> in the project.</li><li>After restart or refresh, the Registry enumerates those plugins and instructions through this toolset.</li><li>Confirm the tools appear in the in-editor AI assistant; this is unrelated to <code class="usage-code">AIModule</code> behavior trees.</li><li>Keep <code class="usage-code">AgentPluginToolsetEditor</code> on an Editor target; run <code class="usage-code">AgentPluginToolsetTests</code> from Session Frontend.</li></ol><p class="usage-note">Experimental editor toolset that feeds the AI assistant; it is not a shipping game feature.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">AgentPluginToolset</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AgentPluginToolsetEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AgentPluginToolsetTests</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/AgentPluginToolset/AgentPluginToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
