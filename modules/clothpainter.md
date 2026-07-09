---
layout: default
title: ClothPainter
---

<!-- ai-generation-failed -->

<h1>ClothPainter</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ClothPainter/ClothPainter.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AdvancedPreviewScene, AssetRegistry, AssetTools, ClassViewer, ClothingSystemEditorInterface, ClothingSystemRuntimeCommon, ClothingSystemRuntimeInterface, ClothingSystemRuntimeNv, Core, CoreUObject, DeveloperToolSettings, EditorFramework, EditorWidgets, Engine, InputCore, Kismet, MainFrame, MeshPaint, PropertyEditor, SkeletalMeshEditor, Slate, SlateCore, ToolMenus, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Engine that provides the vertex-painting interface for the clothing system. While the broader clothing modules handle the physics and asset management, ClothPainter specifically manages the “Paint Mode” inside the Skeletal Mesh Editor.

It is used by technical artists to visually define simulation parameters—such as how far a cape can move or how stiff a sleeve is—by painting values directly onto the mesh’s vertices.

Practical Usage Tips and Best Practices
1. Use the “H” Key for Instant Preview

When you are in the middle of a painting session, it can be hard to see the underlying mesh or the simulation results. Hold the H keyboard shortcut to quickly toggle the preview of your cloth simulation. This allows you to verify if your current weights have “eliminated” clipping or if the movement is too restricted without leaving the tool.

2. Toggle Brush Modes with “Q” and “A”

Efficiency in the Cloth Painter comes from mastering hotkeys. Use Q to switch to the Smooth brush and A to return to the Paint brush. Smoothing is essential for preventing “stretching” artifacts that occur when there is a sharp jump in values between two adjacent vertices.

3. Leverage the Gradient Tool for Long Garments

For assets like long coats or banners, avoid manual brushing. The Gradient Tool is superior for these tasks. Click to set a “Start” value (Green dot) and Ctrl+Click to set an “End” value (Red dot), then press Enter. This ensures a mathematically perfect transition of Max Distance, preventing the “jittering” that often results from uneven manual painting.

4. Hide Triangles to Reach Inner Layers

If you are working on multi-layered clothing (like a jacket over a shirt), use the Hide Triangles brush mode. This allows you to temporarily “eliminate” the visibility of the outer mesh layers so you can accurately paint the weights on the inner geometry that would otherwise be occluded.

5. Paint on the Render Mesh (UE 5.4+)

Modern versions of the engine allow you to paint weight maps directly on the high-resolution Render Mesh. In the paint tool properties, you can toggle between the Sim Mesh and Render Mesh. Using the Render Mesh for painting is a best practice when using the Proxy Deformer, as it provides much higher precision for complex folding patterns.

6. Use “Flood” for Base Values

Instead of painting a whole mesh by hand, use the Fill tool or the Flood button to set a baseline value for the entire section. For example, flood the entire cloth with a small Max Distance value (like 5.0) to “eliminate” static rigidity, then manually paint the areas that need higher mobility.

7. Adjust Brush Strength and Size with Hotkeys

Maintain your flow by using S and D to adjust the Brush Size and W and E to adjust the Paint Value/Strength. This allows you to quickly transition from painting large, free-moving areas to fine-tuning the “locked” vertices near the seams where the cloth attaches to the character.

8. Verify with the “White/Red” Color Map

By default, the painter uses a Black/White mask. You can toggle the Display Color Map in the tool settings to use a White/Red visualization. This is often easier to read in bright lighting conditions and helps you identify “rogue” vertices that might have been missed, which could otherwise cause the cloth to snag or stretch unnaturally.

Performance & Best Practices
Vertex Density: Remember that the painter only affects vertices. If your simulation mesh is too low-poly, your masks will be chunky. Use a dedicated “Simulation Proxy” mesh for the best balance of detail and performance.
Mask Types: Don’t just paint “Max Distance.” Use the painter to define Backstop Distance and Backstop Radius to “eliminate” the cloth’s ability to clip into the character’s body capsules.
Save Often: The Cloth Painter generates data that is stored within the Clothing Asset. Ensure you save the Skeletal Mesh after a painting session to commit these changes to the asset.