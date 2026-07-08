---
layout: default
title: NaniteBuilder
---

<!-- ai-generation-failed -->

<h1>NaniteBuilder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/NaniteBuilder/NaniteBuilder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, GeometryCore, ImageCore, NaniteUtilities, QuadricMeshReduction, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

core geometric processing required to convert standard meshes into the Nanite format. It implements the complex algorithms that partition a mesh into clusters, build the hierarchical LOD structure, and compress the data for efficient GPU streaming.

This module works in tandem with the MeshBuilder pipeline. When a Static Mesh has “Enable Nanite” checked, the engine invokes NaniteBuilder to perform the cluster-based simplification and encoding. Its primary goal is the elimination of traditional LOD management by providing a seamless, highly detailed virtualized geometry representation.

Practical Usage Tips and Best Practices
1. Add to Editor Build Dependencies

The NaniteBuilder module is an editor-only utility located in the Developer folder. If you are writing custom tools that programmatically trigger Nanite builds (such as a custom importer), you must include it in your Editor.Build.cs. This leads to the elimination of linker errors during your tool’s compilation.

2. Configure the “Trim Relative Error”

Within the FMeshNaniteSettings structure used by the builder, the Trim Relative Error is the most important parameter. Increasing this value allows the builder to simplify the clusters more aggressively, leading to the elimination of unnecessary disk space and memory usage for meshes that don’t require microscopic detail.

3. Handle Hard Edges and Seams

The NaniteBuilder respects UV seams and hard normals, but these force the builder to create more cluster boundaries. Minimizing unnecessary hard edges in your source geometry leads to the elimination of “Cluster Bloat,” resulting in better performance and smaller file sizes after the build process completes.

4. Monitor Build Time for Massive Meshes

Nanite building is computationally intensive. For meshes with millions of triangles, the process can take significant time and RAM. Ensuring your development machine has sufficient memory assists in the elimination of “Out of Memory” crashes during the cluster-generation phase of the build.

5. Leverage the Proxy Mesh Workflow

For assets that cannot be fully converted to Nanite, the builder can generate a “Fallback Mesh.” Using the builder to tune the Fallback Relative Error leads to the elimination of visual popping when the engine switches from the Nanite representation to the standard proxy mesh at extreme distances.

6. Audit Nanite Overdraw

Use the Nanite “Overdraw” visualization in the editor to see how the builder has partitioned your mesh. If the builder produces too many overlapping clusters, it can lead to performance hits. Adjusting the source geometry to be more manifold leads to the elimination of overdraw bottlenecks on the GPU.

7. Validate Geometry Integrity

The NaniteBuilder requires manifold geometry for the best results. Using the module’s internal validation to check for non-manifold edges or self-intersections before building leads to the elimination of “Holes” or “Cracks” in the rendered Nanite mesh.

8. Use for Custom Procedural Nanite Assets

If your project generates complex procedural geometry at edit-time (like a custom city generator), you can call the NaniteBuilder API to ensure your generated meshes utilize virtualized geometry. This facilitates the elimination of draw call limitations, allowing you to render vast amounts of procedural detail without sacrificing frame rate.