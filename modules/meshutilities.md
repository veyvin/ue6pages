---
layout: default
title: MeshUtilities
---

<!-- ai-generation-failed -->

<h1>MeshUtilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MeshUtilities/MeshUtilities.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ClothingSystemRuntimeCommon, Core, CoreUObject, EditorFramework, Engine, GraphColor, HierarchicalLODUtilities, Landscape, LevelEditor, MaterialUtilities, MeshBoneReduction, MeshBuilderCommon, MeshDescription, MeshUtilitiesCommon, MeshUtilitiesEngine, Persona, PropertyEditor, RHI, RawMesh, RenderCore, SkeletalMeshUtilitiesCommon, Slate, SlateCore, StaticMeshDescription, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the heavy lifting of geometry processing. While MeshDescription stores the data, MeshUtilities provides the algorithms to manipulate it, including generating Levels of Detail (LODs), computing tangents and normals, creating proxy meshes, and merging multiple meshes into a single asset.

It serves as the backend for the “Build” process of Static and Skeletal Meshes. By leveraging its interfaces, developers can automate complex optimization tasks, helping to eliminate manual cleanup work and ensuring that geometry is always performant and “render-ready” for the GPU.

Practical Usage Tips and Best Practices
Add to Editor Module Dependencies
Since this is an editor-only module, you must wrap your dependency in your Build.cs file. Use if (Target.bBuildEditor) to include "MeshUtilities". This ensures you eliminate linker errors when trying to package a “Shipping” build, as the module is stripped during the packaging process.
Access via the IMeshUtilities Interface
In C++, do not try to instantiate the class directly. Use FModuleManager::LoadModuleChecked<IMeshUtilities>("MeshUtilities") to get a reference to the interface. This standardized access helps you eliminate crashes caused by uninitialized modules during editor startup.
Automate LOD Generation
Use the GenerateLODs function to programmatically create lower-resolution versions of a mesh. By defining a FLODWeights struct, you can control the reduction percentage, helping you eliminate the need for artists to manually export five different versions of every rock or prop in a scene.
Compute Tangent Space for Proper Lighting
When generating procedural geometry, use the CalculateTangents and CalculateNormals utilities. Correct tangent space is vital for normal mapping; using these built-in functions helps you eliminate “seam” artifacts and inverted lighting that occur with incorrect vertex data.
Use Mesh Merging to Reduce Draw Calls
The module provides functions to merge several Static Mesh Actors into a single mesh. For small, recurring props like scattered debris, merging them helps you eliminate excessive draw calls, which is one of the most common performance bottlenecks in complex levels.
Leverage Proxy Mesh Creation
For distant background buildings or complex machinery, use the CreateProxyMesh utility. This function generates a simplified “shell” of the object and bakes the textures down. This helps you eliminate the high triangle counts of interior geometry that will never be seen from a distance.
Handle Vertex Color Re-mapping
When reducing a mesh, use the module’s re-mapping features to preserve vertex color data. This ensures that logic tied to vertex colors (like wind animation in foliage) continues to work on lower LODs, helping you eliminate “static” or broken animations on distant trees.
Sanitize Geometry Before Build
Before finalizing a mesh, use the utility’s “Remove Degenerate Triangles” logic. These are triangles with zero area that can cause rendering glitches; removing them helps you eliminate visual flickering and “nanite-unfriendly” geometry from your pipeline.