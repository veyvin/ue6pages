---
layout: default
title: DatasmithFacadeCSharp
---

<!-- ai-generation-failed -->

<h1>DatasmithFacadeCSharp</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithFacadeCSharp/DatasmithFacadeCSharp.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DatasmithCore, DatasmithExporter, DatasmithExporterUI, DatasmithFacade, UdpMessaging</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

# or .NET (such as Revit, Rhino, or Navisworks). The module allows you to construct a Datasmith Scene in memory—including meshes, materials, lights, and metadata—and then export that scene into a .udatasmith file format that Unreal Engine can import.

Practical Usage Tips and Best Practices
1. Manage Unmanaged Memory (IDatasmithElement)

Since this module wraps a C++ SDK, many of the C# objects are just handles to unmanaged C++ memory. When you create elements like FDatasmithFacadeActor or FDatasmithFacadeMesh, you must be mindful of their lifecycle. Always ensure that the parent FDatasmithFacadeScene is kept in scope as long as you are adding elements to it, as the scene typically owns the underlying data.

2. Coordinate System Conversion

Design applications often use different coordinate systems (e.g., Right-handed Z-up vs. Unreal’s Left-handed Z-up). The Facade provides utility functions for transformation. A best practice is to perform all your logic in the source application’s coordinate space and apply a single global conversion at the root or during the export step to ensure the orientation in Unreal matches the source exactly.

3. Use the Mesh Exporter for Geometry

To export geometry, use the FDatasmithFacadeMeshElement and the accompanying FDatasmithFacadeMeshExporter. Do not attempt to manually write geometry data. The exporter handles the complex task of converting your application’s vertex and index buffers into the specialized format that Datasmith requires, ensuring compatibility with Unreal’s vertex attributes.

4. Leverage Metadata via Tags

One of the most powerful features of Datasmith is the ability to carry “User Data” from the source app into Unreal. Use FDatasmithFacadeMetaDataElement to attach key-value pairs to your actors. This allows technical artists in Unreal to use Python or Blueprints to automate tasks (like assigning gameplay tags or collision profiles) based on the metadata you exported.

5. Material Schema Mapping

Instead of trying to replicate complex shaders, map your source application’s materials to the Datasmith Material PBR schema. This module allows you to define Base Color, Roughness, and Metallic properties. Unreal’s Datasmith importer will then automatically generate a matching Master Material instance, which is much more efficient than creating unique shaders for every object.

6. Optimize via Texture Reuse

If multiple objects in your source scene use the same texture map, ensure you only create one FDatasmithFacadeTextureElement and reference it multiple times. This is a critical best practice for the elimination of redundant texture memory and significantly reduces the size of the exported .udatasmith folder and the eventual Unreal project size.

7. Handle Scene Cleanup and Elimination

When the export process is complete or if the user cancels the operation, you must explicitly call the Shutdown or cleanup methods provided by the Facade. Failing to do so can leave large chunks of unmanaged memory allocated in the host application’s process. Proper elimination of these temporary data structures prevents the host CAD software from slowing down or crashing after multiple export attempts.

8. Validate with the Datasmith SDK Samples

Before building a full-scale exporter, refer to the sample C# projects provided in the Unreal Engine GitHub repository (under Source/Programs/Enterprise/Datasmith/DatasmithSDK). These samples demonstrate the correct order of initialization for the Facade and show how to properly structure the scene hierarchy for the most reliable import results.