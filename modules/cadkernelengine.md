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

e’s proprietary CADKernel library. Introduced to replace legacy third-party tessellators, it serves as a high-performance geometry processing bridge within the Datasmith import pipeline.

Its primary purpose is to translate parametric CAD data (B-Rep) into optimized triangular meshes. It provides a more modern, multi-threaded tessellation algorithm that produces higher-quality surfaces with lower polygon counts compared to older methods, specifically addressing common issues like “T-junctions” and open edges in complex engineering models.

Practical Usage Tips and Best Practices
Enable for Nanite-Ready Geometry
CADKernel is the preferred engine for Nanite workflows. Because it produces cleaner topology with fewer open edges, it significantly improves the Nanite conversion process. Use it to eliminate visible cracks or shading artifacts often found in CAD-to-Nanite transitions.
Toggle via Console Variables (CVars)
If you encounter a specific model that fails to tessellate correctly, you can revert to the legacy system to eliminate the error by using the command:
ds.CADTranslator.DisableCADKernelTessellation 1.
Note that CADKernel is the default starting from version 5.3.
Optimize Import Speed with Multi-Threading
CADKernel is natively multi-threaded. To eliminate long wait times during massive assembly imports, ensure your CPU has sufficient logical cores available. You can limit the impact on your system during import by adjusting the thread count via:
ds.CADTranslator.MaxImportThreads.
Utilize Max Edge Length
Unlike legacy tessellators, CADKernel effectively supports the Max Edge Length parameter in the Datasmith import settings. Use this to eliminate overly long, thin triangles on flat surfaces, which improves both rendering performance and lightmap UV generation.
Manage the CAD Cache
The module works closely with the CADCache system (located in your project’s Intermediate/Datasmith/ folder). If you change tessellation settings but don’t see results, use ds.CADTranslator.OverwriteCache 1 to eliminate stale mesh data and force a full re-tessellation of the source files.
Fine-Tune Stitching Tolerances
CADKernel uses a specific geometric tolerance to merge adjacent surfaces. If your model appears “shattered” or has holes, adjust the Stitching Tolerance in the Datasmith import options. This allows the kernel to “eliminate” gaps by snapping nearby edges together during the mesh generation phase.
Leverage Retessellation for Level of Detail
You do not need to re-import the entire CAD file to change quality. Right-click a Static Mesh asset in the Content Browser and select Datasmith > Retessellate. This uses the CADKernelEngine to re-process the cached parametric data with new settings, eliminating the need to access the original source file on disk.
Monitor Memory During Large Imports
While fast, the kernel can be memory-intensive when processing thousands of parts simultaneously. If the editor crashes during import, eliminate the memory bottleneck by importing smaller sub-assemblies or reducing the number of concurrent import threads.