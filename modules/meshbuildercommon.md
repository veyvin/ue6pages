---
layout: default
title: MeshBuilderCommon
---

<!-- ai-generation-failed -->

<h1>MeshBuilderCommon</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MeshBuilderCommon/MeshBuilderCommon.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ides shared logic for generating and processing mesh data in Unreal Engine. It acts as the “bridge” between raw geometry descriptions (like FMeshDescription) and the final, render-ready data used by UStaticMesh or USkeletalMesh.

This module is essential for developers working on custom mesh importers, procedural geometry tools, or any system that needs to convert raw vertex/polygon data into optimized engine assets with proper tangents, normals, and LOD structures.

Practical Usage Tips & Best Practices
1. Use for FMeshDescription Translation

The modern Unreal mesh pipeline relies on FMeshDescription as a generic container. MeshBuilderCommon provides the utilities to translate this high-level description into the low-level buffers required by the engine.

Best Practice: Always use the builder classes (like FStaticMeshBuilder) provided by this module rather than trying to manually populate FStaticMeshLODResources. This ensures the elimination of data corruption and ensures all required vertex attributes are correctly initialized.
2. Leverage TMeshAttributes for Data Access

When processing geometry, you often need to access specific data like UVs, Normals, or Vertex Colors stored in the Mesh Description.

Tip: Use the attribute accessors defined in this module to retrieve specific data arrays. Properly using these typed accessors results in the elimination of “off-by-one” errors and casting issues when iterating over complex vertex data.
3. Optimize with BulkData for Large Meshes

For high-poly meshes, moving data from the builder to the asset can be slow due to memory allocations.

Best Practice: Utilize the BulkSerialize and raw memory copying functions found in this module’s helpers. This facilitates the elimination of redundant memory allocations during the “Build” phase, significantly speeding up import and procedural generation times.
4. Handle Tangent and Normal Generation

Calculating smooth normals and bitangents is computationally expensive and mathematically complex.

Tip: Use the common utility functions to calculate “MikkTSpace” tangents or smoothed vertex normals. Relying on these standardized algorithms leads to the elimination of visual “seams” and shading artifacts on your 3D models.
5. Integrate with the Nanite Builder

For UE5 projects, the mesh building process often involves preparing data for Nanite’s virtualized geometry.

Best Practice: Ensure your builder logic correctly flags the mesh for Nanite processing through the shared build settings. Proper integration ensures the elimination of “Nanite Fallback” issues where high-poly meshes fail to render correctly in the virtualized pipeline.
6. Thread-Safe Mesh Building

Mesh building is a CPU-intensive task that can hang the editor UI if performed on the Game Thread.

Tip: The builder logic in this module is designed to be run within AsyncTask or ParallelFor blocks. Offloading the geometry processing to worker threads results in the elimination of editor freezes during large asset imports or procedural world generation.
7. Manage Vertex Splitting and Welding

Raw meshes often contain redundant vertices or require splitting (duplicating) vertices at UV seams and hard edges.

Best Practice: Use the “Overlapping Vertices” helpers to identify which vertices can be welded and which must be split. Correct vertex management leads to the elimination of bloated vertex buffers and ensures your lighting and textures wrap correctly around corners.
8. Verify Build Settings and Versioning

The way meshes are built changes between engine versions (e.g., changes to UV precision or vertex format).

Tip: Check the FMeshBuildSettings struct before starting a build. Validating these settings against the current engine version ensures the elimination of “stale” mesh data that might not be compatible with newer rendering features like Lumen or Virtual Shadow Maps.