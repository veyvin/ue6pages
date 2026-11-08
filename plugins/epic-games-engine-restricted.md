---
layout: default
title: Epic Games 引擎受限 / Epic Games Engine Restricted
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Epic Games Engine Restricted</div>
      <div class="hero-title-cn">Epic Games 引擎受限 · Epic Games Engine 受限 API - 不适合公众</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Verse</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Verse/EpicGamesEngineRestricted/EpicGamesEngineRestricted.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Epic Games Engine 受限 API - 不适合公众使用</div><div class="lang-content">Epic Games Engine Restricted API - not for public use</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Engine 模块是游戏框架核心：Actor、Pawn、PlayerController、World、组件、材质与关卡流送的运行时实现。绝大多数游戏模块都会直接或间接依赖它。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：EpicGamesEngineRestricted。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>The Engine module is the gameplay-framework core: Actor, Pawn, PlayerController, World, components, materials, and streaming at runtime. Almost every game module depends on it, directly or not.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: EpicGamesEngineRestricted. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">Epic Games Engine Restricted</code> 是 Epic 内部受限 API（模块 <code class="usage-code">EpicGamesEngineRestricted</code>），明确标注“不适合公众使用”。</li><li>公开版 UE 里通常不提供或不允许启用，在插件列表里看不到/无法勾选是正常现象。</li><li>只有具备 Epic 内部权限的构建里，才能在编辑器中启用并引用该受限模块的接口。</li><li>即便能访问，也应严格隔离在内部工具链，绝不进入对外发布的项目或 Shipping 包。</li></ol><p class="usage-note">这是个“看得到名字但用不了”的插件，别指望在公开账号下启用；如果你的项目不依赖它，直接忽略即可。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">Epic Games Engine Restricted</code> is an Epic-internal restricted API (module <code class="usage-code">EpicGamesEngineRestricted</code>) explicitly marked &quot;not for public use&quot;.</li><li>Public UE builds usually don&#x27;t ship or allow enabling it; not appearing or being greyed out in the plugin list is expected.</li><li>Only in builds with Epic-internal access can you enable it in the editor and call the restricted module&#x27;s interfaces.</li><li>Even then, keep it strictly inside internal tooling and never let it into a public project or Shipping build.</li></ol><p class="usage-note">This is a name-only, effectively unusable plugin on public accounts; if your project doesn&#x27;t depend on it, just ignore it.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">EpicGamesEngineRestricted</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Verse/EpicGamesEngineRestricted/EpicGamesEngineRestricted.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
