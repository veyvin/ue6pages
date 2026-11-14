---
layout: default
title: ICVFX / ICVFX
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">I</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">ICVFX</div>
      <div class="hero-title-cn">ICVFX · 方便地收集相机内 VFX 插件</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">0</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/ICVFX/ICVFX.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">方便地收集相机内 VFX 插件</div><div class="lang-content">Conveniently collects plugins for In-Camera VFX</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：方便地收集相机内 VFX 插件</p><p>虚拟制片显示家族：集群视口、同步、LED 墙或舞台控制。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Conveniently collects plugins for In-Camera VFX</p><p>Virtual-production display family: cluster views, sync, LED walls, or stage control.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">ICVFX</code> 插件，它本身不打包模块，只是便捷地集合 In-Camera VFX 相关插件。</li><li>在虚拟制片项目中借此一键带出 nDisplay、Live Link、Composure 等相关依赖。</li><li>配合舞台/摄像机/追踪使用；具体功能看被集合的各个子插件。</li><li>这是聚合型插件，真正的能力来自其收集的子插件。</li></ol><p class="usage-note">ICVFX 聚合插件（无自身模块），方便一次性启用相关插件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable the <code class="usage-code">ICVFX</code> plugin; it ships no modules itself and simply collects In-Camera VFX plugins for convenience.</li><li>In a virtual production project, use it to pull in related dependencies like nDisplay, Live Link, and Composure.</li><li>Use it alongside stage/camera/tracking; actual features come from the collected sub-plugins.</li><li>It is an aggregator plugin; real capability comes from the sub-plugins it gathers.</li></ol><p class="usage-note">An ICVFX aggregator (no own modules) to enable related plugins together.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/ICVFX/ICVFX.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
