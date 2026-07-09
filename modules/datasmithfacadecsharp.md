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

asmith SDK (Datasmith Facade). It is primarily used by developers building external 3D applications or plugins (such as those for Revit, Rhino, or custom CAD tools) who want to export their data into the .udatasmith format using C# instead of C++. It acts as a bridge, allowing managed code to interface with the high-performance C++ Datasmith Core to build scenes, manage meshes, and handle material definitions.

Practical Usage Tips & Best Practices
1. Understand the Wrapper Architecture

Since this is a C# wrapper for a C++ SDK, most classes (like FDatasmithFacadeScene) are thin layers over native pointers.

Best Practice: Be mindful of object lifecycles. Ensure that you properly initialize and dispose of scene objects. Failure to manage the scope of these objects can lead to the elimination of memory stability in your host application.
2. Efficient Mesh Data Handling

Exporting large geometry sets can be memory-intensive in a managed environment.

Tip: When using FDatasmithFacadeMesh, pass large arrays of vertex and index data in chunks if possible. Use the SDK to convert your host application’s coordinate system to Unreal’s (Z-up, Left-handed) during the export phase to ensure the elimination of orientation issues upon import.
3. Standardize Material and Texture Names

The Datasmith import process in Unreal Engine relies on unique identifiers to prevent duplication.

Best Practice: Assign consistent, unique names to FDatasmithFacadeMaterialID and textures. If you export two different objects with the same material name but different properties, Datasmith may overwrite one, leading to the elimination of visual accuracy in the final Unreal scene.
4. Leverage the Scene Hierarchy

Datasmith allows you to recreate complex parent-child relationships using FDatasmithFacadeActor.

Tip: Mirror your host application’s hierarchy as closely as possible using nested actors. This makes the resulting Unreal level much easier for designers to navigate and facilitates the elimination of “flat” scenes where every object is at the root level.
5. Use Metadata for Downstream Automation

You can attach custom key-value pairs to actors using FDatasmithFacadeMetaData.

Best Practice: Export relevant BIM or manufacturing data (like Part Numbers or Material costs) as metadata. Once in Unreal, this data can be used by Visual Dataprep or Blueprints to automate the elimination of manual tasks, such as automatically replacing placeholder meshes based on a “Type” tag.
6. Manage Resource Paths Carefully

When adding textures to a scene via FDatasmithFacadeTexture, the SDK usually expects absolute paths or paths relative to the .udatasmith file.

Tip: Always verify that the texture files exist on disk before finalizing the export. Missing textures will cause the importer to fail or result in the elimination of material fidelity, leaving your objects with the default gray checkerboard.
7. Clean Up Temporary Export Assets

The export process often generates temporary files or large memory buffers in the C# heap.

Best Practice: Explicitly call cleanup methods provided by the Facade API once the Export() function has successfully written to disk. This ensures the elimination of “memory bloat” in your host application, which is especially important if the user performs multiple exports in a single session.
8. Verify with the Datasmith Message Window

The SDK can log warnings and errors that occur during the conversion process.

Tip: If you are using the Facade within a custom tool, check the return codes of the Export functions. If an export fails, these logs are the primary way to identify if the issue was a file access error or a geometry violation, helping in the quick elimination of bugs in your exporter logic.