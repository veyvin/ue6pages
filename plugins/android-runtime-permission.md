---
layout: default
title: Android 运行时权限 / Android Runtime Permission
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Android Runtime Permission</div>
      <div class="hero-title-cn">Android 运行时权限 · 支持Android运行时权限</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Android</span><span class="chip">Google</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Google</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AndroidPermission/AndroidPermission.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持Android运行时权限</div><div class="lang-content">Support for Android Runtime Permission</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：支持Android运行时权限</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AndroidPermission。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Support for Android Runtime Permission</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AndroidPermission. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Android Runtime Permission</code>（模块 <code class="usage-code">AndroidPermission</code>）。</li><li>在 <code class="usage-code">Project Settings &gt; Platforms &gt; Android</code> 的 <code class="usage-code">Extra Permissions</code> 写入清单权限，例如 <code class="usage-code">android.permission.CAMERA</code>、<code class="usage-code">android.permission.RECORD_AUDIO</code>（对应 <code class="usage-code">DefaultEngine.ini</code> 里 <code class="usage-code">[/Script/AndroidRuntimeSettings.AndroidRuntimeSettings]</code> 的 <code class="usage-code">+ExtraPermissions=</code>）。</li><li>运行时先调 <code class="usage-code">UAndroidPermissionFunctionLibrary::CheckPermission</code>，未授权再 <code class="usage-code">AcquirePermissions</code>；回调对象是 <code class="usage-code">UAndroidPermissionCallbackProxy</code>（蓝图节点 <code class="usage-code">Check Permission</code> / <code class="usage-code">Acquire Permissions</code>）。</li><li>游戏 <code class="usage-code">Build.cs</code> 依赖 <code class="usage-code">AndroidPermission</code>，<code class="usage-code">#include &quot;AndroidPermissionFunctionLibrary.h&quot;</code>。</li><li>在真机 Android 6+ 上验证系统权限对话框；编辑器与非 Android 目标不会弹出授权 UI。</li><li>Shipping 仍需清单里声明权限，否则运行时请求会被系统直接拒绝。</li></ol><p class="usage-note">这是运行时动态授权；清单 Extra Permissions 与代码请求必须成对出现。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Android Runtime Permission</code> (module <code class="usage-code">AndroidPermission</code>).</li><li>Add manifest permissions under <code class="usage-code">Project Settings &gt; Platforms &gt; Android</code> → <code class="usage-code">Extra Permissions</code> (e.g. <code class="usage-code">android.permission.CAMERA</code>, <code class="usage-code">android.permission.RECORD_AUDIO</code>), which writes <code class="usage-code">+ExtraPermissions=</code> in <code class="usage-code">[/Script/AndroidRuntimeSettings.AndroidRuntimeSettings]</code> of <code class="usage-code">DefaultEngine.ini</code>.</li><li>At runtime call <code class="usage-code">UAndroidPermissionFunctionLibrary::CheckPermission</code>, then <code class="usage-code">AcquirePermissions</code> if needed; the callback is <code class="usage-code">UAndroidPermissionCallbackProxy</code> (Blueprint <code class="usage-code">Check Permission</code> / <code class="usage-code">Acquire Permissions</code>).</li><li>Depend on <code class="usage-code">AndroidPermission</code> in the game <code class="usage-code">Build.cs</code> and <code class="usage-code">#include &quot;AndroidPermissionFunctionLibrary.h&quot;</code>.</li><li>Verify the system permission dialog on an Android 6+ device; the editor and non-Android targets will not show it.</li><li>Shipping builds still need the permission in the manifest, or the OS will deny the request.</li></ol><p class="usage-note">Runtime grants only; Extra Permissions in the manifest must match the code request.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidPermission</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AndroidPermission/AndroidPermission.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
