---
layout: default
title: 天穹 / CelestialVault
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">CelestialVault</div>
      <div class="hero-title-cn">天穹 · 使用星历表实现地球天穹的 DaySequence</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Other</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">2</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/CelestialVault/CelestialVault.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">使用星历表实现地球天穹的 DaySequence</div><div class="lang-content">A DaySequence implementation of a Celestial Vault for Earth using ephemeris</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：使用星历表实现地球天穹的 DaySequence</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：CelestialVault, CelestialVaultEditor。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A DaySequence implementation of a Celestial Vault for Earth using ephemeris</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: CelestialVault, CelestialVaultEditor. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">CelestialVault</code>（运行时 <code class="usage-code">CelestialVault</code>，编辑器 <code class="usage-code">CelestialVaultEditor</code>）。</li><li>关卡里放置或选中 <code class="usage-code">DaySequence</code> 相关 Actor，把天穹实现切到基于星历的 <code class="usage-code">Celestial Vault</code>（地球），而不是普通天空大气材质。</li><li>在细节面板核对经纬度、日期时间和星历源，让太阳/月亮位置跟地理时间对齐。</li><li>Sequencer 里对 Day Sequence 打关键帧做昼夜；PIE 里看太阳方向是否随时间走。</li><li>游戏模块只依赖 <code class="usage-code">CelestialVault</code>；<code class="usage-code">CelestialVaultEditor</code> 不要写进 Game Target。</li></ol><p class="usage-note">这是 Day Sequence 的地球天穹实现，不是普通 Sky Atmosphere 后处理。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">CelestialVault</code> (runtime <code class="usage-code">CelestialVault</code>, editor <code class="usage-code">CelestialVaultEditor</code>).</li><li>In the level, use a <code class="usage-code">DaySequence</code> actor and pick the ephemeris-based <code class="usage-code">Celestial Vault</code> for Earth instead of a generic sky atmosphere material.</li><li>Set latitude/longitude, date/time, and the ephemeris source in Details so sun/moon match geography.</li><li>Keyframe the Day Sequence in Sequencer; in PIE confirm the sun moves with time.</li><li>Game modules depend on <code class="usage-code">CelestialVault</code> only; keep <code class="usage-code">CelestialVaultEditor</code> off Game targets.</li></ol><p class="usage-note">A Day Sequence celestial vault for Earth, not the stock Sky Atmosphere post-process.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (2)</div><div class="module-item"><span class="dot"></span><span class="name mono">CelestialVault</span><span class="tag runtime">Runtime</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CelestialVaultEditor</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/CelestialVault/CelestialVault.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
