---
layout: default
title: DatasmithCore
---

<!-- ai-generation-failed -->

<h1>DatasmithCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Datasmith/DatasmithCore/DatasmithCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DirectLink, Json, MeshDescription, RawMesh, StaticMeshDescription, XmlParser</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

h framework. It provides the C++ API used to construct and manipulate a universal scene representation that Unreal Engine can understand.

What it is and What it’s used for

Located in the Enterprise section of the engine source, DatasmithCore is responsible for the in-memory representation of a scene during the translation process. It acts as an abstraction layer between third-party software (like 3ds Max, Revit, or Rhino) and Unreal Engine’s internal asset formats.

Primary uses include:

Scene Construction: Defining the hierarchy of a scene using IDatasmithScene, including actors, meshes, lights, and materials.
Data Translation: Providing a common language to map third-party properties (e.g., V-Ray materials or CAD metadata) into Unreal-compatible structures.
Asset Definition: Creating “Elements” such as IDatasmithMeshElement or IDatasmithLightSpaceElement which are later compiled into real Unreal assets.
Metadata Management: Attaching custom key-value pairs to objects that persist through the import process.
Practical Usage Tips and Best Practices
1. Use the “Facade” for Simplified Development

If you are building a custom exporter, use the DatasmithFacade (built on top of DatasmithCore). The Facade provides a higher-level, more stable C++ interface that handles much of the boilerplate code required to initialize scenes and manage memory, making it easier to maintain across engine versions.

2. Ensure Unique Element Names

Every element in a DatasmithCore scene (meshes, materials, textures) must have a unique name. The engine uses these names as keys during the import process to prevent duplication. A best practice is to use a combination of the source application’s internal GUID and the object name to ensure uniqueness.

3. Efficient Mesh Handling with IDatasmithMeshElement

Avoid creating a new IDatasmithMeshElement for every object in your scene if they share the same geometry. Instead, define one mesh element and create multiple IDatasmithMeshActorElement instances that reference it. This enables the engine to use Instancing, significantly reducing memory usage.

4. Leverage Metadata for Pipeline Automation

DatasmithCore allows you to attach metadata to any element via IDatasmithMetaDataElement. Use this to pass custom information from the source app (like “Department: Architecture” or “Cost: 500”). This data can then be read by Visual Dataprep or Editor Utility Blueprints to automate asset placement or material assignment.

5. Clean Up Materials with the Overriding Logic

DatasmithCore supports a robust material override system. Instead of creating thousands of unique materials, try to identify common parameters and use Datasmith Material Instances. This allows the engine to create a single Master Material, which is much better for rendering performance and shader compilation times.

6. Coordinate Systems and Scaling

Different CAD/BIM applications use different coordinate systems (Y-up vs. Z-up) and units (cm vs. mm). Use the DatasmithCore utility functions to handle the conversion of transforms early in the scene construction. This ensures the elimination of “flipped” meshes or incorrectly scaled objects upon import.

7. Define Actor Hierarchies Logically

When building the IDatasmithScene, mirror the hierarchy of the source application using IDatasmithActorElement. A clean hierarchy in DatasmithCore directly translates to a clean Outliner in Unreal, which is essential for level designers who need to navigate complex architectural or mechanical assemblies.

8. Validation Before Export

Before passing the scene to the DatasmithExporter, run a validation pass on your IDatasmithScene. Check for null pointers, empty mesh references, or invalid texture paths. Implementing a simple “Sanity Check” within your usage of DatasmithCore prevents the exporter from crashing or producing corrupted .udatasmith files.