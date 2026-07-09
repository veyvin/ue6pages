---
layout: default
title: nvTessLib
---

<!-- ai-generation-failed -->

<h1>nvTessLib</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/nvtesslib/nvTessLib.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

in Unreal Engine. It is a specialized geometry utility used during the mesh build process to generate optimized tessellation structures. While modern Unreal Engine workflows have shifted toward Nanite, this library remains part of the core mesh processing pipeline for handling legacy hardware tessellation data and generating PN (Point-Normal) Triangles.

Its primary role is to take low-resolution input geometry and calculate the necessary data to smooth out silhouettes and surfaces without requiring a high-resolution source mesh, specifically by interpolating normals to create a curved appearance.

Practical Usage Tips & Best Practices
1. Understand the Shift to Nanite

In Unreal Engine 5.x, hardware tessellation (the primary consumer of nvtesslib data) has been deprecated in favor of Nanite.

Best Practice: For new projects, use Nanite Tessellation (introduced in UE 5.4) instead of legacy displacement. This ensures the elimination of the high performance cost associated with older hardware-tessellation pipelines while providing much higher geometric detail.
2. Use PN Triangles for Silhouette Smoothing

The core feature of this library is the generation of PN Triangles, which smooths out the “faceted” look of low-poly models by using vertex normals to calculate a curved surface.

Tip: Use PN Triangles on organic shapes like characters or smooth terrain to maintain visual quality at close range. This results in the elimination of jagged edges on low-poly assets without the memory overhead of a high-density mesh.
3. Prevent “Cracking” at UV Seams

Tessellation algorithms often cause “cracks” in a mesh where UV islands meet because the displacement values don’t match across the seam.

Best Practice: When using displacement logic associated with this module, ensure your meshes have “Smooth Normals” across seams. Properly aligned normals facilitate the elimination of visible gaps in the geometry when the mesh is subdivided at runtime.
4. Optimize via “Flat Tessellation” for Hard Surfaces

Not every mesh needs the curved interpolation provided by PN Triangles.

Tip: For hard-surface objects like stone walls or bricks, use “Flat Tessellation” settings. This uses the library to add geometric density for displacement maps but skips the normal interpolation, leading to the elimination of unwanted “bloating” or rounded corners on sharp architectural edges.
5. Monitor “Dicing Rate” Performance

The “Dicing Rate” determines how many sub-triangles the library and engine generate for a given patch of geometry.

Best Practice: Keep the dicing rate as high as possible (larger triangles) while maintaining the desired detail. Reducing the density results in the elimination of GPU bottlenecks, especially in scenes with many tessellated objects.
6. Leverage for Disk Space Savings

One of the primary advantages of utilizing this library’s logic is that it allows you to store very small files on disk.

Tip: Store a low-poly base mesh and a heightmap rather than a multi-million polygon high-poly mesh. This results in the elimination of massive project repository sizes and significantly faster asset sync times for your team.
7. Combine with World Position Offset (WPO)

Data processed by this module is often used as the foundation for WPO-based displacement in materials.

Best Practice: Use a “Distance-Based Tessellation” node in your material to fade out the displacement as the camera moves away. This ensures the elimination of redundant geometry processing for objects that are too far away for the detail to be visible.
8. Verify Asset Build Settings

If your displacement isn’t showing up, it is often because the mesh was not built with the correct “Support Compute Skinned Tessellation” or “Allow CPU Access” flags.

Tip: Check the Build Settings in the Static Mesh Editor. Ensuring these flags are enabled during the build phase leads to the elimination of “flat” geometry bugs where displacement maps fail to deform the mesh surface.