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

tility in Unreal Engine, providing high-performance decimation for both Static and Skeletal Meshes.

Description and Purpose

This module implements a Quadric Error Metrics (QEM) algorithm, which simplifies geometry by performing “edge collapses.” It calculates the visual impact of merging two vertices and prioritizes collapsing edges that result in the least amount of geometric distortion. Its primary purpose is the automatic generation of LODs (Levels of Detail) and the creation of Proxy Geometry. By utilizing this module, developers can eliminate excessive polygon counts in the distance, significantly improving rendering performance while preserving the overall silhouette of the original high-poly model.

Practical Usage Tips and Best Practices
Configure via LOD Group Presets
Instead of manually setting reduction percentages for every asset, use the LOD Group dropdown (e.g., LargeProp, SmallProp) in the Static Mesh Editor. This applies pre-configured reduction settings from the module, which is a best practice to eliminate inconsistency across your project’s assets.
Protect Seams with Lock Free Edges
When simplifying modular assets or character parts (like a head and body), enable the Lock Free Edges option. This tells the module not to move vertices on the open boundaries of a mesh, helping you eliminate visible “cracks” or gaps that appear when two adjacent meshes are reduced differently.
Set Importance via Bone Weighting
For Skeletal Meshes, you can specify “Important Bones” in the reduction settings. The module will be less aggressive with geometry weighted to those bones (like the face or hands). This allows you to eliminate “cubist” or distorted faces while still reducing the poly count on the character’s torso and limbs.
Use the r.MeshReductionModule Console Variable
If you have third-party reduction tools installed, verify which module is active by typing r.MeshReductionModule in the console. Ensuring this is set to QuadricMeshReduction is the fastest way to eliminate confusion if the LOD generation behavior changes unexpectedly after a plugin update.
Balance Triangle vs. Vert Budgets
The module allows you to target either a specific Triangle Percentage or a Max Vertex Count. For mobile development, targeting a vertex count is often more effective to eliminate transform-bound performance bottlenecks on limited mobile GPUs.
Leverage for HLOD Generation
When using the Hierarchical LOD (HLOD) system, the QuadricMeshReduction module is used to simplify the combined cluster of meshes. Use the “Proxy Mesh” settings to tune the simplification strength, which helps you eliminate the massive draw call overhead of distant cities or forests.
Adjust Silhouette and Texture Importance
In the Reduction Settings, you can increase the Silhouette Quality or Texture Importance sliders. Increasing these values tells the algorithm to prioritize the outer shape and UV mapping over internal geometric density, helping you eliminate “texture swimming” or wobbling on simplified meshes.
Verify Results with the LOD Coloration View
Use the Mesh LOD Coloration view mode in the viewport to see exactly when the engine switches to a reduced mesh. If the pop is too noticeable, you can adjust the “Screen Size” threshold in the module’s settings to eliminate visual popping during gameplay.