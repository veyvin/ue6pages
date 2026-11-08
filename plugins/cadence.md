---
layout: default
title: 节奏 / Cadence
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cadence</div>
      <div class="hero-title-cn">节奏 · Cadence 是一种固定滴答网络物理系统：它驱动 UWorld</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Physics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Cadence/Cadence/Cadence.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">Cadence 是一种固定滴答网络物理系统：它驱动 UWorld::Tick 作为每个引擎帧的 N 个固定子滴答，复制每帧增强输入，并从一个游戏线程拥有的重模拟驱动程序倒带和重放游戏线程和混沌解算器。</div><div class="lang-content">Cadence is a fixed-tick networked-physics system: it drives UWorld::Tick as N fixed sub-ticks per engine frame, replicates per-frame Enhanced Input, and rewinds and replays both the game thread and the Chaos solver from one game-thread-owned resimulation driver.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：Cadence 是一种固定滴答网络物理系统：它驱动 UWorld::Tick 作为每个引擎帧的 N 个固定子滴答，复制每帧增强输入，并从一个游戏线程拥有的重模拟驱动程序倒带和重放游戏线程和混沌解算器。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：Cadence。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Cadence is a fixed-tick networked-physics system: it drives UWorld::Tick as N fixed sub-ticks per engine frame, replicates per-frame Enhanced Input, and rewinds and replays both the game thread and the Chaos solver from one game-thread-owned resimulation driver.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: Cadence. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>在 <code class="usage-code">Edit &gt; Plugins</code> 启用 <code class="usage-code">Cadence</code>（模块 <code class="usage-code">Cadence</code>）并重启；它改的是整世界固定子滴答，不是给 Actor 挂的普通物理组件。</li><li>项目必须走 <code class="usage-code">Enhanced Input</code>：在 <code class="usage-code">Project Settings &gt; Input</code> 关掉旧轴映射依赖。Cadence 按子滴答复制每帧 EI，松开按键时要在 <code class="usage-code">Completed</code>/<code class="usage-code">Canceled</code> 把输入写回 0，否则倒带会一直吃最后一帧推力。</li><li>在 <code class="usage-code">Project Settings</code> 搜 <code class="usage-code">Cadence</code>，设定每个引擎帧拆成的固定子滴答数 N，让 <code class="usage-code">UWorld::Tick</code> 按定步长推进；同时打开 Chaos 的 <code class="usage-code">Tick Physics Async</code> 与 <code class="usage-code">Enable Physics Prediction</code>，异步步长与 Cadence 子滴答对齐（例如 1/60）。</li><li>对需要预测的 Pawn/载具：开启 <code class="usage-code">Replicates</code>、把 <code class="usage-code">Physics Replication Mode</code> 设为 <code class="usage-code">Resimulation</code>，力与约束只在 Chaos 刚体上施加。Cadence 用游戏线程持有的单一重模拟驱动同时倒带游戏逻辑和求解器，不要再在同一 Actor 上叠一套独立的 Network Prediction 移动。</li><li>游戏逻辑按 <code class="usage-code">GetWorld()-&gt;GetDeltaSeconds()</code> 做的位移、冷却、随机数必须能在重放时得到同一结果；把不可复现的 <code class="usage-code">FMath::Rand</code>、真实墙钟、未复制的计时器移出 Cadence 子滴答。</li><li>C++ 在游戏 <code class="usage-code">Build.cs</code> 加入 <code class="usage-code">Cadence</code>，从该模块 Public 头使用重模拟驱动/世界接口，而不是自己缓存另一份物理历史。</li><li>用 Listen Server 开两份 PIE，人为加延迟后撞动物体：确认客户端会 rewind 再 replay，而不是只做位置插值。</li></ol><p class="usage-note">Cadence 同时倒带游戏线程与 Chaos；可变帧率 Tick 或旧 Input Axis 都会让客户端/服务器物理分叉。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Cadence</code> in <code class="usage-code">Edit &gt; Plugins</code> (module <code class="usage-code">Cadence</code>) and restart. It retimes the whole world into fixed sub-ticks; it is not a component you drop on an Actor.</li><li>Use <code class="usage-code">Enhanced Input</code> only (<code class="usage-code">Project Settings &gt; Input</code>). Cadence replicates per-sub-tick EI; write 0 on <code class="usage-code">Completed</code>/<code class="usage-code">Canceled</code> so rewind does not keep the last held axis.</li><li>In <code class="usage-code">Project Settings</code> search <code class="usage-code">Cadence</code> and set N fixed sub-ticks per engine frame so <code class="usage-code">UWorld::Tick</code> is deterministic. Enable Chaos <code class="usage-code">Tick Physics Async</code> and <code class="usage-code">Enable Physics Prediction</code>, matching the async step to those sub-ticks (for example 1/60).</li><li>On predicted pawns/vehicles: <code class="usage-code">Replicates</code> on, <code class="usage-code">Physics Replication Mode</code> = <code class="usage-code">Resimulation</code>, forces only on Chaos bodies. Cadence’s one game-thread resimulation driver rewinds gameplay and the solver together — do not also run Network Prediction movement on the same Actor.</li><li>Any gameplay that uses <code class="usage-code">GetWorld()-&gt;GetDeltaSeconds()</code> (motion, cooldowns, RNG) must be replay-safe. Keep wall-clock time, unreplicated timers, and <code class="usage-code">FMath::Rand</code> off the Cadence sub-tick.</li><li>Add <code class="usage-code">Cadence</code> to the game <code class="usage-code">Build.cs</code> and use the plugin’s Public resimulation/world API instead of a second physics-history cache.</li><li>PIE as Listen Server with two clients, inject latency, then collide: the client should rewind and replay, not merely interpolate transforms.</li></ol><p class="usage-note">Cadence rewinds the game thread and Chaos together. Variable-rate Tick or legacy Input Axis will desync client vs server physics.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">Cadence</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Cadence/Cadence/Cadence.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
