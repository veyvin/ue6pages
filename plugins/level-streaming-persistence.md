---
layout: default
title: 关卡流持久化 / Level Streaming Persistence
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">L</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Level Streaming Persistence</div>
      <div class="hero-title-cn">关卡流持久化 · 持久世界状态的实验框架：参与者和子对象属性值、参与者被破坏的状态</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Uncategorized</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.2</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/LevelStreamingPersistence/LevelStreamingPersistence.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">持久世界状态的实验框架：参与者和子对象属性值、参与者被破坏的状态以及参与者重生。状态与流级别相关联，并且可选地与持久级别相关联。</div><div class="lang-content">An experimental framework for persisting world state: actor and subobject property values, actor destroyed states, and actor respawning. State is associated with streaming levels, and optionally the persistent level.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：持久世界状态的实验框架：参与者和子对象属性值、参与者被破坏的状态以及参与者重生。状态与流级别相关联，并且可选地与持久级别相关联。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：LevelStreamingPersistence。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: An experimental framework for persisting world state: actor and subobject property values, actor destroyed states, and actor respawning. State is associated with streaming levels, and optionally the persistent level.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: LevelStreamingPersistence. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 Experimental 的 <code class="usage-code">Level Streaming Persistence</code>（模块 <code class="usage-code">LevelStreamingPersistence</code>）。</li><li>用它持久化世界状态：Actor/子对象属性、被破坏状态、Actor 重生。</li><li>状态与流送关卡关联（可选与持久关卡关联），卸载/重载后恢复。</li><li>Experimental：接口可能变动；面向开放世界的大世界状态持久化。</li></ol><p class="usage-note">随流送关卡持久化世界状态（属性/破坏/重生），开放世界用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable Experimental <code class="usage-code">Level Streaming Persistence</code> (module <code class="usage-code">LevelStreamingPersistence</code>).</li><li>Use it to persist world state: actor/subobject properties, destroyed states, and actor respawning.</li><li>State is associated with streaming levels (optionally with persistent levels) and restored after unload/reload.</li><li>Experimental: contract may change; aimed at large-world state persistence.</li></ol><p class="usage-note">Persists world state (properties/destruction/respawn) with streaming levels, for open worlds.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">LevelStreamingPersistence</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/LevelStreamingPersistence/LevelStreamingPersistence.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
