---
layout: default
title: 通过 nDisplay 进行实时链接 / Live Link Over nDisplay
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">L</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Live Link Over nDisplay</div>
      <div class="hero-title-cn">通过 nDisplay 进行实时链接 · nDisplay 设置的 LiveLink 主题同步</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Misc</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/LiveLinkOvernDisplay/LiveLinkOverNDisplay.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">nDisplay 设置的 LiveLink 主题同步</div><div class="lang-content">LiveLink subjects synchronization for nDisplay setup</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>nDisplay 把一台场景渲染到多台同步的机器/窗口上，用于 LED 墙、洞穴、集群视口。和 Switchboard、Live Link、摄像机跟踪一起做虚拟制片。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：LiveLinkOverNDisplay。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">参考文档：<a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-in-unreal-engine</a></p></div><div class="lang-content"><p>nDisplay renders one scene across synchronized machines or windows for LED walls, CAVE, and cluster viewports. It is used in virtual production with Switchboard, Live Link, and camera tracking.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: LiveLinkOverNDisplay. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Docs: <a href="https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-in-unreal-engine" target="_blank" rel="noopener">https://dev.epicgames.com/documentation/en-us/unreal-engine/ndisplay-in-unreal-engine</a></p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Live Link Over nDisplay</code>（模块 <code class="usage-code">LiveLinkOverNDisplay</code>）。</li><li>它为 nDisplay 集群同步 Live Link 主体数据，让各渲染节点拿到一致的实时数据。</li><li>在多节点 nDisplay 虚拟制片环境里配置该同步。</li><li>属 nDisplay 数据同步，需 nDisplay 与 Live Link 已启用。</li></ol><p class="usage-note">nDisplay 集群的 Live Link 主体同步。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Live Link Over nDisplay</code> (module <code class="usage-code">LiveLinkOverNDisplay</code>).</li><li>It synchronizes Live Link subject data across the nDisplay cluster so every render node gets consistent real-time data.</li><li>Configure this sync in a multi-node nDisplay virtual production environment.</li><li>It is nDisplay data sync; nDisplay and Live Link must be enabled.</li></ol><p class="usage-note">Live Link subject sync for nDisplay clusters.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">LiveLinkOverNDisplay</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/LiveLinkOvernDisplay/LiveLinkOverNDisplay.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
