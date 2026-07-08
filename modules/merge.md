---
layout: default
title: Merge
---

<!-- ai-generation-failed -->

<h1>Merge</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Merge/Merge.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetTools, Core, CoreUObject, EditorFramework, Engine, GraphEditor, InputCore, Kismet, PropertyEditor, Slate, SlateCore, SourceControl, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

underlying logic for the engine’s Actor Merging and Proxy Geometry systems. It is a critical tool for performance optimization, used to consolidate multiple separate objects into more efficient, unified assets.

What it is and What it’s used for

Located in Engine/Source/Developer/Merge, this module enables the “Merge Actors” functionality found in the Unreal Editor. It allows developers to take multiple Static Mesh Actors in a level and combine them into a single new Static Mesh asset, potentially with unified materials and simplified geometry.

Primary uses include:

Draw Call Reduction: Combining dozens of small props (like furniture in a room) into one mesh to reduce the overhead on the CPU and GPU.
Proxy Geometry Generation: Creating low-detail versions of complex areas for use in the distance or for HLODs (Hierarchical Levels of Detail).
Material Baking: Merging multiple materials from different source meshes into a single texture atlas with one unified material.
Mesh Approximation: Simplifying high-poly Nanite geometry into manageable proxy meshes for collision or lower-end platform support.
Practical Usage Tips and Best Practices
1. Group Meshes by Spatial Proximity

Only merge actors that are located in the same room or immediate area. Merging objects from opposite sides of a map results in a massive bounding box, which leads to the elimination of efficient occlusion culling, as the engine will render the entire merged object even if only a tiny corner is visible.

2. Match Materials Before Merging

If you select the “Batch” merge method, the module works best if the source meshes already share the same material. Consolidating assets that use the same material into one mesh is the most effective way to ensure the elimination of redundant draw calls without needing to bake new textures.

3. Use “Merge Materials” for Atlasing

If your source meshes use many different materials, enable the Merge Materials setting. This will bake all textures into a single UV atlas. This is a best practice for the elimination of material-switching overhead on the GPU, though it requires careful management of the final texture resolution.

4. Optimize Lightmap Resolution

When merging meshes, the module must generate a new UV layout for lightmaps. Be sure to check the “Target Lightmap Resolution” in the merge settings. Setting this too low causes overlapping UV errors, while setting it too high prevents the elimination of excessive memory usage.

5. Leverage the “Approximate” Mode for Nanite

In UE5, the “Approximate” merge mode is specifically designed to handle Nanite-scale geometry. It uses a voxel-based approach to create a simplified shell. This is a primary strategy for the elimination of complexity when creating collision geometry for highly detailed environments.

6. Retain Only Necessary LODs

By default, the merge tool might try to keep all LODs of the source meshes. For distant geometry or background props, use the “Specific LOD Level” setting to merge only the lowest-detail version. This results in the elimination of unnecessary vertex data in the final merged asset.

7. Be Mindful of Collision Complexity

Merged actors can have very complex collision if not configured correctly. After a merge, check the “Collision Complexity” in the Static Mesh Editor. Choosing “Simple as Complex” for a massive merged object can lead to the elimination of physics performance; use a simplified box or convex hull instead.

8. Strategic Elimination of the Source Actors

After successfully merging and verifying your new mesh, the tool gives you the option to replace the source actors in the level. Using this option ensures the elimination of the original separate meshes from the scene, instantly providing the performance gains intended by the merge.