---
layout: default
title: 组播分析提供商 / Multicast Analytics Provider
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Multicast Analytics Provider</div>
      <div class="hero-title-cn">组播分析提供商 · 将分析 API 调用转发到分析提供商列表，以一次将数据记录到多个</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Analytics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">2.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Analytics/AnalyticsMulticast/AnalyticsMulticast.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">将分析 API 调用转发到分析提供商列表，以一次将数据记录到多个服务</div><div class="lang-content">Forwards analytics API calls to a list of analytics providers to log data to multiple services at once</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：将分析 API 调用转发到分析提供商列表，以一次将数据记录到多个服务</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AnalyticsMulticastEditor, AnalyticsMulticast。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Forwards analytics API calls to a list of analytics providers to log data to multiple services at once</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AnalyticsMulticastEditor, AnalyticsMulticast. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Multicast Analytics Provider</code>（运行时 <code class="usage-code">AnalyticsMulticast</code>，编辑器 <code class="usage-code">AnalyticsMulticastEditor</code>）。</li><li>它把分析（analytics）API 调用转发到一组分析提供商，一次把数据记录到多个服务。</li><li>配置多个下游 provider，事件经它广播给全部目标。</li><li>Game 模块依赖 <code class="usage-code">AnalyticsMulticast</code>；编辑器模块只进 Editor Target。</li></ol><p class="usage-note">把分析调用广播到多个 provider（一次上报多服务）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Multicast Analytics Provider</code> (runtime <code class="usage-code">AnalyticsMulticast</code>, editor <code class="usage-code">AnalyticsMulticastEditor</code>).</li><li>It forwards analytics API calls to a list of analytics providers, logging data to multiple services at once.</li><li>Configure multiple downstream providers; events broadcast to all of them.</li><li>Game modules depend on <code class="usage-code">AnalyticsMulticast</code>; editor modules go to Editor targets only.</li></ol><p class="usage-note">Forwards analytics calls to multiple providers at once.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AnalyticsMulticastEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AnalyticsMulticast</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Analytics/AnalyticsMulticast/AnalyticsMulticast.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
