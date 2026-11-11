---
layout: default
title: 音频定义模型 (ADM) / Audio Definition Model (ADM)
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Audio Definition Model (ADM)</div>
      <div class="hero-title-cn">音频定义模型 (ADM) · 目前仅支持使用 WASAPI 聚合输出通道进行空间化输出以及使用</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Audio</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/ADM/ADM.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">目前仅支持使用 WASAPI 聚合输出通道进行空间化输出以及使用开放声音控制 (OSC) 传输的空间 ADM 信息。</div><div class="lang-content">Currently only supports output spatialized using WASAPI aggregate output channels and spatial ADM information transmitted using Open Sound Control (OSC).</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：目前仅支持使用 WASAPI 聚合输出通道进行空间化输出以及使用开放声音控制 (OSC) 传输的空间 ADM 信息。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：ADMSpatialization。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Currently only supports output spatialized using WASAPI aggregate output channels and spatial ADM information transmitted using Open Sound Control (OSC).</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: ADMSpatialization. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 Windows 上启用 <code class="usage-code">Audio Definition Model (ADM)</code>（模块 <code class="usage-code">ADMSpatialization</code>），并启用依赖的 <code class="usage-code">OSC</code> 插件。</li><li>操作系统里把输出设为 WASAPI 聚合设备，通道布局要能对应 ADM 对象床。</li><li>游戏模块依赖 <code class="usage-code">ADMSpatialization</code>；取 <code class="usage-code">UADMEngineSubsystem</code>（<code class="usage-code">AudioEngineSubsystem</code>）。</li><li>调用 <code class="usage-code">SetSendIPAddress</code> 指定接收 ADM-OSC 的渲染器/调音台 IP 与端口（常用 4001）。</li><li>在关卡里播放空间化声音；插件把对象位置通过 OSC（如 <code class="usage-code">/adm/obj/{n}/xyz</code>）送出，而不是新建一种 Sound Class。</li><li>用外部 ADM-OSC 监听器确认坐标在更新。该路径目前仅 WASAPI 聚合输出 + OSC。</li></ol><p class="usage-note">Experimental：对象音频经 WASAPI 聚合口输出，元数据走 OSC，不是 Ambisonics 文件解码器。</p></div><div class="lang-content"><ol class="usage-steps"><li>On Windows, enable <code class="usage-code">Audio Definition Model (ADM)</code> (module <code class="usage-code">ADMSpatialization</code>) and the dependent <code class="usage-code">OSC</code> plugin.</li><li>Set the OS output to a WASAPI aggregate device whose channel layout matches the ADM object bed.</li><li>Depend on <code class="usage-code">ADMSpatialization</code> and get <code class="usage-code">UADMEngineSubsystem</code> (an <code class="usage-code">AudioEngineSubsystem</code>).</li><li>Call <code class="usage-code">SetSendIPAddress</code> with the renderer/console IP and port (often 4001).</li><li>Play spatialized sounds in a level; object poses go out over OSC (e.g. <code class="usage-code">/adm/obj/{n}/xyz</code>) — this is not a new Sound Class.</li><li>Confirm an external ADM-OSC listener sees updates. Current path is WASAPI aggregate output plus OSC only.</li></ol><p class="usage-note">Experimental: object audio over WASAPI aggregate channels with OSC metadata — not an Ambisonics file decoder.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ADMSpatialization</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/ADM/ADM.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
