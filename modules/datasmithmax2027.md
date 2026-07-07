---
layout: default
title: DatasmithMax2027
---

<!-- ai-generation-failed -->

<h1>DatasmithMax2027</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/DatasmithMax2027.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>DatasmithMaxBase</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

r plugin designed specifically for Autodesk 3ds Max 2027 to bridge high-fidelity 3D scenes into Unreal Engine.

Description and Purpose

This module provides the necessary translation logic to convert 3ds Max scene data—including complex geometry, V-Ray/Corona materials, physical lights, and hierarchical metadata—into a format Unreal Engine can consume. It supports both the File Export (.udatasmith) workflow for static snapshots and the Datasmith DirectLink workflow for real-time synchronization. Its primary purpose is to eliminate the manual reconstruction of scenes in Unreal Engine by preserving the spatial relationships, material properties, and pivot points defined within 3ds Max 2027.

Practical Usage Tips and Best Practices
Synchronize via DirectLink
Use the DirectLink panel in the 3ds Max ribbon to establish a live connection with the Unreal Editor. This allows you to push changes instantly with a single click, helping you eliminate the time-consuming process of re-exporting and re-importing files during the iterative design phase.
Standardize Scene Units to Centimeters
Before exporting, ensure your 3ds Max System Unit Scale is set to Centimeters. While Datasmith attempts to handle unit conversion, matching the native Unreal Engine unit scale at the source is the best way to eliminate scaling issues and physics inconsistencies during the import process.
Clean Up Normals and Backface Culling
Unreal Engine does not enable double-sided rendering by default. Enable “Backface Cull” in the 3ds Max object properties to identify inverted faces. Correcting these normals before export will eliminate “invisible” surfaces or lighting artifacts once the mesh is brought into the engine.
Utilize the Datasmith Attributes Modifier
Apply the Datasmith Attributes Modifier to specific objects in 3ds Max to customize how they are handled. You can use this to define lightmap resolutions or designate specific meshes to be exported as “Collision” geometry, which helps eliminate the need for manual post-import adjustments.
Manage XRef Scenes via Settings
If your 3ds Max project relies on externally referenced (XRef) scenes, ensure the “Export XRef Scenes” option is enabled in the Datasmith settings panel. This ensures that your entire assembly is preserved, helping you eliminate missing geometry errors in your Unreal level.
Optimize High-Density Meshes
3ds Max allows for extremely high-poly geometry that can tank real-time performance. Use the ProOptimizer modifier to reduce vertex counts on non-essential objects before export. This practice will eliminate frame rate hitches, especially during complex scenes like a cinematic elimination sequence.
Bake Procedural Maps to Bitmaps
Unreal Engine cannot natively evaluate complex 3ds Max procedural maps. Use the “Bake” settings in the Datasmith ribbon to convert these into textures. Setting a reasonable maximum resolution (e.g., 4K) in the Settings panel will eliminate blurry textures while keeping memory usage under control.
Filter Out Hidden and Unwanted Layers
Datasmith only exports visible objects by default. Use 3ds Max layers to organize your scene and hide construction geometry, helper objects, or unused assets. This allows you to eliminate scene clutter and keeps the Unreal World Outliner clean and organized.