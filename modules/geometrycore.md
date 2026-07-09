---
layout: default
title: GeometryCore
---


<h1>GeometryCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/GeometryCore/GeometryCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

onal geometry in Unreal Engine. It is distinct from the standard rendering-focused StaticMesh system, providing a high-performance library for mesh manipulation, geometric algorithms, and spatial queries. It serves as the underlying engine for Modeling Mode, Geometry Scripting, and the PCG (Procedural Content Generation) framework, handling complex tasks like mesh booleans, simplification, and hole filling.

Practical Usage Tips & Best Practices
1. Use FDynamicMesh3 for Topological Edits

Standard Unreal meshes (like FMeshDescription) are designed for static data. If your logic involves frequently adding or removing vertices and triangles, use UE::Geometry::FDynamicMesh3.

Best Practice: Use this class for any procedural generation that requires high-speed connectivity updates. Its internal pointer-free index structure ensures the elimination of the performance overhead typically associated with complex topological changes.
2. Leverage TMeshAABBTree3 for Spatial Queries

Standard Unreal raycasts rely on the physics scene (Chaos). If you need to perform high-precision ray-mesh intersections or find the nearest point on a raw geometric surface without a physics proxy, use the AABB Tree.

Tip: Construct a TMeshAABBTree3 for your mesh. This specialized spatial data structure allows for the elimination of heavy physics dependencies when performing purely geometric analysis or surface-following logic.
3. Understand Attribute Overlays

In GeometryCore, UVs, Normals, and Colors are stored in “Overlays” rather than simple arrays. This allows a single vertex to have multiple UV coordinates (for seams) or multiple normals (for hard edges).

Best Practice: Always use the Attributes() accessor to manage UVs. Proper use of the FDynamicMeshAttributeSet results in the elimination of visual artifacts like “broken” textures or incorrect lighting at mesh seams.
4. Prioritize Thread-Safe Geometry Processing

Most algorithms in GeometryCore, such as FMeshSimplification or FMeshSelfUnion, are designed to be thread-neutral.

Tip: Perform heavy geometric operations inside a background Task. Since FDynamicMesh3 is a standard C++ object and not a UObject, it can be processed safely outside the game thread, leading to the elimination of frame-rate hitches during complex generation.
5. Compact Indices After Massive Deletions

Deleting many triangles in FDynamicMesh3 creates “holes” (invalid indices) in the internal arrays. While the mesh remains functional, these holes can waste memory and slow down iterations.

Best Practice: Call Mesh.CompactIndices() after finishing a series of deletions. This re-indexes the mesh to be contiguous, which assists in the elimination of wasted memory and improves cache locality for subsequent algorithms.
6. Use TPointHashGrid3 for Proximity Searches

If you need to find all vertices within a certain radius (e.g., for a “welding” operation), a linear search is too slow.

Tip: Use TPointHashGrid3 to spatially bin your vertices. This ensures the elimination of \(O(n^2)\) complexity, making proximity-based operations significantly faster as the vertex count increases.
7. Efficient Conversion via MeshDescription

To turn your geometric data into an actual asset, you must convert it to a MeshDescription or a UStaticMesh.

Best Practice: Use the FMeshDescriptionToDynamicMesh and FDynamicMeshToMeshDescription converters. Using these specialized utility classes ensures the elimination of data loss (like tangent or normal information) during the transfer between the modeling and rendering systems.
8. Verify Mesh Integrity with Validations

Complex procedural edits can sometimes result in “degenerate” geometry (e.g., zero-area triangles or non-manifold edges) that crashes subsequent algorithms.

Tip: Use FDynamicMesh3::CheckValidity() during development. Detecting and fixing these structural issues early facilitates the elimination of hard-to-trace crashes in the more complex mesh-processing pipelines.