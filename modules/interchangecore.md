---
layout: default
title: InterchangeCore
---

<!-- ai-generation-failed -->

<h1>InterchangeCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Interchange/Core/InterchangeCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, Json, JsonUtilities, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

f the Interchange Framework, Unreal Engine’s modern, extensible system for importing and exporting assets.

Description and Purpose

While the high-level Interchange system handles specific file formats (like FBX or glTF), InterchangeCore defines the base classes, interfaces, and the “node graph” logic that makes the framework format-agnostic. Its primary purpose is to manage the Interchange Base Node Graph, which acts as an intermediary representation of a file. It converts external data into generic nodes (like UInterchangeBaseNode) before specialized factories turn them into actual Unreal assets. This decoupled architecture allows developers to create custom import pipelines and eliminate the rigid, hard-coded logic associated with the legacy FBX importer.

Practical Usage Tips and Best Practices
Manipulate the Node Graph via Pipelines
The core of Interchange customization happens in the Pipeline. Use the UInterchangePipelineBase class to intercept nodes before they reach the factory. By modifying node attributes here, you can eliminate the need for manual post-import adjustments (e.g., automatically renaming meshes or adjusting scale).
Utilize the Results Container for Reporting
Always use the UInterchangeResultsContainer to log messages, warnings, or errors during the import process. This ensures that your feedback is surfaced correctly in the Interchange UI, helping you eliminate “silent failures” where an asset fails to import without explanation.
Implement Custom Translators with IInterchangeTranslator
If you need to support a proprietary file format, inherit from the core’s translator interfaces. The core handles the orchestration, while your translator simply fills the node graph. This modularity helps you eliminate the complexity of writing a full importer from scratch.
Filter Nodes to Optimize Large Imports
In large scenes, the node graph can become massive. Use core filtering functions to identify only specific node types (like UInterchangeMeshNode). Processing only the nodes you need helps you eliminate unnecessary CPU overhead and speeds up the import of complex architectural scenes.
Leverage Attribute Storage for Custom Metadata
Every node in the core can store custom attributes. Use this to pass metadata from your source file through to the final asset. This is a best practice to eliminate data loss during the transition from DCC tools (like Maya or Blender) to Unreal Engine.
Check Node Validity Before Factory Execution
Before a factory attempts to create an asset, use the core’s validation checks on the source nodes. Ensuring that a node has a valid “Unique ID” and “Display Name” is the best way to eliminate crashes or asset name collisions in the Content Browser.
Use the Asynchronous Framework for Runtime Imports
InterchangeCore is designed to be asynchronous. When using it at runtime (e.g., for modding tools), always call the import functions asynchronously. This helps you eliminate “frame hitches” or game freezes while the engine is parsing large external files.
Define Pipeline Stacks in Project Settings
The core relies on “Pipeline Stacks” to determine the order of operations. Organize your stacks in Project Settings > Interchange so that generic cleanup happens before specialized processing. This logical ordering helps you eliminate conflicting settings between different import stages.