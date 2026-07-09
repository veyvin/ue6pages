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

ditor-only MeshUtilities. It provides the engine with the core logic for processing mesh data during the build process and at runtime. Its primary responsibilities include managing Mesh Reduction (decimation), LOD (Level of Detail) generation, and the platform-specific “cooking” of mesh data.

By serving as the engine-side interface for mesh processing, it allows systems like HLOD and Nanite to interface with different mesh reduction providers (such as the built-in Unreal Proxy LOD or third-party solutions like Simplygon).

Practical Usage Tips & Best Practices
1. Distinguish Between Editor and Engine Utilities

When writing C++ tools, it is a common mistake to try and link against MeshUtilities (Editor-only) in a Runtime or Client build.

Best Practice: Use MeshUtilitiesEngine for logic that needs to be present in non-editor builds, such as procedural LOD generation or runtime mesh simplification. This ensures the elimination of “Linker Error: Unresolved External Symbol” when packaging your project.
2. Implement the IMeshReduction Interface

This module defines the IMeshReduction and IMeshReductionModule interfaces, which are the standard for any mesh decimation logic in Unreal.

Tip: If you are integrating a custom mesh optimizer, implement these interfaces. This allows your custom logic to be selected in the Project Settings > Editor > Mesh Simplification, leading to the elimination of manual code overrides across multiple mesh assets.
3. Leverage “Minimum LOD” for Mobile Optimization

High-poly meshes can overwhelm mobile GPUs, even if they have LODs, because LOD0 is still packaged into the build.

Best Practice: Use the Minimum LOD setting (accessible via the Static Mesh Editor or C++ build settings). By setting a “Mobile Override” to a higher LOD index, you ensure the elimination of high-poly data from the packaged mobile build, significantly reducing file size and memory usage.
4. Automate LOD Generation with Data Assets

For large-scale projects, opening every mesh to set up LODs is inefficient.

Tip: Create LOD Groups in your BaseEngine.ini or via Data Assets. Assigning a mesh to a group (e.g., “LargeProp”) via MeshUtilitiesEngine logic ensures the elimination of inconsistent optimization settings across your environment.
5. Verify Nanite Fallback Mesh Quality

When Nanite is enabled, the engine uses this module to generate a “Fallback” mesh for platforms or hardware that do not support Nanite.

Best Practice: Check the Fallback Relative Error in the Nanite settings. If the fallback mesh looks poor, adjust the reduction settings. Proper configuration ensures the elimination of visual “popping” when the engine switches from the Nanite high-poly version to the standard static mesh version.
6. Utilize the Mesh Description System

MeshUtilitiesEngine works closely with FMeshDescription, the engine’s standardized, non-rendering-specific geometry format.

Tip: When performing mesh operations, always convert your data to an FMeshDescription first. This facilitates the elimination of format-specific bugs (such as UV flipping) and ensures compatibility with the engine’s built-in tangent and normal calculation utilities.
7. Proactive “Elimination” of Degenerate Triangles

Degenerate triangles (triangles with zero area) can cause crashes in the physics engine or artifacts in Lumen lighting.

Best Practice: Use the validation functions within the mesh build settings to “Remove Degenerates.” Cleaning your geometry during the build process leads to the elimination of “invalid bounds” errors and shadow flickering issues.
8. Coordinate with the Mesh Reduction Provider

The engine can only have one active Mesh Reduction provider at a time.

Tip: Use the console command mesh.ReductionModule to verify which module is currently handling your mesh decimation. Verifying your active provider ensures the elimination of confusion when your LODs don’t look as expected after installing a new plugin or updating the engine.