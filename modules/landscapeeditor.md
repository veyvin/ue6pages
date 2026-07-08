---
layout: default
title: LandscapeEditor
---

<!-- ai-generation-failed -->

<h1>LandscapeEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/LandscapeEditor/LandscapeEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, CQTest, Core, CoreUObject, DeveloperSettings, DeveloperToolSettings, DirectoryWatcher, Documentation, EditorFramework, EditorInteractiveToolsFramework, EditorWidgets, Engine, Foliage, ImageCore, ImageWrapper, InputCore, Json, Landscape, LandscapeEditorUtilities, NavigationSystem, PlacementMode, PropertyEditor, RHI, RenderCore, Slate, SlateCore, SourceControl, ToolMenus, ToolWidgets, UnrealEd, VirtualTexturingEditor</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nd UI for creating, sculpting, and painting massive terrain environments. It is the backend that powers the “Landscape Mode” in the Unreal Engine viewport.

What it is and What it’s used for

Located in Engine/Source/Editor/LandscapeEditor, this module manages the interaction between the user’s brush strokes and the underlying Landscape Actor and its components. It handles the specialized data structures needed to store heightmaps and weightmaps (layer data) for terrains that can span several kilometers.

Primary uses include:

Terrain Sculpting: Providing tools for the elevation, smoothing, and flattening of terrain surfaces.
Layer Painting: Managing the blending of materials (e.g., grass, rock, mud) through Landscape Layer info assets.
Component Management: Allowing users to add, delete, or resize sections of the landscape grid to optimize performance.
Spline Integration: Managing Landscape Splines for the automated deformation of terrain to create roads and paths.
Practical Usage Tips and Best Practices
1. Leverage Non-Destructive Layers

One of the most powerful features managed by this module is Landscape Layers. Always enable “Edit Layers” when creating a new landscape. This allows you to sculpt mountains on one layer and erosion on another. This non-destructive workflow is a best practice for the elimination of the fear of making permanent mistakes during the design phase.

2. Optimize Component Size for Performance

The module divides landscapes into “Components.” Each component is a draw call. For large worlds, use larger component sizes (e.g., 63x63 or 127x127 quads) to keep the total component count low. This is a primary strategy for the elimination of CPU bottlenecks on the render thread.

3. Use Landscape Blueprint Brushes

Beyond manual sculpting, the LandscapeEditor supports Blueprint Brushes. These allow you to use shapes (like a Box or Circle) or even landmass plugins to procedurally shape the terrain. Using these brushes allows for the elimination of tedious manual sculpting for repetitive features like riverbeds or flat building pads.

4. Manage Layer Info Assets Carefully

Every material layer you paint needs a “Layer Info” asset (Weight-Blended or Non-Weight-Blended). Keep these organized in a dedicated folder. Deleting or losing these assets will lead to the elimination of your painted data, as they hold the actual mask information for the terrain.

5. Prevent Texture Tiling in Materials

When painting large areas, textures often look repetitive. In your Landscape Material, use the LandscapeLayerCoords node combined with noise or “Texture Bombing” logic. This ensures the elimination of obvious tiling patterns, which is essential for visual realism in expansive outdoor environments.

6. Utilize the Erosion Tool for Realism

The Erosion and Hydro-Erosion tools in the Sculpt menu simulate soil movement over time. Use these sparingly after primary sculpting to add natural-looking gullies and sediment flows. This helps in the elimination of the “synthetic” or “blobby” look often associated with digital terrain.

7. Set Collision Thickness for Fast Projectiles

For high-speed games, projectiles can sometimes phase through the landscape. In the Landscape Actor’s details, you can adjust the “Collision Thickness.” Increasing this value helps in the elimination of “collision tunneling” where fast-moving objects miss the thin collision surface of the heightmap.

8. Strategic Elimination of Unseen Components

If your world has a large ocean or a mountain range that blocks the view of the terrain behind it, use the Manage Mode to delete those hidden components. This reduces the memory footprint and the number of triangles being processed, leading to the elimination of wasted GPU resources.