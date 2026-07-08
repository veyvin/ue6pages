---
layout: default
title: ChaosSpatialPartitionsTests
---

<!-- ai-generation-failed -->

<h1>ChaosSpatialPartitionsTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/ChaosSpatialPartitionsTests/ChaosSpatialPartitionsTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ChaosCore, ChaosSpatialPartitions, ChaosTestHarness, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

arios.

2. Run Tests via the Automation Scheduler

You can access these tests in the Session Frontend under the Physics > Chaos > Spatial category. Running these regularly during development ensures the elimination of “ghost” collisions or missed traces that can occur if the spatial acceleration structure becomes corrupted or unoptimized.

3. Stress-Test Scene Query Accuracy

The module includes tests for “Point Queries” and “Raycasts” against thousands of moving particles. If your gameplay relies on precision traces (like high-speed projectiles), these tests verify that the spatial partition correctly updates as objects move, preventing the elimination of accuracy during high-velocity physics updates.

4. Validate Custom Chaos Particles

If you are implementing custom physics particles or low-level Chaos objects in C++, use the patterns found in this module’s source code (SpatialAccelerationTests.cpp) to write your own unit tests. This ensures your new objects are correctly inserted into the spatial acceleration structure.

5. Analyze Memory Overhead

Spatial partitions trade memory for speed. Use the benchmarks in this module to monitor the memory footprint of the AABB tree. For mobile or memory-constrained platforms, this is vital for the elimination of “Out of Memory” crashes caused by overly complex physics broadphase structures.

6. Debugging “False Negatives” in Traces

If a LineTrace fails to hit an object that clearly should have been hit, the issue often lies in the spatial partition failing to return that object as a candidate. Running the tests in this module can help confirm if a specific engine version has a bug in its AABB Tree refitting logic.

7. Profile Structure “Refitting” vs. “Rebuilding”

Chaos can either “refit” (adjust) or “rebuild” (start over) its spatial structures as actors move. This module contains tests that measure the cost of both. Use this data to tune your p.Chaos.Broadphase.Rebuild console variables, aiming for the elimination of frame-rate hitches during heavy movement.

8. Verify Determinism in Queries

For networked games using Async Physics, spatial partition consistency is key. These tests help verify that queries return identical results across multiple runs, which is essential for the elimination of desyncs between the server and clients in a multiplayer environment.