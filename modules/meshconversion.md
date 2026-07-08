---
layout: default
title: MeshConversion
---

<!-- ai-generation-failed -->

<h1>MeshConversion</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MeshConversion/MeshConversion.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, GeometryCore, MeshDescription, SkeletalMeshDescription, StaticMeshDescription</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

or translating geometry data between different internal representations. It provides the low-level logic required to convert standard static meshes, skeletal meshes, and procedural data into the high-performance Dynamic Mesh format used by the Modeling Mode and Geometry Scripting.

What it is and What it’s used for

Located in Engine/Source/Runtime/MeshConversion, this module facilitates the movement of vertex, index, and attribute data across the engine’s various mesh containers. It is the engine’s “translator” for geometry, ensuring that attributes like UVs, Normals, and Tangents are preserved regardless of the source or destination format.

Primary uses include:

Static Mesh to Dynamic Mesh: Powering the “Dynamic Mesh Converter” used in procedural workflows and the Motion Design (Avalanche) toolset.
Asset Baking: Enabling the conversion of procedurally generated Dynamic Meshes back into persistent Static Mesh or Skeletal Mesh assets.
Physics Representation: Converting complex visual geometry into simplified formats suitable for Chaos Physics collision.
Geometry Scripting Support: Providing the backend for Blueprint nodes like Copy Mesh From Component, which extracts geometry for real-time manipulation.
Practical Usage Tips and Best Practices
1. Utilize for Non-Destructive Modeling

Use the MeshConversion module (via the Dynamic Mesh Converter modifier) to work on Static Meshes non-destructively. Converting to a Dynamic Mesh allows you to apply geometry modifiers like “Mirror” or “Pattern” while keeping the source asset intact, leading to the elimination of permanent data loss during the design phase.

2. Manage Attribute Overlays Carefully

When converting from a Static Mesh to a Dynamic Mesh, ensure you are capturing all UV and Normal overlays. If these are not explicitly requested during conversion, it can result in the elimination of smoothed edges or correctly mapped textures on the resulting mesh.

3. Match Material Slots Before Conversion

Before converting multiple components into a single Dynamic Mesh, ensure their Material Slots are organized. The conversion process attempts to merge slots; improper organization can lead to the elimination of correct material assignments on the final output.

4. Optimize the Update Interval

In the Dynamic Mesh Converter properties, set the Update Interval strategically. For static objects, set this to 0 or a very high number. Frequent updates cause constant re-conversion of the geometry, which results in the elimination of CPU frame-time overhead for objects that aren’t actually changing.

5. Use for Collision Mesh Generation

If you have complex procedural geometry, use MeshConversion to “Bake” a simplified version for collision. By converting a high-poly Dynamic Mesh to a low-poly Static Mesh with “Simple” collision, you ensure the elimination of physics performance bottlenecks in your level.

6. Leverage “Copy Mesh From Component” in Blueprints

For runtime procedural effects (like a building being sliced), use the Geometry Scripting nodes backed by this module to copy the mesh from a StaticMeshComponent. This is the most efficient way to achieve the elimination of static geometry in favor of dynamic, interactable pieces.

7. Clean Up “Compute Meshes”

When using the conversion module for complex procedural chains, always call “Release All Compute Meshes” at the end of your logic. Failing to release these intermediate conversion buffers leads to the elimination of available system memory, potentially causing the editor to slow down over time.

8. Strategic Elimination of the Original Source

When “Baking” a Dynamic Mesh back into a Static Mesh Asset, use the option to replace the actor in the world. This ensures the elimination of the procedural overhead once the final shape is decided, allowing the engine to treat the object as a standard, optimized Static Mesh for rendering.