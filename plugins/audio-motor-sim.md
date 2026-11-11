---
layout: default
title: 音频引擎 是 / Audio Motor Sim
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Audio Motor Sim</div>
      <div class="hero-title-cn">音频引擎 是 · 模拟车辆音频的合成方法。</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Audio</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">3</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/AudioMotorSim/AudioMotorSim.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">模拟车辆音频的合成方法。</div><div class="lang-content">Compositional method for simulating audio for vehicles.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：模拟车辆音频的合成方法。</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：AudioMotorSim, AudioMotorSimStandardComponents, AudioMotorSimDebug。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Compositional method for simulating audio for vehicles.</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: AudioMotorSim, AudioMotorSimStandardComponents, AudioMotorSimDebug. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Audio Motor Sim</code>（<code class="usage-code">AudioMotorSim</code>、<code class="usage-code">AudioMotorSimStandardComponents</code>、<code class="usage-code">AudioMotorSimDebug</code>）。</li><li>在载具 Pawn 上添加 <code class="usage-code">UAudioMotorSimComponent</code>，作为发动机音频状态的合成器（不是普通 <code class="usage-code">Audio Component</code>）。</li><li>再从 <code class="usage-code">AudioMotorSimStandardComponents</code> 挂标准件：<code class="usage-code">UThrottleStateMotorSimComponent</code>、<code class="usage-code">UMotorPhysicsSimComponent</code>、<code class="usage-code">UResistanceMotorSimComponent</code>、<code class="usage-code">URevLimiterMotorSimComponent</code>、<code class="usage-code">UBoostMotorSimComponent</code>、<code class="usage-code">UVelocitySyncMotorSimComponent</code>。</li><li>每帧把油门、转速、挡位、速度写入这些 Sim 组件；<code class="usage-code">UAudioMotorSimComponent</code> 按组合结果输出 RPM/Load 等参数。</li><li>用这些参数驱动载具 MetaSound（或 Sound Cue 参数），不要把 Sim 组件当成可播放的 Sound Wave。</li><li>调试时打开 <code class="usage-code">AudioMotorSimDebug</code> 的绘制/日志核对 Sim 输出；Shipping 可关 Debug 模块。</li><li>C++ 游戏模块依赖 <code class="usage-code">AudioMotorSim</code> 与 <code class="usage-code">AudioMotorSimStandardComponents</code>，自定义 Sim 实现 <code class="usage-code">IAudioMotorSim</code>。</li></ol><p class="usage-note">这是载具发动机音频的组合仿真，不是混响或 Control Bus。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Audio Motor Sim</code> (<code class="usage-code">AudioMotorSim</code>, <code class="usage-code">AudioMotorSimStandardComponents</code>, <code class="usage-code">AudioMotorSimDebug</code>).</li><li>Add <code class="usage-code">UAudioMotorSimComponent</code> to the vehicle pawn as the composer of engine-audio state (not a generic <code class="usage-code">Audio Component</code>).</li><li>Attach stock pieces from <code class="usage-code">AudioMotorSimStandardComponents</code>: <code class="usage-code">UThrottleStateMotorSimComponent</code>, <code class="usage-code">UMotorPhysicsSimComponent</code>, <code class="usage-code">UResistanceMotorSimComponent</code>, <code class="usage-code">URevLimiterMotorSimComponent</code>, <code class="usage-code">UBoostMotorSimComponent</code>, <code class="usage-code">UVelocitySyncMotorSimComponent</code>.</li><li>Feed throttle, RPM, gear, and speed into those sim components each frame; <code class="usage-code">UAudioMotorSimComponent</code> composes RPM/Load outputs.</li><li>Drive the vehicle MetaSound (or Sound Cue parameters) from those outputs; the sim components are not playable Sound Waves.</li><li>Use <code class="usage-code">AudioMotorSimDebug</code> draw/logs while tuning; omit the debug module from shipping if you do not need it.</li><li>Game modules depend on <code class="usage-code">AudioMotorSim</code> and <code class="usage-code">AudioMotorSimStandardComponents</code>; custom pieces implement <code class="usage-code">IAudioMotorSim</code>.</li></ol><p class="usage-note">This is compositional vehicle-engine audio simulation, not reverb or Control Buses.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (3)</div><div class="module-item"><span class="dot"></span><span class="name mono">AudioMotorSim</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AudioMotorSimStandardComponents</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AudioMotorSimDebug</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/AudioMotorSim/AudioMotorSim.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
