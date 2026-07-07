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

e Chaos Physics engine responsible for the “Broadphase” layer of physics simulation. Its primary purpose is to manage Spatial Acceleration Structures (such as Grids, AABB Trees, and Hash Maps) that organize physics particles in 3D space.

Instead of performing expensive collision checks between every single object in a scene (which would be \(O(n^2)\)), this module partitions the world so the engine only checks objects that are near each other. It is also the underlying system that handles Scene Queries (Line Traces, Sweeps, and Overlaps).

Practical Usage Tips and Best Practices
1. Tune the Broadphase Type for Your World

Chaos allows you to choose between different acceleration structures (Bounding Volume Hierarchies/BVH vs. Grids).

Best Practice: For large-scale open worlds with many static objects, a BVH (AABB Tree) is generally superior. For high-density simulations with many moving parts (like massive destruction), a Spatial Hash or Grid may perform better. You can toggle these in the Physics Project Settings.
2. Optimize Grid Cell Size

If you are using a Grid-based partition, the “Cell Size” is the most critical performance variable.

Tip: If cells are too large, the engine performs too many “Narrowphase” checks per cell. If they are too small, memory usage and management overhead spike. Aim for a cell size that roughly fits your average “active” gameplay actor to eliminate unnecessary collision overhead.
3. Use the Chaos Visual Debugger (CVD)

The Chaos Visual Debugger is the best way to see the spatial partition in action.

Action: Open CVD (Tools > Chaos Visual Debugger) to visualize “Query Visits.” If a simple line trace is “visiting” hundreds of nodes in the spatial partition, it indicates your broadphase is unoptimized. Use this data to eliminate density bottlenecks in your level.
4. Implement Physics Proxies for Complex Actors

Large, complex meshes with thousands of collision primitives can bloat the spatial partition.

Best Practice: Replace complex collision on background props with simple “Physics Proxies” (simplified boxes or spheres). This keeps the spatial acceleration structure lean and helps eliminate slow query times when tracing through cluttered environments.
5. Leverage Async Scene Queries (C++ Only)

Performing scene queries (Raycasts) can often hitch the Game Thread if the spatial partition is dense.

Tip: Use World->AsyncLineTraceByChannel. This offloads the traversal of the spatial partition to worker threads. While the result is delayed by one frame, it can eliminate significant Game Thread performance bottlenecks.
6. Minimize “Dirty” Partition Updates

When a physics object moves, it must update its position within the spatial partition.

Best Practice: Disable “Simulate Physics” or “Generate Overlap Events” on objects that don’t absolutely need them. Every moving physics object forces the spatial partition to “re-bucket” the item, and eliminating unnecessary updates saves significant CPU cycles on the physics thread.
7. Use CVARs to Debug the Hierarchy

You can visualize the spatial partition nodes directly in the viewport using console variables.

Command: Use P.Chaos.DrawHierarchy.Enable 1 and P.Chaos.DrawHierarchy.Cells 1. This allows you to see exactly how Chaos is carving up your world, helping you eliminate areas where the spatial partition is becoming too deep or fragmented.
8. Scale Scopes for World Partition

When using World Partition, the physics scene is loaded and unloaded in “streaming cells.”

Tip: Be mindful of the “Loading Radius.” If your physics loading radius is significantly larger than your visual radius, you may be populating the ChaosSpatialPartitions with thousands of off-screen objects, which can eliminate the performance gains of streaming. Match these radii closely for optimal performance.