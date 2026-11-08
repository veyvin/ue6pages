---
layout: default
title: 踏频输入系统 / Cadence Input System
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cadence Input System</div>
      <div class="hero-title-cn">踏频输入系统 · 通过执行输入动作委托的每帧记录和重放来扩展增强输入，因此游戏输入</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Input</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Cadence/CadenceInput/CadenceInput.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">通过执行输入动作委托的每帧记录和重放来扩展增强输入，因此游戏输入可以参与网络重新模拟和回滚。</div><div class="lang-content">Extends Enhanced Input with per-frame recording and replay of executed input action delegates, so gameplay input can participate in network resimulation and rollback.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：通过执行输入动作委托的每帧记录和重放来扩展增强输入，因此游戏输入可以参与网络重新模拟和回滚。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CadenceInput。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Extends Enhanced Input with per-frame recording and replay of executed input action delegates, so gameplay input can participate in network resimulation and rollback.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CadenceInput. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>同时启用 <code class="usage-code">Cadence</code> 与 <code class="usage-code">Cadence Input System</code>（模块 <code class="usage-code">CadenceInput</code>），并保持 <code class="usage-code">Enhanced Input</code> 开启，然后重启。</li><li>按 Enhanced Input 常规流程创建 <code class="usage-code">UInputAction</code> 和 <code class="usage-code">UInputMappingContext</code>，通过 <code class="usage-code">UEnhancedInputLocalPlayerSubsystem</code> 加到本地玩家。</li><li>把会改变模拟状态的玩法（移动、开火、跳跃）绑在 Input Action 的 <code class="usage-code">Triggered</code> / <code class="usage-code">Started</code> / <code class="usage-code">Completed</code> 委托上，而不是每帧轮询按键。</li><li><code class="usage-code">CadenceInput</code> 会按固定子 tick 记录这些已执行的 action 委托；网络回滚时按同一帧顺序重放，从而参加 Cadence 的 resimulation。</li><li>不要在普通 <code class="usage-code">Tick</code> 里直接读原始按键来改 Chaos/位置，否则回放对不上记录的输入。</li><li>需要扩展时在模块 <code class="usage-code">Build.cs</code> 加入 <code class="usage-code">CadenceInput</code>（通常还要 <code class="usage-code">Cadence</code>、<code class="usage-code">EnhancedInput</code>），以引擎该模块 Public 头文件为准。</li><li>用 Cadence 校正/resim 报告或 <code class="usage-code">Cadence Tests</code> 夹具验证：同一输入序列在客户端预测与服务器重放后状态一致。</li></ol><p class="usage-note">它扩展 Enhanced Input 的委托记录/重放，并不替换 Mapping Context。玩法必须走 action 委托才能进 Cadence 回滚。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Cadence</code> and <code class="usage-code">Cadence Input System</code> (module <code class="usage-code">CadenceInput</code>) together with <code class="usage-code">Enhanced Input</code>, then restart.</li><li>Author <code class="usage-code">UInputAction</code> and <code class="usage-code">UInputMappingContext</code> as usual and add the context via <code class="usage-code">UEnhancedInputLocalPlayerSubsystem</code>.</li><li>Drive sim-changing gameplay (move, fire, jump) from Input Action <code class="usage-code">Triggered</code> / <code class="usage-code">Started</code> / <code class="usage-code">Completed</code> delegates, not from raw key polling.</li><li><code class="usage-code">CadenceInput</code> records those executed action delegates per Cadence sub-tick and replays them in order on rollback so input joins resimulation.</li><li>Do not mutate Chaos/transform from a generic <code class="usage-code">Tick</code> that reads hardware keys — that path is invisible to recorded replay.</li><li>To extend in C++, add <code class="usage-code">CadenceInput</code> (typically with <code class="usage-code">Cadence</code> and <code class="usage-code">EnhancedInput</code>) in <code class="usage-code">Build.cs</code> and follow that module’s Public headers.</li><li>Verify with Cadence correction/resim reports or the <code class="usage-code">Cadence Tests</code> fixture that a recorded input sequence matches after client predict and server replay.</li></ol><p class="usage-note">Records and replays Enhanced Input action delegates; it does not replace Mapping Contexts. Gameplay must sit on those delegates to join Cadence rollback.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CadenceInput</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Cadence/CadenceInput/CadenceInput.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
