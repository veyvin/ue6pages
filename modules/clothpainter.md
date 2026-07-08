---
layout: default
title: ClothPainter
---

<!-- ai-generation-failed -->

<h1>ClothPainter</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ClothPainter/ClothPainter.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AdvancedPreviewScene, AssetRegistry, AssetTools, ClassViewer, ClothingSystemEditorInterface, ClothingSystemRuntimeCommon, ClothingSystemRuntimeInterface, ClothingSystemRuntimeNv, Core, CoreUObject, DeveloperToolSettings, EditorFramework, EditorWidgets, Engine, InputCore, Kismet, MainFrame, MeshPaint, PropertyEditor, SkeletalMeshEditor, Slate, SlateCore, ToolMenus, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

les handle the storage of cloth assets or the physics simulation itself (Chaos), this module is responsible for the user interface, brush math, and the visual representation of weights on the mesh.

Primary uses include:

Vertex Weight Mapping: Painting values for properties like Max Distance (how far cloth can move) or Backstop (preventing clipping).
Visual Feedback: Rendering the color-coded heatmaps on the character’s geometry that indicate simulation strength.
Tool Selection: Providing the logic for different painting modes such as Brush, Gradient, Smooth, and Fill.
Property Distribution: Distributing values across the mesh vertices and ensuring that the painted data is correctly serialized into the cloth asset.
Practical Usage Tips and Best Practices
1. Master the Paint Value Scale

In the Cloth Painter, a Paint Value of 0.0 represents a pinned vertex (no simulation), while a value of 100.0 allows the vertex to move 1 meter from its animated position. Always start with a value of 0 at the waist or seams and gradually increase it toward the edges of the fabric.

2. Use “Smooth” to Fix Jitter

If you notice the cloth “shivering” or jittering in certain areas, use the Smooth tool. Jitter is often caused by sharp contrasts in weight values between adjacent vertices. Running a smooth pass averages these values, creating a more stable simulation for the Chaos solver.

3. Gradient for Long Garments

For long items like capes or dresses, the Gradient tool is superior to the standard brush.

Left-click to set the Start (Green dot).
Ctrl + Left-click to set the End (Red dot).
Press Enter to apply. This ensures a mathematically perfect linear falloff, which is difficult to achieve by hand.
4. Surface vs. Volume Painting

Choose the right brush mode for the job:

Surface Mode: Falloff follows the mesh surface. Use this for painting specific layers without affecting geometry underneath.
Volume Mode: Affects all vertices within a 3D sphere. Use this for painting through thick folds or multiple layers of a skirt simultaneously.
5. Toggle Preview with “H”

The most important shortcut in this module is the H key. Holding H hides the paint heatmap and activates the simulation. This allows you to “paint and play” instantly, ensuring the elimination of the guesswork involved in how a specific weight value will actually move in-game.

6. Leverage “Fill” for Base Layers

When starting a new piece of clothing, use the Fill tool to set a global base value (e.g., 50). It is much faster to start with a fully simulated mesh and paint back the pinned “0” areas than it is to paint a large cape vertex-by-vertex with a brush.

7. Masking for Complex Outfits

If your character has many overlapping cloth pieces, use the Selection tool to isolate specific Material IDs before you start painting. This locks the other sections of the mesh, preventing you from accidentally painting weights onto the wrong part of the character’s outfit.

8. Verify with “Draw Focus Plane”

When using the painter, pay close attention to the Backstop properties. Painting a Backstop value creates an invisible “collision wall” behind the cloth vertex. Using the painter to carefully define this prevents the fabric from clipping into the character’s legs during high-speed movement or complex animations.