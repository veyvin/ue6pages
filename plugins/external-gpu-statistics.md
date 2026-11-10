---
layout: default
title: 外部 GPU 统计信息 / External GPU Statistics
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">E</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">External GPU Statistics</div>
      <div class="hero-title-cn">外部 GPU 统计信息 · 用于查找 NVIDIA、AMD 和 Intel GPU 的更详细</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Rendering</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/ExternalGPUStatistics/ExternalGPUStatistics.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于查找 NVIDIA、AMD 和 Intel GPU 的更详细 GPU 使用情况的插件。</div><div class="lang-content">Plugin to find out more detailed GPU usage for NVIDIA, AMD, and Intel GPUs.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于查找 NVIDIA、AMD 和 Intel GPU 的更详细 GPU 使用情况的插件。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：ExternalGPUStatistics。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Plugin to find out more detailed GPU usage for NVIDIA, AMD, and Intel GPUs.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: ExternalGPUStatistics. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">ExternalGPUStatistics</code>（运行时模块 <code class="usage-code">ExternalGPUStatistics</code>）后，在 NVIDIA/AMD/Intel 显卡的机器上运行编辑器或打包游戏。</li><li>用控制台 <code class="usage-code">stat GPU</code> / <code class="usage-code">stat RHI</code> 做基准，再用该插件拉取驱动层更细的 GPU 占用（各引擎、队列与 pass 的耗时）。</li><li>结合外部 GPU 厂商 profiler（如 Nsight、Radeon GPU Profiler）或启动参数导出，交叉比对插件统计与驱动数据。</li><li>分别在 DX12、Vulkan 等 RHI 下各跑一遍，确认统计口径一致再采信数值。</li><li>做性能对比时固定场景与摄像机，一次只改一个变量，避免多变量噪声掩盖真实差异。</li><li>它是运行时插件可进包，但只建议在 profiling 构建里开启，正式发布包关掉以减少额外开销。</li></ol><p class="usage-note">用于拿 GPU 驱动层更细的占用，需与厂商 profiler 交叉验证；建议仅在 profiling 构建开启。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">ExternalGPUStatistics</code> (runtime module <code class="usage-code">ExternalGPUStatistics</code>), then run the editor or a packaged game on an NVIDIA/AMD/Intel GPU machine.</li><li>Take a baseline with <code class="usage-code">stat GPU</code> / <code class="usage-code">stat RHI</code>, then use the plugin to pull finer driver-level GPU usage (per-engine, per-queue, per-pass timings).</li><li>Cross-check the plugin numbers against an external vendor profiler (Nsight, Radeon GPU Profiler) or an exported run, to validate what the plugin reports.</li><li>Run once each under DX12, Vulkan, etc., and confirm the metrics line up before trusting the numbers.</li><li>For perf comparisons, fix the scene and camera and change one variable at a time so multi-variable noise does not mask the real difference.</li><li>It is a runtime plugin that can ship, but enable it only in profiling builds and turn it off in release packages to avoid the extra overhead.</li></ol><p class="usage-note">Gets finer driver-level GPU usage; cross-check with vendor profilers and enable it only in profiling builds.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ExternalGPUStatistics</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/ExternalGPUStatistics/ExternalGPUStatistics.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
