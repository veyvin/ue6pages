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

igned to take advantage of modern multi-core CPUs.

Best Practice: When importing massive assemblies, ensure your workstation has high core counts. The worker process can spin up multiple instances to tessellate different parts of the CAD file simultaneously, leading to the rapid elimination of long import wait times.
2. Optimize via CADKernel

In recent versions of Unreal Engine, the CAD Worker uses a proprietary tessellation algorithm called CADKernel.

Tip: Use CADKernel for better surface quality with lower polygon counts compared to legacy tessellators. If you encounter specific geometry errors, you can toggle this via the console variable ds.CADTranslator.DisableCADKernelTessellation 1, though this should be a last resort for troubleshooting.
3. Control Fidelity with Chord Tolerance

The worker relies on “Chord Tolerance” to determine how many triangles to generate for a curved surface.

Best Practice: Use a larger Chord Tolerance for background objects to keep poly counts low. For hero assets, decrease the value. Finding the right balance ensures the elimination of “jagged” edges on curved surfaces without overloading the GPU with unnecessary triangles.
4. Manage Memory via Standalone Isolation

Because CAD translation is extremely memory-intensive, it can often crash a 32GB or 64GB machine if handled within the Editor.

Tip: If the worker crashes, check the Windows Task Manager. If you see the DatasmithCADWorker.exe reaching your RAM limit, try importing the assembly in smaller sub-sections. The isolation provided by the module ensures that a worker crash does not cause the elimination of your unsaved progress in the Unreal Editor.
5. Use CAD Cache for Iterative Imports

The module supports a caching system to avoid re-processing geometry that hasn’t changed.

Best Practice: Keep ds.CADTranslator.EnableCADCache 1 enabled. This allows the worker to skip files that were previously processed, which is essential for the elimination of redundant processing time when re-importing updated versions of a complex assembly.
6. Debug via Worker Logs

When an import fails, the error is often buried in the worker’s specific logs rather than the main Unreal output log.

Tip: Look for log files in your project’s Saved/Logs or the intermediate Datasmith folders. Identifying specific “Tessellation Failed” messages in the worker log is the fastest way to achieve the elimination of corrupt source data that prevents a successful import.
7. Clean Up Stale Worker Processes

Occasionally, if an import is forcefully canceled, the DatasmithCADWorker process may remain active in the background.

Best Practice: If you notice your CPU usage remains high after a canceled import, manually check the Task Manager and end any lingering DatasmithCADWorker tasks. This ensures the elimination of “zombie” processes that could slow down subsequent import attempts.
8. Prefer “Sew Mesh” for High-Quality Surfaces

For manufacturing-grade CAD data with many small surfaces, the worker can “sew” edges together during translation.

Tip: If you see “light leaks” or cracks between panels in Unreal, ensure the “Sew Mesh” option is active in the import settings. This allows the worker to heal T-junctions, resulting in the elimination of visual artifacts on complex surfaces like car bodies.