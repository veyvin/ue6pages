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

efficient rendering and management of massive amounts of instanced geometry, such as trees, grass, rocks, and bushes.

Description

The Foliage module utilizes Hardware Instancing to render thousands of meshes with minimal draw call overhead. It provides the “Foliage Mode” editor interface and the underlying AInstancedFoliageActor which clusters instances into manageable groups. This system is essential for world-building, allowing designers to paint vegetation over landscapes or static meshes. In Unreal Engine 5, the module has been deeply integrated with Nanite and World Partition, enabling cinematic-quality forests and vast open worlds that would otherwise be impossible to render using traditional static mesh actors.

Practical Usage Tips and Best Practices
1. Enable Nanite “Preserve Area”

When using the Foliage module with Nanite-enabled meshes (like grass or small leaves), always enable Preserve Area in the Static Mesh Editor. This prevents the geometry from “thinning out” or disappearing at a distance. As Nanite simplifies the mesh, it will scale up the remaining triangles to maintain the visual density and silhouette of the foliage.

2. Use Geometry Instead of Masked Cards

With the move to Nanite foliage, the traditional “alpha-masked card” approach is often less performant than high-poly geometry. Masked materials cause heavy overdraw and expensive pixel shader costs. A best practice is to use fully modeled geometry for leaves and blades of grass; Nanite handles the high triangle count much more efficiently than the GPU handles thousands of overlapping transparent layers.

3. Control Density via Scalability

The Foliage module supports the foliage.DensityScale console variable. In your Foliage Type assets, ensure Enable Density Scaling is checked. This allows you to dynamically reduce the number of instances on lower-end hardware, providing an easy path for the elimination of performance bottlenecks on mobile or older consoles without redesigning the level.

4. Batch Edit via Property Matrix

When managing dozens of different foliage types, use the Property Matrix (select assets > Right Click > Asset Actions > Bulk Edit via Property Matrix). This is the most efficient way to synchronize Cull Distances, collision settings, and shadow casting behaviors across your entire library, ensuring consistency in your world’s optimization.

5. Optimize World Position Offset (WPO)

WPO is commonly used for wind animation, but it can be expensive when applied to thousands of instances. In the Foliage Type settings, use the WPO Disable Distance to stop wind animations on distant foliage. This leads to the elimination of unnecessary vertex shader calculations for objects that are too small on-screen for the player to notice their movement.

6. Use the Foliage Grid Size for World Partition

In World Partition maps, foliage is managed in a specialized grid. If your level has extremely dense grass, consider decreasing the Instanced Foliage Grid Size in the Project Settings. Smaller grid cells allow World Partition to load and unload foliage more granularly, which helps in the elimination of memory hitches during player movement.

7. Minimize Collision on Small Foliage

For small plants, pebbles, and grass, always set the Collision Preset to NoCollision in the Foliage Type asset. Calculating collision for thousands of tiny instances significantly degrades CPU performance and can interfere with character movement. Reserve collision only for large “blocker” assets like trees and large boulders.

8. Leverage Virtual Shadow Maps (VSM)

Unreal Engine 5’s VSM system is designed to work with foliage to provide high-resolution shadows for every leaf. However, to maintain performance, ensure that “Evaluate World Position Offset” is only enabled for shadows on hero assets. For background forest fillers, disabling this setting will provide a significant boost by the elimination of shadow map redraws every frame.