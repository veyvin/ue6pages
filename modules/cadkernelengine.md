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

ngine’s proprietary CAD (Computer-Aided Design) processing library. Introduced as a modern replacement for older third-party tessellation libraries, it is responsible for converting mathematically precise CAD data (NURBS, B-Rep) into the triangular meshes used by the engine for real-time rendering.

This module is the “engine” behind the Datasmith CAD importer, enabling faster, multi-threaded tessellation and providing better control over the balance between visual fidelity and polygon count.

Practical Usage Tips and Best Practices
1. Add to Module Dependencies

If you are developing custom tools that programmatically import or manipulate CAD data via C++, you must include this module in your Build.cs.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "CADKernelEngine", "DatasmithContent" });
Copy code
2. Toggle CADKernel via CVAR for Debugging

While CADKernel is the modern default, you can switch back to the legacy tessellator if you encounter specific geometry errors.

Action: Use the console command ds.CADTranslator.DisableCADKernelTessellation 1 to bypass this module. This is useful to determine if a visual artifact is a result of the CADKernel algorithm or the source file itself, helping you eliminate bugs during the import process.
3. Optimize Performance with Multi-Threading

The CADKernelEngine is designed to be highly parallel. Unlike older importers that processed files sequentially, this module can distribute the tessellation of different parts across multiple CPU cores.

Tip: When importing large assemblies, monitor your CPU usage. If it isn’t maxed out, check your Datasmith Import Settings to ensure that your hardware is being fully utilized to eliminate long waiting periods.
4. Tune Tessellation via Chord Tolerance

This module uses “Chord Tolerance” to define how closely the mesh must follow the original CAD curve.

Best Practice: For small, highly detailed parts (like screws or gears), use a lower Chord Tolerance. For large, flat surfaces, increase it. Finding the right balance will eliminate unnecessary triangles while maintaining smooth silhouettes on curved surfaces.
5. Leverage the CAD Cache

The engine uses a caching system to avoid re-processing the same CAD data multiple times.

Tip: Use the CVAR ds.CADTranslator.EnableCADCache 1 (default) to ensure that re-importing the same asset is nearly instantaneous. If you need to force a fresh re-tessellation to test new settings, set ds.CADTranslator.OverwriteCache 1 to eliminate stale data.
6. Use ‘Sew Mesh’ for Smooth Surfaces

When importing complex surfaces (like car body panels), small gaps can sometimes appear between patches.

Action: Enable the “Sew Mesh” option in the import settings. This module will attempt to weld coincident vertices along the edges of NURBS patches, which helps eliminate T-junctions and unsightly “light leaks” in your materials.
7. Prefer JtFile Embedded Tessellation for Speed

If you are working with JT files that already contain pre-tessellated mesh data:

Tip: Use the CVAR ds.CADTranslator.PreferJtFileEmbeddedTessellation 1. This allows the engine to skip the CADKernelEngine’s computation entirely and use the pre-made mesh, which can eliminate significant processing time for massive industrial datasets.
8. Monitor Memory During Import

CAD translation is a memory-intensive process. Because this module converts complex mathematical data into heavy meshes in RAM before saving them to disk:

Best Practice: Close unnecessary applications during a large CAD import. If the engine runs out of memory, it may eliminate the import process entirely and crash. Monitor the “Memory” stat to ensure your system has enough headroom for the specific complexity of your CAD assembly.