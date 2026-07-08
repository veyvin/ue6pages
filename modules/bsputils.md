---
layout: default
title: BSPUtils
---

<!-- ai-generation-failed -->

<h1>BSPUtils</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/BSPUtils/BSPUtils.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine that provides low-level functions for managing and manipulating Binary Space Partitioning (BSP) geometry, commonly referred to as Geometry Brushes.

What it is and What it’s used for

This module contains the FBSPUtils class, which holds a collection of static helper functions used by the editor to process brush-based geometry. While modern level design primarily uses Static Meshes or Modeling Tools, BSP remains a vital part of the “blockout” phase and the underlying architecture for specialized volumes.

Primary uses include:

Brush Conversion: Handling the transformation of additive and subtractive brushes into rendered surfaces.
Static Mesh Generation: Providing the logic to convert complex BSP shells into permanent Static Mesh assets.
Geometry Rebuilding: Triggering the recalculation of the level’s “BspTree” and visibility data after a brush is moved or resized.
Collision Synthesis: Calculating the simplified collision hulls that allow players to interact with brush-based floors and walls.
Practical Usage Tips and Best Practices
1. Use for High-Speed Blockouts

The primary workflow for BSPUtils is supporting the rapid “whiteboxing” of a level. Use Geometry Brushes to define the scale and flow of your environment before involving the art team. This allows you to iterate on gameplay metrics (like jump heights or corridor widths) without the overhead of external 3D modeling.

2. Convert to Static Mesh for Performance

Geometry Brushes are computationally expensive for the renderer compared to Static Meshes. Once a layout is finalized, use the Create Static Mesh button in the Brush details panel (which calls functions within BSPUtils) to convert your blockout. This creates a more optimized asset and helps eliminate unnecessary draw calls.

3. Maintain Grid Snapping

When working with BSP, always keep Grid Snapping enabled. FBSPUtils logic is sensitive to floating-point precision. If brushes are slightly off-grid, the module may fail to calculate the intersection of faces correctly, resulting in “BSP holes”—invisible gaps in the world where players might fall through.

4. Order of Operations Matters

The module processes brushes in a specific list order. If a subtractive brush is placed before the additive brush it is meant to cut into, the subtraction will not appear. Use the Order commands (Bring to Front / Send to Back) in the editor to re-sort how BSPUtils calculates the final geometry.

5. Keep Brushes Simple

Avoid creating highly complex shapes using only BSP. The more vertices and faces a brush has, the longer BSPUtils takes to rebuild the level. For complex shapes, it is better to use the engine’s Modeling Mode tools, which use modern triangle-based logic rather than the legacy BSP tree structure.

6. Utilize Developer Materials

Apply “Developer Materials” (found in the Engine Content folder) to your BSP surfaces. These materials often feature grid patterns and measurement markers. Because BSPUtils handles texture mapping per-face, these materials help you verify that your architectural scale is correct relative to the player character.

7. Trigger Rebuilds Strategically

In large levels, moving a brush can trigger a slow “Update BSP” process. You can change your Editor Preferences to disable “Update BSP Automatically.” This allows you to move many brushes at once and then manually trigger a single rebuild via the Build Geometry menu, saving significant development time.

8. Use for Specialized Volumes

Even if you don’t use BSP for visual geometry, the logic in this module is used for Volumes (like Kill Z, Trigger, or Physics Volumes). If you need a volume that isn’t a simple box or sphere, you can use a Geometry Brush to define a custom shape and then convert it into a Volume, ensuring the elimination of “dead zones” in your level logic.