---
layout: default
title: ClothingSystemEditorInterface
---

<!-- ai-generation-failed -->

<h1>ClothingSystemEditorInterface</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ClothingSystemEditorInterface/ClothingSystemEditorInterface.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ClothingSystemRuntimeInterface, Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the Unreal Engine Editor interacts with clothing simulation data. It provides the abstract base classes and interfaces required to create, edit, and paint clothing assets within the Skeletal Mesh Editor.

This module acts as the “glue” between the UI (the Cloth Paint tool and the Section Selection context menus) and the underlying physics solvers like Chaos Cloth. It allows the editor to handle tasks like vertex weight painting, mask creation, and the conversion of render meshes into simulation meshes without being hard-coded to a specific physics provider.

1. Enable Advanced Cloth Paint Tools

This module powers the “Cloth Paint” panel in the Skeletal Mesh Editor.

Best Practice: When painting, use the Gradient Tool provided by this interface for smooth transitions (e.g., from a pinned waist to a free-moving hem). Setting a “Start Value” of 0 and an “End Value” of 100 over a selection of vertices is far more efficient and stable for the solver than painting by hand.
2. Manage Clothing LODs Correctly

The interface allows you to create different simulation meshes for different Levels of Detail (LODs).

Tip: Use the “Create Clothing Asset from LOD Section” feature to provide a lower-resolution simulation proxy for distant characters. This significantly improves performance by reducing the number of particles the Chaos solver must process per frame.
3. Use Masks for Parameter Control

Instead of just painting “Max Distance,” use the interface to create multiple Masks.

Best Practice: Create separate masks for Max Distance (how far cloth moves), Backstop (preventing cloth from entering the body), and Anim Drive (how much the animation influences the cloth). You can swap which mask is “Targeted” at any time, allowing for non-destructive iteration of different material behaviors (e.g., silk vs. heavy denim).
4. Leverage Physics Asset Collisions

The module allows you to link a Physics Asset to your clothing asset during creation.

Tip: Ensure your Physics Asset has “Sphysics” or “Tapered Capsule” shapes that closely match the character’s body. The ClothingSystemEditorInterface uses these shapes to generate the collision constraints for the simulation. If your cloth is clipping, the issue is often in the Physics Asset, not the cloth weights.
5. Transition to the New Dataflow Editor

With the introduction of the Chaos Cloth Asset (Experimental in 5.3+), this module now supports the Dataflow graph-based workflow.

Tip: For complex garments, consider moving away from legacy “Mesh-bound” cloth and use the new Cloth Asset workflow. This interface allows you to import external .nvcloth or .apx files and convert them into the new node-based format, providing much finer control over XPBD (Extended Position-Based Dynamics) constraints.
6. Copy Clothing Data Between Meshes

If you have multiple characters wearing the same outfit (e.g., a uniform), you don’t need to repaint.

Best Practice: Use the “Copy Clothing Data from Mesh” option within the Clothing Data panel. This uses the interface’s mapping logic to transfer painted weights from one Skeletal Mesh to another based on vertex proximity, drastically reducing authoring time for variants.
7. Monitor Simulation Mesh vs. Render Mesh

The interface provides visualization modes to see the “Physical Mesh.”

Tip: Always toggle the “Physical Mesh” view in the viewport. If your simulation mesh is too dense, the ClothingSystemEditorInterface will struggle to maintain performance. Aim for a simulation mesh that is significantly lower in density than your render mesh to keep the solver efficient.
8. Eliminate Interpenetration with Backstop

One of the most powerful features of this interface is the Backstop mask.

Best Practice: Use Backstop to define a “safety zone” behind the cloth. By painting a Backstop Radius, you essentially create a virtual sphere at each vertex that prevents the cloth from moving too close to the character’s skin. This is the most effective way to eliminate “popping” through geometry during fast animations.