---
layout: default
title: 通用UI工具集 / CommonUI ToolSet
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">CommonUI ToolSet</div>
      <div class="hero-title-cn">通用UI工具集 · 用于 CommonUI 激活和焦点路由的 AI 调试器工具集：可</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>UI</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/CommonUIToolset/CommonUIToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于 CommonUI 激活和焦点路由的 AI 调试器工具集：可激活树快照、焦点发散诊断、激活/路由事件记录和假设检验写入工具。</div><div class="lang-content">AI debugger toolset for CommonUI activation & focus routing: activatable-tree snapshots, focus divergence diagnosis, activation/routing event recording, and hypothesis-testing write tools.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于 CommonUI 激活和焦点路由的 AI 调试器工具集：可激活树快照、焦点发散诊断、激活/路由事件记录和假设检验写入工具。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：CommonUIToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: AI debugger toolset for CommonUI activation & focus routing: activatable-tree snapshots, focus divergence diagnosis, activation/routing event recording, and hypothesis-testing write tools.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: CommonUIToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>先启用 <code class="usage-code">Common UI Plugin</code>，再开实验性 <code class="usage-code">CommonUI ToolSet</code>（模块 <code class="usage-code">CommonUIToolset</code>）。这是给编辑器 AI/自动化的调试工具集，不是游戏 UI 库。</li><li>在 PIE 里打开至少一层 <code class="usage-code">UCommonActivatableWidget</code>，让 Action Router 有激活树。</li><li>让编辑器助手调用 Toolset 的只读工具：抓 activatable-tree 快照、对比期望焦点与 <code class="usage-code">UCommonUIActionRouterBase</code> 实际焦点（focus divergence）、录制激活/路由事件。</li><li>对假设做写入测试（强制激活某页、改焦点目标）后立刻再拍一帧快照，确认栈序与 <code class="usage-code">GetDesiredFocusTarget</code> 一致。</li><li>不要把 <code class="usage-code">CommonUIToolset</code> 写进 Shipping <code class="usage-code">Build.cs</code> 或打包进游戏；工具契约随 Experimental 夜构建可能变。</li></ol><p class="usage-note">调试 CommonUI 激活树与焦点路由的 AI Toolset，不能替代 `CommonUI` 控件。无玩家可见面板。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Common UI Plugin</code> first, then experimental <code class="usage-code">CommonUI ToolSet</code> (module <code class="usage-code">CommonUIToolset</code>). It is an editor AI/automation debugger, not a game UI library.</li><li>PIE with at least one <code class="usage-code">UCommonActivatableWidget</code> so the Action Router has an activation tree.</li><li>Have the editor assistant call the toolset’s read tools: snapshot the activatable tree, diagnose focus divergence versus <code class="usage-code">UCommonUIActionRouterBase</code>, and record activation/routing events.</li><li>After a write/hypothesis test (force-activate a page, retarget focus), snapshot again and check stack order against <code class="usage-code">GetDesiredFocusTarget</code>.</li><li>Do not add <code class="usage-code">CommonUIToolset</code> to Shipping <code class="usage-code">Build.cs</code> or cook it into the game. The Experimental contract can change on nightlies.</li></ol><p class="usage-note">AI toolset for CommonUI activation trees and focus routing — not a substitute for `CommonUI` widgets. No player-facing panel.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CommonUIToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/CommonUIToolset/CommonUIToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
