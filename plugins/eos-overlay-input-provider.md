---
layout: default
title: EOS 覆盖输入提供商 / EOS Overlay Input Provider
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">EOS Overlay Input Provider</div>
      <div class="hero-title-cn">EOS 覆盖输入提供商 · 负责向 EOSSDK Overlay 提供输入转发。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Online Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Online/EOSOverlayInputProvider/EOSOverlayInputProvider.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">负责向 EOSSDK Overlay 提供输入转发。</div><div class="lang-content">Responsible for providing input forwarding to the EOSSDK Overlay.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：负责向 EOSSDK Overlay 提供输入转发。</p><p>属于在线子系统 / 平台服务。</p><p>它打包的模块包括：EOSOverlayInputProvider。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Responsible for providing input forwarding to the EOSSDK Overlay.</p><p>Part of Online Subsystem / platform services.</p><p>It ships these modules: EOSOverlayInputProvider. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">EOS Overlay Input Provider</code>，与 <code class="usage-code">OnlineSubsystemEOS</code> / EOS SDK 一起使用。</li><li>确认 <code class="usage-code">DefaultEngine.ini</code> 里 EOS 已配好凭证并初始化，overlay 本身是 EOSSDK 渲染的。</li><li>游戏运行且已登录 EOS 后按 <code class="usage-code">Shift+F3</code> 呼出 EOS overlay，该插件把鼠标/键盘输入转发给它，让你能在里面操作。</li><li>若 overlay 里点不动、输入无响应，检查此插件是否启用——喂输入给 EOSSDK Overlay 正是它的职责。</li></ol><p class="usage-note">它只做输入转发，不渲染 overlay、也不管登录；overlay 要能用，前提是 EOS SDK 本身已初始化并运行在游戏进程里。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">EOS Overlay Input Provider</code> alongside <code class="usage-code">OnlineSubsystemEOS</code> / the EOS SDK.</li><li>Confirm EOS is configured with credentials and initialized in <code class="usage-code">DefaultEngine.ini</code>; the overlay itself is drawn by the EOSSDK.</li><li>With the game running and EOS logged in, press <code class="usage-code">Shift+F3</code> to bring up the EOS overlay — this plugin forwards mouse/keyboard input into it so it&#x27;s usable.</li><li>If clicks/keypresses do nothing in the overlay, check this plugin is enabled — feeding input to the EOSSDK Overlay is exactly its job.</li></ol><p class="usage-note">It only forwards input — it doesn&#x27;t render the overlay or handle login; the overlay works only if the EOS SDK is initialized in the game process.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">EOSOverlayInputProvider</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Online/EOSOverlayInputProvider/EOSOverlayInputProvider.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
