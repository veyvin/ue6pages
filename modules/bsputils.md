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

a core part of the engine’s architecture for processing subtractive and additive volumes during the initial “blockout” phase of level design.

It is primarily used for rebuilding the “Model” (the hidden data structure that defines brush collisions and visibility) and managing the mathematical operations required when one brush carves into another.

Practical Usage Tips and Best Practices
1. Use for Rapid Architectural Prototyping

Despite being a legacy system, BSP is still the fastest way to “carve” spaces. Use additive brushes for walls and subtractive brushes for doors or windows. The BSPUtils logic allows you to iterate on room dimensions without needing to jump into an external 3D modeling suite.

2. Convert to Static Mesh for Performance

Geometry Brushes are significantly more expensive for the GPU to render than Static Meshes. Once your blockout is finalized, select your brushes and use the “Create Static Mesh” button in the Details panel. This replaces the complex BSP calculations with a optimized mesh, helping to “eliminate” performance bottlenecks in your level.

3. Maintain Strict Grid Snapping

The underlying math in BSPUtils is sensitive to floating-point errors. Always work with a power-of-two grid (e.g., 16, 32, 64 units). If brushes are slightly off-grid, the module may fail to calculate the intersection correctly, leading to “holes” in the world or invisible collision walls.

4. Manage Brush Order

The order in which brushes are created determines how they interact. If a subtractive window isn’t appearing in a wall, use the “To Front” or “To Back” commands (under the Brush Settings). This reorders the processing stack within the BSPUtils rebuilder, ensuring the subtraction occurs after the addition.

5. Minimize Complex Brush Shapes

Avoid creating highly complex shapes (like cylinders with 64 sides) using BSP. High-poly BSP brushes drastically increase “Build Geometry” times and can lead to instability. For complex shapes, use the Modeling Mode tools instead of Geometry Brushes.

6. Leverage “Select All Adjacent” for Texturing

When working with BSP, you can select one face and use the “Select” menu to find all adjacent surfaces or all surfaces with the same material. This makes it easy to bulk-apply developer textures (like grid materials) across an entire room created by the BSPUtils system.

7. Rebuild Geometry to Fix “Ghost” Collision

If you delete a brush but its collision remains, or if you move a brush and the lighting breaks, you must trigger a Geometry Rebuild. Go to Build > Build Geometry. This forces the BSPUtils module to clear the old spatial index and “eliminate” any orphaned data that is no longer relevant to the current layout.

8. Use for Trigger and Blocking Volumes

Many of the invisible volumes in Unreal (like TriggerVolume or BlockingVolume) share the same underlying logic as Geometry Brushes. Understanding how to manipulate brush vertices in Brush Editing Mode allows you to create precisely shaped trigger zones that fit perfectly into non-rectangular corridors.

Performance & Best Practices
Shadowing: BSP surfaces use “Lightmaps” differently than Static Meshes. If your BSP looks blotchy, increase the Lightmap Resolution (note: in BSP, a lower number means higher resolution).
Collision Complexity: Every time you add a BSP brush, the engine must recalculate the BSP tree. In very large levels, a high number of brushes will “eliminate” editor performance; always merge or convert them to meshes as the level grows.
Clean Geometry: Use the “Optimize” command in the Brush Settings to remove unnecessary edges and vertices created by complex boolean operations.