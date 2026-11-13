---
layout: default
title: GDK网络驱动程序 / GDK Net Driver
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">GDK Net Driver</div>
      <div class="hero-title-cn">GDK网络驱动程序 · GDK 平台的网络驱动程序</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Online Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Online/Microsoft/GDKNetDriver/GDKNetDriver.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">GDK 平台的网络驱动程序</div><div class="lang-content">Net driver for GDK platforms</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：GDK 平台的网络驱动程序</p><p>属于在线子系统 / 平台服务。</p><p>它打包的模块包括：GDKNetDriver。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Net driver for GDK platforms</p><p>Part of Online Subsystem / platform services.</p><p>It ships these modules: GDKNetDriver. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">GDK Net Driver</code>（模块 <code class="usage-code">GDKNetDriver</code>），面向 GDK / Xbox 平台。</li><li>在 <code class="usage-code">DefaultEngine.ini</code> 的 <code class="usage-code">[/Script/Engine.Engine]</code> 或网络设置里把 NetDriver 指向 GDK 实现，替换默认 UDP NetDriver。</li><li>构建并部署到 GDK 目标，联机时确认走的是 GDK 网络栈。</li><li>只对 GDK 平台生效；其他平台不要依赖 <code class="usage-code">GDKNetDriver</code>。</li></ol><p class="usage-note">GDK 平台专用网络驱动，替换默认 NetDriver。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">GDK Net Driver</code> (module <code class="usage-code">GDKNetDriver</code>); it targets GDK / Xbox platforms.</li><li>Point the NetDriver at the GDK implementation in <code class="usage-code">DefaultEngine.ini</code> networking settings instead of the default UDP driver.</li><li>Build and deploy to a GDK target and confirm online play uses the GDK network stack.</li><li>It only applies to GDK platforms; do not depend on <code class="usage-code">GDKNetDriver</code> elsewhere.</li></ol><p class="usage-note">A GDK-only net driver that replaces the default NetDriver.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">GDKNetDriver</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Online/Microsoft/GDKNetDriver/GDKNetDriver.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
