---
layout: default
title: MassEntityEditor
---

<!-- Hero card -->
<div class="hero">
  <div class="hero-top">
    <div class="hero-badge" style="background:linear-gradient(135deg,#8A5CF6 0%,#B08BF9 100%);">
      <span>M</span>
    </div>
    <div class="hero-info">
      <div class="hero-subtitle">Module / C++ Build Rule</div>
      <div class="hero-title mono">MassEntityEditor</div>
      <div class="hero-tags">
        <span class="chip chip-primary"><span style="width:6px;height:6px;border-radius:50%;background:var(--primary);display:inline-block;"></span>Module</span>
        <span class="chip">extends <span class="mono">ModuleRules</span></span>
        <span class="chip">26 dependencies</span>
      </div>
    </div>
  </div>
  <div class="meta-grid">
    <div class="meta-item"><div class="meta-label">Type</div><div class="meta-value mono">Module</div></div>
    <div class="meta-item"><div class="meta-label">Base</div><div class="meta-value mono">ModuleRules</div></div>
    <div class="meta-item"><div class="meta-label">Dependencies</div><div class="meta-value mono">26</div></div>
    <div class="meta-item"><div class="meta-label">Language</div><div class="meta-value">C# (Build.cs)</div></div>
    <div class="meta-item file-col"><div class="meta-label">File</div><div class="file-path mono">Editor/MassEntityEditor/MassEntityEditor.Build.cs</div></div>
  </div>
</div>

<!-- Two-column content -->
<div class="content-grid">
  <div>
    <div class="card">
      <div class="card-title"><span class="card-title-sep"></span>Overview<span class="card-title-cn">概览</span></div>
      <div class="desc-body">
<div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active">该模块依赖于 26 个其他模块：AIGraph、AssetTools、ComponentVisualizers、Core、CoreUObject、DetailCustomizations、DeveloperSettings、EditorSubsystem、Engine、GraphEditor、InputCore、KismetWidgets、MassCore、MassDeveloper、MassEntity、MessageLog、Projects、PropertyEditor、RenderCore、RewindDebuggerInterface、Slate、SlateCore、ToolMenus、TraceLog、TraceServices、虚幻编辑器。</div><div class="lang-content">This module depends on 26 other module(s): AIGraph, AssetTools, ComponentVisualizers, Core, CoreUObject, DetailCustomizations, DeveloperSettings, EditorSubsystem, Engine, GraphEditor, InputCore, KismetWidgets, MassCore, MassDeveloper, MassEntity, MessageLog, Projects, PropertyEditor, RenderCore, RewindDebuggerInterface, Slate, SlateCore, ToolMenus, TraceLog, TraceServices, UnrealEd.</div></div>
      </div>
    </div>
    

    

    

    

    

        <div class="card role-card" id="role">
      <div class="card-title"><span class="card-title-sep"></span>Role<span class="card-title-cn">作用</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><p>Epic 在插件/模块描述里写的职责是：该模块依赖于 26 个其他模块：AIGraph、AssetTools、ComponentVisualizers、Core、CoreUObject、DetailCustomizations、DeveloperSettings、EditorSubsystem、Engine、GraphEditor、InputCore、KismetWidgets、MassCore、MassDeveloper、MassEntity、MessageLog、Projects、PropertyEditor、RenderCore、RewindDebuggerInterface、Slate、SlateCore、ToolMenus、TraceLog、TraceServices、虚幻编辑器。</p><p>Mass 家族：ECS 风格的大规模实体（碎片、处理器、可视化或 AI）。不要按普通 Actor 组件去理解。</p><p>这是 Editor 模块，只在编辑器进程加载，不能链进 Game Target。</p><p>UBT 声明它还依赖：AIGraph, AssetTools, ComponentVisualizers, Core, CoreUObject, DetailCustomizations, DeveloperSettings, EditorSubsystem。这些依赖暗示了它和哪些子系统协作。</p><p class="usage-note">作用说明综合了 Epic 在 .uplugin / Build.cs 中的官方描述，以及该插件在引擎源码树中的位置与模块职责（非「点启用」模板）。</p></div><div class="lang-content"><p>Epic’s own description of its job: This module depends on 26 other module(s): AIGraph, AssetTools, ComponentVisualizers, Core, CoreUObject, DetailCustomizations, DeveloperSettings, EditorSubsystem, Engine, GraphEditor, InputCore, KismetWidgets, MassCore, MassDeveloper, MassEntity, MessageLog, Projects, PropertyEditor, RenderCore, RewindDebuggerInterface, Slate, SlateCore, ToolMenus, TraceLog, TraceServices, UnrealEd.</p><p>Mass family: ECS-style mass entities (fragments, processors, debug, or AI) — not a typical Actor component.</p><p>This is an Editor module, loaded only in the editor process — do not link it into a Game target.</p><p>UBT also lists dependencies on: AIGraph, AssetTools, ComponentVisualizers, Core, CoreUObject, DetailCustomizations, DeveloperSettings, EditorSubsystem. Those names show which subsystems it talks to.</p><p class="usage-note">Role text combines Epic’s official Description with where this item lives in the engine tree and which modules it ships — not an enable-plugin template.</p></div></div></div>
    </div>


    <div class="card usage-card" id="usage" data-usage-source="ai">
      <style>.usage-steps{margin:0;padding-left:22px}.usage-steps li{margin-bottom:12px;line-height:1.7}.usage-steps li:last-child{margin-bottom:0}.usage-code{font-family:'JetBrains Mono',ui-monospace,monospace;font-size:12.5px;background:var(--surface-container-highest);padding:1px 7px;border-radius:8px;word-break:break-all}.usage-note{margin-top:16px;font-size:13px;color:var(--on-surface-variant);line-height:1.6}.usage-card .desc-body .bilingual-block{margin-bottom:0}</style>
      <div class="card-title"><span class="card-title-sep"></span>How to use<span class="card-title-cn">使用方法</span></div>
      <div class="desc-body"><div class="bilingual-block"><div class="lang-tabs"><button class="lang-tab active" onclick="switchLang(this)">中文</button><button class="lang-tab" onclick="switchLang(this)">English</button></div><div class="lang-content active"><ol class="usage-steps"><li>用途：<code class="usage-code">MassEntityEditor</code> 位于 <code class="usage-code">Editor</code>，构建规则 <code class="usage-code">Editor/MassEntityEditor/MassEntityEditor.Build.cs</code>。它直接依赖 8 个模块：<code class="usage-code">AIGraph</code>, <code class="usage-code">AssetTools</code>, <code class="usage-code">ComponentVisualizers</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">DetailCustomizations</code>, <code class="usage-code">DeveloperSettings</code>, <code class="usage-code">EditorSubsystem</code>。</li><li>依赖：在 <code class="usage-code">YourModule.Build.cs</code> 加入 <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;MassEntityEditor&quot; });</code>；对外暴露 <code class="usage-code">MassEntityEditor</code> 类型用 Public，仅内部调用用 Private，然后 Generate Project Files 并编译。</li><li>部署：<code class="usage-code">MassEntityEditor</code> 是编辑器模块，只能写进 <code class="usage-code">*Editor.Build.cs</code> 或编辑器插件；加进 Game Target 会链接失败。</li><li>调用：#include 其 Public 头（常见 <code class="usage-code">MassEntityEditor.h</code> / <code class="usage-code">MassEntityEditorModule.h</code>），再用 <code class="usage-code">FModuleManager::LoadModulePtr&lt;MassEntityEditorModule&gt;</code> 或直接使用导出类型。</li><li>传递依赖：<code class="usage-code">MassEntityEditor</code> 还依赖 <code class="usage-code">AIGraph</code>, <code class="usage-code">AssetTools</code>, <code class="usage-code">ComponentVisualizers</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">DetailCustomizations</code>, <code class="usage-code">DeveloperSettings</code>, <code class="usage-code">EditorSubsystem</code>；不必在游戏模块重复填写，除非你要直接 include 那些头文件。</li></ol><p class="usage-note">`MassEntityEditor` 的构建规则位于 `Editor/MassEntityEditor/MassEntityEditor.Build.cs`，直接依赖 8 个模块，分类 Module。</p></div><div class="lang-content"><ol class="usage-steps"><li>Purpose: <code class="usage-code">MassEntityEditor</code> lives under <code class="usage-code">Editor</code>; build rule <code class="usage-code">Editor/MassEntityEditor/MassEntityEditor.Build.cs</code>.It directly depends on 8 modules: <code class="usage-code">AIGraph</code>, <code class="usage-code">AssetTools</code>, <code class="usage-code">ComponentVisualizers</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">DetailCustomizations</code>, <code class="usage-code">DeveloperSettings</code>, <code class="usage-code">EditorSubsystem</code>.</li><li>Depend: in <code class="usage-code">YourModule.Build.cs</code> add <code class="usage-code">PublicDependencyModuleNames.AddRange(new string[] { &quot;MassEntityEditor&quot; });</code>. Use Public when exposing <code class="usage-code">MassEntityEditor</code> types, Private if only calling it; then Generate Project Files and rebuild.</li><li>Placement: <code class="usage-code">MassEntityEditor</code> is editor-only. Put it in <code class="usage-code">*Editor.Build.cs</code> or an editor plugin — never a Game target.</li><li>Call: include Public headers (often <code class="usage-code">MassEntityEditor.h</code> / <code class="usage-code">MassEntityEditorModule.h</code>), then use <code class="usage-code">FModuleManager::LoadModulePtr&lt;MassEntityEditorModule&gt;</code> or the exported types directly.</li><li>Transitive deps: <code class="usage-code">MassEntityEditor</code> also needs <code class="usage-code">AIGraph</code>, <code class="usage-code">AssetTools</code>, <code class="usage-code">ComponentVisualizers</code>, <code class="usage-code">Core</code>, <code class="usage-code">CoreUObject</code>, <code class="usage-code">DetailCustomizations</code>, <code class="usage-code">DeveloperSettings</code>, <code class="usage-code">EditorSubsystem</code>; do not re-list them unless you include their headers.</li></ol><p class="usage-note">`MassEntityEditor` build rule is `Editor/MassEntityEditor/MassEntityEditor.Build.cs`; depends on 8 modules; category Module.</p></div></div></div>
    </div>

  </div>
  <aside class="detail-sidebar">
    <div class="sidebar-card">
      <div class="sidebar-card-title">Dependencies (26)</div>
      <div class="module-item"><span class="dot"></span><span class="name mono">AIGraph</span></div><div class="module-item"><span class="dot"></span><span class="name mono">AssetTools</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ComponentVisualizers</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Core</span></div><div class="module-item"><span class="dot"></span><span class="name mono">CoreUObject</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DetailCustomizations</span></div><div class="module-item"><span class="dot"></span><span class="name mono">DeveloperSettings</span></div><div class="module-item"><span class="dot"></span><span class="name mono">EditorSubsystem</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Engine</span></div><div class="module-item"><span class="dot"></span><span class="name mono">GraphEditor</span></div><div class="module-item"><span class="dot"></span><span class="name mono">InputCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">KismetWidgets</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MassCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MassDeveloper</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MassEntity</span></div><div class="module-item"><span class="dot"></span><span class="name mono">MessageLog</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Projects</span></div><div class="module-item"><span class="dot"></span><span class="name mono">PropertyEditor</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RenderCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">RewindDebuggerInterface</span></div><div class="module-item"><span class="dot"></span><span class="name mono">Slate</span></div><div class="module-item"><span class="dot"></span><span class="name mono">SlateCore</span></div><div class="module-item"><span class="dot"></span><span class="name mono">ToolMenus</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TraceLog</span></div><div class="module-item"><span class="dot"></span><span class="name mono">TraceServices</span></div><div class="module-item"><span class="dot"></span><span class="name mono">UnrealEd</span></div>
    </div>
    <div class="sidebar-card" style="background:var(--surface-container);">
      <div class="sidebar-card-title">Build rule file</div>
      <div style="font-size:12px;color:var(--on-surface-variant);line-height:1.6;">
        <span class="mono">Editor/MassEntityEditor/MassEntityEditor.Build.cs</span>
      </div>
    </div>
  </aside>
</div>
