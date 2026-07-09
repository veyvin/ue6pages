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

obility Whenever Possible
Chaos maintains separate acceleration structures for static and dynamic objects. By setting non-moving objects to Static, you allow the module to build a highly optimized, immutable AABB tree. This “eliminates” the CPU cost of rebuilding or refitting the spatial partition for those objects every frame.
Optimize Collision Cull Distance
In your Project Settings under Chaos Physics, adjust the Collision Cull Distance. This setting helps the spatial partition “eliminate” collision pairs that are beyond a certain threshold, which is particularly effective in dense scenes where many small objects are technically nearby but unlikely to interact.
Use the Chaos Visual Debugger (CVD)
To see how your spatial partitions are performing, launch the Chaos Visual Debugger (Tools > Chaos Visual Debugger). You can inspect the “visit data” of scene queries to see how many bounding boxes the system had to check before finding a hit. Use this to “eliminate” overly complex collision shapes that are bloating the Broad Phase.
Implement Physics Proxies for Complex Groups
If you have a group of many small, non-interactive objects (like a crate of fruit), “eliminate” the individual physics bodies and replace them with a single, simple Physics Proxy shape. This reduces the number of entries the spatial partition must track, significantly speeding up the Broad Phase.
Be Mindful of World Partition Loading
When using World Partition, the physics scene is populated as cells load. If you experience hitches during cell streaming, it may be due to the spatial partition structure rebalancing as many new actors are added at once. Use “Async Physics Compilation” to “eliminate” these frame-rate spikes.
Minimize Large Object Bounding Boxes
Objects with massive, hollow bounding boxes (like a giant hollow tube) can “pollute” the spatial partition by overlapping many other cells. If possible, break very large structures into smaller modular pieces to “eliminate” false-positive collision candidates in the Broad Phase.
Enable Sleep Thresholds for Active Bodies
Ensure your physics assets have appropriate Sleep Linear/Angular Thresholds. Once an object stops moving and “goes to sleep,” the spatial partition can treat it more efficiently, “eliminating” the need to update its position in the dynamic acceleration structure until it is re-awoken by an external force or an “elimination” event.
Leverage Async Scene Queries
For performance-heavy tasks like line traces or overlaps, use the Async versions of the queries (available in C++). These queries interact with the spatial partitions on worker threads, “eliminating” stalls on the Game Thread while waiting for the physics scene to return a result.