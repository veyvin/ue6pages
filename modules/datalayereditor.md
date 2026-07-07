---
layout: default
title: DataLayerEditor
---

<!-- ai-generation-failed -->

<h1>DataLayerEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DataLayerEditor/DataLayerEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetTools, ContentBrowserData, Core, CoreUObject, DeveloperToolSettings, EditorFramework, EditorSubsystem, EditorWidgets, Engine, InputCore, PropertyEditor, SceneOutliner, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

I, and logic for managing Data Layers within World Partition levels. While Data Layers act as a runtime filter for loading and unloading world data, the DataLayerEditor module specifically handles the Data Layer Outliner, actor assignment workflows, and the conversion of legacy layers into the modern asset-based system.

It is primarily used by level designers and world builders to organize massive datasets and define which actors should be streamed in for specific gameplay scenarios or artistic variations.

Practical Usage Tips and Best Practices
1. Use the Data Layer Outliner for Batch Operations

To manage your world effectively, open the Data Layer Outliner via Window > World Partition > Data Layer Outliner. This tool allows you to select multiple actors in the viewport and drag them directly into a Data Layer. This ensures the elimination of the tedious process of assigning layers individually through the Details panel.

2. Differentiate Between Asset and Instance

Understand that a Data Layer Asset is a shared definition, while a Data Layer Instance is world-specific. Use this module to create instances that override default behaviors for a specific map. This design facilitates the elimination of redundant assets when you want the same “Forest” layer to be “Initially Active” in one level but “Unloaded” in another.

3. Leverage the DataLayerToAsset Commandlet

If you are upgrading an older project, use the commandlet logic provided by this module to convert legacy “Layers” into the new Data Layer system. Running this automated process ensures the elimination of manual re-assignment work for thousands of actors in converted World Partition maps.

4. Control Editor Visibility vs. Runtime State

In the Data Layer Editor, you can toggle the eye icon to hide actors in the viewport. Note that Editor Visibility is independent of the Initial Runtime State. Always verify that your “Hidden” editor layers are set to the correct runtime state (Unloaded, Loaded, or Activated) to ensure the elimination of “missing” content when you transition from Editor to PIE (Play In Editor).

5. Clean Up “Unassigned” Actors

Periodically check the “Unassigned” category in the Data Layer Editor. Actors not assigned to a Data Layer are always loaded with the base grid. Moving decorative or mission-specific props into Data Layers is a best practice for the elimination of unnecessary memory overhead in your persistent world.

6. Utilize Actor Coloration for Debugging

The Data Layer Editor supports an Actor Coloration mode. Enabling this will tint actors in the viewport based on their assigned Data Layer color. This is the fastest way to visually audit your level and ensures the elimination of errors where actors are accidentally placed in the wrong layer (e.g., a “Night” light placed in a “Day” layer).

7. Interface via UDataLayerEditorSubsystem

If you are building custom editor tools or Python scripts to automate world building, interface with the UDataLayerEditorSubsystem. This allows you to programmatically create layers or move actors between them, which is essential for the elimination of human error during large-scale environment assembly.

8. Parent Data Layers for Organization

The Data Layer Editor allows for hierarchical nesting. Use parent layers to group related sub-layers (e.g., a “Mission_01” parent containing “M1_Enemies” and “M1_Props”). Toggling the parent visibility or state will affect all children, leading to the elimination of “click fatigue” when managing complex world states.