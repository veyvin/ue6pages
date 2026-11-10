---
layout: default
title: 控制装置知识库 / Control Rig Knowledge Base
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Control Rig Knowledge Base</div>
      <div class="hero-title-cn">控制装置知识库 · Control Rig 的知识库提供程序：Control Rig</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Animation</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/ControlRigKnowledgeBase/ControlRigKnowledgeBase.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Control Rig 的知识库提供程序：Control Rig 图形可以放置的节点目录。</div><div class="lang-content">Knowledge base providers for Control Rig: the catalogue of nodes a Control Rig graph can place.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Control Rig 是引擎里的绑定与程序化动画工具：在绑定图里做 FK/IK、空间切换，可在 Sequencer 里关键帧，也可在运行时驱动。常和 IK Rig、重定向一起做角色动画。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：ControlRigKnowledgeBase。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine</a></p></div><div class="lang-content"><p>Control Rig is Unreal’s rigging and procedural animation toolkit: FK/IK and space switching in a rig graph, keyable in Sequencer or driven at runtime. It is often paired with IK Rig and retargeting.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: ControlRigKnowledgeBase. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/control-rig-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">Control Rig Knowledge Base</code>（模块 <code class="usage-code">ControlRigKnowledgeBase</code>），并同时保持 <code class="usage-code">Control Rig</code> 与编辑器 AI 助手可用。</li><li>打开任意 <code class="usage-code">Control Rig</code> 资产的 Rig Graph，确认能手动放置 <code class="usage-code">RigVM</code> 节点（FK、IK、Set Transform 等）——知识库描述的就是这份节点目录。</li><li>在编辑器 AI / Toolset 会话里请求「列出可放置的 Control Rig 节点」或「插入某条 Rig Unit」：助手通过本插件的 provider 读目录，而不是猜节点名。</li><li>目录变更随引擎 <code class="usage-code">RigVM</code> 单元走；不要在游戏模块引用 <code class="usage-code">ControlRigKnowledgeBase</code>，它只服务编辑器知识检索。</li></ol><p class="usage-note">给 AI 的节点目录，不是 Modular Control Rig 模块资源包。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">Control Rig Knowledge Base</code> (module <code class="usage-code">ControlRigKnowledgeBase</code>) and keep <code class="usage-code">Control Rig</code> plus the in-editor AI assistant available.</li><li>Open any <code class="usage-code">Control Rig</code> asset’s Rig Graph and confirm you can place <code class="usage-code">RigVM</code> nodes (FK, IK, Set Transform). That catalogue is what this plugin describes.</li><li>In an editor AI / Toolset session, ask to list placeable Control Rig nodes or insert a Rig Unit: the assistant reads this provider instead of guessing names.</li><li>The catalogue tracks engine <code class="usage-code">RigVM</code> units. Do not reference <code class="usage-code">ControlRigKnowledgeBase</code> from game modules — editor knowledge lookup only.</li></ol><p class="usage-note">AI node catalogue, not the Modular Control Rig content pack.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ControlRigKnowledgeBase</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/ControlRigKnowledgeBase/ControlRigKnowledgeBase.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
