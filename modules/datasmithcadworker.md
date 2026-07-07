---
layout: default
title: DatasmithCADWorker
---

<!-- ai-generation-failed -->

<h1>DatasmithCADWorker</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithCADWorker/DatasmithCADWorker.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, CADInterfaces, CADTools, Core, DatasmithDispatcher, Projects, Sockets</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

process, it prevents the Editor from freezing during long imports and allows for multi-threaded tessellation, significantly speeding up the ingestion of massive engineering assemblies.

Practical Usage Tips and Best Practices
Leverage CADKernel for Better Quality
In UE 5.6, the worker uses the CADKernel by default. This is a faster, multi-threaded tessellator that produces higher-quality surfaces with fewer polygons compared to legacy translators. If you encounter issues, you can toggle this via the console variable ds.CADTranslator.DisableCADKernelTessellation 1, though you should only do this to eliminate specific tessellation errors.
Fine-Tune Chord Tolerance
The “Chord Tolerance” setting in the import dialog is the most critical factor for performance. It defines the maximum distance between the original CAD surface and the generated mesh. Increasing this value will eliminate millions of unnecessary triangles in large assemblies, improving both import speed and runtime frame rates.
Manage the CAD Cache
The worker uses a local cache to avoid re-processing files that haven’t changed. If you need to force a clean re-import, use the console variable ds.CADTranslator.EnableCADCache 0 or ds.CADTranslator.OverwriteCache 1. This helps eliminate the risk of using outdated geometry when the source CAD file has been updated.
Monitor Worker Stability in Task Manager
Since the worker runs as a separate executable (DatasmithCADWorker.exe), you can monitor its CPU and memory usage independently of Unreal. If an import hangs, you can manually eliminate the process in Task Manager to recover the Editor without a full crash.
Optimize Large Assembly Hierarchies
CAD files often contain thousands of nested parts. Use the “Stitching” options in the Datasmith settings to merge smaller components. This helps eliminate the overhead of having too many individual Scene Components and Static Mesh Actors in your World Outliner.
Utilize Re-import for Design Iteration
Datasmith is non-destructive. If a part of your CAD model is updated (e.g., a protective casing is redesigned to eliminate a sharp edge), you can re-import just that specific file. The worker will process only the changes, maintaining your materials and actor placements in the level.
Sew Meshes for Smooth Surfaces
If you are seeing “cracks” between surfaces, enable the “Sew Mesh” option. This forces the worker to perform an additional pass to align edges of adjacent patches, which is essential to eliminate T-junctions and light leaks on high-precision mechanical models.
Adjust Normal Tolerance for Curvature
Use the “Normal Tolerance” setting to control how much the angle between adjacent triangles can vary. A smaller angle ensures smoother curves on rounded parts (like pipes or fillets), helping you eliminate “faceted” or “blocky” looks on hero assets.