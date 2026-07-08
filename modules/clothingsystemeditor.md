---
layout: default
title: ClothingSystemEditor
---

<!-- ai-generation-failed -->

<h1>ClothingSystemEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ClothingSystemEditor/ClothingSystemEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ClothingSystemEditorInterface, ClothingSystemRuntimeCommon, ClothingSystemRuntimeInterface, ClothingSystemRuntimeNv, ContentBrowser, Core, CoreUObject, EditorFramework, Engine, RenderCore, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

dynamic fabric.

Primary uses include:

Cloth Asset Creation: Generating simulation data from specific material sections of a Skeletal Mesh.
Weight Painting: Defining “Max Distance” and “Backstop” values directly on the mesh vertices to control how much the fabric can move.
Mask Management: Creating and editing multiple masks to drive different simulation parameters like stiffness, damping, and collision.
LOD Management: Handling the transition of cloth simulation across different Levels of Detail (LODs).
Practical Usage Tips and Best Practices
1. Use the “H” Key for Instant Preview

While in Cloth Paint mode, you can hold the H keyboard shortcut to hide the paint interface and preview the simulation in real-time. This is essential for quickly verifying how your painted weights react to movement without constantly toggling tool modes.

2. Leverage Gradient Painting for Smooth Transitions

Instead of painting weights manually, use the Gradient Tool to define the transition from pinned (0.0) to loose (e.g., 100.0) areas. Click to set a start point and Ctrl+Click to set an end point, then press Enter to apply. This creates a linear falloff that prevents “jitter” at the seams of the simulation.

3. Assign a Physics Asset for Collision

When creating a new Clothing Asset, always ensure you assign a Physics Asset. The cloth solver uses the capsules and spheres defined in that Physics Asset to calculate collisions. Without a properly configured Physics Asset, the cloth will clip through the character’s body.

4. Manage Mesh Density for Chaos

Chaos Cloth performance is directly tied to vertex count. If your render mesh is too high-poly, the simulation will be slow. Use the Remove from Mesh option when creating a cloth asset to drive a high-poly render mesh with a simplified, low-poly simulation mesh.

5. Debug with Chaos Console Commands

If the cloth is behaving unexpectedly, use the following console commands to visualize the underlying simulation physics:

p.ChaosClothEditor.DebugDrawMaxDistances 1 (Shows how far vertices can move).
p.ChaosClothEditor.DebugDrawCollision 1 (Shows the collision volumes being used).
p.ChaosClothEditor.DebugDrawPhysMeshWired 1 (Shows the simulation wireframe).
6. Utilize Backstop to Prevent Clipping

Use the Backstop Distance and Backstop Radius masks to create a “safety zone” behind the cloth. This prevents the fabric from pushing too far back into the character’s body during high-velocity movements, which is the primary cause of unsightly clipping.

7. Copy Clothing Data Between Meshes

If you have multiple characters wearing similar outfits, use the Add Clothing Data from Mesh feature in the Clothing panel. This allows you to transfer your painted masks and configuration settings from one Skeletal Mesh to another, saving significant time on iterative character setups.

8. Strategic Elimination of Hidden Geometry

If a piece of clothing completely covers the body (like a thick coat), consider using a “Mask” or “Delete” material on the underlying body mesh. By using the Clothing Editor to handle the outer shell and eliminating the hidden internal geometry, you improve performance and remove any possibility of the body clipping through the cloth.