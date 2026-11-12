---
layout: default
title: 意义经理 / Significance Manager
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">S</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Significance Manager</div>
      <div class="hero-title-cn">意义经理 · 重要性管理器插件提供了一个可扩展的框架，允许游戏计算对象的重要性</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Performance</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/SignificanceManager/SignificanceManager.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">重要性管理器插件提供了一个可扩展的框架，允许游戏计算对象的重要性并更改响应行为。</div><div class="lang-content">The significance manager plugin provides an extensible framework for allowing games to calculate the significance of an object and change behavior in response.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：重要性管理器插件提供了一个可扩展的框架，允许游戏计算对象的重要性并更改响应行为。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：SignificanceManager。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: The significance manager plugin provides an extensible framework for allowing games to calculate the significance of an object and change behavior in response.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: SignificanceManager. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Significance Manager</code>（模块 <code class="usage-code">SignificanceManager</code>）。</li><li>它提供可扩展框架：计算对象的重要性并据此改变行为（如降频/关闭远处对象的更新）。</li><li>为对象注册意义值计算，按重要性分档调整 Tick/渲染/逻辑开销。</li><li>属性能优化框架；适合大场景降本。</li></ol><p class="usage-note">计算对象重要性并据此调行为的可扩展框架（性能优化）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Significance Manager</code> (module <code class="usage-code">SignificanceManager</code>).</li><li>It provides an extensible framework to compute object significance and change behavior accordingly (e.g. throttle/disable far objects&#x27; updates).</li><li>Register significance computation for objects and tier their Tick/render/logic cost by importance.</li><li>It is a performance-optimization framework; good for cost reduction in large scenes.</li></ol><p class="usage-note">An extensible framework computing object significance to adjust behavior (perf optimization).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">SignificanceManager</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/SignificanceManager/SignificanceManager.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
