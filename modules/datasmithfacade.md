---
layout: default
title: DatasmithFacade
---

<!-- ai-generation-failed -->

<h1>DatasmithFacade</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Datasmith/DatasmithFacade/DatasmithFacade.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DatasmithCore, DatasmithExporter, DirectLink, Imath</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rom a non-Unreal environment.

It acts as a wrapper around Datasmith’s internal data structures, allowing external software to describe scene hierarchies, materials, and geometry in a format that Unreal Engine can perfectly reconstruct.

Practical Usage Tips and Best Practices
1. Implement Instancing via Mesh Actors

The Facade distinguishes between a FDatasmithFacadeMeshElement (the geometry data) and a FDatasmithFacadeMeshActor (the instance in the world). To optimize file size and engine performance, define a mesh once as a MeshElement and create multiple MeshActor instances that reference it. This ensures the elimination of redundant geometry data in your export.

2. Standardize Coordinate Systems Early

External applications often use different coordinate systems (e.g., Y-up or different units like inches). Use the Facade’s transformation methods to convert your source data to Unreal’s LHS Z-up (centimeters) system during the export process. Consistent conversion results in the elimination of spatial orientation errors during import.

3. Use Stable Unique Names

Every element (actors, materials, meshes) requires a name. Use persistent, unique identifiers from your source application, such as a GUID. This is critical for re-import workflows; if names change between exports, Unreal will treat them as new objects, leading to the elimination of any manual overrides or material assignments a user has made in the engine.

4. Batch Metadata via UserData

Datasmith allows you to attach arbitrary key-value pairs to actors using FDatasmithFacadeMetaDataElement. Use this to preserve BIM data or manufacturing specs. Preserving this data allows for the elimination of “information silos,” enabling technical artists to automate processing in Unreal based on these metadata tags.

5. Handle Material IDs Carefully

If a mesh uses multiple materials, you must define FDatasmithFacadeMaterialID elements. Ensure the ID assigned to the polygon groups in your source mesh matches the ID defined on the MeshActor in the Facade. Correct mapping leads to the elimination of default “checkerboard” materials on complex imported objects.

6. Export Textures with Power-of-Two Dimensions

While Datasmith can handle various image formats, providing textures that follow Unreal’s requirements is best. If your source application uses non-standard resolutions, resize them during the export phase to ensure the elimination of mip-mapping issues or memory waste during the Unreal import.

7. Validate Assets Before Finalizing

Always check the return values and validity of your pointers when calling AddMesh, AddMaterial, or AddActor. Passing null pointers or invalid geometry data can result in a corrupted .udatasmith file. Validating source data before passing it to the Facade ensures the elimination of frustrating import crashes.

8. Leverage the Facade for “Direct Link”

The Facade module is the foundation for Datasmith Direct Link. If you are building a live-sync tool, use the Facade to manage the incremental synchronization of the scene. This allows for the elimination of the “Export-Import” loop, providing a real-time bridge between the source software and Unreal Engine.