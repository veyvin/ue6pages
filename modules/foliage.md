---
layout: default
title: Foliage
---

<!-- ai-generation-failed -->

<h1>Foliage</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Foliage/Foliage.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, RHI, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

for the efficient rendering and management of massive amounts of similar meshes, such as trees, grass, and rocks.

Description and Purpose

This module provides the logic for Instanced Static Meshes (ISM) and Hierarchical Instanced Static Meshes (HISM) specifically tailored for environmental dressing. Instead of each tree being a separate Actor with its own draw call, the Foliage module batches them into clusters that are rendered in a single draw call per material. It includes the Foliage Edit Mode, which allows designers to “paint” thousands of instances onto landscapes or static meshes, and the Foliage Type asset, which defines the scaling, density, and placement rules for those instances.

Practical Usage Tips and Best Practices
Utilize Hierarchical ISMs (HISM) for LODs
The Foliage system uses HISMs to allow individual instances to transition through Levels of Detail (LODs) based on their distance from the camera. This is critical to eliminate the performance cost of rendering high-poly meshes in the distance while maintaining high visual quality up close.
Enable Nanite for High-Density Geometry
In UE 5.6, enabling Nanite on your foliage meshes is the most effective way to eliminate polycount bottlenecks. When using Nanite for foliage, ensure you enable “Preserve Area” in the Static Mesh settings; this prevents thin geometry (like leaves or grass blades) from disappearing or “thinning out” as they move further away.
Configure Culling Distances
Always set a Max Draw Distance within the Foliage Type asset. For small items like grass or pebbles, setting a aggressive cull distance will eliminate the GPU overhead of rendering tiny objects that are too far away for the player to see clearly.
Use “Density Scaling” for Scalability
In the Foliage Type settings, check the Enable Density Scaling box. This allows the engine to automatically reduce the number of instances based on the user’s “Foliage” scalability setting, helping you eliminate performance issues on lower-end hardware without manual optimization.
Optimize Collision Settings
By default, painted foliage may have collision enabled. For small plants and ground cover, set the Collision Preset to “NoCollision” within the Foliage Type. This will eliminate unnecessary CPU calculations for physics and traces, which is especially important in scenes with thousands of instances.
Paint on Specific Landscape Layers
You can restrict foliage placement to specific landscape layers (e.g., only paint grass on the “Grass” texture layer). This helps you eliminate manual cleanup work and ensures that trees don’t accidentally sprout on cliff faces or underwater areas.
Adjust World Partition Grid Size
When working in large open worlds, the foliage is managed by the World Partition system. If you notice hitches during streaming, you can adjust the Instanced Foliage Grid Size in the Project Settings. A well-tuned grid size helps eliminate loading stutters by better distributing the instance data across cells.
Leverage Procedural Content Generation (PCG)
While the foliage module handles the rendering, you can use the PCG Framework to drive the placement of foliage instances procedurally. This allows you to eliminate hours of manual painting by defining rules that automatically populate your world with trees and shrubbery based on the environment’s topology.