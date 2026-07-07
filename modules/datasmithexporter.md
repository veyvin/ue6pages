---
layout: default
title: DatasmithExporter
---

<!-- ai-generation-failed -->

<h1>DatasmithExporter</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Datasmith/DatasmithExporter/DatasmithExporter.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, DatasmithCore, DirectLink, FreeImage, InputCore, MeshDescription, MessagingCommon, Projects, RawMesh, Slate, SlateCore, StandaloneRenderer, StaticMeshDescription</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

h SDK. It provides the low-level functionality required to take an in-memory scene representation and write it to disk as a .udatasmith file, along with its associated assets (meshes, textures, and materials).

While DatasmithCore is used to build the scene hierarchy (actors, metadata, and properties), the DatasmithExporter module handles the actual serialization and the conversion of source assets into a format that the Unreal Engine Datasmith Importer can process. It is the primary tool for developers building custom “Datasmith Export” plugins for external CAD, BIM, or DCC applications.

1. Follow the Two-Step Export Process

The Datasmith SDK is designed to work in two distinct phases.

Best Practice: First, use DatasmithCore to parse your host application’s scene and construct an IDatasmithScene. Only once the scene graph is fully built should you pass it to the DatasmithExporter to write the files. This separation allows you to modify the scene in memory—such as adding metadata or renaming actors—without affecting the original source file.
2. Maintain Data Granularity

One of Datasmith’s core philosophies is to preserve the original structure of the source application.

Tip: Do not merge objects or reduce polygon counts during the export phase. The DatasmithExporter works best when it receives granular data. It is much more efficient to handle merging, LOD generation, and optimization inside Unreal Engine (using Visual Dataprep or PCG) where the user has better control over the final result.
3. Leverage Metadata for Automation

Datasmith allows you to attach arbitrary key-value pairs to any actor in the scene.

Best Practice: Export as much architectural or engineering data as possible (e.g., “Manufacturer,” “Cost,” “Material Type”) as Datasmith Metadata. When the file is imported into Unreal, this metadata can be used by Python scripts or Blueprint “OnImport” delegates to automatically assign gameplay logic, tag objects for elimination, or setup complex material overrides.
4. Handle Textures and Power-of-Two Requirements

External CAD programs often use non-standard texture resolutions that can cause performance issues in real-time engines.

Tip: Use the DatasmithExporter utility functions to reformat and resize textures. Ensure that textures are converted to “Power of Two” dimensions (e.g., 1024x1024) during the export process. This ensures that the Unreal Engine can properly generate Mipmaps and compress the textures for the GPU.
5. Utilize the Datasmith Log for User Feedback

When an export fails or encounters a corrupt asset, the user needs to know why.

Best Practice: Use the Datasmith_LogWarning and Datasmith_LogError commands provided by the exporter’s logging interface. These messages are displayed in the Datasmith Messages window, allowing the user to identify specific objects in their source application that are causing issues before they are even imported into the engine.
6. Implement DirectLink for Live Iteration

In addition to file-based exports, the module supports Datasmith DirectLink.

Tip: Instead of requiring users to manually export and import files, use the DirectLink API to send scene updates over the local network. This allows for a “Live Link” style workflow where changes in the source application (like moving a wall or changing a material) are reflected in the Unreal Editor in real-time.
7. Manage Resource Lifecycles to Prevent Memory Leaks

Exporting large scenes (like entire city districts or aircraft carriers) can consume significant amounts of RAM.

Constraint: After calling DatasmithExporter::Export(), you must explicitly destroy the in-memory scene representation to free up resources. Failing to eliminate the IDatasmithScene object after a successful export can lead to memory exhaustion in the host application, especially during batch export operations.
8. Use Path Aliasing for Portable Exports

When exporting assets like textures, the paths written into the .udatasmith file should be relative or correctly aliased.

Best Practice: Ensure that the “Assets” folder is created alongside the .udatasmith file. The exporter should write all converted meshes and textures into this folder. This makes the exported package portable, allowing it to be moved between different machines or version control systems without breaking the reference links during the import process.