---
layout: default
title: 捕获管理器工具集 / Capture Manager Toolset
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Capture Manager Toolset</div>
      <div class="hero-title-cn">捕获管理器工具集 · 用于通过 AI Assistant 检查 Capture Man</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span><span class="chip">Epic Games</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Experimental/Toolsets/CaptureManagerToolset/CaptureManagerToolset.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于通过 AI Assistant 检查 Capture Manager 镜头和 FootageCaptureData 资产的工具集。采集和设备工具由 Capture Manager Editor 插件提供。</div><div class="lang-content">Toolset for inspecting Capture Manager takes and FootageCaptureData assets via the AI Assistant. Ingest and device tools are provided by the Capture Manager Editor plugin.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于通过 AI Assistant 检查 Capture Manager 镜头和 FootageCaptureData 资产的工具集。采集和设备工具由 Capture Manager Editor 插件提供。</p><p>Toolset：给编辑器里的 AI 助手或自动化准备的只读/只写工具，一般不进 Shipping 游戏。</p><p>Epic 把它放在 Experimental：功能可用，但接口可能随夜构建变化。</p><p>它打包的模块包括：CaptureManagerToolset。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Toolset for inspecting Capture Manager takes and FootageCaptureData assets via the AI Assistant. Ingest and device tools are provided by the Capture Manager Editor plugin.</p><p>Toolset: read/write tools for the in-editor AI assistant or automation — not a shipping game feature.</p><p>Epic ships this under Experimental: usable, but the contract may change on nightly builds.</p><p>It ships these modules: CaptureManagerToolset. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用实验性 <code class="usage-code">Capture Manager Toolset</code>（<code class="usage-code">Plugins/Experimental/Toolsets/CaptureManagerToolset</code>，模块 <code class="usage-code">CaptureManagerToolset</code>），并打开编辑器 AI Assistant。</li><li>项目里先有 <code class="usage-code">FootageCaptureData</code> 或 Capture Manager take 元数据；本工具集只检查，不创建镜头。</li><li>向助手询问 take 列表、某资产的 <code class="usage-code">ImageSequences</code> 路数、帧率、<code class="usage-code">CameraCalibrations</code> 是否齐全、<code class="usage-code">CaptureExcludedFrames</code> 是否异常。</li><li>用它做入库后巡检（缺深度、设备类错误、音频轨为空），再决定要不要重采。</li><li>需要真正下载/转码/导入时改用 <code class="usage-code">Capture Manager Editor</code> 的 Ingest 库或 Hub 设备，不要指望本 Toolset 写盘。</li><li>不要把 <code class="usage-code">CaptureManagerToolset</code> 加进游戏 <code class="usage-code">Build.cs</code>；Experimental 接口会随夜构建变化。</li></ol><p class="usage-note">只读巡检工具。入库与设备命令在 Capture Manager Editor，不要和 `capturemanagertoolset` 的写入摄取混淆。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable experimental <code class="usage-code">Capture Manager Toolset</code> (<code class="usage-code">Plugins/Experimental/Toolsets/CaptureManagerToolset</code>, module <code class="usage-code">CaptureManagerToolset</code>) and open the editor AI Assistant.</li><li>Have <code class="usage-code">FootageCaptureData</code> or Capture Manager take metadata in the project first. This toolset inspects; it does not create takes.</li><li>Ask the assistant for take lists, per-asset <code class="usage-code">ImageSequences</code> view counts, frame rate, missing <code class="usage-code">CameraCalibrations</code>, and odd <code class="usage-code">CaptureExcludedFrames</code>.</li><li>Use it as a post-ingest audit (missing depth, wrong device class, empty audio) before you recapture.</li><li>For download/transcode/import, use <code class="usage-code">Capture Manager Editor</code> ingest libraries or Hub devices — this toolset does not write media.</li><li>Do not add <code class="usage-code">CaptureManagerToolset</code> to a game <code class="usage-code">Build.cs</code>. The Experimental contract can change on nightlies.</li></ol><p class="usage-note">Read-only inspection. Ingest and device commands stay on Capture Manager Editor. Do not confuse with the ingest-oriented `capturemanagertoolset` slug.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CaptureManagerToolset</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Experimental/Toolsets/CaptureManagerToolset/CaptureManagerToolset.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
