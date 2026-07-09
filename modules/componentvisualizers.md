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

g custom viewport gizmos and interactive visual aids for Actor Components. While standard components like the USphereComponent have built-in wireframes, this module allows developers to write custom drawing logic (lines, shapes, text) and interactive handles (click-and-drag logic) for their own proprietary components.

It is primarily used to surface “invisible” data—such as AI patrol paths, area-of-effect radii, or complex spline data—directly in the Level Editor viewport without adding overhead to the shipping game.

Practical Usage Tips and Best Practices
1. Register in an Editor-Only Module

Component visualizers are strictly editor features. You must implement the visualizer class in an Editor Module and register it in the StartupModule() function. Registering in a Runtime module will cause compilation errors in packaged builds.

C++
	// In your Editor Module's StartupModule

	if (GUnrealEd)

	{

	    TSharedPtr<FMyComponentVisualizer> Visualizer = MakeShareable(new FMyComponentVisualizer);

	    GUnrealEd->RegisterComponentVisualizer(UMyComponent::StaticClass()->GetFName(), Visualizer);

	    Visualizer->OnRegister();

	}

	```

	 

	#### 2. Leverage the Primitive Draw Interface (PDI)

	Inside the `DrawVisualization` override, use the `FPrimitiveDrawInterface* PDI` to draw 3D shapes. The PDI is highly optimized for editor viewport rendering. You can draw lines, points, spheres, and even meshes. Use `SDPG_Foreground` if you want your gizmo to always draw "on top" of other world geometry.

	 

	#### 3. Implement Hit Proxies for Interaction

	If you want your visualizer to be interactive (e.g., clicking a point to move it), you must use **Hit Proxies**. When drawing in the PDI, wrap your draw calls with `PDI->SetHitProxy(new HMyHitProxy(Component))`. This allows the engine to identify which specific part of your visualizer the user clicked on.

	 

	#### 4. Handle Input with `HandleInputDelta`

	To make your visualizers "draggable," override `HandleInputDelta`. This function provides the mouse movement delta and allows you to update the underlying component's properties (like a radius or a vector offset) in real-time as the user drags a handle in the viewport.

	 

	#### 5. Use Canvas for 2D Information

	While the PDI is for 3D world-space drawing, you can override `DrawVisualizationHUD` to draw 2D text or icons onto the viewport's screen space. This is excellent for displaying numerical values (like "Detection Radius: 500m") that follow the component in the 3D view but remain readable as 2D text.

	 

	#### 6. Coordinate with `PostEditChangeProperty`

	Ensure your visualizer responds to property changes in the Details Panel. When a user types a new value, the visualizer should immediately redraw. In your Component's C++, use `PostEditChangeProperty` to call `MarkRenderStateDirty()`, which signals the editor to refresh the component's visual representation.

	 

	#### 7. Keep Visualization Logic Lightweight

	`DrawVisualization` is called every time the viewport renders. Avoid expensive calculations, complex loops, or memory allocations inside this function. Pre-calculate as much as possible on the Component itself so the visualizer only has to perform simple "read and draw" operations.

	 

	#### 8. Differentiate from "Visualization Components"

	Do not confuse **Component Visualizers** (C++ logic) with **Visualization Components** (Editor-only `USceneComponents`). 

	*   **Visualizers:** Best for complex, interactive, or purely mathematical data (e.g., Splines).

	*   **Visualization Components:** Best for simple meshes or billboards that already exist as component types (e.g., an arrow or a preview mesh).

	 

	---

	 

	### Performance & Best Practices

	*   **Include Management:** Always wrap your visualizer code in `#if WITH_EDITOR` blocks if any part of it must reside in a header shared with a runtime module.

	*   **Undo/Redo:** When modifying component properties via `HandleInputDelta`, wrap the changes in `GEditor->BeginTransaction()` and `EndTransaction()` to ensure the user can "Undo" their viewport movements.

	*   **Selection Check:** By default, visualizers only draw when the component (or its parent actor) is selected. Use this to your advantage to keep the viewport clean of "visual noise" during normal level editing.
Copy code
2. Leverage the Primitive Draw Interface (PDI)

Inside the DrawVisualization override, use the FPrimitiveDrawInterface* PDI to draw 3D shapes. The PDI is highly optimized for editor viewport rendering. You can draw lines, points, spheres, and even meshes. Use SDPG_Foreground if you want your gizmo to always draw “on top” of other world geometry.

3. Implement Hit Proxies for Interaction

If you want your visualizer to be interactive (e.g., clicking a point to move it), you must use Hit Proxies. When drawing in the PDI, wrap your draw calls with PDI->SetHitProxy(new HMyHitProxy(Component)). This allows the engine to identify which specific part of your visualizer the user clicked on.

4. Handle Input with HandleInputDelta

To make your visualizers “draggable,” override HandleInputDelta. This function provides the mouse movement delta and allows you to update the underlying component’s properties (like a radius or a vector offset) in real-time as the user drags a handle in the viewport.

5. Use Canvas for 2D Information

While the PDI is for 3D world-space drawing, you can override DrawVisualizationHUD to draw 2D text or icons onto the viewport’s screen space. This is excellent for displaying numerical values (like “Detection Radius: 500m”) that follow the component in the 3D view but remain readable as 2D text.

6. Coordinate with PostEditChangeProperty

Ensure your visualizer responds to property changes in the Details Panel. When a user types a new value, the visualizer should immediately redraw. In your Component’s C++, use PostEditChangeProperty to call MarkRenderStateDirty(), which signals the editor to refresh the component’s visual representation.

7. Keep Visualization Logic Lightweight

DrawVisualization is called every time the viewport renders. Avoid expensive calculations, complex loops, or memory allocations inside this function. Pre-calculate as much as possible on the Component itself so the visualizer only has to perform simple “read and draw” operations.

8. Differentiate from “Visualization Components”

Do not confuse Component Visualizers (C++ logic) with Visualization Components (Editor-only USceneComponents).

Visualizers: Best for complex, interactive, or purely mathematical data (e.g., Splines).
Visualization Components: Best for simple meshes or billboards that already exist as component types (e.g., an arrow or a preview mesh).
Performance & Best Practices
Include Management: Always wrap your visualizer code in #if WITH_EDITOR blocks if any part of it must reside in a header shared with a runtime module.
Undo/Redo: When modifying component properties via HandleInputDelta, wrap the changes in GEditor->BeginTransaction() and EndTransaction() to ensure the user can “Undo” their viewport movements.
Selection Check: By default, visualizers only draw when the component (or its parent actor) is selected. Use this to your advantage to keep the viewport clean of “visual noise” during normal level editing.