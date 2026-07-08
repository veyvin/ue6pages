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

part of the Datasmith SDK. Its primary purpose is to act as a “facade”—a simplified, stable programming interface—that allows third-party 3D applications (like CAD software, BIM tools, or custom DCCs) to export their data into the .udatasmith format.

Unlike most Unreal modules, this is often used outside the main Unreal Engine process to build standalone export plugins. It abstracts the complexity of the underlying DatasmithCore, providing a clean way to define meshes, materials, lights, and hierarchies for consumption by the Unreal Editor.

Practical Usage Tips and Best Practices
1. Decouple from the Unreal Runtime

The DatasmithFacade is designed to be linked into external applications. When building your exporter, treat it as a standalone SDK. This ensures the elimination of heavy engine dependencies in your external tool, allowing your plugin to remain lightweight and fast to load within the host application.

2. Master the Scene Element Hierarchy

Every export begins with an FDatasmithFacadeScene. Use the “Facade” versions of elements (e.g., FDatasmithFacadeActor, FDatasmithFacadeMesh) to build your scene tree. Always ensure your root actors are properly attached to the scene to ensure the elimination of “orphaned” objects that won’t appear upon import.

3. Handle Coordinate System Conversion

Most CAD and 3D tools use different coordinate systems (e.g., Y-Up vs. Unreal’s Z-Up). The Facade module provides utilities to handle these transforms. Performing the conversion during the export phase leads to the elimination of “sideways” models and manual rotation fixes inside the Unreal Editor.

4. Optimize Mesh Instancing

If your source application has repeated objects (like bolts in a machine or chairs in a room), define a single FDatasmithFacadeMeshElement and create multiple FDatasmithFacadeActor instances that reference it. This is a critical best practice for the elimination of massive file sizes and redundant memory usage in Unreal.

5. Leverage Metadata for Automation

Use FDatasmithFacadeMetaData to attach custom key-value pairs to your actors. This data is preserved during import and can be accessed by Blueprints or Python scripts in Unreal. This enables the elimination of manual setup by allowing you to drive gameplay logic or material swapping based on the source app’s attributes.

6. Manage Texture Pathing and Formats

When defining materials via FDatasmithFacadeMaterial, ensure you provide absolute paths to textures or ensure they are in a common directory. The Facade helps package these, but pre-converting non-standard formats to PNG or JPEG before export will assist in the elimination of texture import failures.

7. Explicit Memory Management

Since this module is often used in a raw C++ environment outside of Unreal’s Garbage Collector, you must be diligent with object lifetimes. Follow the SDK’s patterns for “Add” and “Remove” operations carefully to ensure the elimination of memory leaks within the host application’s process.

8. Use the Built-in Validator

Before calling the Export function, use the SDK’s validation utilities to check for invalid names, circular dependencies, or missing assets. Catching these errors during the export phase facilitates the elimination of frustrating “Import Failed” errors for the end-user.