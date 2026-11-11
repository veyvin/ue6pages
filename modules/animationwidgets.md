---
layout: default
title: AnimationWidgets
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>A</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">AnimationWidgets</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">11 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">11</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Developer/AnimationWidgets/AnimationWidgets.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于其他 11 个模块：AnimationCore、Core、CoreUObject、Engine、GraphEditor、InputCore、PropertyEditor、Slate、SlateCore、ToolWidgets、UnrealEd。</div><div class="lang-content">This module depends on 11 other module(s): AnimationCore, Core, CoreUObject, Engine, GraphEditor, InputCore, PropertyEditor, Slate, SlateCore, ToolWidgets, UnrealEd.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：该模块依赖于其他 11 个模块：AnimationCore、Core、CoreUObject、Engine、GraphEditor、InputCore、PropertyEditor、Slate、SlateCore、ToolWidgets、UnrealEd。</p><p>这是开发者工具或独立程序模块，给 Insights、UBT、命令行用。</p><p>UBT 声明它还依赖：AnimationCore, Core, CoreUObject, Engine, GraphEditor, InputCore, PropertyEditor, Slate。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: This module depends on 11 other module(s): AnimationCore, Core, CoreUObject, Engine, GraphEditor, InputCore, PropertyEditor, Slate, SlateCore, ToolWidgets, UnrealEd.</p><p>This is a developer tool or program module for Insights, UBT, or command-line apps.</p><p>UBT also lists dependencies on: AnimationCore, Core, CoreUObject, Engine, GraphEditor, InputCore, PropertyEditor, Slate. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>

    

    

    

    

    

    

    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li><code class="usage-code">AnimationWidgets</code>（Animation Widgets）：它属于动画系统（骨架、动画图、Control Rig、IK、姿态、MetaHuman/DNA）。位于 <code class="usage-code">Developer</code>，构建规则 <code class="usage-code">Developer/AnimationWidgets/AnimationWidgets.Build.cs</code>。直接依赖 8 个模块：<code class="usage-code">AnimationCore</code>、<code class="usage-code">Core</code>、<code class="usage-code">CoreUObject</code>、<code class="usage-code">Engine</code>、<code class="usage-code">GraphEditor</code> 等。</li><li>部署：<code class="usage-code">AnimationWidgets</code> 开发者/工具模块，供编辑器或命令行使用，不要当游戏运行时依赖。</li><li>怎么用：把资产挂到骨架网格体、在动画蓝图或 Sequencer 轨道采样；动画逻辑放在 AnimGraph 或 C++ AnimNode。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;AnimationWidgets&quot; });</code>；对外暴露 <code class="usage-code">AnimationWidgets</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>调用：包含其 <code class="usage-code">Public/</code> 头文件以使用导出类型；模块由引擎/插件系统自动加载，通常无需手动 <code class="usage-code">LoadModulePtr</code>（仅懒加载时才用 <code class="usage-code">FModuleManager::LoadModuleChecked</code>）。</li></ol><p class="usage-note">`AnimationWidgets`：它属于动画系统（骨架、动画图、Control Rig、IK、姿态、MetaHuman/DNA）；构建规则 `Developer/AnimationWidgets/AnimationWidgets.Build.cs`，直接依赖 8 个模块。</p></div><div class="lang-content"><ol class="usage-steps"><li><code class="usage-code">AnimationWidgets</code> (Animation Widgets): it is part of the animation system (skeleton, anim graph, Control Rig, IK, pose, MetaHuman/DNA). Located under <code class="usage-code">Developer</code>; build rule <code class="usage-code">Developer/AnimationWidgets/AnimationWidgets.Build.cs</code>. It directly depends on 8 modules: <code class="usage-code">AnimationCore</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">Engine</code>, <code class="usage-code">GraphEditor</code> etc.</li><li>Placement: <code class="usage-code">AnimationWidgets</code> is a developer/tool module for editor or CLI use; not a game runtime dependency.</li><li>How to use: attach assets to a skeletal mesh and sample in AnimBP or Sequencer; animation logic lives in AnimGraph or C++ AnimNodes.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;AnimationWidgets&quot; });</code>. Use Public when exposing <code class="usage-code">AnimationWidgets</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Call: include its <code class="usage-code">Public/</code> headers to use exported types; the engine/plugin system loads the module automatically — no manual <code class="usage-code">LoadModulePtr</code> needed (use <code class="usage-code">FModuleManager::LoadModuleChecked</code> only for lazy loading).</li></ol><p class="usage-note">`AnimationWidgets`: it is part of the animation system (skeleton, anim graph, Control Rig, IK, pose, MetaHuman/DNA); build rule `Developer/AnimationWidgets/AnimationWidgets.Build.cs`; depends on 8 modules.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (11)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">AnimationCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Engine</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GraphEditor</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InputCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PropertyEditor</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Slate</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SlateCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ToolWidgets</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealEd</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Developer/AnimationWidgets/AnimationWidgets.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
