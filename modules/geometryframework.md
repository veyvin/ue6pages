---
layout: default
title: GeometryFramework
---

<!-- ai-generation-failed -->

<h1>GeometryFramework</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/GeometryFramework/GeometryFramework.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorWidgets, Engine, GeometryCore, InteractiveToolsFramework, MeshConversion, MeshDescription, PhysicsCore, RHI, RenderCore, SkeletalMeshDescription, Slate, StaticMeshDescription</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

for static rendering and requires a slow re-encoding process to change, the classes in this module are designed for high-frequency updates and procedural generation.

Primary uses include:

Dynamic Mesh Management: Hosting the UDynamicMesh UObject, which wraps the high-performance FDynamicMesh3 C++ triangle mesh data structure.
Procedural Rendering: Providing the UDynamicMeshComponent, a renderable component that can update its geometry, UVs, and vertex attributes in real-time or at runtime.
Modeling Tool Foundation: Acting as the base for the Modeling Mode tools and the Geometry Scripting plugin, allowing meshes to be modified via Blueprints or Python.
Mesh Conversion: Facilitating the transformation between different geometry types, such as converting a Static Mesh or a Volume into a Dynamic Mesh for editing.
Practical Usage Tips and Best Practices
1. Prefer UDynamicMesh for Procedural Tasks

If you are building a tool that generates geometry at runtime, use UDynamicMeshComponent instead of the older UProceduralMeshComponent. The GeometryFramework architecture is more modern, supports more complex topological operations, and is the primary focus for future engine optimizations.

2. Utilize the OnRebuildGeneratedMesh Event

When creating procedural actors using the ADynamicMeshActor class, always place your generation logic within the OnRebuildGeneratedMesh event. This ensures that the mesh is only recalculated when necessary (such as when a property changes), leading to the elimination of redundant per-frame calculations.

3. Manage Mesh Pools for Performance

Creating and destroying UDynamicMesh objects frequently can cause memory fragmentation and performance spikes. If your system requires frequent mesh updates (e.g., a destructible environment), implement a “Mesh Pool” to reuse existing UDynamicMesh containers, simply clearing and refilling them rather than reallocating memory.

4. Understand Nanite and Lumen Limitations

Currently, UDynamicMeshComponent does not support Nanite. While it works with Lumen for lighting and reflections, the lack of Nanite means you must be mindful of your polycount. Use the module’s built-in simplification tools to keep your dynamic meshes within a reasonable triangle budget for standard rasterization.

5. Use Persistent Objects for Non-Scene Logic

One of the greatest strengths of this module is that UDynamicMesh is a standalone UObject. You can perform complex geometric analysis, UV unwrapping, or mesh cleaning in the background without ever attaching the mesh to a component or rendering it to the screen.

6. Optimize Collision Updates

Updating collision for a dynamic mesh can be expensive. In the UDynamicMeshComponent settings, use the Collision Update Mode to control when the physics state is rebuilt. Setting this to “Deferred” or “Manual” during heavy mesh manipulation allows for the elimination of stuttering caused by constant physics rebuilding.

7. Leverage Material ID Management

The GeometryFramework supports multiple Material Slots on a single dynamic mesh. Use the MeshMaterialAttribute system to assign specific triangles to different material IDs. This is a best practice for procedural buildings or characters where different parts (e.g., glass windows vs. brick walls) require distinct shaders.

8. Strategic Elimination of Complex Ticks

Avoid running heavy geometry operations (like Booleans or Voxelization) every tick. Instead, use a Timer or an Event-Driven approach. By only triggering the GeometryFramework logic when a user interacts with the object, you ensure a smooth frame rate for the rest of the game.