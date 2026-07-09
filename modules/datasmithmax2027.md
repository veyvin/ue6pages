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

nent designed to interface between Autodesk 3ds Max 2027 and Unreal Engine. Its primary purpose is to translate 3ds Max scene data—including complex geometry, V-Ray/Corona materials, lights, cameras, and nested hierarchies—into the .udatasmith format or for live synchronization via Datasmith Direct Link. It acts as a bridge that allows architectural and design visualization artists to move their high-fidelity assets into Unreal Engine 5.7 with minimal manual rework.

Practical Usage Tips & Best Practices
1. Utilize Datasmith Direct Link for Iteration

Instead of exporting and re-importing files, use the Direct Link feature provided by the module.

Best Practice: Keep both 3ds Max and Unreal Engine open simultaneously. When you make a change in Max, click the “Sync” button. This allows for the elimination of the traditional “export-to-disk” bottleneck, providing near-instant visual feedback in the engine.
2. Apply the Datasmith Attributes Modifier

The module includes a specific 3ds Max modifier called Datasmith Attributes.

Tip: Apply this to objects to control how they are treated during export. You can use it to specify custom collision shapes or to force certain objects to export as “Bounding Boxes,” which helps in the elimination of excessive polygon counts for distant background props.
3. Standardize UV Channel 2 for Lightmaps

While Unreal Engine can generate lightmap UVs, the 3ds Max exporter works best when you provide them.

Best Practice: Use the “Unwrap UVW” modifier in Max to set up clean, non-overlapping UVs on Channel 2. This ensures the elimination of “overlapping UV” errors during the light baking process in Unreal.
4. Manage Pivot Points and Nesting

3ds Max allows for complex group and layer hierarchies, but deeply nested groups can sometimes cause transformation offsets.

Tip: Ensure your “hero” objects have their pivots centered and “Reset XForm” applied before export. This practice leads to the elimination of “drifting” meshes where the visual mesh is disconnected from its actor’s transform in Unreal.
5. Leverage the Global Exposure Settings

The module attempts to translate 3ds Max physical camera settings and environment exposures.

Best Practice: If your scene appears completely black or blown out after import, check the Post Process Volume in Unreal. The exporter often brings over high physical camera values that may require the elimination of the default “Auto Exposure” to look correct.
6. Optimize Forest Pack and RailClone Objects

The 2027 module has refined support for iToo Software plugins.

Tip: When exporting Forest Pack items, the module creates Hierarchical Instanced Static Meshes (HISM) in Unreal. This is crucial for the elimination of high draw call counts, allowing you to render millions of scattered instances efficiently.
7. Clean Up Materials with the “Scene Converter”

3ds Max scenes often contain legacy “Standard” materials or incompatible shaders.

Best Practice: Run the 3ds Max Scene Converter to change legacy materials to Physical Materials or supported V-Ray/Corona types before using Datasmith. This ensures the elimination of “Missing Material” errors and ensures textures are mapped correctly to the Unreal Master Materials.
8. Handle Object Elimination and Updates

When re-syncing a scene after deleting objects in 3ds Max, the Datasmith module manages the delta update.

Tip: If you remove an object in Max and perform a Sync, the corresponding Actor in Unreal will be removed. However, if you have modified that Actor in Unreal, it may persist. Use the “Reset to Workspace” option in the Datasmith Scene Actor to ensure the total elimination of “ghost” objects that no longer exist in the source file.