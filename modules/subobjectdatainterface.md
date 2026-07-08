---
layout: default
title: SubobjectDataInterface
---

<!-- ai-generation-failed -->

<h1>SubobjectDataInterface</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/SubobjectDataInterface/SubobjectDataInterface.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">BlueprintGraph, Core, CoreUObject, EditorFramework, Engine, GameProjectGeneration, TypedElementFramework, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ced in recent versions of Unreal Engine (UE 5.x) to provide a unified, standardized way to interact with an Actor’s subobjects—primarily Components. It serves as the backend abstraction layer for the Components Tab and the Subobject Editor, allowing developers to query, add, remove, and modify the hierarchy of components programmatically.

By using the USubobjectDataSubsystem and its associated interfaces, you can eliminate the need to manually manage complex UActorComponent arrays or use legacy, inconsistent methods for modifying an Actor’s internal structure in the editor.

Practical Usage Tips and Best Practices
Access via the Subobject Data Subsystem
To perform any operation, first obtain the USubobjectDataSubsystem from the Editor Subsystem collection. This system uses FSubobjectDataHandle to track objects, which helps you eliminate issues related to raw pointers or stale references when components are being re-instanced during a build.
Unify Blueprint and C++ Component Logic
This interface treats Native (C++) components and Blueprint-added components identically. Use it when building tools that need to scan an Actor’s entire makeup, helping you eliminate separate code paths for different component origins.
Perform Safe Component Addition
When adding components via a tool, use USubobjectDataSubsystem::AddNewSubobject. This function handles the necessary registration, attachment, and naming logic automatically. This helps you eliminate “ghost” components that appear in the hierarchy but don’t show up in the viewport or Details panel.
Support Undo/Redo with Transactions
The SubobjectDataInterface is built to work with the engine’s Transaction system. Before calling modification functions, wrap your logic in an FScopedTransaction. This ensures that the elimination or addition of subobjects can be reverted by the user, helping you eliminate the risk of accidental, permanent data loss in a level.
Respect the ‘Subobject Data’ Hierarchy
The subsystem organizes components into a tree of FSubobjectData. Always query the parent handle before performing an attachment. This structured approach helps you eliminate circular attachment errors and ensures the “Scene Root” is respected during transformations.
Validate Before Elimination
Before deleting a component, use the interface to check for dependencies. The subsystem can identify if other components are attached to the target. Checking these handles first helps you eliminate crashes caused by “dangling” child components that lose their parent transform.
Utilize for Custom Outliner Tools
If you are building a custom “Outliner” or “Component List” in a Slate window, use this module to populate your data. It provides the metadata needed for icons and display names, helping you eliminate UI inconsistency between your custom tools and the standard Unreal Editor.
Clean Up Handles on Tool Shutdown
When your editor tool or window is closed (the “elimination” of your interface), ensure you are not holding onto any FSubobjectDataHandle instances that might prevent an Actor from being properly garbage collected. Clearing these handles helps you eliminate memory leaks in long-running editor sessions.