---
layout: default
title: RawMesh
---

<!-- ai-generation-failed -->

<h1>RawMesh</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/RawMesh/RawMesh.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

structure. It provides a “flat,” array-based representation of a 3D mesh, containing raw data for vertex positions, wedge indices, UV coordinates, normals, tangents, and material assignments.

Historically, this was the primary way to pass mesh data to the engine’s static mesh builder. In modern versions of Unreal Engine, it is largely considered a legacy module, having been succeeded by the more robust MeshDescription API. However, it remains in the engine to support older importers and simplified procedural mesh pipelines where a complex half-edge data structure is not required.

Practical Usage Tips and Best Practices
1. Add “RawMesh” to Your Build.cs

To use FRawMesh in your C++ code, you must explicitly include the module in your project’s dependency list. Failure to do this will result in linker errors for the FRawMesh struct.

C#
	// Inside YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "RawMesh" });

	```

	 

	#### 2. Understand the "Wedge" vs "Vertex" Concept

	In `RawMesh`, `VertexPositions` contains unique spatial points, while `WedgeIndices` and other attribute arrays (UVs, Colors) are indexed by "wedges." A wedge represents a vertex as seen by a specific face. This is how you handle "hard edges" or UV seams—multiple wedges can share the same vertex position but have different normals or UVs.

	 

	#### 3. Transition to MeshDescription for Modern Features

	If you are starting a new project that involves complex mesh manipulation, prefer the `MeshDescription` module over `RawMesh`. `MeshDescription` is the foundation for Nanite and the Modeling Mode tools. `RawMesh` is essentially converted to a `MeshDescription` internally during the build process anyway.

	 

	#### 4. Populate FaceMaterialIndices for Multi-Material Support

	To assign different materials to different parts of your mesh, populate the `FaceMaterialIndices` array. Each entry corresponds to a triangle (face) and holds an integer index matching the material slot in your `UStaticMesh`. If this array is empty or mismatched, the entire mesh will default to a single material slot.

	 

	#### 5. Verify Array Lengths Before Building

	The engine expects specific mathematical relationships between the arrays in an `FRawMesh`. For example, `WedgeIndices.Num()` must be exactly `FaceMaterialIndices.Num() * 3`. If your array counts are inconsistent, `StaticMesh::Build()` will likely trigger an assertion or produce a corrupted mesh.

	 

	#### 6. Leverage for Custom Asset Importers

	`RawMesh` is excellent for writing simple, custom file importers (e.g., a proprietary CAD format or a custom JSON mesh). Because it is a "flat" data structure (just `TArray`s of floats and ints), it is much easier to populate from an external file stream than more complex topological structures.

	 

	#### 7. Use Scoped Locking for Bulk Data

	When saving `RawMesh` data into a `UStaticMesh` asset, you typically interact with `SourceModels`. Ensure you use `SourceModel.RawMeshBulkData->SaveRawMesh(YourRawMesh)` to correctly serialize the data into the asset's bulk storage.

	 

	#### 8. Handle Tangents and Normals Properly

	You can choose to provide your own tangents and normals or leave the arrays empty and set `bRecomputeNormals = true` in the build settings. If you provide your own, ensure they are normalized; the `RawMesh` module does not automatically normalize input vectors, which can lead to broken lighting on the final asset.
Copy code
2. Understand the “Wedge” vs “Vertex” Concept

In RawMesh, VertexPositions contains unique spatial points, while WedgeIndices and other attribute arrays (UVs, Colors) are indexed by “wedges.” A wedge represents a vertex as seen by a specific face. This is the primary method for the elimination of UV seams or hard edges, as multiple wedges can share a vertex position while maintaining unique normals or UVs.

3. Transition to MeshDescription for Modern Features

If you are starting a new project involving complex mesh manipulation, prefer the MeshDescription module. MeshDescription is the foundation for Nanite and the Modeling Mode tools. Using the modern API leads to the elimination of compatibility issues with newer engine features, as RawMesh is converted to MeshDescription internally during the build process anyway.

4. Populate FaceMaterialIndices for Multi-Material Support

To assign different materials to different parts of your mesh, you must populate the FaceMaterialIndices array. Each entry corresponds to a triangle (face). Correctly mapping these indices facilitates the elimination of material assignment errors, ensuring the mesh correctly utilizes multiple material slots in the UStaticMesh.

5. Verify Array Lengths Before Building

The engine expects specific mathematical relationships between the arrays. For example, WedgeIndices.Num() must be exactly FaceMaterialIndices.Num() * 3. Ensuring these counts are consistent leads to the elimination of engine crashes or assertions during the StaticMesh::Build() process.

6. Leverage for Simple Custom Asset Importers

RawMesh is excellent for writing simple, custom file importers for proprietary formats. Because it is a “flat” data structure (just TArrays of floats and ints), it is much easier to populate from an external file stream than more complex topological structures. This simplicity assists in the elimination of development friction for basic data-import tools.

7. Use Scoped Locking for Bulk Data

When saving RawMesh data into a UStaticMesh asset, you typically interact with SourceModels. Ensure you use SourceModel.RawMeshBulkData->SaveRawMesh(YourRawMesh) to correctly serialize the data into the asset’s bulk storage. Proper serialization leads to the elimination of data loss when saving or moving assets between project versions.

8. Handle Tangents and Normals Properly

You can choose to provide your own tangents and normals or leave those arrays empty and set bRecomputeNormals = true in the build settings. If you provide your own, ensure they are normalized; the RawMesh module does not automatically normalize input vectors. This careful handling facilitates the elimination of broken lighting and “black face” artifacts on the final asset.