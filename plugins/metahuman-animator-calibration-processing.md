---
layout: default
title: MetaHuman Animator 校准处理 / MetaHuman Animator Calibration Processing
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">M</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">MetaHuman Animator Calibration Processing</div>
      <div class="hero-title-cn">MetaHuman Animator 校准处理 · 虚幻引擎官方 MetaHuman 校准处理工具包</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>MetaHuman</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/MetaHuman/MetaHumanCalibrationProcessing/MetaHumanCalibrationProcessing.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">虚幻引擎官方 MetaHuman 校准处理工具包</div><div class="lang-content">The official MetaHuman Calibration Processing Unreal Engine toolkit</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：虚幻引擎官方 MetaHuman 校准处理工具包</p><p>MetaHuman 家族：数字人生成、面捕、校准或运行时绑定，建立在 Control Rig / Live Link 之上。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：MetaHumanCalibrationGenerator, MetaHumanCalibrationLib, MetaHumanCalibrationCore。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: The official MetaHuman Calibration Processing Unreal Engine toolkit</p><p>MetaHuman family: digital-human generation, face capture, calibration, or runtime, on Control Rig / Live Link.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: MetaHumanCalibrationGenerator, MetaHumanCalibrationLib, MetaHumanCalibrationCore. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">MetaHuman Animator Calibration Processing</code>（模块 <code class="usage-code">MetaHumanCalibrationGenerator</code>、<code class="usage-code">MetaHumanCalibrationLib</code>、<code class="usage-code">MetaHumanCalibrationCore</code>）。</li><li>它是官方 MetaHuman 校准处理工具包，用于生成/处理校准数据。</li><li>在 MetaHuman 面捕前做相机/镜头校准处理，输出校准资产。</li><li>属 MetaHuman 校准工具链；处理阶段使用。</li></ol><p class="usage-note">官方 MetaHuman 校准处理工具包（生成/处理校准数据）。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">MetaHuman Animator Calibration Processing</code> (modules <code class="usage-code">MetaHumanCalibrationGenerator</code>, <code class="usage-code">MetaHumanCalibrationLib</code>, <code class="usage-code">MetaHumanCalibrationCore</code>).</li><li>It is the official MetaHuman calibration processing toolkit to generate/process calibration data.</li><li>Run camera/lens calibration processing before MetaHuman face capture and output calibration assets.</li><li>Part of the MetaHuman calibration toolchain; used in the processing stage.</li></ol><p class="usage-note">The official MetaHuman calibration processing toolkit (generate/process calibration data).</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanCalibrationGenerator</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanCalibrationLib</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MetaHumanCalibrationCore</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/MetaHuman/MetaHumanCalibrationProcessing/MetaHumanCalibrationProcessing.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
