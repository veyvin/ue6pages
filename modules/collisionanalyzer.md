---
layout: default
title: CollisionAnalyzer
---

<!-- ai-generation-failed -->

<h1>CollisionAnalyzer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/CollisionAnalyzer/CollisionAnalyzer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, Slate, SlateCore, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at provides a dedicated suite for recording and inspecting physics collision queries. While standard debug drawing (show COLLISION) shows static geometry, the Collision Analyzer captures dynamic “probes” such as LineTraces, Sweeps, and Overlap checks as they occur during a play session.

By using this tool, developers can see exactly where a trace started, where it ended, what it hit, and—most importantly—how many queries are being executed per frame. This is essential for the elimination of performance hitches and logic errors in complex gameplay systems.

How to Access

To open the tool, go to Tools > Debug > Collision Analyzer (or use the console command vr.CollisionAnalyzer).

Practical Usage Tips and Best Practices
1. Record to Identify Redundant Traces

Click the Record button during a PIE session to capture all collision queries. If you see hundreds of identical line traces appearing in the list, you have identified a redundant system. Consolidating these into a single cached result or a shared component will lead to the elimination of wasted CPU cycles.

2. Filter by Query Type and Status

The analyzer allows you to filter by “Touch” (hits) vs. “No Touch” (misses). If a specific gameplay feature like “Interact” isn’t working, filter for that trace to see if it’s hitting an unintended invisible collision volume, aiding in the elimination of “ghost” blockage bugs.

3. Analyze Trace Costs

The tool displays the “Cost” or time taken for each query. Sort the list by duration to find expensive traces. High-cost traces usually occur when a complex “per-poly” collision is being checked against a long sweep, which you should address for the elimination of frame-rate spikes.

4. Use “Jump to Frame” for Debugging

When you find a suspicious query in the list, you can jump the editor’s view to that specific frame and location. This allows you to see the exact state of the world when the trace occurred, which is vital for the elimination of logic bugs that only happen during high-speed movement.

5. Verify Collision Channel Accuracy

Each recorded entry shows the Collision Channel used (e.g., Visibility, Camera, or a Custom channel). Use this to ensure that your projectiles or line-of-sight checks are using the narrowest possible channel, assisting in the elimination of “false positive” hits against unintended object types.

6. Identify “Broadphase” Overload

If the analyzer shows a massive number of candidates for a single overlap check, it means your Spatial Partitioning is inefficient or your overlap volume is too large. Reducing the size of the volume or refining the collision object types will help in the elimination of broadphase search overhead.

7. Debugging Camera Clipping

Camera collision is a frequent source of performance issues and jitter. By recording while moving the camera through foliage or debris, you can identify if the camera is performing too many “Spring Arm” traces, leading to the elimination of camera-induced stuttering in dense environments.

8. Monitor “Async” vs “Sync” Queries

The analyzer differentiates between synchronous and asynchronous queries. For non-critical traces (like cosmetic effects), ensure they are being run asynchronously. Using the analyzer to verify this distribution helps in the elimination of Game Thread stalls during heavy combat or physics-heavy scenes.