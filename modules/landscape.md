---
layout: default
title: Landscape
---

<!-- ai-generation-failed -->

<h1>Landscape</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Landscape/Landscape.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ActionableMessage, ApplicationCore, Core, CoreUObject, DeveloperSettings, EditorFramework, Engine, Foliage, GeometryCore, ImageCore, MaterialUtilities, MathCore, MeshBuilderCommon, MeshDescription, MeshUtilities, MeshUtilitiesCommon, RHI, RenderCore, Renderer, Slate, SlateCore, StaticMeshDescription, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

creating, sculpting, and rendering expansive outdoor terrains. Unlike standard static meshes, the Landscape system uses a highly optimized, tile-based architecture that utilizes Heightmaps to store elevation data and Weightmaps for layered texture painting. It is designed to handle massive world scales through a dynamic Level of Detail (LOD) system, allowing for the elimination of the performance bottlenecks typically associated with high-poly environment geometry.

Practical Usage Tips & Best Practices
1. Enable Nanite for Modern Hardware

In UE 5.x, you can enable Nanite on your Landscape actors to drastically improve rendering efficiency and shadow performance.

Best Practice: Check Enable Nanite in the Landscape details panel and click Build Data. This allows for the elimination of traditional LOD “popping” artifacts and provides pixel-perfect geometric detail even at extreme distances.
2. Utilize Runtime Virtual Texturing (RVT)

Large landscapes with many layers can become extremely expensive to render due to high shader complexity.

Tip: Implement Runtime Virtual Texturing to cache your landscape’s complex material stack into a single texture at runtime. This results in the elimination of frame rate drops caused by high “texture sample” counts, particularly when blending multiple layers like grass, mud, and rock.
3. Use Non-Weight-Blended Layers for Holes

Creating caves or tunnels through a landscape requires transparency, which can be expensive if not handled correctly.

Best Practice: Use a Landscape Visibility Mask node within your material and set the material’s blend mode to Masked. This allows you to paint “holes” into the terrain, leading to the elimination of collision and visibility in specific areas for seamless cave entrances.
4. Optimize Component Size and Section Count

The way a landscape is divided into components affects both culling and the number of draw calls.

Tip: For large open worlds, prefer larger component sizes (e.g., 2x2 sections per component) to keep the total component count manageable. Proper sizing facilitates the elimination of CPU overhead in the rendering thread by reducing the number of individual objects the engine must track.
5. Leverage Landscape Layers (Non-Destructive)

Landscape Layers allow you to separate different sculpting or painting passes, similar to layers in Photoshop.

Best Practice: Keep your base topography on one layer and specific features (like a road or a hill) on separate Edit Layers. This ensures the elimination of “destructive” editing, allowing you to tweak or remove specific features without ruining the entire terrain’s base shape.
6. Minimize “Weight-Blended” Layers Per Component

The engine compiles a unique shader for every landscape component based on the number of layers painted on it.

Tip: Try to limit each individual square component to 3 or 4 painted layers. Reducing layer density per component results in the elimination of “shader complexity” spikes and helps stay within the GPU’s texture sampler limit.
7. Implement Landscape Splines for Roads and Paths

Manually sculpting roads to follow a specific path is tedious and often results in jagged edges.

Best Practice: Use Landscape Splines to deform the terrain and apply mesh deformations simultaneously. This tool automates the “Flatten to Spline” process, leading to the elimination of manual sculpting errors and ensuring a perfectly smooth surface for vehicles or characters.
8. Proactive “Elimination” of Hidden Components

If your world includes large areas covered by water or static mesh mountains, the landscape underneath is still being processed.

Tip: Use the Delete tool in the Landscape Manage tab to remove components that will never be seen by the player. Removing these invisible blocks results in the elimination of unnecessary memory usage and improves overall occlusion culling performance.