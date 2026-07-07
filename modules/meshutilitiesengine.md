---
layout: default
title: MeshUtilitiesEngine
---

<!-- ai-generation-failed -->

<h1>MeshUtilitiesEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/MeshUtilitiesEngine/MeshUtilitiesEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, MeshUtilitiesCommon</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

engine to interface with mesh optimization and reduction tools during gameplay or within the engine’s core systems.

Description and Purpose

While the standard MeshUtilities module is strictly editor-only, MeshUtilitiesEngine provides an interface that allows the Engine (Runtime) to communicate with mesh reduction providers (like Simplygon or the built-in UE reducer). Its primary purpose is to handle the generation of LODs (Levels of Detail), the calculation of Proxy Geometry, and the creation of Nanite data. It serves as the “coordinator” that ensures mesh data is properly formatted and passed to the correct optimization algorithm to eliminate excessive geometric complexity at runtime or during automated build processes.

Practical Usage Tips and Best Practices
Access via the IMeshReduction Interface
To use this module in C++, utilize FVisualMeshUtilities::GetMeshReductionInterface(). This allows you to check if a reduction provider is active and valid, helping you eliminate null pointer crashes when attempting to generate LODs programmatically.
Prioritize Built-in UE Mesh Reduction
In modern versions of Unreal, the built-in reducer is highly optimized. Ensure your project settings are configured to use “UnrealMeshReduction” to eliminate the need for expensive third-party licenses while still maintaining high-quality mesh decimation for your assets.
Coordinate Nanite Data Generation
This module is heavily involved in the pipeline that converts standard Static Meshes into Nanite-enabled assets. If you are building tools to automate asset imports, use this module to trigger the Nanite build process, which helps you eliminate the manual “Enable Nanite” checkbox step for thousands of assets.
Leverage for Runtime LOD Management
If your project involves procedural content or user-generated meshes, this module provides the hooks necessary to generate LODs on the fly. Implementing an automated LOD strategy is the best way to eliminate frame rate drops when players introduce high-poly custom geometry into a scene.
Handle Skeletal Mesh Reduction Safely
The module includes specific logic for reducing Skeletal Meshes while maintaining bone influences. Always verify the “Max Bone Influences” setting during reduction to eliminate “stretching” artifacts where vertices lose their connection to the character’s rig.
Optimize Proxy Mesh Silhouettes
When creating proxy meshes for HLODs, use the “Silhouette Importance” settings within the reduction interface. Higher importance on the silhouette helps you eliminate “popping” or visible shape changes when the engine switches from the high-poly mesh to the simplified proxy at a distance.
Validate Material Slot Conservation
During mesh reduction, the module can attempt to merge material slots. Ensure that “Consolidate Materials” is handled carefully to eliminate visual bugs where different parts of a mesh (like wood and metal) accidentally share a single, incorrect material after the reduction process.
Monitor Build Logs for Reduction Failures
If a mesh fails to generate an LOD, MeshUtilitiesEngine will output specific error codes to the log. Monitoring these logs in your CI/CD pipeline allows you to eliminate corrupted assets from reaching the final build, ensuring that all meshes have a valid LOD chain.