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

thin the Datasmith ecosystem designed to handle the heavy processing and translation of CAD (Computer-Aided Design) data.

Description

This module functions as an out-of-process worker that translates raw mathematical CAD formats (such as CATIA, SolidWorks, Rhino, or JT) into a format Unreal Engine can understand. Because CAD files are typically represented as precise NURBS or parametric surfaces rather than polygons, they require significant CPU resources to “tessellate” (convert to triangles). By using a dedicated worker process, DatasmithCADWorker ensures that the Unreal Editor remains responsive and stable during massive data imports, isolating the memory-intensive translation tasks from the main editor process.

Practical Usage Tips and Best Practices
1. Enable CADKernel for Superior Tessellation

In Unreal Engine 5.3+, the worker defaults to using CADKernel. This is a modern tessellation engine that provides better surface quality with fewer polygons. Use it to generate cleaner meshes that are better suited for Nanite, as it significantly reduces the occurrence of T-junctions and overlapping faces compared to legacy translators.

2. Manage Parallel Processing via CVars

The worker system is multi-threaded and can spin up multiple instances to process parts of a large assembly simultaneously. If your machine is hanging during import, you can limit the number of worker threads using the console command ds.CADTranslator.MaxParallelWorkers. Reducing this number can help eliminate system instability on machines with limited RAM.

3. Leverage the CAD Cache for Rapid Re-imports

The module utilizes a CAD Cache (stored in your project’s Intermediate/Datasmith/CADCache folder). This cache stores the results of the translation and tessellation. When you re-import a file with the same name and timestamp, the worker pulls from the cache instead of re-processing the file, which can save hours of time on large-scale architectural or manufacturing models.

4. Tune Chord and Normal Tolerance

The worker uses specific parameters to determine how many triangles to create.

Chord Tolerance: The maximum distance between a generated triangle and the original curved surface.
Normal Tolerance: The maximum angle between adjacent triangles. Decreasing these values results in higher fidelity but higher poly counts. Start with “Medium” presets and only refine specific small parts to keep the overall project performance high.
5. Use “Sew Mesh” to Fix Surface Gaps

If you notice small holes or light leaks in your imported CAD geometry, enable the Sew Mesh option in the import settings. This instructs the worker to perform an additional pass to stitch adjacent surfaces together. This is a best practice for automotive visualization to ensure that car panels look like a single continuous surface.

6. Optimize Memory via Standalone Execution

Because DatasmithCADWorker runs as a separate .exe (found in Engine/Binaries/Win64/DatasmithCADWorker.exe), it can utilize its own memory space. This is critical when importing files that exceed 10GB; it allows the worker to use all available system RAM for the translation without the Unreal Editor’s own memory footprint causing an “Out of Memory” crash.

7. Handle Data Cleanup and Elimination

During the import of massive assemblies, the worker may identify redundant components or “phantom” parts. Use the Stitching Tolerance and Geometric Tolerance settings to help the worker identify and merge nearly-identical vertices. This helps in the elimination of microscopic gaps and tiny, invisible sliver-polygons that can cause artifacts in Lumen or ray-tracing.

8. Troubleshoot via Worker Logs

If an import fails, the answer is usually in the worker-specific logs. Check Saved/Logs for files prefixed with DatasmithCADWorker. These logs contain the specific error codes from the underlying CAD SDKs (like OpenCASCADE), which are much more descriptive than the general “Import Failed” message in the Editor.