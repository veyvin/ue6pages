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

eshes. It is designed to produce higher-quality surfaces with lower polygon counts by intelligently managing “stitching” and “healing” of edges during the import process.

Practical Usage Tips and Best Practices
1. Prioritize Over Legacy Tessellation

For most modern CAD imports, ensure CADKernel is the active tessellator. It is generally faster and produces fewer “T-junctions” (gaps between triangles) than the legacy system. You can verify it is active via the console variable: ds.CADTranslator.DisableCADKernelTessellation 0.

2. Balance Chord Tolerance and Visual Fidelity

The Chord Tolerance (the maximum distance between the original curve and the new triangle) is the most critical setting. A smaller value increases detail but also increases the triangle count. To “eliminate” performance lag in large scenes, use a higher tolerance for background machinery and a lower tolerance only for hero assets.

3. Leverage “Retessellate” for Iteration

If a specific part looks blocky after import, you do not need to reimport the entire CAD file. Select the Static Mesh in the Content Browser, right-click, and choose Datasmith > Retessellate. This allows CADKernel to re-process just that asset with higher quality settings while keeping other scene data intact.

4. Optimize with Max Edge Length

Use the Max Edge Length setting to prevent the creation of extremely long, thin triangles on flat surfaces. Long triangles often cause lighting artifacts in Lumen or Nanite. Setting a reasonable limit ensures a more uniform mesh distribution, which improves both shadow quality and Nanite virtualization.

5. Clean Up Geometry with “Sew Mesh”

If your source CAD data has small gaps between surfaces (common in older files), enable the Sew Mesh option. CADKernel will attempt to “stitch” these edges together during tessellation, which helps “eliminate” light leaks and ensures that the resulting mesh is considered “watertight” for physics and lighting.

6. Use CAD Cache for Speed

CADKernel works with the CAD Cache system. If you are re-importing the same file with different settings, the module will only re-process the parts that have changed. Ensure ds.CADTranslator.EnableCADCache 1 is set to avoid redundant processing time during long working sessions.

7. Monitor Normal Tolerance for Curves

For highly curved surfaces (like car fenders or pipes), pay close attention to Normal Tolerance. This setting controls the maximum angle between adjacent triangles. If your curves look “faceted” even with a low Chord Tolerance, lowering the Normal Tolerance will force CADKernel to add more subdivisions along the curve.

8. Verify with Wireframe Mode

After a CADKernel import, always check your mesh in Wireframe Mode (Alt+2). Look for areas of extreme density or “slivers” (overlapping triangles). If you see excessive density on flat surfaces, increase your tolerance values to “eliminate” unnecessary polygons that would otherwise waste memory.

Performance & Best Practices
Nanite Integration: When importing via Datasmith, enable the “Build Nanite” option. CADKernel creates very clean topology that Nanite can easily compress, allowing you to use high-fidelity CAD data directly in-game.
Stitching vs. Healing: Use “Stitching” for parts that should be a single continuous surface and “Healing” for parts that have corrupted topology. Over-using healing can significantly increase import times.
Multi-threading: CADKernel is highly parallelized. If your imports are slow, check your CPU usage in Task Manager; more cores will directly lead to faster CAD translation.