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

nables high-fidelity data exchange between Autodesk 3ds Max 2027 and Unreal Engine 5.6⁄5.7.

Description

This module serves as the “Exporter” side of the Datasmith pipeline for the 2027 version of 3ds Max. It is designed to translate complex 3ds Max scene data—including V-Ray/Arnold materials, physical cameras, photometric lights, and nested hierarchies—into the .udatasmith format. It also powers the Datasmith Direct Link workflow, allowing for real-time synchronization between the 3ds Max viewport and the Unreal Editor, eliminating the need for constant file exports during the look-development phase.

Practical Usage Tips and Best Practices
1. Leverage the Datasmith Attributes Modifier

Before exporting, apply the Datasmith Attributes Modifier to your objects within 3ds Max. This allows you to specify per-object settings such as custom collision shapes (Box, Capsule, or Convex), lightmap resolution overrides, and specific UV channels. This is a best practice for ensuring that your assets require zero manual “fix-up” once they arrive in Unreal.

2. Use Direct Link for Iterative Lighting

Instead of exporting a file every time you move a light, use the Direct Link feature. By clicking “Synchronize” in the Datasmith ribbon in 3ds Max, the DatasmithMax2027 module pushes only the changed data to Unreal. This is the most efficient way to match the lighting and composition between your DCC tool and the game engine.

3. Optimize via Proxy Mesh Substitution

If your 3ds Max scene contains extremely high-poly “hero” assets that would hinder performance, use the Datasmith “Replace” functionality. You can tag objects in Max to be replaced by specific Unreal Assets (like a simplified Nanite mesh) upon import. This helps in the elimination of heavy geometry in the runtime project while maintaining the original scene layout.

4. Consolidate Multi-Resolution UVs

Unreal Engine supports up to 8 UV channels, but 3ds Max supports 99. The exporter will prioritize the first few channels. Ensure your primary textures are on Channel 1 and your custom lightmaps (if not using Unreal’s auto-generated ones) are on Channel 2. This ensures the DatasmithMax2027 module maps your coordinates correctly without data loss.

5. Clean the Scene Explorer

Datasmith exports the hierarchy exactly as it appears in the 3ds Max Scene Explorer. A best practice is to remove empty groups, hidden helper objects, and unused layers before export. This simplifies the resulting Outliner in Unreal and helps in the elimination of “Ghost Actors” that serve no purpose in a real-time environment.

6. Convert to Physical Materials

While the exporter supports many legacy 3ds Max materials, it is most reliable when using Physical Materials or the latest V-Ray/Arnold equivalents. The DatasmithMax2027 module is highly optimized to translate these into Unreal’s PBR (Physically Based Rendering) Master Materials, ensuring that roughness and metallic values look consistent between both applications.

7. Handle Instance Elimination

If you delete or “eliminate” an instance of an object in 3ds Max and then use Direct Link to synchronize, the corresponding Actor in Unreal will also be removed. However, if you have manually moved that Actor into a different Folder or Sub-level in Unreal, the sync may lose track of it. Always keep your Datasmith-imported folder structure intact to ensure the elimination and addition of objects stay in sync.

8. Check the “Missing Files” Dialog

If textures are missing in Unreal after an import, check the 3ds Max “Asset Tracking” toggle. The DatasmithMax2027 module cannot export what it cannot find on disk. Use the “Relink Bitmaps” script in Max to ensure all paths are absolute and accessible before running the Datasmith export to prevent “Checkerboard” material errors in Unreal.