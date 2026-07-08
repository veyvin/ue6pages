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

rovides the interface and logic for managing Data Layers within World Partition levels. While Data Layers exist at runtime to stream content in and out, this module specifically handles the “Data Layer Outliner,” the creation of Data Layer Assets, and the assignment of actors to these layers within the Unreal Editor.

It is a critical component for large-scale world building, allowing teams to organize massive levels into manageable, toggleable subsets of data for both organizational and gameplay purposes.

Practical Usage Tips and Best Practices
1. Use the Data Layer Outliner for Organization

Open the visual interface via Window > World Partition > Data Layer Outliner. This tool allows you to group actors logically (e.g., “Foliage,” “Base_Building,” “Mission_01”). Using this for visual organization leads to the elimination of a cluttered World Outliner and allows artists to focus only on relevant geometry.

2. Differentiate Between Asset and Instance

Data Layers in UE5 use a “Data Layer Asset” (stored in the Content Browser) and a “Data Layer Instance” (stored in the level). Use assets to share settings across different maps. This architecture facilitates the elimination of redundant setup when the same mission logic or environmental set needs to be reused across multiple levels.

3. Leverage Editor-Only Data Layers

When creating a layer, you can designate it as “Editor Only.” This is a best practice for utility actors like measurement rulers, high-poly reference meshes, or developer notes. These layers are stripped out during the cook process, ensuring the elimination of unnecessary memory overhead in the final game build.

4. Configure Initial Runtime States

In the Data Layer Editor, you can set the Initial Runtime State to Unloaded, Loaded, or Activated. For a dynamic mission system, set your mission layers to Unloaded by default. This ensures the elimination of performance drops at the start of the game by only loading data when the player triggers a specific event.

5. Assign Actors via Drag-and-Drop

The most efficient way to work in this module is by selecting actors in the viewport and dragging them directly onto a layer in the Data Layer Outliner. You can also right-click a layer to “Add Selected Actors.” This workflow is essential for the elimination of manual, one-by-one property editing in the Details panel.

6. Utilize External Data Layers (UE 5.5+)

If working on DLC or a Game Feature Plugin, use External Data Layers. These allow you to inject content into a base level without modifying the original map file. This practice assists in the elimination of file conflicts in source control when multiple teams are adding content to the same world location.

7. Debug with “Actor Coloration”

The Data Layer Editor includes an Actor Coloration mode. Enabling this will tint actors in the viewport based on which Data Layer they belong to. This visual feedback is vital for the elimination of “stray” actors that have been accidentally assigned to the wrong layer or left in the default persistent layer.

8. Parent Layers for Hierarchical Control

You can parent Data Layers to one another within the Outliner. Toggling the visibility or loading state of a parent layer will affect all children. This hierarchy is highly effective for the elimination of repetitive clicks when you need to hide a large complex of sub-layers (like all interior props within a specific building).