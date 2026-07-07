---
layout: default
title: DatasmithMax2025
---

<!-- ai-generation-failed -->

<h1>DatasmithMax2025</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/Enterprise/Datasmith/DatasmithMaxExporter/DatasmithMax2025.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>DatasmithMaxBase</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

a specialized bridge designed to translate high-fidelity scene data from Autodesk 3ds Max 2025 into Unreal Engine. It is a critical component of the Datasmith ecosystem, enabling architectural, engineering, and design visualization professionals to move complex scenes—including geometry, lights, cameras, and physical materials—into the engine while preserving hierarchy and metadata.

This module supports both the standard .udatasmith file export workflow and the Datasmith Direct Link workflow, allowing for real-time synchronization between the 3ds Max viewport and the Unreal Editor.

Practical Usage Tips and Best Practices
1. Standardize Scene Units to Centimeters

While Datasmith attempts to scale scenes automatically, 3ds Max users often work in various unit scales (inches, millimeters, etc.).

Best Practice: Set your 3ds Max System Unit Scale to 1 Unit = 1.0 Centimeter before exporting. This ensures a 1:1 scale ratio with Unreal Engine’s internal units, which helps eliminate lighting artifacts and physics calculation errors caused by extreme scale transforms.
2. Utilize Direct Link for Iterative Design

Instead of constantly exporting and re-importing files, use the Datasmith Direct Link feature.

Tip: Enable the Direct Link connection in both 3ds Max and the Unreal Datasmith Hub. This allows you to push incremental changes (like moving a chair or swapping a material) with a single click, eliminating the downtime associated with full scene re-exports.
3. Leverage the ‘Datasmith Attributes’ Modifier

3ds Max 2025 supports the Datasmith Attributes modifier, which allows you to define Unreal-specific data directly on your Max objects.

Action: Use this modifier to specify custom Lightmap resolutions or to tag objects for specific “Usage” categories. By defining these in Max, you eliminate the need to manually re-configure static mesh settings every time you re-import the asset into Unreal.
4. Clean Up the Slate Material Editor

Datasmith attempts to convert complex V-Ray, Corona, or Arnold materials into Unreal Engine Material Instances.

Best Practice: Collapse or simplify complex procedural maps into “Baked” textures when possible. While Datasmith 2025 is highly capable, simplifying the material graph before export helps eliminate overly complex, unoptimized shader networks that can degrade real-time performance.
5. Use ‘Export Selected’ for Modular Workflows

In large architectural scenes, exporting the entire file can be slow and result in a cluttered Content Browser.

Tip: Break your scene into logical layers (e.g., Furniture, Structure, Landscape) and use Export Selected. This allows you to update specific parts of the world independently, eliminating the risk of accidentally overwriting manual adjustments made to other objects in Unreal.
6. Check Normal Orientation (Backface Culling)

Unreal Engine renders single-sided materials by default, whereas 3ds Max often displays double-sided geometry in the viewport.

Action: Enable Backface Culling in the 3ds Max object properties before exporting. This allows you to see “holes” in your geometry where normals are flipped, helping you eliminate invisible walls or flickering surfaces before they reach the engine.
7. Manage XRef Scenes Correctly

The 2025 exporter includes improved support for XRef (External Reference) scenes.

Best Practice: Ensure all XRef paths are relative and the files are accessible. You can toggle “Export XRef Scenes” in the Datasmith export settings. Properly managing these helps eliminate missing geometry issues when collaborating across different workstations or network drives.
8. Optimize Geometry with ProOptimizer

High-poly CAD data from Max can quickly tank Unreal Engine’s frame rate if not managed.

Tip: Use the 3ds Max ProOptimizer modifier on high-density meshes to reduce vertex counts while preserving UVs. Reducing the complexity of the source geometry helps eliminate long “Processing Geometry” wait times during the Datasmith import process.