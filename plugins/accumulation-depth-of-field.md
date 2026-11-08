---
layout: default
title: 累积景深 / Accumulation Depth of Field
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Accumulation Depth of Field</div>
      <div class="hero-title-cn">累积景深 · 用于生产渲染的薄透镜孔径采样景深</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/AccumulationDOF/AccumulationDOF.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">用于生产渲染的薄透镜孔径采样景深</div><div class="lang-content">Thin-lens aperture-sampled depth of field for production rendering</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：用于生产渲染的薄透镜孔径采样景深</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：AccumulationDOF, AccumulationDOFEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Thin-lens aperture-sampled depth of field for production rendering</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: AccumulationDOF, AccumulationDOFEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Accumulation Depth of Field</code>（运行时 <code class="usage-code">AccumulationDOF</code>，编辑器 <code class="usage-code">AccumulationDOFEditor</code>）。</li><li>放置 <code class="usage-code">CineCameraActor</code>，在 Details 的 <code class="usage-code">Current Camera Settings</code> / <code class="usage-code">Focus Settings</code> 里设置 Focal Length、Aperture（F-stop）和 Manual Focus Distance。</li><li>打开 <code class="usage-code">Window &gt; Cinematics &gt; Movie Render Queue</code>（或 Movie Render Graph），把该摄像机加入渲染任务。</li><li>提高 Anti-Aliasing 的 Temporal/Spatial Sample Count，让薄透镜孔径采样跨帧累积，而不是依赖实时 Circle DOF。</li><li>检查输出序列的焦外散景；不要以 PIE 实时后期为准。</li><li><code class="usage-code">AccumulationDOFEditor</code> 只做编辑器细节定制，不要链进 Game Target。</li></ol><p class="usage-note">这是生产/离线累积景深，实时视口观感不能代表最终成像。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Accumulation Depth of Field</code> (runtime <code class="usage-code">AccumulationDOF</code>, editor <code class="usage-code">AccumulationDOFEditor</code>).</li><li>Place a <code class="usage-code">CineCameraActor</code> and set Focal Length, Aperture (F-stop), and Manual Focus Distance under Details <code class="usage-code">Current Camera Settings</code> / <code class="usage-code">Focus Settings</code>.</li><li>Open <code class="usage-code">Window &gt; Cinematics &gt; Movie Render Queue</code> (or Movie Render Graph) and add that camera to the job.</li><li>Raise Anti-Aliasing Temporal/Spatial Sample Count so thin-lens aperture samples accumulate across frames instead of using real-time circle DOF.</li><li>Judge bokeh on the rendered sequence, not on PIE post-process.</li><li>Keep <code class="usage-code">AccumulationDOFEditor</code> on an Editor target only.</li></ol><p class="usage-note">This is production/offline accumulated DOF; the real-time viewport is not the final look.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">AccumulationDOF</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AccumulationDOFEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/AccumulationDOF/AccumulationDOF.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
