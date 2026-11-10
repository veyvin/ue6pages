---
layout: default
title: 数据流代理 / DataflowAgent
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">DataflowAgent</div>
      <div class="hero-title-cn">数据流代理 · 用于编辑数据流图的 AI 代理工具集</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/DataflowAgent/DataflowAgent.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于编辑数据流图的 AI 代理工具集</div><div class="lang-content">AI Agent toolset for editing Dataflow graphs</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于编辑数据流图的 AI 代理工具集</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：DataflowAgent。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: AI Agent toolset for editing Dataflow graphs</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: DataflowAgent. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental Toolset <code class="usage-code">DataflowAgent</code>（模块 <code class="usage-code">DataflowAgent</code>），并同时打开 Dataflow 编辑器；这是给编辑器 AI 助手的写图工具，不是游戏子系统。</li><li>打开一个 <code class="usage-code">Dataflow</code> 资产，让助手处于可调用 Toolset 的会话（Editor AI / Agent 面板）。</li><li>让代理列出当前图节点、按类型添加节点、连接引脚或改字面量参数；核对图上确实出现了新节点而不是只生成了文本说明。</li><li>求值 Dataflow，确认代理改过的节点输出符合你的约束（例如不要删掉终端 Output 节点）。</li><li>用 Undo 回滚一次代理编辑，确认事务落在 Dataflow 资产上。</li><li>不要把 <code class="usage-code">DataflowAgent</code> 写进 Game Target 或 Shipping；接口随夜构建可能变。</li></ol><p class="usage-note">编辑器 AI 改 Dataflow 图的 Toolset，不进游戏包。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental Toolset <code class="usage-code">DataflowAgent</code> (module <code class="usage-code">DataflowAgent</code>) together with the Dataflow editor. These are write tools for the in-editor AI assistant, not a game subsystem.</li><li>Open a <code class="usage-code">Dataflow</code> asset and start an assistant session that can invoke Toolsets (Editor AI / Agent panel).</li><li>Ask the agent to list nodes, add nodes by type, wire pins, or edit literals; confirm new nodes appear on the graph, not just in chat text.</li><li>Evaluate the Dataflow and check that agent edits still satisfy your constraints (for example, terminal Output nodes remain).</li><li>Undo one agent edit and confirm the transaction landed on the Dataflow asset.</li><li>Do not link <code class="usage-code">DataflowAgent</code> into a Game target or Shipping build; the contract can change on nightlies.</li></ol><p class="usage-note">Editor-AI Toolset for mutating Dataflow graphs; not a shipping feature.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">DataflowAgent</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/DataflowAgent/DataflowAgent.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
