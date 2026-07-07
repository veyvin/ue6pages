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

physics programmers to ensure that spatial queries (like Raycasts, Sweeps, and Overlaps) return accurate results and that the underlying data structures—which organize physics objects in 3D space—are optimized for the elimination of unnecessary collision checks.

Practical Usage Tips and Best Practices
1. Use as a Template for Custom Physics Tests

If you are developing custom spatial algorithms or extending Chaos, use the source code in this module as a reference. It demonstrates how to set up a minimal Chaos environment without booting the entire Unreal Editor, which is the fastest way to verify low-level physics logic.

2. Run Tests via the Command Line

Since these are Low-Level Tests, they are compiled into a standalone executable. You can run them outside the editor for faster iteration. Navigate to your binaries folder and run: Path/To/LowLevelTests/ChaosSpatialPartitionsTests.exe This allows for the elimination of the heavy overhead associated with the Unreal Editor splash screen and UI.

3. Benchmark Spatial Query Performance

The module contains performance benchmarks. Use these to compare different spatial partitioning strategies. If you notice a regression in raycast speeds in your project, running these tests can help determine if the bottleneck is in the core Chaos structures or your specific implementation.

4. Validate Bounding Box Accuracy

A key focus of these tests is ensuring that bounding volumes are tight. Use the test logic to verify that your physics objects aren’t generating overly large AABBs, which would prevent the elimination of “false positive” collision checks and drag down performance in dense scenes.

5. Debug Spatial Leaks and Memory

Use the module in conjunction with memory profilers. Because these tests repeatedly create and destroy spatial partitions, they are excellent for identifying memory leaks within the Chaos partitioners that might lead to the eventual elimination of system resources during long play sessions.

6. Leverage Catch2 Selectors

You can run specific subsets of tests by using tags. For example, if you only want to test BVH structures, you can use: ChaosSpatialPartitionsTests.exe [BVH] This targeted approach saves time by focusing only on the relevant physics components you are currently modifying.

7. Profile with “Unreal Insights”

While the tests provide text-based output, you can run them with Trace enabled to view the results in Unreal Insights. This provides a visual timeline of how long specific spatial queries take, helping you identify hitches in the acceleration structure’s traversal logic.

8. Verify Multithreading Safety

Chaos is highly parallel. These tests are designed to catch race conditions where multiple threads might access the spatial partition simultaneously. If your project utilizes Async Physics, ensure these tests pass to confirm that the elimination of data races has been successfully maintained in the core engine.