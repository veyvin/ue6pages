---
layout: default
title: 音频测试助手 / Audio Test Helper
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Audio Test Helper</div>
      <div class="hero-title-cn">音频测试助手 · 跨音频测试模块共享可重复使用的音频测试实用程序（信号生成、缓冲区</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Audio</span><span class="chip">Epic Games Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Tests/AudioTestHelper/AudioTestHelper.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">跨音频测试模块共享可重复使用的音频测试实用程序（信号生成、缓冲区比较和 A/B 性能回归测量）。</div><div class="lang-content">Reusable audio test utilities (signal generation, buffer comparison, and A/B performance-regression measurement) shared across audio test modules.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：跨音频测试模块共享可重复使用的音频测试实用程序（信号生成、缓冲区比较和 A/B 性能回归测量）。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：AudioTestHelper。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Reusable audio test utilities (signal generation, buffer comparison, and A/B performance-regression measurement) shared across audio test modules.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: AudioTestHelper. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>仅在测试工程启用 <code class="usage-code">Audio Test Helper</code>（模块 <code class="usage-code">AudioTestHelper</code>，路径 <code class="usage-code">Plugins/Tests/AudioTestHelper</code>）。</li><li>在音频自动化/单元测试模块的 <code class="usage-code">Build.cs</code> 里把 <code class="usage-code">AudioTestHelper</code> 加为 Private 依赖，不要加进游戏运行时模块。</li><li>测试里用它生成参考信号（正弦/噪声等），再对 DSP 输出做缓冲区比较，而不是放到关卡里播 Sound。</li><li>写 A/B 性能回归时，用同一组 helper 测量处理前后耗时，断言退化。</li><li>通过 <code class="usage-code">Tools &gt; Session Frontend &gt; Automation</code> 跑依赖该模块的音频用例；不要在 Shipping 目标链接它。</li></ol><p class="usage-note">测试基础设施：信号生成、缓冲对比、A/B 性能回归，不是游戏内音频功能。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Audio Test Helper</code> only on test projects (module <code class="usage-code">AudioTestHelper</code>, <code class="usage-code">Plugins/Tests/AudioTestHelper</code>).</li><li>Add <code class="usage-code">AudioTestHelper</code> as a Private dependency in audio automation/unit-test <code class="usage-code">Build.cs</code> files, not in game runtime modules.</li><li>Use it to generate reference signals (sine/noise, etc.) and compare DSP output buffers — do not place it as a level Sound.</li><li>For A/B perf regressions, time processing with the same helpers and assert against the baseline.</li><li>Run dependent audio cases from <code class="usage-code">Tools &gt; Session Frontend &gt; Automation</code>; do not link it into Shipping.</li></ol><p class="usage-note">Test infrastructure for signal generation, buffer compare, and A/B perf regression — not in-game audio.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">AudioTestHelper</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Tests/AudioTestHelper/AudioTestHelper.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
