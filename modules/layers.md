---
layout: default
title: Layers
---

<!-- ai-generation-failed -->

<h1>Layers</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/Layers/Layers.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, Engine, InputCore, SceneOutliner, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ality for the Layers Panel in the Unreal Engine interface. It allows developers and level designers to organize Actors into named groups, primarily serving as a “saved selection set” system.

Unlike the World Outliner, which is a hierarchical tree, the Layers module allows an Actor to exist in multiple layers simultaneously. Its primary purpose is to help manage complex scenes by providing quick ways to select, hide, or lock groups of related objects (e.g., “Environment,” “Lighting,” “Collision”). This organization helps eliminate the visual clutter and manual effort of managing thousands of individual actors during level construction.

Practical Usage Tips and Best Practices
Use as Overlapping Selection Sets
Because an actor can belong to many layers, use them to create overlapping categories. For example, a street lamp could be in both the “Lighting” layer and the “StreetProps” layer. This flexibility helps you eliminate the limitation of the World Outliner’s strict parent-child hierarchy.
Wrap Code in Editor Guards
The ILayers interface belongs to an editor module. If you are writing C++ to manage layers, always wrap your code in #if WITH_EDITOR blocks. This ensures you eliminate compilation errors when building your game for “Shipping,” as the Layers module is stripped out of non-editor builds.
Toggle Visibility to Boost Performance
Hide layers that are not currently relevant to your task (such as high-density foliage or heavy blueprints) using the “Eye” icon. This helps you eliminate viewport lag and maintains a high frame rate while you work on specific level sections.
Batch Add Actors for Efficiency
When writing editor scripts, use AddActorsToLayer instead of calling AddActorToLayer in a loop. Batching these requests allows the module to refresh the UI only once, which helps eliminate “hitching” or freezing in the editor when processing large groups of actors.
Distinguish from Data Layers
In UE 5.6+, do not confuse this module with Data Layers. The legacy Layers module is for Editor-only organization, while Data Layers are meant for Runtime streaming in World Partition. Use the Layers module specifically for workflow organization to eliminate unnecessary overhead in your runtime streaming logic.
Leverage ‘Select Actors in Layer’
Double-clicking a layer in the panel instantly selects all actors within it. This is the fastest way to perform bulk operations, such as moving an entire district or changing a material on all related props, helping you eliminate the time spent searching the Outliner.
Use Layers for Locking Content
While not a replacement for source control, you can use layers to hide and effectively “ignore” certain assets while working on others. This focus helps you eliminate accidental movement or deletion of finished environmental assets while you are iterating on gameplay triggers.
Manage via Build.cs
To interact with this module in your C++ tools, you must add "Layers" to your PrivateDependencyModuleNames in your Build.cs. This provides access to the ILayers interface, allowing you to programmatically automate level organization and eliminate manual sorting tasks for your artists.