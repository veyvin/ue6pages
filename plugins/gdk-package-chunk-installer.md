---
layout: default
title: GDK 包块安装程序 / GDK Package Chunk Installer
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">G</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">GDK Package Chunk Installer</div>
      <div class="hero-title-cn">GDK 包块安装程序 · 允许游戏使用 GDK 块安装程序 (XPackage)</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Microsoft/GDKPackageChunkInstall/GDKPackageChunkInstall.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">允许游戏使用 GDK 块安装程序 (XPackage)</div><div class="lang-content">Allows titles to use GDK chunk installer (XPackage)</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：允许游戏使用 GDK 块安装程序 (XPackage)</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：GDKPackageChunkInstall。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Allows titles to use GDK chunk installer (XPackage)</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: GDKPackageChunkInstall. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">GDK Package Chunk Installer</code>（模块 <code class="usage-code">GDKPackageChunkInstall</code>），面向 GDK / Xbox。</li><li>在打包时为内容划分 chunk，运行时用 XPackage / chunk installer API 按需下载并安装。</li><li>在游戏代码里查询 chunk 安装状态，处理下载进度与可用性判断。</li><li>只在 GDK 目标使用；其他平台用各自的 DLC/分块方案。</li></ol><p class="usage-note">GDK 的 XPackage 分块安装，不是通用补丁/DLC 系统。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">GDK Package Chunk Installer</code> (module <code class="usage-code">GDKPackageChunkInstall</code>) for GDK / Xbox.</li><li>Split content into chunks at packaging, then download and install on demand via the XPackage / chunk installer API at runtime.</li><li>Query chunk install state in game code and handle download progress and availability.</li><li>Use it on GDK targets only; other platforms use their own DLC/chunk solutions.</li></ol><p class="usage-note">GDK XPackage chunked installs, not a generic patch/DLC system.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">GDKPackageChunkInstall</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Microsoft/GDKPackageChunkInstall/GDKPackageChunkInstall.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
