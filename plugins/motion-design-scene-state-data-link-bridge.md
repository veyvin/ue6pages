---
layout: default
title: 运动设计场景状态数据链路桥 / Motion Design Scene State Data Link Bridge
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Motion Design Scene State Data Link Bridge</div>
      <div class="hero-title-cn">运动设计场景状态数据链路桥 · 执行数据链接图的场景状态任务</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/SceneStateDataLink/SceneStateDataLink.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">执行数据链接图的场景状态任务</div><div class="lang-content">Scene State Tasks that execute Data Link Graphs</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：执行数据链接图的场景状态任务</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：SceneStateDataLink, SceneStateDataLinkEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Scene State Tasks that execute Data Link Graphs</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: SceneStateDataLink, SceneStateDataLinkEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Motion Design Scene State Data Link Bridge</code>（运行时 <code class="usage-code">SceneStateDataLink</code>，编辑器 <code class="usage-code">SceneStateDataLinkEditor</code>）。</li><li>它提供“执行数据链接图”的场景状态任务，把 Data Link 接进 Scene State。</li><li>在 Scene State 机里用这些任务触发数据链接图执行。</li><li>Game 模块依赖 <code class="usage-code">SceneStateDataLink</code>；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">执行数据链接图的场景状态任务桥。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Motion Design Scene State Data Link Bridge</code> (runtime <code class="usage-code">SceneStateDataLink</code>, editor <code class="usage-code">SceneStateDataLinkEditor</code>).</li><li>It provides Scene State tasks that execute Data Link graphs, bridging Data Link into Scene State.</li><li>In a Scene State machine, use these tasks to trigger data-link graph execution.</li><li>Game modules depend on <code class="usage-code">SceneStateDataLink</code>; editor modules go to Editor targets only.</li></ol><p class="usage-note">Scene State tasks that execute Data Link graphs.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">SceneStateDataLink</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SceneStateDataLinkEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/SceneStateDataLink/SceneStateDataLink.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
