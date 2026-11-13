---
layout: default
title: DMX 控制台 / DMX Control Console
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">D</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">DMX Control Console</div>
      <div class="hero-title-cn">DMX 控制台 · 可以从 DMX 库修补并将 DMX 发送到输出端口的控制台</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/DMX/DMXControlConsole/DMXControlConsole.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">可以从 DMX 库修补并将 DMX 发送到输出端口的控制台</div><div class="lang-content">Console that can be patched from DMX Libraries and sends DMX to Output Ports</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：可以从 DMX 库修补并将 DMX 发送到输出端口的控制台</p><p>DMX 家族：舞台灯光协议、灯具、像素映射，把引擎接到真实灯光台。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：DMXControlConsole, DMXControlConsoleEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Console that can be patched from DMX Libraries and sends DMX to Output Ports</p><p>DMX family: lighting protocols, fixtures, and pixel mapping from the engine to a lighting desk.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: DMXControlConsole, DMXControlConsoleEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>先启用 <code class="usage-code">DMX Engine</code> 与 <code class="usage-code">DMX Protocol</code>，再启用 <code class="usage-code">DMX Control Console</code>（<code class="usage-code">DMXControlConsole</code> + <code class="usage-code">DMXControlConsoleEditor</code>）并重启。</li><li>内容浏览器新建 <code class="usage-code">DMX Control Console</code> 资产，或打开 <code class="usage-code">Window &gt; DMX &gt; DMX Control Console</code>。</li><li>从已有 <code class="usage-code">DMX Library</code> 的 Fixture Patch 把通道拖进控制台，生成推子/编码器（Patch，不是把控制台当灯具 Actor 放进关卡）。</li><li>确认输出端口已在 DMX Protocol 里配好，按 Play/推子把通道值送到 Art-Net 或 sACN，用灯台或网口抓包核对。</li><li>可保存多个 Console 布局资产在演播间切换；现场操作走这套推子，不要用 Sequencer 关键帧代替灯台。</li><li><code class="usage-code">DMXControlConsoleEditor</code> 只进 Editor Target；Shipping 里不要链编辑器模块。</li></ol><p class="usage-note">这是从 DMX Library 修补并往输出端口发 DMX 的虚拟灯台，不是灯具蓝图。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">DMX Engine</code> and <code class="usage-code">DMX Protocol</code> first, then <code class="usage-code">DMX Control Console</code> (<code class="usage-code">DMXControlConsole</code> + <code class="usage-code">DMXControlConsoleEditor</code>) and restart.</li><li>Create a <code class="usage-code">DMX Control Console</code> asset, or open <code class="usage-code">Window &gt; DMX &gt; DMX Control Console</code>.</li><li>Patch faders/encoders from Fixture Patches in an existing <code class="usage-code">DMX Library</code> — do not place the console as a fixture actor in the level.</li><li>With output ports configured in DMX Protocol, Play or move faders so channel values leave on Art-Net or sACN; confirm with a desk or a packet capture.</li><li>Save multiple console layout assets for stage presets. This is a live desk, not Sequencer lighting keys.</li><li>Keep <code class="usage-code">DMXControlConsoleEditor</code> on Editor targets only.</li></ol><p class="usage-note">A virtual lighting desk that patches a DMX Library onto output ports, not a fixture Blueprint.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">DMXControlConsole</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DMXControlConsoleEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/DMX/DMXControlConsole/DMXControlConsole.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
