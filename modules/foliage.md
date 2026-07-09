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

ment and rendering of thousands of static meshes within a scene. It utilizes hardware instancing via the AInstancedFoliageActor and UFoliageType classes to draw vast amounts of vegetation—such as grass, trees, and rocks—with minimal draw call overhead. This module is essential for world-building, allowing artists to “paint” assets onto landscapes or static meshes while providing the engine with optimized culling and LOD (Level of Detail) data.

Practical Usage Tips & Best Practices
1. Enable Nanite for High-Density Foliage

In Unreal Engine 5.6 and 5.7, Nanite is highly optimized for foliage, even those with masked materials (leaves).

Best Practice: Enable Nanite on your foliage Static Meshes to allow for the elimination of traditional LOD management. Nanite handles millions of triangles with much better performance and memory efficiency than standard instanced static meshes, especially for dense forests.
2. Configure Cull Distances via Property Matrix

Small foliage items (like pebbles or tiny grass tufts) should not be rendered from a kilometer away.

Tip: Select multiple assets in the Foliage Mode list, right-click, and select Bulk Edit via Property Matrix. Set the Cull Distance (Min/Max) to ensure the elimination of invisible, distant objects that would otherwise waste GPU cycles.
3. Set a World Position Offset (WPO) Disable Distance

Wind animations are usually handled via WPO in the material. Calculating wind for thousands of distant trees is a major performance drain.

Best Practice: In the UFoliageType settings, set a WPO Disable Distance. This causes the engine to stop calculating vertex movement for distant instances, leading to the elimination of unnecessary CPU/GPU vertex shader instructions.
4. Use “Enable Density Scaling” for Scalability

Different hardware configurations (Low vs. Epic) require different foliage densities.

Tip: Check the Enable Density Scaling box in the Foliage Type settings. This allows the player’s scalability settings (foliage.DensityScale) to automatically adjust the number of instances rendered, facilitating the elimination of frame rate drops on lower-end machines.
5. Adjust Instanced Foliage Grid Size for World Partition

When using World Partition, foliage is managed in a grid. If the grid is too large, too much foliage is loaded at once; if too small, the engine spends too much time loading/unloading cells.

Best Practice: For large open worlds, use the World Partition Foliage Builder commandlet to tune your InstancedFoliageGridSize. Finding the “sweet spot” ensures the elimination of hitching during world streaming as the player moves.
6. Shadow Optimization with Virtual Shadow Maps (VSM)

Foliage often creates “shadow acne” or high shadow depth complexity.

Tip: If using VSM, utilize the Contact Shadows setting in your Post Process Volume or Light settings for small foliage. This allows for the elimination of heavy high-resolution shadow maps for tiny blades of grass while maintaining visual depth.
7. Prefer Procedural Content Generation (PCG) for Scale

While the Foliage module is great for hand-painting, manual placement is inefficient for massive maps.

Best Practice: Use the PCG Framework to spawn Foliage Types. This method allows for the elimination of tedious manual labor and ensures that vegetation is automatically updated if the underlying landscape shape or material changes.
8. Use Collision Only Where Necessary

Enabling “Block All” collision on every blade of grass will destroy physics performance.

Tip: Set collision to NoCollision for small ground cover. For trees, use a simplified capsule or box collision. This results in the elimination of thousands of unnecessary physics calculations per frame, keeping the simulation smooth.