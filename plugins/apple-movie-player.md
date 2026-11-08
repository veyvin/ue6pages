---
layout: default
title: 苹果电影播放器 / Apple Movie Player
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Apple Movie Player</div>
      <div class="hero-title-cn">苹果电影播放器 · 使用 AVPlayer 库的 Apple 平台电影播放器</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AppleMoviePlayer/AppleMoviePlayer.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用 AVPlayer 库的 Apple 平台电影播放器</div><div class="lang-content">Apple Platform Movie Player using AVPlayer library</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用 AVPlayer 库的 Apple 平台电影播放器</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AppleMoviePlayer。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Apple Platform Movie Player using AVPlayer library</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AppleMoviePlayer. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>仅在 iOS/macOS/tvOS 工程启用 <code class="usage-code">Apple Movie Player</code>（模块 <code class="usage-code">AppleMoviePlayer</code>）。它用 <code class="usage-code">AVPlayer</code> 播引擎启动/加载影片，不是 Media Framework 的 <code class="usage-code">UMediaPlayer</code> 资产。</li><li>把 <code class="usage-code">.mp4</code> / <code class="usage-code">.mov</code> 放到 <code class="usage-code">Content/Movies/</code>（或 <code class="usage-code">Project Settings &gt; Project &gt; Movies</code> 指向的目录），并纳入对应 Apple 平台烹饪。</li><li>在 <code class="usage-code">Project Settings &gt; Project &gt; Movies</code> 把文件名写入 <code class="usage-code">Startup Movies</code>，按需勾选 <code class="usage-code">Wait for Movies to Complete</code> / <code class="usage-code">Movies are Skippable</code>。</li><li>等价配置：<code class="usage-code">DefaultGame.ini</code> 的 <code class="usage-code">[/Script/MoviePlayer.MoviePlayerSettings]</code> 使用 <code class="usage-code">+StartupMovies=</code>。设备上由 <code class="usage-code">AppleMoviePlayer</code> 的 <code class="usage-code">AVPlayer</code> 流接管 <code class="usage-code">IGameMoviePlayer</code>。</li><li>用 Launch on Device / 包装 IPA 看启动片；Windows PIE 不会走这条播放器。</li><li>游戏内循环视频请用 <code class="usage-code">AVF Media Player</code> + <code class="usage-code">File Media Source</code>；不要给 Actor 加「Movie Player 组件」。游戏 <code class="usage-code">Build.cs</code> 通常不必链接 <code class="usage-code">AppleMoviePlayer</code>。</li></ol><p class="usage-note">Apple 启动/加载片，对位 Android 的 `Android Movie Player`。游戏内片源走 AVF/Electra，不要当 `Media Plate`。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Apple Movie Player</code> (module <code class="usage-code">AppleMoviePlayer</code>) only on iOS/macOS/tvOS. It plays engine startup/loading movies through <code class="usage-code">AVPlayer</code>, not a Media Framework <code class="usage-code">UMediaPlayer</code> asset.</li><li>Place <code class="usage-code">.mp4</code> / <code class="usage-code">.mov</code> under <code class="usage-code">Content/Movies/</code> (or the folder from <code class="usage-code">Project Settings &gt; Project &gt; Movies</code>) and cook it for the Apple platform.</li><li>Add the clip to <code class="usage-code">Startup Movies</code> under <code class="usage-code">Project Settings &gt; Project &gt; Movies</code>, and set <code class="usage-code">Wait for Movies to Complete</code> / <code class="usage-code">Movies are Skippable</code> as needed.</li><li>Equivalently set <code class="usage-code">+StartupMovies=</code> under <code class="usage-code">[/Script/MoviePlayer.MoviePlayerSettings]</code> in <code class="usage-code">DefaultGame.ini</code>. On device, <code class="usage-code">AppleMoviePlayer</code>’s <code class="usage-code">AVPlayer</code> streamer implements <code class="usage-code">IGameMoviePlayer</code>.</li><li>Verify with Launch on Device or a packaged IPA; Windows PIE does not use this player.</li><li>For in-game looping video use <code class="usage-code">AVF Media Player</code> with a <code class="usage-code">File Media Source</code>. Do not add a “Movie Player component”. Game <code class="usage-code">Build.cs</code> usually omits <code class="usage-code">AppleMoviePlayer</code>.</li></ol><p class="usage-note">Apple startup/loading movies, counterpart to `Android Movie Player`. In-game playback is AVF/Electra, not a `Media Plate`.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AppleMoviePlayer</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AppleMoviePlayer/AppleMoviePlayer.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
