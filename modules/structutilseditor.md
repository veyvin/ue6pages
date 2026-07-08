---
layout: default
title: StructUtilsEditor
---

<!-- ai-generation-failed -->

<h1>StructUtilsEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/StructUtilsEditor/StructUtilsEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIGraph, AIModule, ApplicationCore, AssetTools, BlueprintGraph, ComponentVisualizers, Core, CoreUObject, DataHierarchyEditor, DetailCustomizations, Engine, GraphEditor, InputCore, KismetCompiler, KismetWidgets, PropertyEditor, RenderCore, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

StructUtils plugin, specifically focusing on the specialized UI and Details Panel logic for Instanced Structs (FInstancedStruct). It is responsible for the property customization that allows you to select, create, and edit different struct types within a single variable in the Unreal Editor.

This module is essential for creating data-driven tools that require the flexibility of a UObject but with the performance benefits of a UStruct. It helps you eliminate the memory and performance overhead of “EditInlineNew” objects by allowing you to swap out data structures programmatically within a single property.

Practical Usage Tips and Best Practices
Define Base Structs for Better Filtering
When using an FInstancedStruct property in C++, always use the BaseStruct metadata specifier (e.g., meta = (BaseStruct = "/Script/MyModule.MyBaseStruct")). This restricts the editor dropdown to only show children of that base, helping you eliminate the risk of users selecting irrelevant or incompatible data structures.
Use ‘ExcludeBaseStruct’ to Enforce Implementation
If your base struct is intended to be abstract (containing only logic or shared properties), use the ExcludeBaseStruct metadata. This forces designers to pick a specific child implementation, which helps you eliminate runtime errors caused by empty or generic base data.
Enable ‘ShowTreeView’ for Deep Hierarchies
For projects with dozens of child structs, add the ShowTreeView metadata to your FInstancedStruct. This changes the selection dropdown from a flat list to a searchable tree based on the struct hierarchy, helping you eliminate the time spent scrolling through long menus.
Leverage Blueprint Support for Designers
In UE 5.2+, FInstancedStruct has native Blueprint support. You can use the “Make Instanced Struct” and “Break Instanced Struct” nodes to handle data dynamically in Blueprints. This allows you to eliminate hard-coded logic branches by passing around polymorphic data containers.
Implement Custom Validation via ‘PostEditChangeProperty’
Because FInstancedStruct can hold any data type, use the PostEditChangeProperty function in your Actor or Data Asset to validate the current struct instance. This allows you to eliminate invalid data states immediately after a user makes a selection in the Details Panel.
Utilize ‘SInstancedStructPicker’ in Custom Widgets
If you are building a custom Editor Utility Widget or Slate tool, you can use the SInstancedStructPicker widget provided by this module. This gives your custom tools the same robust selection UI as the Details Panel, helping you eliminate UI inconsistency across your pipeline.
Optimize Memory with Struct Elimination
When a user clears an instanced struct (setting it to “None”), the module handles the elimination of the underlying memory for that specific instance. Use this to your advantage in large Data Tables or Arrays to keep your memory footprint lean by only populating the structs you actually need for a specific level.
Prefer Instanced Structs over ‘Instanced’ UObjects
Whenever possible, use FInstancedStruct instead of UObject* with the Instanced specifier for data-only containers. This helps you eliminate the overhead of the Reflection System’s garbage collection and reduces the number of UObjects the engine has to track, leading to faster save/load times.