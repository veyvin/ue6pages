---
layout: default
title: metis
---

<!-- ai-generation-failed -->

<h1>metis</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/metis/metis.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">GKlib</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

hich is a set of programs for partitioning graphs, partitioning finite element meshes, and producing fill-reducing orderings for sparse matrices. Within Unreal Engine, it is primarily utilized by high-end geometry processing pipelines like Nanite and ProxyLOD.

Its main purpose is to solve the complex mathematical problem of “graph partitioning.” When Nanite breaks a massive mesh into “Clusters,” or when the ProxyLOD system simplifies a city block into a single proxy, the METIS module determines how to “cut” the geometry into balanced pieces. This helps you eliminate irregular data distribution, ensuring that every GPU cluster or processing task has an equal amount of work.

Practical Usage Tips and Best Practices
Understand Its Role in Nanite Generation
METIS is the engine behind Nanite’s cluster partitioning. It analyzes the connectivity of a mesh to group triangles into clusters of 128. By providing balanced partitions, it helps eliminate “long-edged” clusters that would otherwise cause poor rasterization performance and artifacts.
Dependency Management in Build.cs
If you are developing custom low-level mesh processing tools in C++, you must include "Metis" in your PrivateDependencyModuleNames. Because it is an external library wrapper, ensure you also include the MeshUtilities or NaniteBuilder modules if you intend to use it for standard engine geometry tasks.
Use for Sparse Matrix Ordering
For developers working on custom physics solvers or complex simulation systems (like those found in Chaos), METIS can be used to reorder sparse matrices. This reordering helps eliminate “fill-in” during matrix factorization, which significantly speeds up the math required for high-fidelity simulations.
Optimize ProxyLOD Partitions
When using the ProxyLOD tool to merge multiple actors, METIS handles the spatial partitioning of the combined geometry. If you find your proxy meshes have strange “seams,” adjusting your spatial bounds can help METIS eliminate awkward cuts across thin geometry.
Leverage for Parallel Processing
If you are writing a custom procedural system that needs to distribute tasks across many CPU cores, use METIS to partition your data into \(N\) equal parts (where \(N\) is your thread count). This helps you eliminate “worker starvation,” where some threads finish instantly while others are overloaded.
Avoid Runtime Use in Games
METIS is computationally expensive and intended for “offline” use (during asset cooking or in-editor processing). Attempting to use METIS for real-time mesh partitioning in a shipping build will likely cause massive frame drops; you should eliminate its use from any runtime performance-critical paths.
Check for Non-Manifold Geometry
METIS relies on a clean connectivity graph. If your mesh has “non-manifold” edges (where more than two triangles share an edge), the partitioner may produce suboptimal results. Cleaning your geometry in a modeling tool beforehand helps eliminate logic errors in the METIS partitioning phase.
Monitor Output during ‘Elimination’ of Geometry
When using METIS to simplify a mesh (an “elimination” of excess detail), monitor the “Cluster Count” in the Nanite stats. If METIS is struggling to create clean partitions, it may result in a higher number of clusters than necessary. Tuning the “Cluster Error” threshold in the Static Mesh settings can help eliminate this inefficiency.