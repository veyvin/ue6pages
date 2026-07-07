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

ing and rendering expansive, high-detail outdoor terrains.

Description and Purpose

This module manages the ALandscape Actor and its constituent ULandscapeComponent units. It is designed to handle terrains that are orders of magnitude larger than traditional static meshes by using a sophisticated Level of Detail (LOD) system and tile-based rendering. Its primary purpose is to provide a memory-efficient way to sculpt mountains, valleys, and slopes while supporting advanced features like non-destructive Edit Layers, procedural foliage placement, and native integration with World Partition for massive open-world streaming.

Practical Usage Tips and Best Practices
Utilize Non-Destructive Edit Layers
Always enable “Edit Layers” when creating a new landscape. This allows you to separate different modifications—such as a base sculpt, a road path, and erosion details—into independent layers. This practice helps you eliminate the fear of making permanent mistakes, as you can hide or adjust individual layers at any time.
Optimize Component and Section Sizes
Choose your landscape resolution carefully based on the “Recommended Landscape Sizes” documentation (typically power-of-two minus one, like 505x505). Using the correct component size helps you eliminate performance bottlenecks in the vertex shader and ensures that the LOD transitions are smooth and efficient.
Avoid Overloading Texture Samples
Landscape materials are limited by the number of texture samplers available on the GPU. To eliminate the “grey grid” error caused by exceeding this limit, use Shared Wrap samplers in your Material Expressions and try to limit the number of unique layers painted on a single landscape component.
Leverage Landscape Grass for Procedural Detail
Instead of manually placing every blade of grass, use the Landscape Grass Type asset linked to your landscape material. This automatically spawns mesh instances based on your layer masks, which helps you eliminate hours of manual foliage placement while maintaining high performance through instancing.
Adjust LOD Distance Factor for Silhouette Areas
For components that make up a distinct mountain silhouette, lower the LOD Distance Factor. This forces those specific areas to stay at a higher resolution longer, helping you eliminate noticeable “popping” or morphing of the terrain’s outline as the player moves.
Use the Sculpt Retopologize Tool
If your landscape becomes stretched or distorted after extreme sculpting (like a vertical cliff), use the Retopologize brush. This tool redistributes the vertices more evenly across the surface to eliminate texture stretching and jagged collision artifacts.
Streamline with World Partition
For large worlds, the landscape module automatically subdivides into Landscape Proxies when using World Partition. This allows the engine to load and unload only the terrain tiles near the player, which is the best way to eliminate excessive memory usage and long loading times.
Clean Up Small Layer Traces
Landscape components compile unique shaders based on the layers painted on them. If a component only has a tiny, accidental speck of a “Snow” layer, it still incurs the cost of that layer’s textures. Using the Smooth or Flatten tool to remove these micro-traces helps you eliminate unnecessary material complexity.