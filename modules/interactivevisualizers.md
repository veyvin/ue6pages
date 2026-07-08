---
layout: default
title: InteractiveVisualizers
---

<!-- ai-generation-failed -->

<h1>InteractiveVisualizers</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/Experimental/InteractiveVisualizers/InteractiveVisualizers.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, EditorInteractiveToolsFramework, Engine, GeometryCore, InputCore, InteractiveToolsFramework, Slate, SlateCore, ToolWidgets, TypedElementFramework, ViewportPanelStyle</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

lements overlap in the viewport.

2. Use PDI for 3D Drawing

Inside the DrawVisualization override, use the Primitive Draw Interface (PDI) to render shapes like lines, spheres, and boxes. Since PDI draws are not actual scene components, they lead to the elimination of performance overhead during editor navigation, as they do not require full transform updates or lighting calculations.

3. Project to Canvas for 2D Info

If you need to display text labels or distances next to your component, use the DrawVisualizationHUD function. This provides access to a Canvas, allowing you to project 3D coordinates into screen space. This practice assists in the elimination of clutter by keeping technical data as a flat overlay rather than 3D geometry.

4. Register in an Editor Module

Component Visualizers must be registered in the StartupModule of an Editor-only module. Link your visualizer class to a specific component type using GUnrealEd->RegisterComponentVisualizer(). Properly unregistering it during ShutdownModule is a best practice for the elimination of memory leaks and “hanging” references when closing the editor.

5. Leverage Proxy Selection States

When drawing, check if the component or a specific handle is selected using the visualizer’s selection state. You can change the color of lines or handles based on selection, which facilitates the elimination of user error by providing clear visual confirmation of which part of the component is currently active.

6. Handle Transactions for Undo/Redo

When a user moves a handle in your visualizer, you must wrap the logic in a GEditor->BeginTransaction() call and call Modify() on the component. This ensures that every interactive change is recorded, leading to the elimination of frustration when users need to undo complex spatial adjustments.

7. Keep Visuals “Editor-Only”

Always wrap your visualizer code and its references within #if WITH_EDITOR blocks. This ensures that the specialized drawing logic is excluded from the shipping build, aiding in the elimination of unnecessary code bloat and potential linker errors in your final game executable.

8. Use Custom Gizmos for Complex Logic

If your component requires more than simple point-dragging, you can integrate the Interactive Tools Framework alongside this module. Using dedicated gizmos for rotation or scaling within your visualizer leads to the elimination of clunky “value-typing” for complex transformations like local-space offsets.