---
layout: default
title: 网络代码单元测试 - 虚幻引擎 / Netcode Unit Test - Unreal Engine
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">N</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Netcode Unit Test - Unreal Engine</div>
      <div class="hero-title-cn">网络代码单元测试 - 虚幻引擎 · 基于 Netcode 单元测试框架，利用虚幻引擎和一些基础虚幻引</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Networking</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/NetcodeUnitTest/NUTUnrealNUTUnrealEngine.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">基于 Netcode 单元测试框架，利用虚幻引擎和一些基础虚幻引擎游戏的单元测试</div><div class="lang-content">Exploit unit tests for Unreal Engine and some base Unreal Engine games, based on the Netcode Unit Test framework</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Engine 模块是游戏框架核心：Actor、Pawn、PlayerController、World、组件、材质与关卡流送的运行时实现。绝大多数游戏模块都会直接或间接依赖它。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：NUTUnrealEngine。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>The Engine module is the gameplay-framework core: Actor, Pawn, PlayerController, World, components, materials, and streaming at runtime. Almost every game module depends on it, directly or not.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: NUTUnrealEngine. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Netcode Unit Test - Unreal Engine</code>（模块 <code class="usage-code">NUTUnrealEngine</code>）。</li><li>它基于 Netcode 单元测试框架，包含针对引擎及部分基础 UE 游戏的漏洞利用单元测试。</li><li>在自动化里跑这些用例，验证网络代码安全性。</li><li>这是测试插件，不要打进发行版本。</li></ol><p class="usage-note">针对引擎/基础游戏的网络漏洞利用单元测试。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Netcode Unit Test - Unreal Engine</code> (module <code class="usage-code">NUTUnrealEngine</code>).</li><li>Based on the Netcode Unit Test framework, it contains exploit unit tests for the engine and some base UE games.</li><li>Run these cases in automation to validate netcode security.</li><li>It is a test plugin; do not ship it in release builds.</li></ol><p class="usage-note">Exploit unit tests for the engine and base games.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">NUTUnrealEngine</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/NetcodeUnitTest/NUTUnrealNUTUnrealEngine.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
