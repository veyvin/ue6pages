---
layout: default
title: 用于虚幻引擎的 Microsoft GDK 插件的配置 / Configuration for Microsoft GDK Plug-ins for Unreal Engine
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Configuration for Microsoft GDK Plug-ins for Unreal Engine</div>
      <div class="hero-title-cn">用于虚幻引擎的 Microsoft GDK 插件的配置 · Microsoft Gaming Runtime 和 Micro</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Windows/MSGamingSupport/MSGamingSupport.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Microsoft Gaming Runtime 和 Microsoft Game Store 插件。</div><div class="lang-content">Microsoft Gaming Runtime and Microsoft Game Store plugins.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Engine 模块是游戏框架核心：Actor、Pawn、PlayerController、World、组件、材质与关卡流送的运行时实现。绝大多数游戏模块都会直接或间接依赖它。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：MSGamingSupportEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>The Engine module is the gameplay-framework core: Actor, Pawn, PlayerController, World, components, materials, and streaming at runtime. Almost every game module depends on it, directly or not.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: MSGamingSupportEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Configuration for Microsoft GDK Plug-ins for Unreal Engine</code>（描述符 <code class="usage-code">MSGamingSupport.uplugin</code>，模块 <code class="usage-code">MSGamingSupportEditor</code>）。</li><li>本机安装 Microsoft GDK，然后打开 <code class="usage-code">Edit &gt; Project Settings</code> 的 Windows / GDK / Microsoft Game Store 相关页，填 Title ID、Sandbox、包标识。</li><li>这些设置给后续 GDK / Xbox / Microsoft Store 运行时插件用；先在这里配好再 Packaged 到 GDK 目标。</li><li>用 <code class="usage-code">File &gt; Package Project</code> 或平台 Project Launcher 打 Windows GDK / Xbox 包，确认清单读到刚才的 Store/Runtime 字段。</li><li><code class="usage-code">MSGamingSupportEditor</code> 只属于 Editor Target；游戏模块不要依赖它，运行时走各 GDK 插件自己的模块。</li></ol><p class="usage-note">GDK/商店配置壳，不是 Xbox 输入或成就运行时。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Configuration for Microsoft GDK Plug-ins for Unreal Engine</code> (<code class="usage-code">MSGamingSupport.uplugin</code>, module <code class="usage-code">MSGamingSupportEditor</code>).</li><li>Install the Microsoft GDK locally, then fill Title ID, sandbox, and package identity under <code class="usage-code">Edit &gt; Project Settings</code> (Windows / GDK / Microsoft Game Store pages).</li><li>Later GDK / Xbox / Microsoft Store runtime plugins consume this config — set it here before packaging a GDK target.</li><li>Package with <code class="usage-code">File &gt; Package Project</code> or Project Launcher for Windows GDK / Xbox and confirm the manifest picked up those Store/Runtime fields.</li><li><code class="usage-code">MSGamingSupportEditor</code> is Editor-target only; game modules must not depend on it — runtime lives in the GDK plugins themselves.</li></ol><p class="usage-note">GDK/Store configuration shell, not Xbox input or achievements runtime.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">MSGamingSupportEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Windows/MSGamingSupport/MSGamingSupport.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
