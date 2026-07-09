---
layout: default
title: ForsythTriOptimizer
---

<!-- ai-generation-failed -->

<h1>ForsythTriOptimizer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/ForsythTriOO/ForsythTriOptimizer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ments Tom Forsyth’s linear-speed vertex cache optimization algorithm. Its primary purpose is to reorder the indices of a triangle mesh to maximize the efficiency of the Post-Transform Vertex Cache (PTVC) on the GPU. By organizing triangles so that they reuse recently transformed vertices, the module significantly reduces the number of times the vertex shader must execute for a given mesh, directly improving rendering performance.

Practical Usage Tips & Best Practices
1. Rely on the Automatic Build Pipeline

In most cases, you do not need to call this module manually. Unreal Engine automatically invokes the Forsyth algorithm during the Static Mesh “Build” process.

Best Practice: Ensure your meshes are properly “Built” after import. This reordering happens behind the scenes, leading to the elimination of redundant vertex shader invocations without requiring manual artist intervention.
2. Monitor “Vertex Reuse” in Profiling

If you suspect a mesh is poorly optimized, you can check its vertex-to-triangle ratio in the Static Mesh Editor stats.

Tip: A high number of vertex shader invocations relative to the vertex count suggests poor cache locality. Running the optimizer (via a re-import or build) assists in the elimination of “over-shading” where the GPU processes the same vertex multiple times.
3. Use for Custom Mesh Procedural Generation

If you are generating complex meshes at runtime or via custom editor tools using MeshDescription, you should incorporate the optimizer.

Best Practice: Before finalizing a procedural index buffer, pass your data through the ForsythTriOptimizer functions. This ensures the elimination of performance bottlenecks in your custom geometry that would otherwise result from randomized or “naive” index ordering.
4. Distinguish from Spatial Clustering

It is important to understand that Forsyth reorders indices for cache hits, which is different from spatial clustering used for occlusion.

Tip: Use Forsyth for local vertex reuse and use the MeshOptimizer or Nanite tools for spatial clustering. Combining both strategies results in the elimination of both unnecessary vertex processing and unnecessary draw calls.
5. Prioritize for High-Poly Non-Nanite Meshes

While Nanite uses its own internal clustering and optimization, traditional Static Meshes (especially those used on mobile or legacy platforms) rely heavily on PTVC optimization.

Best Practice: For mobile projects where vertex throughput is limited, double-check that the Forsyth optimizer has been applied to high-density assets. This facilitates the elimination of GPU stalls on mobile hardware with small vertex caches.
6. Avoid Constant Re-Optimization on Dynamic Meshes

Reordering indices is a computationally expensive task meant for the build-time or load-time phase.

Tip: Do not run the Forsyth algorithm every frame on dynamic procedural meshes (like a deforming ocean). The CPU cost of re-indexing will outweigh the GPU gains. Reserve optimization for static or semi-static data to ensure the elimination of CPU frame-time spikes.
7. Combine with Index Buffer Compression

Optimizing for the vertex cache often makes the index buffer more “predictable,” which benefits compression algorithms.

Best Practice: Use Forsyth optimization in conjunction with Meshoptimizer’s index compression for shipping builds. This leads to the elimination of excessive disk space and memory bandwidth usage for large index buffers.
8. Verify with RenderDoc

To see the real-world impact of the module, use a graphics debugger like RenderDoc to inspect the “Vertex Cache Hit” stats.

Tip: Compare an unoptimized index buffer to an optimized one. You should see a noticeable elimination of “Cache Misses,” proving that the GPU is successfully pulling transformed vertices from the cache rather than re-running the vertex shader.