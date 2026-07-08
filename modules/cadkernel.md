---
layout: default
title: CADKernel
---

<!-- ai-generation-failed -->

<h1>CADKernel</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Datasmith/CADKernel/Base/CADKernel.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, GeometryCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

c surfaces (NURBS, B-Rep) into the triangular meshes used by Unreal Engine’s renderer. It is specifically built to handle the massive complexity of industrial data from software like Catia, SolidWorks, Rhino, and Alias.

Primary uses include:

High-Fidelity Tessellation: Creating optimized triangular meshes that maintain the smooth curves of the original CAD model.
Model Repair: Automatically “sewing” together surfaces that have small gaps or misaligned edges to ensure a watertight mesh.
Multi-threaded Processing: Speeding up the import process by distributing the heavy math required for surface conversion across multiple CPU cores.
Memory Efficiency: Generating fewer polygons in flat areas while maintaining high density on complex curves to balance visual quality and performance.
Practical Usage Tips and Best Practices
1. Prioritize CADKernel for Industrial Data

Always use CADKernel (enabled by default in modern UE5 versions) over the legacy tessellator when importing complex machinery or automotive models. It produces significantly better topology with a lower triangle count, which is essential for maintaining high frame rates in real-time visualizations.

2. Master the Core Tessellation CVAR

If you suspect an import issue is related to the new system, you can toggle CADKernel off using the following console variable: ds.CADTranslator.DisableCADKernelTessellation 1 Note: Use this only for troubleshooting; generally, CADKernel should remain enabled for production imports.

3. Leverage the “Retessellate” Workflow

You do not need to re-import an entire file to change quality. In the Content Browser, right-click a Datasmith Static Mesh asset and select Datasmith > Retessellate. This allows CADKernel to re-process the original parametric data stored in the Datasmith scene, letting you increase detail for “hero” objects without restarting the import.

4. Optimize via Chord Tolerance

When importing via Datasmith, adjust the Chord Tolerance. This value represents the maximum distance between the generated triangle and the original mathematical surface. Lowering this value (e.g., from 0.1 to 0.01) will make curves smoother but increase the polygon count.

5. Use “Max Edge Length” for Nanite

If you are importing CAD data intended for Nanite, use a smaller Max Edge Length setting in the import options. This forces CADKernel to create more uniform triangles, which helps Nanite’s compression and prevents long, thin triangles that can cause shading artifacts.

6. Clear the CAD Cache for Clean Imports

Unreal Engine caches processed CAD data to speed up subsequent imports. If a file is updated but appears “stale” in the engine, use ds.CADTranslator.EnableCADCache 0 to force the module to re-tessellate from scratch, ensuring the elimination of outdated geometry.

7. Repair Surfaces with Stitching

For “dirty” CAD files with unjoined surfaces, ensure that the Stitching option is enabled in the Datasmith import settings. This utilizes CADKernel’s geometric healing algorithms to merge nearby vertices, creating a continuous surface that reacts correctly to Unreal’s lighting and shadows.

8. Monitor via LogDatasmith

When importing large assemblies, keep the Output Log open and filtered to LogDatasmith. CADKernel will report specific errors if surfaces fail to tessellate or if the geometry is degenerate. Identifying these specific parts allows you to fix them in the source CAD software or isolate them for manual retessellation.