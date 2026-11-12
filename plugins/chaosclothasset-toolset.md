---
layout: default
title: ChaosClothAsset 工具集 / ChaosClothAsset Toolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">ChaosClothAsset Toolset</div>
      <div class="hero-title-cn">ChaosClothAsset 工具集 · 用于创建 ChaosClothAsset 服装并将其分配给骨架网</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Cloth</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">—</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/ChaosClothAssetToolset/ChaosClothAssetToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于创建 ChaosClothAsset 服装并将其分配给骨架网格物体的 AI 代理工具。</div><div class="lang-content">AI agent tools for creating and assigning ChaosClothAsset clothing to skeletal meshes.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Chaos 是引擎默认物理与破坏求解器（刚体、布料、破碎、字段）。相关插件把编辑器工具和运行时求解接到关卡里的几何体上。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：ChaosClothAssetToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Chaos is the default physics and destruction solver (rigid body, cloth, fracture, fields). Related plugins connect editor tools and the runtime solver to level geometry.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: ChaosClothAssetToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">ChaosClothAsset Toolset</code>（模块 <code class="usage-code">ChaosClothAssetToolset</code>）并重启。它是给编辑器 AI 代理调用的工具，不是运行时布料求解器。</li><li>同时打开 <code class="usage-code">Chaos Cloth Asset</code>（以及要用套装时的 <code class="usage-code">Chaos Outfit Asset</code>），否则代理创建的资产无法求值。</li><li>在编辑器 AI / Agent 会话里让它「用指定骨架网格创建 ChaosClothAsset 并分配到角色」。工具集会走创建 Cloth 资产、绑骨骼、赋 Chaos Cloth 组件的流程。</li><li>生成后打开 Cloth 资产的 Dataflow 检查仿真网格、权重图和碰撞体，再 PIE 角色；不要把工具集输出直接当 Shipping 服装。</li><li>不要把 <code class="usage-code">ChaosClothAssetToolset</code> 写进游戏 <code class="usage-code">Build.cs</code> 或 Shipping 插件列表；只留在编辑器 Toolsets 目录。</li></ol><p class="usage-note">编辑器 AI 工具集：创建并分配 ChaosClothAsset。不含求解器，不要当布料运行时插件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">ChaosClothAsset Toolset</code> (module <code class="usage-code">ChaosClothAssetToolset</code>) and restart. It is an editor AI-agent toolbox, not a runtime cloth solver.</li><li>Also enable <code class="usage-code">Chaos Cloth Asset</code> (and <code class="usage-code">Chaos Outfit Asset</code> if assembling outfits) or assets the agent creates cannot evaluate.</li><li>In an editor AI / Agent session, ask it to create a <code class="usage-code">ChaosClothAsset</code> for a given skeletal mesh and assign it on the character. The toolset runs create / bind / assign through a Chaos Cloth component.</li><li>Open the new Cloth asset Dataflow and verify sim mesh, weight maps, and colliders, then PIE the character. Do not treat toolset output as Shipping wardrobe.</li><li>Do not add <code class="usage-code">ChaosClothAssetToolset</code> to game <code class="usage-code">Build.cs</code> or Shipping plugin lists; it stays under editor Toolsets.</li></ol><p class="usage-note">Editor AI toolset for creating and assigning ChaosClothAsset. No solver; not a runtime cloth plugin.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ChaosClothAssetToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/ChaosClothAssetToolset/ChaosClothAssetToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
