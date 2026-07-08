---
layout: default
title: DatasmithMax2023
---

<!-- ai-generation-failed -->

<h1>DatasmithMax2023</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/DatasmithMax2023.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>DatasmithMaxBase</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nreal Engine. It is a specialized version of the Datasmith exporter plugin tailored specifically for the 3ds Max 2023 environment.

What it is and What it’s used for

This module functions as an exporter and synchronization tool. It translates complex 3ds Max scene data—including geometry, V-Ray/Corona materials, light rigs, and hierarchical structures—into a format (.udatasmith) that Unreal Engine can ingest. It also powers the Direct Link functionality, allowing for real-time updates between the two applications without manual file exports.

Primary uses include:

Scene Translation: Converting Max-specific data like XRefs, instances, and pivot points into Unreal Actors and Assets.
Direct Link Synchronization: Establishing a live connection to push changes from 3ds Max to UE5 instantly.
Material Conversion: Automatically mapping complex shader networks from engines like V-Ray or Arnold into Unreal’s PBR material system.
Automated Optimization: Handling the conversion of high-poly Max geometry into engine-ready meshes, often maintaining instancing to save memory.
Practical Usage Tips and Best Practices
1. Leverage Datasmith Direct Link

Instead of exporting files to disk, use the Direct Link feature. By enabling the Datasmith Hub, you can push “Sync” commands directly from the 3ds Max ribbon. This eliminates the need for managing intermediate .udatasmith files and allows you to see lighting and material changes in the engine almost immediately.

2. Clean Up the Scene with the Messages Window

Before finalizing an export, always check the Datasmith Messages window in 3ds Max. It provides vital warnings about unsupported map types, non-orthogonal matrices, or missing textures. Addressing these warnings in Max ensures the elimination of “broken” materials or misplaced meshes in Unreal.

3. Control Texture Baking Limits

In the Datasmith tab of the 3ds Max ribbon, you can set the Bake Resolution. For procedural textures or complex Max maps that Unreal cannot read natively, the exporter will bake them into bitmaps. Ensure this is set to an appropriate resolution (e.g., 2048 or 4096) to maintain visual quality without inflating memory usage.

4. Manage XRefs Efficiently

The 2023 module includes improved support for XRef Scenes. You can choose whether to merge XRef scenes into a single hierarchy or keep them separate. For large architectural projects, keeping them separate allows you to re-import only specific sub-sections of a building, saving significant processing time.

5. Use “Export Selected” for Iteration

Don’t always export the entire scene. If you are only working on a specific piece of furniture or a single room, use Export Selected. This creates a smaller Datasmith file that imports much faster, allowing for rapid iteration on specific assets within a larger master level.

6. Verify Pivot Point Placement

Datasmith respects the pivot points set in 3ds Max. Before exporting, ensure your pivots are logically placed (e.g., at the base of a pillar or the center of a door hinge). This ensures that when you manipulate the Actors in Unreal, they rotate and scale as expected by the level designers.

7. Standardize Material Names

The module uses material names to identify unique shaders. If two different objects have different materials both named “Chrome,” the exporter may merge them or cause conflicts. Establish a unique naming convention in Max to ensure every material is correctly translated into a unique Unreal Material Instance.

8. Use the “Active Time Segment” for Animation

If your scene contains animated transforms (like a moving elevator or a rotating fan), ensure the export setting is set to Active Time Segment. This will generate a Level Sequence in Unreal that perfectly replicates the movement from the 3ds Max timeline, including any specific easing or keyframe timing.