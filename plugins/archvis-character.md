---
layout: default
title: ArchVis 角色 / ArchVis Character
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge">A</div>
    <div class="hero-info">
      <div class="hero-subtitle">Plugin / 插件</div>
      <div class="hero-title">ArchVis Character</div>
      <div class="hero-title-cn">ArchVis 角色 · 专为建筑应用而调整的可控角色</div>
      <div class="hero-tags"><span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Gameplay</span><span class="chip">Epic Games, Inc.</span></div>
    </div>
  </div>
  <div class="meta-grid"><div class="meta-item"><div class="meta-label">Version</div><div class="meta-value mono">1.0</div></div><div class="meta-item"><div class="meta-label">Engine</div><div class="meta-value mono">—</div></div><div class="meta-item"><div class="meta-label">Author</div><div class="meta-value">Epic Games, Inc.</div></div><div class="meta-item"><div class="meta-label">Modules</div><div class="meta-value mono">1</div></div><div class="meta-item file-col"><div class="meta-label">Plugin File</div><div class="file-path mono">Plugins/Runtime/ArchVisCharacter/ArchVisCharacter.uplugin</div></div></div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Description<span class="card-title-cn">描述</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">专为建筑应用而调整的可控角色</div><div class="lang-content">A controllable character tuned for architectural applications</div></div></div>
    </div>
    
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：专为建筑应用而调整的可控角色</p><p>运行时插件，启用后可进游戏包。</p><p>它打包的模块包括：ArchVisCharacter。运行时逻辑在非 Editor 模块里，编辑器 UI 在 *Editor 模块里。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: A controllable character tuned for architectural applications</p><p>A runtime plugin that can ship in a cooked game.</p><p>It ships these modules: ArchVisCharacter. Runtime lives in non-Editor modules; UI in *Editor modules.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>启用 <code class="usage-code">ArchVis Character</code>（模块 <code class="usage-code">ArchVisCharacter</code>）。这是建筑漫游用的 <code class="usage-code">AArchVisCharacter</code>，不是动画骨架或 ArchVis 网格库。</li><li>新建继承 <code class="usage-code">ArchVisCharacter</code> 的蓝图，确认使用 <code class="usage-code">UArchVisCharMovementComponent</code>（平滑旋转加速度，而不是默认 <code class="usage-code">CharacterMovement</code> 的瞬时转向手感）。</li><li>在细节里调 <code class="usage-code">MouseSensitivityScale_Pitch</code> / <code class="usage-code">MouseSensitivityScale_Yaw</code>，以及移动组件上的 <code class="usage-code">RotationalAcceleration</code>、<code class="usage-code">RotationalDeceleration</code>、<code class="usage-code">MaxRotationalVelocity</code>；轴名属性（<code class="usage-code">MoveForwardAxisName</code>、<code class="usage-code">TurnAtRateAxisName</code> 等）必须与项目 Input Mapping 一致。</li><li>把 Game Mode 的 <code class="usage-code">Default Pawn Class</code> 设为该蓝图，碰撞胶囊按真实视高（约 160–180 cm）对齐室内门洞；通常关掉跳跃，避免穿出楼板。</li><li>游戏 <code class="usage-code">Build.cs</code> 加 <code class="usage-code">ArchVisCharacter</code>，头文件 <code class="usage-code">ArchVisCharacter.h</code> / <code class="usage-code">ArchVisCharMovementComponent.h</code>。在目标建筑关卡 PIE 走楼梯与窄廊验证加速度，不要用射击游戏默认 <code class="usage-code">FirstPersonCharacter</code> 代替。</li></ol><p class="usage-note">建筑第一人称漫游 Pawn。不导入建筑资产，也不替代 Chaos 物理角色。</p></div><div class="lang-content"><ol class="usage-steps"><li>Enable <code class="usage-code">ArchVis Character</code> (module <code class="usage-code">ArchVisCharacter</code>). This is the architectural walkthrough pawn <code class="usage-code">AArchVisCharacter</code>, not an animation skeleton or a mesh pack.</li><li>Create a Blueprint subclass of <code class="usage-code">ArchVisCharacter</code> and keep <code class="usage-code">UArchVisCharMovementComponent</code> (smoothed rotational acceleration, not stock <code class="usage-code">CharacterMovement</code> snap-turn feel).</li><li>Tune <code class="usage-code">MouseSensitivityScale_Pitch</code> / <code class="usage-code">MouseSensitivityScale_Yaw</code> and the movement component’s <code class="usage-code">RotationalAcceleration</code>, <code class="usage-code">RotationalDeceleration</code>, <code class="usage-code">MaxRotationalVelocity</code>. Axis name properties (<code class="usage-code">MoveForwardAxisName</code>, <code class="usage-code">TurnAtRateAxisName</code>, …) must match the project’s Input Mapping.</li><li>Set the Game Mode <code class="usage-code">Default Pawn Class</code> to that Blueprint. Size the capsule to a real eye height (~160–180 cm) for doorways; typically disable jump so you cannot leave the floor slab.</li><li>Add <code class="usage-code">ArchVisCharacter</code> to game <code class="usage-code">Build.cs</code> and include <code class="usage-code">ArchVisCharacter.h</code> / <code class="usage-code">ArchVisCharMovementComponent.h</code>. PIE the target interior (stairs, narrow halls). Do not substitute a shooter <code class="usage-code">FirstPersonCharacter</code>.</li></ol><p class="usage-note">First-person architectural pawn. It does not import archviz meshes and is not a Chaos physics character.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card"><div class="sidebar-card-title">Modules (1)</div><div class="module-item"><span class="dot"></span><span class="name mono">ArchVisCharacter</span><span class="tag runtime">Runtime</span></div></div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Auto-generated</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        Sourced from <span class="mono">Plugins/Runtime/ArchVisCharacter/ArchVisCharacter.uplugin</span>. Updated daily from the Unreal Engine source tree.
      </div>
    </div>
  </aside>
</div>
