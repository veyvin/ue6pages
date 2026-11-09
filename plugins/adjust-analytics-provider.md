---
layout: default
title: 调整分析提供商 / Adjust Analytics Provider
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Adjust Analytics Provider</div>
      <div class="hero-title-cn">调整分析提供商 · 调整分析提供商</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Analytics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Analytics/Adjust/Adjust.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">调整分析提供商</div><div class="lang-content">Adjust Analytics Provider</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：调整分析提供商</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AdjustEditor, AndroidAdjust, IOSAdjust。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Adjust Analytics Provider</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AdjustEditor, AndroidAdjust, IOSAdjust. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Adjust Analytics Provider</code>（<code class="usage-code">AndroidAdjust</code>、<code class="usage-code">IOSAdjust</code>、<code class="usage-code">AdjustEditor</code>）。</li><li>在 Adjust 控制台创建应用并复制 App Token。</li><li>在 <code class="usage-code">Project Settings</code> 的 Analytics 页，或 <code class="usage-code">DefaultEngine.ini</code> 的 <code class="usage-code">[Analytics]</code>，把 provider 设为 <code class="usage-code">AndroidAdjust</code> 或 <code class="usage-code">IOSAdjust</code> 并填入 token。</li><li>用 <code class="usage-code">UAnalyticsBlueprintLibrary</code> 的 <code class="usage-code">Record Event</code> / <code class="usage-code">Record Event with Attributes</code> 打点，不要找 Window 菜单面板。</li><li>打 Android/iOS 开发包，到 Adjust 后台核对事件；桌面 PIE 没有原生 Adjust SDK。</li><li><code class="usage-code">AdjustEditor</code> 只用于编辑器里配密钥，不要链进 Game Target。</li></ol><p class="usage-note">仅 Android/iOS 运行时有效，桌面编辑器里看不到真实归因数据。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Adjust Analytics Provider</code> (<code class="usage-code">AndroidAdjust</code>, <code class="usage-code">IOSAdjust</code>, <code class="usage-code">AdjustEditor</code>).</li><li>Create the app in the Adjust dashboard and copy the App Token.</li><li>In <code class="usage-code">Project Settings</code> Analytics, or <code class="usage-code">[Analytics]</code> in <code class="usage-code">DefaultEngine.ini</code>, set the provider to <code class="usage-code">AndroidAdjust</code> or <code class="usage-code">IOSAdjust</code> and paste the token.</li><li>Fire events with <code class="usage-code">UAnalyticsBlueprintLibrary</code> <code class="usage-code">Record Event</code> / <code class="usage-code">Record Event with Attributes</code>; there is no Window panel.</li><li>Verify on an Android/iOS dev build in the Adjust dashboard; desktop PIE has no native Adjust SDK.</li><li><code class="usage-code">AdjustEditor</code> is editor configuration only — keep it off Game targets.</li></ol><p class="usage-note">Live only on Android/iOS runtimes; the desktop editor will not show real Adjust attribution.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">AdjustEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidAdjust</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">IOSAdjust</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Analytics/Adjust/Adjust.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
