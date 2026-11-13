---
layout: default
title: 伊莱克特拉玩家 / Electra Player
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Electra Player</div>
      <div class="hero-title-cn">伊莱克特拉玩家 · 用于本地文件和互联网流媒体的跨平台媒体播放器。
还为台式机提供优</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Media Players</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">8</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Media/ElectraPlayer/ElectraPlayer.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于本地文件和互联网流媒体的跨平台媒体播放器。
还为台式机提供优化的仅本地 mp4 文件播放器 (Protron)。</div><div class="lang-content">Cross platform media player for local files and internet streaming.
Also provides optimized local mp4 file only player (Protron) for desktop machines.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于本地文件和互联网流媒体的跨平台媒体播放器。
还为台式机提供优化的仅本地 mp4 文件播放器 (Protron)。</p><p>媒体/Electra 家族：为 Electra 播放器提供某种封装格式或硬件解码，供 Media Framework 播视频。</p><p>属于 Media Framework / Electra 播流与解码。</p><p>它打包的模块包括：ElectraPlayerPluginHandler, ElectraPlayerRuntime, ElectraPlayerPlugin, ElectraPlayerFactory, ElectraPlayerFactory, ElectraProtron, ElectraProtronFactory, ElectraProtronFactory。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Cross platform media player for local files and internet streaming.
Also provides optimized local mp4 file only player (Protron) for desktop machines.</p><p>Media/Electra family: a container or hardware decoder for Electra so Media Framework can play video.</p><p>Part of Media Framework / Electra playback and decode.</p><p>It ships these modules: ElectraPlayerPluginHandler, ElectraPlayerRuntime, ElectraPlayerPlugin, ElectraPlayerFactory, ElectraPlayerFactory, ElectraProtron, ElectraProtronFactory, ElectraProtronFactory. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 <code class="usage-code">编辑 &gt; 插件</code> 启用 <code class="usage-code">Electra Player</code>；在 <code class="usage-code">项目设置 &gt; 插件 &gt; Electra Player</code> 里为目标平台（Win64/Mac）勾选启用，并把它设为默认媒体解码后端。</li><li>在内容浏览器右键 <code class="usage-code">媒体 &gt; 文件媒体源</code>（流媒体用 <code class="usage-code">流媒体源</code>），指向本地 <code class="usage-code">.mp4</code> 文件或 HLS/DASH 地址。</li><li>右键 <code class="usage-code">媒体 &gt; 媒体播放器</code> 新建播放器，在资产的 <code class="usage-code">播放器 &gt; 平台播放器</code> 里为桌面平台选 Protron/Electra（Protron 只吃本地 mp4）。</li><li>新建 <code class="usage-code">MediaTexture</code>，把它的 <code class="usage-code">媒体播放器</code> 指向上面那个播放器，接入材质后贴到 <code class="usage-code">Media Plate</code> 或平面网格上。</li><li>蓝图对播放器调用 <code class="usage-code">Open Source</code> 打开源，再 <code class="usage-code">Play</code> 播放、<code class="usage-code">Pause</code> 暂停、<code class="usage-code">Close</code> 释放。</li><li>打包后确认目标平台的插件列表里已打开 Electra，否则运行时找不到可用播放器。</li></ol><p class="usage-note">Electra 是跨平台 Media Framework 播放器；桌面本地 mp4 场景用 Protron 变体，流媒体用 Electra 主播放器，目标平台要单独为它打开插件。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Electra Player</code> under <code class="usage-code">Edit &gt; Plugins</code>; in <code class="usage-code">Project Settings &gt; Plugins &gt; Electra Player</code> turn it on for the target platform (Win64/Mac) and pick Electra as the default media backend.</li><li>Right-click <code class="usage-code">Media &gt; File Media Source</code> (or <code class="usage-code">Stream Media Source</code>) and point it at a local <code class="usage-code">.mp4</code> or an HLS/DASH URL.</li><li>Right-click <code class="usage-code">Media &gt; Media Player</code>, then on the asset set <code class="usage-code">Player &gt; Platform Player</code> to Protron/Electra for desktop (Protron handles local mp4 only).</li><li>Create a <code class="usage-code">MediaTexture</code>, set its <code class="usage-code">Media Player</code> to that player, feed it into a Material and apply it to a <code class="usage-code">Media Plate</code> or plane mesh.</li><li>In Blueprint call <code class="usage-code">Open Source</code>, then <code class="usage-code">Play</code>, <code class="usage-code">Pause</code>, and <code class="usage-code">Close</code> on the Media Player.</li><li>After packaging, confirm Electra is enabled for the target platform in the plugin list, or no player is found at runtime.</li></ol><p class="usage-note">Electra is the cross-platform Media Framework player; use the Protron variant for local desktop mp4 and the main Electra player for streaming, enabling the plugin per target platform.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (8)</div><div class="module-item"><span class="dot"></span><span class="name mono">ElectraPlayerPluginHandler</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ElectraPlayerRuntime</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ElectraPlayerPlugin</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ElectraPlayerFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ElectraPlayerFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ElectraProtron</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ElectraProtronFactory</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ElectraProtronFactory</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Media/ElectraPlayer/ElectraPlayer.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
