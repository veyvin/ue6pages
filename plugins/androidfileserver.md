---
layout: default
title: Android文件服务器 / AndroidFileServer
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">AndroidFileServer</div>
      <div class="hero-title-cn">Android文件服务器 · 向 Android 项目添加对远程文件管理的支持。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Android</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AndroidFileServer/AndroidFileServer.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">向 Android 项目添加对远程文件管理的支持。</div><div class="lang-content">Adds support for remote file management to Android projects.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：向 Android 项目添加对远程文件管理的支持。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AndroidFileServer, AndroidFileServerEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Adds support for remote file management to Android projects.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AndroidFileServer, AndroidFileServerEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">AndroidFileServer</code>（运行时 <code class="usage-code">AndroidFileServer</code>，设置 UI 在 <code class="usage-code">AndroidFileServerEditor</code>）。</li><li>打开 <code class="usage-code">Project Settings &gt; Platforms &gt; Android</code> 的 <code class="usage-code">File Server</code> / Android File Server 段，勾选启用插件与允许网络连接，设置 Security Token、压缩与日志。</li><li>配置写入 <code class="usage-code">DefaultEngine.ini</code> 的 <code class="usage-code">[/Script/AndroidFileServerEditor.AndroidFileServerRuntimeSettings]</code>（<code class="usage-code">bEnablePlugin</code>、<code class="usage-code">bAllowNetworkConnection</code>、<code class="usage-code">SecurityToken</code> 等）。</li><li>用编辑器 Launch on Device 或命令行 <code class="usage-code">UnrealAndroidFileTool</code>（UAFT）向设备推送已 cook 的文件，避免整包重装。</li><li>开发迭代保持 File Server 开启；Shipping/商店包务必关掉 <code class="usage-code">bEnablePlugin</code>，不要把远程写盘留在正式包。</li><li><code class="usage-code">AndroidFileServerEditor</code> 只进 Editor Target；设备上跑的是运行时 <code class="usage-code">AndroidFileServer</code>。</li></ol><p class="usage-note">这是 Android 远程文件推送（UAFS），不是内容浏览器里的文件服务器 Actor。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">AndroidFileServer</code> (runtime <code class="usage-code">AndroidFileServer</code>, settings UI in <code class="usage-code">AndroidFileServerEditor</code>).</li><li>Open <code class="usage-code">Project Settings &gt; Platforms &gt; Android</code> File Server / Android File Server, enable the plugin and network connection, and set the security token, compression, and logging.</li><li>Settings land in <code class="usage-code">DefaultEngine.ini</code> under <code class="usage-code">[/Script/AndroidFileServerEditor.AndroidFileServerRuntimeSettings]</code> (<code class="usage-code">bEnablePlugin</code>, <code class="usage-code">bAllowNetworkConnection</code>, <code class="usage-code">SecurityToken</code>, …).</li><li>Push cooked files with editor Launch on Device or <code class="usage-code">UnrealAndroidFileTool</code> (UAFT) instead of a full reinstall.</li><li>Leave File Server on for iteration; turn off <code class="usage-code">bEnablePlugin</code> for Shipping/store builds so remote writes are not in the packaged game.</li><li>Keep <code class="usage-code">AndroidFileServerEditor</code> on an Editor target; the device runs <code class="usage-code">AndroidFileServer</code>.</li></ol><p class="usage-note">Android remote file push (UAFS), not a file-server actor in the Content Browser.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidFileServer</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidFileServerEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AndroidFileServer/AndroidFileServer.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
