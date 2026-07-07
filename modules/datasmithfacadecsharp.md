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

de, providing a high-level managed interface for creating custom Datasmith exporters.

Description and Purpose

This module acts as a wrapper around the native C++ Datasmith SDK, allowing developers to build export plugins for third-party applications using C#. It is primarily used by tools and pipeline engineers who want to translate data from a host application (like a CAD tool, BIM software, or custom DCC) into the .udatasmith format without writing low-level C++. The module provides classes to construct a DatasmithScene, define actors, meshes, materials, and lights, and then serialize that scene to disk. It is essential for developers working in .NET environments who need to bridge their proprietary data structures into the Unreal Engine ecosystem.

Practical Usage Tips and Best Practices
Manage Native Resource Cleanup
Since this is a C# wrapper for C++ memory, you must be diligent with object lifetimes. Ensure you call .Shutdown() or properly dispose of your Datasmith objects when the export is finished. This is the most effective way to eliminate memory leaks and “zombie” processes in your host application.
Configure the DLL Environment Path
The C# facade requires access to the underlying native DatasmithFacade DLLs. You must ensure that the path to the Datasmith SDK binaries is added to your system environment variables or loaded dynamically via PATH at runtime. This will eliminate “DLL Not Found” exceptions when initializing your plugin.
Handle Coordinate System Translation
Most CAD or DCC tools use different coordinate systems (e.g., Z-up vs. Y-up). Use the built-in transform utilities within the facade to convert your local coordinates to Unreal’s Left-Handed Z-up system early in the export process. Correcting this at the source helps eliminate confusing “flipped” or “mirrored” assets in the engine.
Utilize Hash-Based Mesh Uniqueness
To keep file sizes small, calculate a hash for your geometry data before creating a DatasmithMeshElement. If multiple objects in your host scene share the same geometry, point them to the same Mesh Element in the Datasmith scene. This practice will eliminate redundant mesh data and significantly speed up the final import.
Implement Metadata via Tags
Use the AddKeyValueProperty methods to attach custom metadata to your actors. This information is preserved upon import and can be accessed by the Dataprep system or Blueprints. Providing rich metadata at the export stage helps eliminate manual sorting and labeling tasks for the technical artist.
Leverage DirectLink for Live Sync
If your plugin supports iterative changes, use the DirectLink features provided by the SDK. DirectLink allows you to push updates to Unreal Engine without a full file export. This creates a real-time feedback loop and helps you eliminate the tedious “Export-Import-Repeat” cycle.
Validate Material Slot Consistency
Ensure that the number of material slots in your mesh elements matches the actual material assignments. Discrepancies here can cause “Default Material” overrides in Unreal. Auditing your material indices during the export phase will eliminate visual artifacts and broken shaders.
Match SDK and Engine Versions
Always use the version of the Datasmith SDK that corresponds to your target Unreal Engine version (e.g., use the 5.6 SDK for UE 5.6). Version mismatches in the .udatasmith file schema can lead to crashes or failed imports, which you must eliminate through consistent versioning.