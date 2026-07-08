---
layout: default
title: MeshDescription
---

<!-- ai-generation-failed -->

<h1>MeshDescription</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MeshDescription/MeshDescription.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DerivedDataCache</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ting 3D geometry within Unreal Engine. It serves as a universal intermediary between raw geometric data (vertices, edges, polygons) and engine-specific assets like StaticMesh or SkeletalMesh.

Introduced to replace the legacy “Raw Mesh” format, it provides a structured, attribute-based API that allows developers to manipulate geometry with high precision. It is the backbone for the engine’s modeling tools, the Geometry Scripting plugin, and the Datasmith import pipeline, helping you eliminate the complexity of manually managing triangle indices and vertex buffers.

Practical Usage Tips and Best Practices
Use Attribute Getters/Setters for Metadata
MeshDescription uses a generic attribute system. Instead of accessing variables directly, use TAttributesSet. This allows you to store custom data on vertices or polygons (like unique IDs or material indices), helping you eliminate the need for external side-tables to track metadata during geometry processing.
Follow the Element Hierarchy
Understand the ownership flow: Vertex -> VertexInstance -> Polygon -> PolygonGroup.
A Vertex is a position in 3D space.
A VertexInstance holds data like UVs and Normals. Using VertexInstances for split-normals/UV seams is critical to eliminate visual smoothing errors at hard edges.
Perform Bulk Operations with ‘Reserved’ Memory
When generating large meshes via C++, use the Reserve functions for vertices, edges, and polygons before adding them. This prevents multiple reallocations of the underlying arrays, which helps you eliminate CPU hitches during complex procedural mesh generation.
Convert to StaticMesh for Rendering
FMeshDescription is a data container, not a renderable object. To see your mesh in-game, you must use UStaticMesh::CreateMeshDescription and BuildFromMeshDescription. This workflow ensures that Nanite and LOD generation are triggered, helping you eliminate performance issues associated with raw dynamic rendering.
Leverage MeshDescriptionOperations for Cleanup
Include the MeshDescriptionOperations module in your Build.cs to access utility functions like FStaticMeshOperations::ComputeTangentsAndNormals. Automating these calculations helps you eliminate “black facets” or incorrect lighting caused by missing tangent space data.
Sanitize Indices During Elimination
When removing geometry (the “elimination” of a face or vertex), use the DeletePolygon or DeleteVertex methods. Be aware that these do not automatically “compact” the IDs. If you need a contiguous index range, call CompactIndices afterward to eliminate “null holes” in your data arrays.
Handle Coordinate System Conversions Early
If importing data from external libraries (like Blender or CAD software), use the MeshDescription API to flip the Y-axis or scale the vertices immediately. Handling this at the data level helps you eliminate the need for “Correction Transforms” on your Actors later.
Utilize for Procedural Content (PCG)
MeshDescription is the ideal format for PCG and modeling tools because it is “topology-aware.” Unlike a simple triangle soup, it knows which edges are shared, making it easy to implement logic like “extrude” or “bevel.” Using this module for procedural tools helps you eliminate overlapping geometry and “Z-fighting” issues.