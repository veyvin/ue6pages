---
layout: default
title: MeshMergeUtilities
---

<!-- ai-generation-failed -->

<h1>MeshMergeUtilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MeshMergeUtilities/MeshMergeUtilities.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

consolidate multiple separate meshes and materials into a single, optimized asset.

Description and Purpose

This module provides the core logic behind the Merge Actors tool and the Proxy Geometry system. Its primary purpose is to reduce the performance overhead of complex scenes by “flattening” geometry and baking unique materials into a single texture atlas. It is a critical component for optimization workflows, especially when creating HLODs (Hierarchical Levels of Detail) for large environments. By utilizing this module, developers can eliminate excessive draw calls caused by hundreds of small objects, significantly improving the frame rate in dense levels.

Practical Usage Tips and Best Practices
Implement via IMeshMergeUtilities Interface
In C++, do not try to call internal functions directly. Instead, access the module through IMeshMergeUtilities& MeshMergeUtilities = FModuleManager::Get().LoadModuleChecked<IMeshMergeUtilities>("MeshMergeUtilities");. This is the safest way to eliminate linker errors and access high-level functions like MergeComponentsToStaticMesh.
Reduce Draw Calls with “Bake Materials”
When merging actors, enable the material baking options. This module will take all unique textures from the source actors and combine them into a single “Atlas.” This allows the engine to render the entire merged group in one pass, helping you eliminate the performance bottleneck of having dozens of unique material IDs.
Use for “Proxy Geometry” in Distance
For background objects that the player will never reach, use the Proxy Method (available through this module). This creates a simplified “shell” of the objects rather than a precise merge. This is a best practice to eliminate thousands of unnecessary internal triangles that are never seen by the camera.
Optimize Voxel Size for Memory
When generating proxy meshes, the “Voxel Size” determines the resolution of the merged shell. Setting this too low can cause memory spikes and long bake times. Start with a higher value and lower it incrementally to eliminate “Out of Memory” crashes during the merge process.
Fix Hard Edges with Normal Calculation
If your merged mesh looks “facetted” or blocky, adjust the Hard Edge Angle setting within the merge options. Fine-tuning this threshold helps you eliminate unsightly shading artifacts where smooth surfaces meet at sharp angles.
Preserve Vertex Colors for VFX
If your source meshes use Vertex Colors for wind animation or masking, ensure “Keep Vertex Colors” is enabled in the settings. This ensures the merged result retains that data, helping you eliminate the issue of “static” or broken vegetation after a merge.
Automate via Editor Utility Blueprints
You can expose MeshMergeUtilities logic to Editor Utility Blueprints to batch-process thousands of assets. Automating the consolidation of “scatter” assets (like rocks or debris) is the most efficient way to eliminate manual optimization work during the final stages of production.
Check for Overlapping UVs Post-Merge
After a merge, the module generates a new UV set (usually in Channel 1) for lightmaps. Always verify this in the Static Mesh Editor to eliminate “Overlapping UV” errors, which can cause dark splotches or artifacts when using baked Lighting.