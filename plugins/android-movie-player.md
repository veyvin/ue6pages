---
layout: default
title: 安卓电影播放器 / Android Movie Player
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Android Movie Player</div>
      <div class="hero-title-cn">安卓电影播放器 · 使用 Android 媒体库的 Android 平台电影播放器</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AndroidMoviePlayer/AndroidMoviePlayer.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用 Android 媒体库的 Android 平台电影播放器</div><div class="lang-content">Android Platform Movie Player using Android Media library</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用 Android 媒体库的 Android 平台电影播放器</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AndroidMoviePlayer。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Android Platform Movie Player using Android Media library</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AndroidMoviePlayer. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Android Movie Player</code>（模块 <code class="usage-code">AndroidMoviePlayer</code>）。它是 Android 上的平台开场/加载影片播放器，不是 Media Framework 的 <code class="usage-code">Media Player</code> 资产。</li><li>把要播的 <code class="usage-code">.mp4</code> 放到项目 <code class="usage-code">Content/Movies/</code>（或 <code class="usage-code">Project Settings &gt; Movies</code> 指向的影片目录），并加入 Android 包装。</li><li>打开 <code class="usage-code">Project Settings &gt; Project &gt; Movies</code>，把文件名填进 <code class="usage-code">Startup Movies</code>，按需勾选 <code class="usage-code">Wait for Movies to Complete</code> / <code class="usage-code">Movies are Skippable</code>。</li><li>也可用 <code class="usage-code">DefaultGame.ini</code> 的 <code class="usage-code">[/Script/MoviePlayer.MoviePlayerSettings]</code> 写 <code class="usage-code">+StartupMovies=</code>，由 <code class="usage-code">AndroidMoviePlayer</code> 在设备上用 Android Media 库解码。</li><li>用 Launch on Device / 包装 APK 验证启动片；编辑器 PIE 不会走这条 Android 播放器。</li><li>游戏内循环视频请改用 <code class="usage-code">Android Media Player</code> + <code class="usage-code">UMediaPlayer</code>/<code class="usage-code">File Media Source</code>，不要把本插件当运行时组件去加。</li></ol><p class="usage-note">只负责 Android 启动/加载影片；设备内游戏视频走 Media Framework。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Android Movie Player</code> (module <code class="usage-code">AndroidMoviePlayer</code>). It is the Android startup/loading movie player, not a Media Framework <code class="usage-code">Media Player</code> asset.</li><li>Put the <code class="usage-code">.mp4</code> under <code class="usage-code">Content/Movies/</code> (or the folder used by <code class="usage-code">Project Settings &gt; Movies</code>) and include it in the Android cook.</li><li>Open <code class="usage-code">Project Settings &gt; Project &gt; Movies</code>, add the clip to <code class="usage-code">Startup Movies</code>, and set <code class="usage-code">Wait for Movies to Complete</code> / <code class="usage-code">Movies are Skippable</code> as needed.</li><li>Alternatively set <code class="usage-code">+StartupMovies=</code> under <code class="usage-code">[/Script/MoviePlayer.MoviePlayerSettings]</code> in <code class="usage-code">DefaultGame.ini</code>; <code class="usage-code">AndroidMoviePlayer</code> decodes it with the Android Media library on device.</li><li>Verify with Launch on Device or a packaged APK; editor PIE does not use this Android player.</li><li>For in-game looping video use <code class="usage-code">Android Media Player</code> with <code class="usage-code">UMediaPlayer</code> / <code class="usage-code">File Media Source</code> — do not add this plugin as a component.</li></ol><p class="usage-note">Android startup/loading movies only; in-game video belongs to Media Framework.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AndroidMoviePlayer</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AndroidMoviePlayer/AndroidMoviePlayer.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
