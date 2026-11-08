---
layout: default
title: 配置设置工具集 / ConfigSettingsToolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">ConfigSettingsToolset</div>
      <div class="hero-title-cn">配置设置工具集 · 用于通过 AI 工具集注册表列出、检查和编辑配置设置部分的工具集</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/ConfigSettingsToolset/ConfigSettingsToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于通过 AI 工具集注册表列出、检查和编辑配置设置部分的工具集。</div><div class="lang-content">Toolset for listing, inspecting, and editing Config Settings sections via the AI Toolset Registry.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于通过 AI 工具集注册表列出、检查和编辑配置设置部分的工具集。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：ConfigSettingsToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Toolset for listing, inspecting, and editing Config Settings sections via the AI Toolset Registry.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: ConfigSettingsToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">ConfigSettingsToolset</code>，并打开 <code class="usage-code">Toolset Registry</code> / 编辑器 AI（或 MCP）客户端。</li><li>在助手里选用 Config Settings 工具集，列出 <code class="usage-code">DefaultEngine.ini</code> / <code class="usage-code">DefaultGame.ini</code> / <code class="usage-code">DefaultEditor.ini</code> 等配置**段**，不要去关卡里找组件。</li><li>对某一段（例如 <code class="usage-code">/Script/Engine.RendererSettings</code>）做 inspect，核对键值是否等于 <code class="usage-code">Project Settings</code> 里看到的项。</li><li>用工具集的 edit 接口改键并写回对应 <code class="usage-code">.ini</code>（或 Saved/Config 覆盖层），再重开 Project Settings 或重启编辑器确认生效。</li><li>实验性 AI 工具，不要加入 Game Target；改 ini 前先提交版本控制。</li></ol><p class="usage-note">按配置段读写 `.ini`，不是控制台 `stat` 命令，也不是 Project Settings 面板替代品。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">ConfigSettingsToolset</code> and turn on <code class="usage-code">Toolset Registry</code> / the editor AI (or MCP) client.</li><li>In the assistant, pick the Config Settings toolset and list config **sections** in <code class="usage-code">DefaultEngine.ini</code> / <code class="usage-code">DefaultGame.ini</code> / <code class="usage-code">DefaultEditor.ini</code> — not a level component.</li><li>Inspect one section (for example <code class="usage-code">/Script/Engine.RendererSettings</code>) and check keys against <code class="usage-code">Project Settings</code>.</li><li>Edit keys through the toolset write API so they land in the matching <code class="usage-code">.ini</code> (or Saved/Config overlay), then reopen Project Settings or restart to confirm.</li><li>Experimental AI tools — not a Game target. Commit version control before rewriting ini files.</li></ol><p class="usage-note">Reads/writes `.ini` sections; not console `stat` commands and not a replacement Project Settings UI.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ConfigSettingsToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/ConfigSettingsToolset/ConfigSettingsToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
