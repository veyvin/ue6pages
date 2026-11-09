---
layout: default
title: 混沌变形底座 / Chaos Deformable Base
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Chaos Deformable Base</div>
      <div class="hero-title-cn">混沌变形底座 · 混沌布料和可变形模拟资产的共享基础资产类别。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Physics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/ChaosDeformableBase/ChaosDeformableBase.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">混沌布料和可变形模拟资产的共享基础资产类别。</div><div class="lang-content">Shared base asset class for Chaos cloth and deformable simulation assets.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Chaos 是引擎默认物理与破坏求解器（刚体、布料、破碎、字段）。相关插件把编辑器工具和运行时求解接到关卡里的几何体上。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：ChaosDeformableBaseEngine, ChaosDeformableBaseTools。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Chaos is the default physics and destruction solver (rigid body, cloth, fracture, fields). Related plugins connect editor tools and the runtime solver to level geometry.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: ChaosDeformableBaseEngine, ChaosDeformableBaseTools. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Chaos Deformable Base</code>，作为 Flesh/可变形体的公共运行时底座。</li><li>游戏或插件模块若要调用可变形 API，在 <code class="usage-code">Build.cs</code> 依赖该底座，再依赖具体的 Chaos Flesh 等上层插件。</li><li>不要单独指望它提供可放置的 Actor；场景里放的是 Flesh 资产/组件。</li><li>编辑器工具走 Flesh Generator / Flesh 编辑器，不走这个 base 模块的 UI。</li></ol><p class="usage-note">可变形求解的底层库，最终用户应通过 Chaos Flesh 使用。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Chaos Deformable Base</code> as the shared runtime for Flesh/deformables.</li><li>If your module calls deformable APIs, depend on this base, then on Chaos Flesh (or similar) above it.</li><li>It does not ship a placeable actor; you place Flesh assets/components.</li><li>Authoring UI lives in Flesh Generator / Flesh editors, not this base module.</li></ol><p class="usage-note">Low-level deformable runtime; end users go through Chaos Flesh.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">ChaosDeformableBaseEngine</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ChaosDeformableBaseTools</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/ChaosDeformableBase/ChaosDeformableBase.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
