---
layout: default
title: 火力基地 / Firebase
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">F</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Firebase</div>
      <div class="hero-title-cn">火力基地 · 支持使用 Firebase 进行远程通知</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Online Platform</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/Firebase/Firebase.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持使用 Firebase 进行远程通知</div><div class="lang-content">Support for remote notifications using Firebase</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：支持使用 Firebase 进行远程通知</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：Firebase。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Support for remote notifications using Firebase</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: Firebase. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Firebase</code>（模块 <code class="usage-code">Firebase</code>）。它走 Firebase Cloud Messaging 远程推送，不是 Analytics 也不是 Firestore 全套 SDK。</li><li>Android 把 <code class="usage-code">google-services.json</code> 放到项目 Android 构建目录并在 UPL/Gradle 里让插件读到；iOS 放入 <code class="usage-code">GoogleService-Info.plist</code>。控制台打开 Cloud Messaging。</li><li>打包到真机，启动后向 Firebase 注册并拿到设备 token（看 Output Log / 插件回调）。用 Firebase 控制台发一条测试通知，应用在后台时应弹出系统通知。</li><li>前台/点击通知的处理写在游戏模块对 <code class="usage-code">Firebase</code> 的回调里（打开指定关卡、深链）；不要在蓝图里找「Firebase 组件」当 Actor 挂件。</li><li>游戏 <code class="usage-code">Build.cs</code> 仅在移动目标依赖 <code class="usage-code">Firebase</code>。桌面 PIE 收不到 FCM；凭证填错会注册失败而不是静默启用。</li></ol><p class="usage-note">移动端远程通知桥，不是通用后端 BaaS 插件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Firebase</code> (module <code class="usage-code">Firebase</code>). It is Firebase Cloud Messaging for remote notifications — not Analytics and not the full Firestore SDK.</li><li>Place Android <code class="usage-code">google-services.json</code> where the Android build/UPL/Gradle can see it, and <code class="usage-code">GoogleService-Info.plist</code> on iOS. Turn on Cloud Messaging in the Firebase console.</li><li>Ship to a device, register, and capture the FCM token (Output Log / plugin callback). Send a test message from the console; a backgrounded app should show a system notification.</li><li>Handle foreground/tap payloads in game-module callbacks (open a map, deep link). There is no <code class="usage-code">Firebase</code> actor component to drop in the level.</li><li>Depend on <code class="usage-code">Firebase</code> only on mobile game targets. Desktop PIE will not receive FCM; bad credentials fail registration rather than silently working.</li></ol><p class="usage-note">Mobile remote-notification bridge, not a full Firebase BaaS plugin.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">Firebase</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/Firebase/Firebase.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
