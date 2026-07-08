---
layout: default
title: MeshBuilder
---

<!-- ai-generation-failed -->

<h1>MeshBuilder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MeshBuilder/MeshBuilder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ClothingSystemRuntimeNv, Core, CoreUObject, DerivedDataCache, Engine, MeshBoneReduction, MeshBuilderCommon, MeshDescription, MeshReductionInterface, MeshUtilities, MeshUtilitiesCommon, RHI, RawMesh, RenderCore, SkeletalMeshDescription, SkeletalMeshUtilitiesCommon, StaticMeshDescription</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e for converting raw geometric data (stored in FMeshDescription) into optimized, engine-ready render formats. It serves as the primary bridge between high-level geometry representations and the specialized data structures required for Static Meshes, Skeletal Meshes, and Nanite.

This module handles the heavy lifting of the mesh “build” process, including generating tangents, calculating normals, and creating Level of Detail (LOD) versions. By providing a standardized pipeline for processing vertex and index data, it facilitates the elimination of manual mesh optimization tasks and ensures geometry is correctly formatted for the GPU.

Practical Usage Tips and Best Practices
1. Add to Editor Build Dependencies

The MeshBuilder module is primarily intended for use within the Unreal Editor or during the cooking process. When writing custom mesh generation tools or importers, you must include it in your Editor.Build.cs file. This practice ensures the elimination of linker errors when accessing classes like FStaticMeshBuilder.

2. Utilize FMeshDescription as the Input

Modern Unreal Engine mesh building relies on the FMeshDescription class as the intermediate format. Before calling the builder, you should populate this structure with your vertex, edge, and polygon data. This approach leads to the elimination of legacy “Direct Entry” methods that are less performant and harder to debug.

3. Parallelize with the Distributed Build System

The MeshBuilder module is designed to work with the engine’s background task system. When building thousands of meshes, ensure your code allows for asynchronous processing. Utilizing background threads for mesh builds facilitates the elimination of “UI Hangs” and significantly reduces total project cook times.

4. Configure Nanite Settings Properly

If you are building meshes intended for Nanite, the MeshBuilder logic must be passed specific Nanite build settings. Correctly configuring the FMeshNaniteSettings structure before the build begins leads to the elimination of artifacts and ensures the geometry properly utilizes the cluster-based rendering architecture.

5. Trigger Rebuilds only when Necessary

Rebuilding a mesh is a computationally expensive operation that involves regenerating collision, UVs, and tangents. Always check the bRequiresFullRebuild flag before invoking the builder. Managing build triggers intelligently assists in the elimination of redundant CPU cycles during iterative asset development.

6. Handle “Elimination” of Invalid Geometry

The MeshBuilder provides validation logic to find “degenerate” triangles or zero-area polygons. Running a validation pass before the build process leads to the elimination of “Invisible Mesh” bugs and shadow artifacts caused by malformed geometry that the GPU cannot render correctly.

7. Leverage for Custom Procedural Tooling

If you are developing a custom plugin that converts point cloud data or external CAD files into Static Meshes, call FStaticMeshBuilder::Build. This ensures that your generated assets follow the same optimization path as assets imported via FBX or USD, leading to the elimination of performance discrepancies between asset types.

8. Monitor Vertex and Triangle Budgets

The builder output logs provide detailed information about the final vertex and triangle counts after optimization. Reviewing these logs assists in the elimination of “over-budget” assets. If a mesh is too heavy, you can use the builder’s integration with the Mesh Reduction Interface to automatically simplify the geometry during the build phase.