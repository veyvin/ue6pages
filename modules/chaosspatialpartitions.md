---
layout: default
title: ChaosSpatialPartitions
---

<!-- ai-generation-failed -->

<h1>ChaosSpatialPartitions</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/ChaosSpatialPartitions/ChaosSpatialPartitions.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ChaosCore, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the Chaos Physics engine. It provides the spatial acceleration structures (such as Uniform Grids, Hash Grids, and BVH trees) used to organize physical objects in 3D space.

Its primary purpose is to “eliminate” the need for the physics solver to check every object against every other object. By partitioning the world into manageable chunks, the engine can rapidly identify which actors are near each other for collision detection and which ones are relevant for scene queries like raycasts or overlaps.

Practical Usage Tips and Best Practices
Select the Correct Partition Type for Your World
For large, open worlds with sparse objects, a Hash Grid or BVH is often superior. For dense, uniform distributions (like a field of destructible debris), a Uniform Grid can be faster. Use the project settings to tune this and eliminate unnecessary broad-phase overhead.
Optimize for Large World Coordinates (LWC)
ChaosSpatialPartitions is fully LWC-aware. When working on massive maps, ensure your spatial structures are configured with appropriate cell sizes. If cells are too small, the grid becomes memory-intensive; if too large, it fails to eliminate enough distant pairs, slowing down collision detection.
Utilize the Chaos Visual Debugger (CVD)
Open the Chaos Visual Debugger (Tools > Chaos Visual Debugger) to see the spatial partitions in real-time. This is the most effective way to identify “hotspots” where too many objects are crammed into a single partition cell, helping you eliminate performance spikes.
Adjust Collision Cull Distance
Use the p.Chaos.Solver.Collision.CullDistance console variable to define the range at which the spatial partition should stop considering pairs. Lowering this value can eliminate thousands of unnecessary checks in complex scenes without noticeably affecting simulation quality.
Manage Static vs. Dynamic Partitioning
Static geometry is stored in a stable acceleration structure, while dynamic objects require constant updates. To eliminate CPU “thrashing,” ensure that objects that do not move are explicitly set to Static mobility, as this allows the spatial partition to bake them into a cheaper, non-updating structure.
Fine-Tune Broad-Phase Expansion
The spatial partition “inflates” object bounds to account for velocity. If your objects move extremely fast, they may overlap too many cells. Use Continuous Collision Detection (CCD) for these specific objects to eliminate the need for massive bounds inflation, which keeps the spatial grid efficient.
Monitor Memory Overhead with stat Chaos
Spatial structures consume memory. Use the stat Chaos and stat ChaosCounters commands to monitor the memory footprint of your partitions. If memory usage is climbing, consider increasing the cell size of your grid to eliminate excessive memory allocation for empty space.
Leverage Async Physics Simulation
In UE 5.4+, you can run the physics simulation (including spatial partitioning) on its own thread. This helps eliminate Game Thread hitches caused by complex spatial queries, allowing the renderer and gameplay logic to run smoothly even during heavy physical interactions.