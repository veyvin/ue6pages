---
layout: default
title: CADKernelEngine
---

<!-- ai-generation-failed -->

<h1>CADKernelEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Datasmith/CADKernel/Engine/CADKernelEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CADKernel, Core, CoreUObject, GeometryCore, Json, MeshConversion, MeshDescription, StaticMeshDescription, TechSoft</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ce quality, T-junction repair, and multi-threaded performance. It is used to convert mathematical NURBS or B-Rep surfaces from formats like CATIA, SolidWorks, and Alias into Unreal Engine static meshes.

Practical Usage Tips and Best Practices
Prioritize CADKernel for Nanite Workflows
CADKernel is optimized to produce high-quality topology with fewer open edges and T-joints. This is essential for a successful Nanite conversion. By using CADKernel, you “eliminate” many of the shading artifacts and “cracks” that occur when complex CAD assemblies are converted to virtualized geometry.
Toggle via Console Variables (CVARs)
If you encounter specific tessellation errors on a complex model, you can switch back to the legacy tessellator using the following command to “eliminate” the issue: ds.CADTranslator.DisableCADKernelTessellation 1 (Note: 0 is the default, enabling CADKernel).
Utilize Max Edge Length for Uniformity
In the Datasmith/Interchange import settings, utilize the Max Edge Length parameter supported by CADKernel. Setting a maximum edge size ensures that large, flat surfaces are subdivided into smaller triangles, which helps “eliminate” lighting artifacts from Lumen and provides a more uniform density for vertex painting.
Configure Stitching and Sewing Tolerances
CADKernel uses a specific stitching algorithm to merge open edges. If your imported model has visible gaps, increase the Stitching Tolerance. This tells the engine to “eliminate” small gaps by snapping nearby vertices together during the tessellation phase.
Manage the CAD Cache Subfolder
CADKernel generates intermediate data stored in the project’s Intermediate/DatasmithCADCache folder. If you change your tessellation settings but don’t see the updates, you may need to “eliminate” the cache or use the CVAR ds.CADTranslator.OverwriteCache 1 to force a re-process of the geometry.
Leverage Multi-Threaded Tessellation
One of the primary advantages of this module is its ability to process multiple bodies in parallel. If you have a massive assembly (e.g., a full vehicle), ensure your CPU has high core availability. You can control the thread count via ds.CADTranslator.MaxConcurrentTasks to “eliminate” bottlenecks during large-scale imports.
Optimize for “Wire” Formats
For Alias (.wire) files, CADKernel supports specific options like “Use Layer as Actor.” This best practice allows you to maintain the organizational structure of the designer’s work, “eliminating” the need to manually reorganize thousands of parts after the import is complete.
Balance Chord Tolerance and Normal Tolerance
To “eliminate” “blocky” curves while keeping the triangle count manageable, use a small Chord Tolerance (distance between the mesh and the mathematical surface) but a more relaxed Normal Tolerance. This keeps high detail on sharp curves while simplifying flatter areas of the CAD model.