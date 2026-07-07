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

logic and data structures for converting high-level mesh data into the optimized formats used by the engine for rendering and physics.

Description and Purpose

This module serves as the foundational “toolkit” for the engine’s various mesh builders (Static Mesh, Skeletal Mesh, and Nanite). Its primary purpose is to provide a standardized set of utilities for processing Mesh Descriptions—the raw, editable representation of geometry—into Render Data. It handles critical tasks such as vertex merging, coordinate system conversions, and tangent space calculation. By using this module, developers can eliminate the complexity of writing custom geometry processing logic when building specialized mesh importers or procedural generation tools.

Practical Usage Tips and Best Practices
Utilize FMeshBuildSettings for Consistency
When programmatically building a mesh, always use the FMeshBuildSettings struct provided by this module. This ensures your custom-generated geometry respects global engine standards (like “Recompute Normals” or “Remove Degenerates”), helping you eliminate visual artifacts in the final asset.
Leverage MikkTSpace for Tangents
The module includes helpers for the MikkTSpace algorithm, the industry standard for calculating tangents. Using this within your build pipeline is a best practice to eliminate “seams” and shading inconsistencies when your assets are viewed under different lighting conditions.
Process via FMeshDescriptionHelper
Instead of manually iterating over every triangle and vertex, use the helper classes in this module to perform bulk operations like coordinate swapping (e.g., converting from Y-up to Z-up). This specialized logic helps you eliminate common “flipped” or inverted geometry errors during import.
Manage Vertex Color and UV Channel Merging
Use the module’s merging utilities to combine duplicate vertices that share the same UV and Color data. This optimization is essential to eliminate redundant vertex data, which reduces the memory footprint and increases the rendering performance of your meshes.
Standardize Overlapping UV Detection
The module contains logic to detect and report overlapping UVs in lightmap channels. Incorporating these checks into your automated build pipeline allows you to eliminate “Lightmap Overlap” warnings that often result in splotchy or broken baked lighting.
Coordinate with the Mesh Description Module
MeshBuilderCommon is designed to work in tandem with the MeshDescription module. Always ensure your raw geometry is correctly formatted as a UMeshDescription before passing it to the builder helpers to eliminate crashes caused by null pointers or invalid geometry references.
Optimize for Thread-Safe Building
The functions in this module are generally designed to be thread-safe to support the engine’s asynchronous mesh building. When calling these utilities from a background thread, ensure you are not modifying the source UObject to eliminate race conditions during the build process.
Verify Material Slot Index Mapping
Use the common builder utilities to validate that your mesh sections correctly map to their intended material slots. Proper validation at the builder level helps you eliminate “Default Material” fallback issues where parts of your mesh appear as a grey checkerboard pattern in the level.