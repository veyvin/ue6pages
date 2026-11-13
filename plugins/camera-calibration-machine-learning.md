---
layout: default
title: 相机校准机器学习 / Camera Calibration Machine Learning
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Camera Calibration Machine Learning</div>
      <div class="hero-title-cn">相机校准机器学习 · 失真校准机器学习方法的参考实现。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Virtual Production</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/VirtualProduction/CameraCalibrationML/CameraCalibrationML.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">失真校准机器学习方法的参考实现。</div><div class="lang-content">Reference implementation of a machine learning approach to distortion calibration.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：失真校准机器学习方法的参考实现。</p><p>属于虚拟制片工具链（摄像机、舞台、同步、LED）。</p><p>它打包的模块包括：CameraCalibrationML。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Reference implementation of a machine learning approach to distortion calibration.</p><p>Part of the virtual-production toolchain (cameras, stage, sync, LED).</p><p>It ships these modules: CameraCalibrationML. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>先启用 <code class="usage-code">Camera Calibration Core</code>，再启用实验性 <code class="usage-code">Camera Calibration Machine Learning</code>（模块 <code class="usage-code">CameraCalibrationML</code>）。它是畸变拟合的参考实现，不是完整现场标定台。</li><li>准备覆盖画面边缘的镜头素材（棋盘格/特征丰富的实拍），焦段与对焦与上舞台镜头一致；纯 OpenCV 多项式拟合不好的桶形/须状畸变才需要这条路径。</li><li>在镜头文件的畸变步骤里改用 ML 算法（<code class="usage-code">UCameraLensDistortionAlgo</code> 的机器学习实现），把序列送进 <code class="usage-code">CameraCalibrationML</code> 拟合，而不是只点 <code class="usage-code">Add To Lens Distortion Calibration</code> 的棋盘格求解。</li><li>把拟合结果写回同一份 <code class="usage-code">ULensFile</code>（球面系数或模型权重），再用 <code class="usage-code">ULensComponent</code> 在电影摄像机上求值，对比 ML 与 OpenCV 两套重投影误差。</li><li>确认本机 NNE/推理后端能加载插件自带的参考网络；缺运行时会静默退回传统求解。</li><li>不要把 <code class="usage-code">CameraCalibrationML</code> 写进 Shipping 游戏 <code class="usage-code">Build.cs</code>；舞台只消费已经烘焙进 <code class="usage-code">Lens File</code> 的参数。</li></ol><p class="usage-note">Experimental 参考实现；结果仍落在 `Lens File`，合成管线读的是 Core，不是 ML 模块。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Camera Calibration Core</code> first, then experimental <code class="usage-code">Camera Calibration Machine Learning</code> (module <code class="usage-code">CameraCalibrationML</code>). It is a reference fitter, not the full on-set calibrator.</li><li>Capture plates that fill the frame edges (checkerboard or feature-rich set) at the same focus/zoom as the show lens. Use this path when OpenCV polynomials fail on strong barrel/mustache distortion.</li><li>On the Lens File distortion step, switch to the ML <code class="usage-code">UCameraLensDistortionAlgo</code> and feed the sequence into <code class="usage-code">CameraCalibrationML</code> instead of only OpenCV <code class="usage-code">Add To Lens Distortion Calibration</code>.</li><li>Write the fit back into the same <code class="usage-code">ULensFile</code> (spherical coeffs or model weights), evaluate with <code class="usage-code">ULensComponent</code> on the cine camera, and compare reprojection error against the OpenCV table.</li><li>Confirm an NNE/inferencing backend can load the reference network; missing runtime often falls back to the classical solver with no obvious UI error.</li><li>Do not add <code class="usage-code">CameraCalibrationML</code> to a shipping game <code class="usage-code">Build.cs</code>. The stage should consume parameters already baked into the <code class="usage-code">Lens File</code>.</li></ol><p class="usage-note">Experimental reference only. Results still land in the `Lens File`; compositing reads Core, not the ML module.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CameraCalibrationML</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/VirtualProduction/CameraCalibrationML/CameraCalibrationML.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
