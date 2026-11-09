---
layout: default
title: 相机校准 / Camera Calibration
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Camera Calibration</div>
      <div class="hero-title-cn">相机校准 · 支持引擎中镜头畸变和相机校准的框架。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/CameraCalibration/CameraCalibration.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">支持引擎中镜头畸变和相机校准的框架。</div><div class="lang-content">Framework to support lens distortion and camera calibration in engine.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：支持引擎中镜头畸变和相机校准的框架。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：CameraCalibrationEditor, TrackingAlignment, TrackingAlignmentEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Framework to support lens distortion and camera calibration in engine.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: CameraCalibrationEditor, TrackingAlignment, TrackingAlignmentEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Camera Calibration</code>（<code class="usage-code">CameraCalibrationEditor</code>、<code class="usage-code">TrackingAlignment</code>、<code class="usage-code">TrackingAlignmentEditor</code>），并确保 <code class="usage-code">Camera Calibration Core</code> 已开。</li><li>放置 <code class="usage-code">CineCameraActor</code>（接 Live Link 摄像机主题 + 媒体板），再放置 <code class="usage-code">Camera Calibration Checkerboard</code>，按实物标板填写 <code class="usage-code">Num Corner Rows</code> / <code class="usage-code">Num Corner Cols</code> / <code class="usage-code">Square Side Length</code>。</li><li>双击 <code class="usage-code">Lens File</code> 打开标定步骤：先在 <code class="usage-code">Lens Information</code> 填厂商/焦距并保存，再进 <code class="usage-code">Lens Distortion</code>，算法选 Checkerboard 或 Points，从不同角度采集多张后点 <code class="usage-code">Add To Lens Distortion Calibration</code>。</li><li>切到 <code class="usage-code">Nodal Offset</code>：先用 <code class="usage-code">Nodal Offset Checkerboard</code> 点视口并 <code class="usage-code">Apply to Calibrator</code> 对齐虚拟标板，再用 Points / ArUco / Optical Axis 点 <code class="usage-code">Add To Nodal Offset Calibration</code>，把虚拟摄像机放到物理节点。</li><li>多组 Focus/Zoom 重复畸变与节点偏移，让 <code class="usage-code">ULensFile</code> 插值表覆盖走焦走焦段。</li><li>两套跟踪坐标系（例如头显 vs 摄影测量）时，新建 <code class="usage-code">TrackingAlignmentCalibrationProfile</code>，指定 <code class="usage-code">Tracker A</code> / <code class="usage-code">Tracker B</code> 的 Source 与 Origin Actor，多次 <code class="usage-code">Capture Sample</code> 后求解对齐，不要和节点偏移混成同一次采集。</li><li><code class="usage-code">CameraCalibrationEditor</code> 与 <code class="usage-code">TrackingAlignmentEditor</code> 只进编辑器模块；运行时对齐数据走 <code class="usage-code">TrackingAlignment</code>。</li></ol><p class="usage-note">这是现场标定会话：棋盘格、节点偏移、跟踪空间对齐。镜头求值仍由 Core 的 `ULensComponent` 完成。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Camera Calibration</code> (<code class="usage-code">CameraCalibrationEditor</code>, <code class="usage-code">TrackingAlignment</code>, <code class="usage-code">TrackingAlignmentEditor</code>) with <code class="usage-code">Camera Calibration Core</code> already on.</li><li>Place a Live Link–driven <code class="usage-code">CineCameraActor</code> plus media plate, then a <code class="usage-code">Camera Calibration Checkerboard</code> whose <code class="usage-code">Num Corner Rows</code> / <code class="usage-code">Num Corner Cols</code> / <code class="usage-code">Square Side Length</code> match the physical chart.</li><li>Open the <code class="usage-code">Lens File</code> calibration steps: fill <code class="usage-code">Lens Information</code>, then <code class="usage-code">Lens Distortion</code> (Checkerboard or Points). Capture many poses and click <code class="usage-code">Add To Lens Distortion Calibration</code>.</li><li>On <code class="usage-code">Nodal Offset</code>, use <code class="usage-code">Nodal Offset Checkerboard</code>, click the viewport, <code class="usage-code">Apply to Calibrator</code>, then Points / ArUco / Optical Axis and <code class="usage-code">Add To Nodal Offset Calibration</code> so the virtual camera sits on the physical nodal point.</li><li>Repeat distortion and nodal offset at several Focus/Zoom stops so the <code class="usage-code">ULensFile</code> tables interpolate across pulls.</li><li>For two tracking spaces (HMD vs photogrammetry), create a <code class="usage-code">TrackingAlignmentCalibrationProfile</code>, set Tracker A/B source and origin actors, <code class="usage-code">Capture Sample</code> repeatedly, and solve alignment — do not mix this with nodal-offset captures.</li><li><code class="usage-code">CameraCalibrationEditor</code> and <code class="usage-code">TrackingAlignmentEditor</code> are editor-only; runtime alignment data uses <code class="usage-code">TrackingAlignment</code>.</li></ol><p class="usage-note">This is the on-set session: charts, nodal offset, tracking-space alignment. Runtime evaluation still goes through Core’s `ULensComponent`.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">CameraCalibrationEditor</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TrackingAlignment</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TrackingAlignmentEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/CameraCalibration/CameraCalibration.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
