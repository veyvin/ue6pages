---
layout: default
title: QuadricMeshReduction
---

<!-- ai-generation-failed -->

<h1>QuadricMeshReduction</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MeshSimplifier/QuadricMeshReduction.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, MeshDescription, MeshUtilitiesCommon, NaniteUtilities, RenderCore, StaticMeshDescription</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ion system in Unreal Engine. It uses a “Quadric Error Metrics” algorithm to calculate the visual impact of collapsing edges and merging vertices. By identifying and removing the edges that contribute least to the overall shape, it can drastically reduce the triangle count of a mesh while preserving its silhouette and UV mapping.

This module is the core engine behind the Static Mesh LOD (Level of Detail) Generator and is used to create optimized versions of high-poly geometry for better rendering performance.

Practical Usage Tips & Best Practices
1. Use LOD Group Presets for Consistency

Instead of manually entering reduction percentages for every asset, utilize the LOD Group dropdown in the Static Mesh Editor.

Best Practice: Assign a group like “LargeProp” or “Foliage.” This applies pre-configured reduction settings across your project, ensuring the elimination of visual inconsistency where some assets appear much lower quality than others at the same distance.
2. Prioritize Silhouette Preservation

The “Termination Criterion” in the reduction settings determines how the algorithm stops.

Tip: If your mesh looks “melted” after reduction, increase the Welding Threshold. This prevents the algorithm from merging distant vertices, which leads to the elimination of jagged edges and preserves the recognizable outline of the object.
3. Protect UV Seams and Hard Edges

Aggressive reduction can often “pinch” textures or break hard lighting edges.

Best Practice: Enable the Keep Percent of Vertices or Lock Mesh Edges options in the reduction settings. Protecting these critical areas results in the elimination of texture stretching and lighting artifacts on simplified geometry.
4. Optimize Screen Size Thresholds

The QuadricMeshReduction module works in tandem with the Screen Size variable to determine when an LOD becomes active.

Tip: Use the “Auto Compute LOD Distances” feature as a starting point, then manually pull the screen size sliders. Tuning these values leads to the elimination of “popping” (where a mesh visibly changes shape) by ensuring the transition happens when the object is small enough on screen.
5. Bake Nanite Fallback Meshes

For Nanite-enabled assets, this module is used to generate the “Fallback Mesh” seen on platforms that do not support Nanite or in certain ray-tracing passes.

Best Practice: Open the Nanite settings and adjust the Fallback Relative Error. Setting this correctly ensures the elimination of performance hits on older hardware by providing a high-quality, reduced-poly version of the Nanite asset.
6. Combine with Merge Actors for HLODs

When creating Hierarchical LODs (HLODs), this module simplifies the combined geometry of multiple actors.

Tip: When merging actors, use the “Simplify” mesh method. Reducing the combined mesh facilitates the elimination of thousands of hidden internal triangles that are no longer visible, significantly lowering the draw call count for distant vistas.
7. Monitor Vertex Color Preservation

If you use Vertex Colors for shader masking (like wind or moss), reduction can sometimes “blur” these values.

Best Practice: Check the Attribute Weights section in the reduction settings and increase the weight for Vertex Color. This ensures the elimination of broken shader logic by prioritizing the placement of vertices where color data is most dense.
8. Use the “Small Prop” Tool for Bulk Optimization

If you have thousands of tiny assets (like bolts or pebbles), you don’t need complex LODs for each.

Tip: Use the Bulk Edit via Property Matrix to set a high reduction percentage (e.g., 90%) for LOD 1 across all small assets. This broad optimization leads to the elimination of memory waste on objects that contribute very little to the final image at a distance.