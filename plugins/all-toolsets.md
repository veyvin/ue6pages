---
layout: default
title: 所有工具集 / All Toolsets
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">All Toolsets</div>
      <div class="hero-title-cn">所有工具集 · 依赖于所有工具集插件的聚合器插件。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">0</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/AllToolsets/AllToolsets.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">依赖于所有工具集插件的聚合器插件。</div><div class="lang-content">Aggregator plugin that depends on all Toolsets plugins.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：依赖于所有工具集插件的聚合器插件。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Aggregator plugin that depends on all Toolsets plugins.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 聚合插件 <code class="usage-code">All Toolsets</code>（<code class="usage-code">AllToolsets.uplugin</code>，无模块），它会依赖目录下全部 Toolset 插件。</li><li>同时启用 <code class="usage-code">AI Assistant</code> 并重启，让 Registry 一次性挂上 <code class="usage-code">AIModuleToolset</code>、各类检查/改写 Toolset 等。</li><li>在助手面板试一条会调用工具的请求（例如描述当前 Widget/行为树），确认工具列表远多于只开单个 Toolset。</li><li>体积大、仅编辑器：按需改开单个 Toolset（如只要 AI 就开 <code class="usage-code">AIModuleToolset</code>），避免无谓加载。</li><li>禁止写入游戏 Target 或包装；这不是关卡工具窗口。</li></ol><p class="usage-note">一键启用全部编辑器 AI Toolset 的聚合器，无运行时 API。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental aggregator <code class="usage-code">All Toolsets</code> (<code class="usage-code">AllToolsets.uplugin</code>, no modules); it depends on every Toolset plugin in that tree.</li><li>Enable <code class="usage-code">AI Assistant</code> and restart so the registry mounts <code class="usage-code">AIModuleToolset</code> and the other inspect/edit toolsets at once.</li><li>In the assistant, run a tool-using prompt (describe the current Widget/Behavior Tree) and confirm far more tools than a single toolset.</li><li>It is heavy and editor-only: prefer a single toolset such as <code class="usage-code">AIModuleToolset</code> when you do not need everything.</li><li>Never add it to a game target or package; it is not a level-editing window.</li></ol><p class="usage-note">Aggregator that enables every editor AI toolset; no runtime API.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/AllToolsets/AllToolsets.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
