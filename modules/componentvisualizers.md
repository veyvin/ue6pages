---
layout: default
title: ComponentVisualizers
---

<!-- ai-generation-failed -->

<h1>ComponentVisualizers</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ComponentVisualizers/ComponentVisualizers.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIModule, Core, CoreUObject, EditorFramework, Engine, InputCore, LevelEditor, PropertyEditor, Slate, SlateCore, UnrealEd, ViewportInteraction</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

property settings in the Details panel.
Practical Usage Tips and Best Practices
1. Strictly Separate Editor and Runtime Modules

Component Visualizers must reside in an Editor module. The component they visualize should live in a Runtime module. This prevents your game’s shipping build from trying to link against editor-only drawing code, which would result in a compilation failure during packaging.

2. Register Visualizers in StartupModule

You must manually register your visualizer when your editor module loads. Use the GUnrealEd global pointer to link your custom class to your component:

C++
	if (GUnrealEd)

	{

	    TSharedPtr<FMyComponentVisualizer> Visualizer = MakeShareable(new FMyComponentVisualizer());

	    GUnrealEd->RegisterComponentVisualizer(UMyComponent::StaticClass()->GetFName(), Visualizer);

	    Visualizer->OnRegister();

	}

	```

	 

	#### 3. Leverage FPrimitiveDrawInterface (PDI) for 3D

	Inside the `DrawVisualization` override, use the `FPrimitiveDrawInterface* PDI` to draw 3D primitives. PDI provides efficient methods like `DrawLine`, `DrawWireSphere`, and `DrawWireBox`. These are much lighter than spawning actual "Debug Helper" actors and are automatically cleaned up every frame.

	 

	#### 4. Use Hit Proxies for Interaction

	To make your visualizer interactive (clickable), use **Hit Proxies**. In your `DrawVisualization` function, call `PDI->SetHitProxy(new HMyProxy(Component))` before drawing a shape. This allows the editor to identify which specific part of your visualization the user clicked on, enabling custom drag-and-drop behavior.

	 

	#### 5. Cache Data for Performance

	The `DrawVisualization` function is called every time the viewport updates. Avoid performing complex math or expensive actor lookups inside this function. Instead, calculate the necessary points or bounds inside the component itself (or a cached struct) and simply read that data during the draw call.

	 

	#### 6. Draw Text with FCanvas

	If you need to display labels or property values (like distance markers), use the `DrawVisualizationHUD` override. While PDI handles 3D space, `FCanvas` allows you to project 2D text and icons onto the screen at the component's location, ensuring labels remain legible regardless of camera zoom.

	 

	#### 7. Respect the "Selected" State

	A best practice is to check `bIsSelected` before drawing complex visualizations. To avoid viewport clutter, draw only essential wireframes when an actor is unselected, and reveal detailed data, handles, and text only when the designer actively selects the component.

	 

	#### 8. Use WITH_EDITOR Preprocessor Gates

	Even though the visualizer is in an editor module, ensure your component’s internal data used for visualization is wrapped in `#if WITH_EDITORONLY_DATA`. This ensures that any extra metadata or "Editor-Only" arrays you create for the visualizer to read are stripped out of the final packaged game.
Copy code
3. Leverage FPrimitiveDrawInterface (PDI) for 3D

Inside the DrawVisualization override, use FPrimitiveDrawInterface* PDI to draw 3D primitives. PDI provides efficient methods like DrawLine, DrawWireSphere, and DrawWireBox. These are much lighter than spawning actual “Debug Helper” actors and are cleared every frame.

4. Use Hit Proxies for Interaction

To make your visualizer interactive (clickable), use Hit Proxies. In your DrawVisualization function, call PDI->SetHitProxy(new HMyProxy(Component)) before drawing a shape. This allows the editor to identify which specific part of your visualization the user clicked on, enabling custom drag-and-drop behavior.

5. Cache Data for Performance

The DrawVisualization function is called every time the viewport updates. Avoid performing complex math or expensive actor lookups inside this function. Instead, calculate the necessary points inside the component itself (wrapped in WITH_EDITOR gates) and simply read that data during the draw call.

6. Draw Text with FCanvas

If you need to display labels (like distance markers), use the DrawVisualizationHUD override. While PDI handles 3D space, FCanvas allows you to project 2D text and icons onto the screen at the component’s location, ensuring labels remain legible regardless of camera zoom.

7. Respect the Selection State

A best practice is to check the selection state before drawing complex visualizations. To ensure the elimination of viewport clutter, draw only essential wireframes when an actor is unselected, and reveal detailed data, handles, and text only when the designer actively selects the component.

8. Use WITH_EDITOR Preprocessor Gates

Even though the visualizer is in an editor module, ensure your component’s internal data used for visualization is wrapped in #if WITH_EDITORONLY_DATA. This ensures that any extra metadata or arrays created for the visualizer to read are stripped out of the final packaged game.