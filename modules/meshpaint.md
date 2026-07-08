---
layout: default
title: MeshPaint
---

<!-- ai-generation-failed -->

<h1>MeshPaint</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/MeshPaint/MeshPaint.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AppFramework, Core, CoreUObject, DesktopPlatform, EditorFramework, Engine, InputCore, MainFrame, MeshDescription, PropertyEditor, RHI, RenderCore, Slate, SlateCore, SourceControl, StaticMeshDescription, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

aint data directly onto mesh instances within the level viewport. It provides a bridge between the 3D environment and the material system, enabling localized visual variety without the need for unique textures for every object.

What it is and What it’s used for

Located in Engine/Source/Editor/MeshPaint, this module powers the Mesh Paint Mode (accessed via the Modes dropdown). It enables the interactive application of vertex colors, texture masks, and weight data directly onto Static and Skeletal Meshes.

Primary uses include:

Vertex Color Blending: Painting RGB values onto vertices to drive material blends (e.g., adding moss to the bottom of a stone or rust to a metal pipe).
Texture Painting: Directly modifying texture assets in 3D space by painting onto the mesh’s UVs.
Masking for VFX: Creating specific masks that Niagara or Materials use to trigger effects like burning, dissolving, or wetness.
Nanite Support: Providing the “Texture Color” painting workflow for Nanite meshes, which do not support per-instance vertex color painting.
Practical Usage Tips and Best Practices
1. Use the RGB Channels for Blend Masks

Instead of painting a single color, use the Red, Green, and Blue channels as separate masks for different materials (e.g., Red for mud, Green for moss, Blue for puddles). This multi-channel approach is a best practice for the elimination of redundant mesh actors, as one asset can look unique in every instance.

2. Balance Vertex Density vs. Detail

Vertex painting resolution depends entirely on the number of vertices in your mesh. If your mesh is too low-poly, the paint will look blocky. For Nanite meshes or low-poly assets, use the Texture Color mode instead. This ensures the elimination of “jagged” paint lines by storing data in a texture rather than on vertices.

3. Enable Virtual Texturing for Nanite Painting

To use Mesh Paint on Nanite meshes, you must enable Virtual Textures in your Project Settings. The MeshPaint module uses Runtime Virtual Texturing (RVT) to store the painted data. Correct setup here is required for the elimination of the “Vertex Color Not Supported” error on Nanite geometry.

4. Use “MeshPaintTextureReplace” for Fallbacks

In your master material, utilize the MeshPaintTextureReplace node. This allows the material to use a default texture or color when no painted data exists. This logic results in the elimination of broken or “black” materials on meshes that haven’t been touched by the paint tool yet.

5. Leverage Instance-Based Storage

Vertex paint data is stored on the Component instance in the level, not the Mesh asset itself. This allows you to have a single “Rock” asset in your Content Browser while having 100 variations in your world. This is the primary strategy for the elimination of disk space bloat from unique texture assets.

6. Optimize Material Instruction Counts

Every channel you sample from a vertex or texture paint mask adds to the pixel shader cost. Use the Shader Complexity view to ensure your blending logic isn’t too heavy. Keeping blending logic efficient leads to the elimination of GPU frame-time spikes in dense environments.

7. Copy/Paste Paint Data for Iteration

If you have perfectly painted a complex pillar and need 10 more just like it, use the Copy/Paste buttons in the Mesh Paint panel. This allows you to transfer vertex color data between instances, ensuring the elimination of manual, repetitive painting work.

8. Strategic Elimination of Legacy Paint Data

If an asset’s look changes and the old paint no longer fits, use the Remove or Fill tool to reset the colors to a neutral state (usually white or black). Performing this elimination of stale data ensures that your material blending logic starts from a clean slate, preventing visual artifacts from old masks.