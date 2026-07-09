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

within a level. Unlike “Level Folders,” which are strictly hierarchical, the Layers system allows an Actor to belong to multiple groups simultaneously.

It is primarily used by level designers to eliminate visual clutter and streamline complex scenes by toggling the visibility, selection, and lock status of specific groups of objects (e.g., all “Lighting,” all “Collision,” or all “Small Foliage”).

Practical Usage Tips and Best Practices
Access via the Layers Subsystem
In modern UE5 C++, use the ULayersSubsystem rather than the legacy ILayers interface. This eliminates manual module loading. Access it through the editor context:
C++
	    #include "Layers/LayersSubsystem.h"

	    // ...

	    if (GEditor)

	    {

	        ULayersSubsystem* LayersSubsystem = GEditor->GetEditorSubsystem<ULayersSubsystem>();

	        LayersSubsystem->AddActorToLayer(MyActor, TEXT("MyLayerName"));

	    }

	    ```

	 

	*   **Add Module Dependencies**  

	    Since this is an editor-specific module, add `"Layers"` to the `PrivateDependencyModuleNames` within an `#if WITH_EDITOR` block in your `Build.cs`. This "eliminates" linker errors when packaging your game, as the Layers system is not present in shipping builds.

	 

	*   **Leverage Multi-Layer Assignment**  

	    An Actor can exist in many layers. For example, a streetlamp can be in the "Lighting" layer and the "StreetProps" layer. Use this to "eliminate" the need for complex nested folder structures when you need to view actors from different functional perspectives.

	 

	*   **Use for Rapid Selection**  

	    Instead of clicking individual items, use the `ULayersSubsystem::SelectActorsInLayer` function. This "eliminates" manual searching in the World Outliner, allowing you to instantly grab all related Actors for batch property edits or transformations.

	 

	*   **Optimize Editor Performance via Visibility**  

	    Hiding layers "eliminates" the rendering overhead for those Actors in the Viewport. In massive levels, keep high-poly background meshes or complex particle systems in a separate layer and hide them while working on gameplay logic to maintain a high framerate in the editor.

	 

	*   **Automate via Editor Utility Blueprints**  

	    The Layers module is fully exposed to the `ULayersBlueprintLibrary`. Create an Editor Utility Widget to "eliminate" repetitive tasks, such as automatically assigning all "PointLights" with an intensity over 5000 to a "HighIntensityLights" layer.

	 

	*   **Distinguish from Data Layers**  

	    Do not confuse this module with **Data Layers** (used for World Partition streaming). Use the standard Layers module for editor organization and the `DataLayers` module for runtime loading/unloading. Using the correct module "eliminates" confusion during level streaming setup.

	 

	*   **Lock Layers to Prevent Accidental Edits**  

	    Once a group of decorative props is finalized, lock their layer. This "eliminates" the frustration of accidentally moving or deleting static background elements while trying to select dynamic gameplay actors in a crowded scene.
Copy code
Add Module Dependencies
Since this is an editor-specific module, add "Layers" to the PrivateDependencyModuleNames within an #if WITH_EDITOR block in your Build.cs. This eliminates linker errors when packaging your game, as the Layers system is not present in shipping builds.
Leverage Multi-Layer Assignment
An Actor can exist in many layers. For example, a streetlamp can be in the “Lighting” layer and the “StreetProps” layer. Use this to eliminate the need for complex nested folder structures when you need to view actors from different functional perspectives.
Use for Rapid Selection
Instead of clicking individual items, use the ULayersSubsystem::SelectActorsInLayer function. This eliminates manual searching in the World Outliner, allowing you to instantly grab all related Actors for batch property edits or transformations.
Optimize Editor Performance via Visibility
Hiding layers eliminates the rendering overhead for those Actors in the Viewport. In massive levels, keep high-poly background meshes or complex particle systems in a separate layer and hide them while working on gameplay logic to maintain a high framerate in the editor.
Automate via Editor Utility Blueprints
The Layers module is fully exposed to the ULayersBlueprintLibrary. Create an Editor Utility Widget to eliminate repetitive tasks, such as automatically assigning all “PointLights” with an intensity over 5000 to a “HighIntensityLights” layer.
Distinguish from Data Layers
Do not confuse this module with Data Layers (used for World Partition streaming). Use the standard Layers module for editor organization and the DataLayers module for runtime loading/unloading. Using the correct module eliminates confusion during level streaming setup.
Lock Layers to Prevent Accidental Edits
Once a group of decorative props is finalized, lock their layer. This eliminates the frustration of accidentally moving or deleting static background elements while trying to select dynamic gameplay actors in a crowded scene.