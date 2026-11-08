---
layout: default
title: 新郎 / Groom
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Groom</div>
      <div class="hero-title-cn">新郎 · 新郎的渲染和模拟</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Geometry</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">7</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/HairStrands/HairStrands.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">新郎的渲染和模拟</div><div class="lang-content">Rendering and simulation of grooms</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：新郎的渲染和模拟</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：HairStrandsCore, HairStrandsDeformer, HairStrandsRuntime, HairStrandsEditor, HairCardGeneratorFramework, HairStrandsDataflow, HairStrandsSolver。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Rendering and simulation of grooms</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: HairStrandsCore, HairStrandsDeformer, HairStrandsRuntime, HairStrandsEditor, HairCardGeneratorFramework, HairStrandsDataflow, HairStrandsSolver. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Groom</code>（模块 <code class="usage-code">HairStrandsCore</code>、<code class="usage-code">HairStrandsRuntime</code>、<code class="usage-code">HairStrandsEditor</code>、<code class="usage-code">HairStrandsSolver</code> 等）。</li><li>导入 Groom 资产（发丝/发卡），赋给骨架网格的 Groom 组件。</li><li>配置渲染与模拟（绑定、重力、碰撞），PIE 里查看头发随头动与风动效果。</li><li>Game 模块依赖运行时模块；<code class="usage-code">HairStrandsEditor</code>、Dataflow 等编辑器模块只进 Editor Target。</li></ol><p class="usage-note">发丝(Groom)的渲染与模拟，替代旧毛发方案。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Groom</code> (modules <code class="usage-code">HairStrandsCore</code>, <code class="usage-code">HairStrandsRuntime</code>, <code class="usage-code">HairStrandsEditor</code>, <code class="usage-code">HairStrandsSolver</code>, etc.).</li><li>Import a Groom asset (strands/cards) and assign it to the Groom component on the skeletal mesh.</li><li>Configure rendering and simulation (binding, gravity, collision) and PIE to see hair follow head motion and wind.</li><li>Game modules depend on runtime modules; editor ones like <code class="usage-code">HairStrandsEditor</code> and Dataflow go to Editor targets only.</li></ol><p class="usage-note">Groom (hair strands) rendering and simulation, replacing older hair solutions.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (7)</div><div class="module-item"><span class="dot"></span><span class="name mono">HairStrandsCore</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HairStrandsDeformer</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HairStrandsRuntime</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HairStrandsEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HairCardGeneratorFramework</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HairStrandsDataflow</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">HairStrandsSolver</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/HairStrands/HairStrands.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
