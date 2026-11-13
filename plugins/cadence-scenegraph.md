---
layout: default
title: Cadence场景图 / Cadence SceneGraph
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">C</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">Cadence SceneGraph</div>
      <div class="hero-title-cn">Cadence场景图 · 跟踪玩家在 Cadence 状态缓存中拥有的 SceneGrap</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Physics</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">0.1</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Cadence/CadenceSceneGraph/CadenceSceneGraph.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">跟踪玩家在 Cadence 状态缓存中拥有的 SceneGraph 实体，因此将其复制的变换与客户端对同一帧的预测进行比较，并通过重新模拟进行纠正；将 Cadence 复制的输入提供给服务器上的 Verse 输入以及各处的 own_input_component。</div><div class="lang-content">Tracks SceneGraph entities a player possesses in the Cadence state cache, so their replicated transforms are compared against the client's prediction for the same frame and corrected by a resimulation; feeds Cadence-replicated input to Verse input on the server and to possessed_input_component everywhere.</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：跟踪玩家在 Cadence 状态缓存中拥有的 SceneGraph 实体，因此将其复制的变换与客户端对同一帧的预测进行比较，并通过重新模拟进行纠正；将 Cadence 复制的输入提供给服务器上的 Verse 输入以及各处的 own_input_component。</p><p>Verse 语言/运行时的一块：编译、VM、设备或编辑器支持，服务 UEFN 体验。</p><p>这是引擎 Plugins 目录下的官方插件，由对应 .uplugin 描述其职责。</p><p>它打包的模块包括：CadenceSceneGraph。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: Tracks SceneGraph entities a player possesses in the Cadence state cache, so their replicated transforms are compared against the client's prediction for the same frame and corrected by a resimulation; feeds Cadence-replicated input to Verse input on the server and to possessed_input_component everywhere.</p><p>A slice of the Verse language/runtime: compiler, VM, devices, or editor support for UEFN.</p><p>This is an engine plugin under Plugins/; its .uplugin states its job.</p><p>It ships these modules: CadenceSceneGraph. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">Cadence</code>、<code class="usage-code">Cadence Input System</code> 与 <code class="usage-code">Cadence SceneGraph</code>（模块 <code class="usage-code">CadenceSceneGraph</code>），并打开项目的 Scene Graph / Verse。</li><li>用 Scene Graph 实体作为玩家拥有物（possess），而不是只依赖传统 Pawn 复制。</li><li>在实体上使用 <code class="usage-code">possessed_input_component</code>（文档也称 own_input_component）：客户端输入经 Cadence 复制后，服务器侧喂给 Verse input，各端组件都能读到同一份输入。</li><li>Cadence 状态缓存会记下这些被拥有实体；每帧把复制过来的变换与客户端对该帧的预测比较，偏差则触发 resimulation 纠正。</li><li>玩法移动/朝向应写在可预测的 Scene Graph / Verse 路径上，避免在不可回放的 Actor Tick 里改同一变换。</li><li>C++ 游戏代码若要挂钩，仅对需要扩展的模块依赖 <code class="usage-code">CadenceSceneGraph</code>，并以该模块 Public 头文件为准。</li><li>用 <code class="usage-code">Cadence SceneGraph Tests</code> 的 specs 回归 possess 变换纠正与输入转发。</li></ol><p class="usage-note">职责是 possess 的 Scene Graph 实体进 Cadence 状态缓存，并转发复制输入到 Verse / `possessed_input_component`。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">Cadence</code>, <code class="usage-code">Cadence Input System</code>, and <code class="usage-code">Cadence SceneGraph</code> (module <code class="usage-code">CadenceSceneGraph</code>), with Scene Graph / Verse on in the project.</li><li>Possess Scene Graph entities as the player-owned objects rather than relying only on classic Pawn replication.</li><li>Put <code class="usage-code">possessed_input_component</code> (also called own_input_component in the plugin text) on those entities: Cadence-replicated input is fed to Verse input on the server and to the component everywhere.</li><li>Cadence’s state cache tracks possessed entities, compares replicated transforms to the client prediction for the same frame, and corrects with resimulation.</li><li>Keep movement/aim on the predict-able Scene Graph / Verse path; do not also write the same transform from an unreplayable Actor <code class="usage-code">Tick</code>.</li><li>If you extend in C++, depend on <code class="usage-code">CadenceSceneGraph</code> only where needed and follow that module’s Public headers.</li><li>Regress possess-transform correction and input forwarding with <code class="usage-code">Cadence SceneGraph Tests</code> specs.</li></ol><p class="usage-note">Tracks possessed Scene Graph entities in the Cadence state cache and forwards replicated input to Verse and `possessed_input_component`.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">CadenceSceneGraph</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Cadence/CadenceSceneGraph/CadenceSceneGraph.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
