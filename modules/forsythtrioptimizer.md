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

l Engine that implements Tom Forsyth’s Linear-Speed Vertex Cache Optimization algorithm.

Description and Purpose

This module is a core part of Unreal Engine’s static mesh build pipeline. Its primary function is to reorder the indices of a triangle mesh to maximize the efficiency of the GPU’s Post-Transform Vertex Cache. When a GPU renders a triangle, it checks if the vertices have already been processed; if a vertex is found in the cache, the GPU skips the vertex shader for that point. The Forsyth algorithm organizes triangles so that vertices are reused as quickly as possible, significantly reducing the number of times the vertex shader must run. This process is essential for high-performance rendering, especially on mobile and console hardware where vertex throughput can be a bottleneck.

Practical Usage Tips and Best Practices
Understand Its Role in the Build Pipeline
The Forsyth optimizer runs automatically when you import a mesh or “Build” geometry. It targets the index buffer specifically. Because it is an automated part of the StaticMeshBuilder, you do not usually need to call it manually, but knowing it exists helps you eliminate confusion when seeing “Optimizing Index Buffer” during long asset imports.
Prioritize for Vertex-Heavy Scenes
If your project features high-density geometry with complex vertex shaders (such as wind-swept foliage or detailed character meshes), this optimizer is critical. By maximizing cache hits, it helps eliminate GPU stalls caused by the vertex fetch and transform stages.
Profile the “Vertex/Attribute” Bound State
If Unreal Insights or RenderDoc shows that your GPU is “Attribute Bound” or “Vertex Bound,” it means the vertex shader is being overworked. While the Forsyth optimizer handles index reordering, you should also ensure your meshes have high vertex reuse (welded vertices) to eliminate redundant calculations that the optimizer cannot fix.
Maintain Clean Topology
The optimizer works best on manifold geometry with consistent connectivity. Avoid creating “T-junctions” or disconnected “floating” geometry within a single mesh. Clean topology allows the algorithm to find better triangle strips, which will eliminate cache misses more effectively.
Impact on Nanite vs. Standard Meshes
Standard Static Meshes rely heavily on index buffer optimization. However, Nanite uses a different clustering and meshlet-based approach for its specialized renderer. For Nanite geometry, the engine uses different optimization passes (like those found in the MeshOptimizer library) to eliminate redundant triangles and optimize cluster bounds.
Monitor Mobile Performance
Mobile GPUs have much smaller vertex caches than desktop GPUs. The Forsyth algorithm is particularly vital for mobile development; ensure your “Build Settings” for static meshes have “Build Adjacency Buffer” and related optimization flags enabled to eliminate performance drops on mobile handsets.
Check for Welded Vertices
The Forsyth optimizer cannot reuse a vertex if it has been “split” due to hard edges or UV seams. If you have a high vertex count relative to your triangle count, consider smoothing your normals or simplifying your UV layout. This allows the optimizer to eliminate unnecessary vertex transformations by treating the shared points as a single cacheable entry.
Use for Procedural Mesh Generation
If you are writing a custom C++ system that generates procedural geometry at runtime, consider that your raw index buffer will be unoptimized. While calling the Forsyth module at runtime can be expensive, doing so for static procedural assets created in the editor will eliminate rendering overhead in the final shipping build.