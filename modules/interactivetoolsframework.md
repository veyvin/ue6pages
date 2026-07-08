---
layout: default
title: InteractiveToolsFramework
---

<!-- ai-generation-failed -->

<h1>InteractiveToolsFramework</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/InteractiveToolsFramework/InteractiveToolsFramework.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, EditorToolEvents, Engine, GeometryCore, InputCore, MeshDescription, RHI, RenderCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

sing the most specific base class helps you eliminate manual implementation of selection logic and focus entirely on your tool’s unique functionality.
Leverage Tool Property Sets
Define your tool’s settings in a UInteractiveToolPropertySet. These properties automatically appear in the “Details” panel when the tool is active. This helps you eliminate the need to write custom UI code for your tool’s parameters.
Use the Change Tracking System for Undo/Redo
The ITF includes a built-in “Change” system. By wrapping your tool’s actions in FToolCommandChange objects, you can eliminate the difficulty of implementing robust Undo and Redo support for complex geometry or world modifications.
Implement Input Behaviors
Instead of checking raw input, use UInputBehavior classes (like USingleClickInputBehavior or UMouseHoverBehavior). This allows the framework to manage input priority and helps eliminate conflicts when multiple tools or editor systems are active at the same time.
Utilize the 5.5 Behavior API
If you are using the latest engine versions, take advantage of the new function-based behavior API. It allows you to compose multiple input behaviors dynamically, which helps you eliminate the need to create massive, deeply nested class hierarchies for complex tools.
Register Tools via ToolBuilders
Every tool requires a UInteractiveToolBuilder. This class acts as a factory that determines if a tool can start based on the current selection. Proper builder logic helps you eliminate runtime errors by ensuring a tool only launches when valid target actors are selected.
Separate Preview Logic from Final Commitment
Always implement a “Preview” state using components like UMeshOpPreviewWithBackgroundCompute. This allows users to see changes in real-time without modifying the actual world actors until they hit “Accept,” helping to eliminate destructive workflow accidents.
Use Gizmos for Intuitive Interaction
The ITF provides a UGizmoManager. Rather than having users type coordinates, attach 3D transformation gizmos to your tool’s active points. This provides a professional “Modeling Mode” feel and helps eliminate user frustration when performing precision alignments.