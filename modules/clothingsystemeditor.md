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

painting workflow, and the management of clothing assets on Skeletal Meshes.

It is primarily used by technical artists to define which parts of a mesh should simulate as cloth, paint physical constraints (like Max Distance), and manage the relationship between the render mesh and the simulation mesh.

Practical Usage Tips and Best Practices
1. Use the Section Selection Tool

To begin authoring cloth, you must first use the Section Selection button in the Skeletal Mesh Editor. This allows you to select specific material ID chunks. Once a section is highlighted, right-click to “Create Clothing Asset from Selection.” This is the primary entry point provided by the ClothingSystemEditor to isolate geometry for simulation.

2. Master the Max Distance Paint Tool

The Max Distance mask is the most critical parameter. A value of 0 means the vertex is “locked” to the animation (skinned), while a higher value (e.g., 100) allows it to move up to 100 units away from its animated position. Use a gradient to “eliminate” harsh snapping between the rigid collar of a shirt and the free-flowing bottom hem.

3. Leverage the “H” Shortcut for Previewing

When in the Cloth Painting mode, hold the H key on your keyboard. This allows you to quickly toggle the visibility of the painted weights. This is an essential workflow tip for verifying that your masks are applied correctly to the mesh without having to exit the paint tool.

4. Utilize the Gradient Tool for Smooth Transitions

Instead of painting vertex-by-vertex with a brush, use the Gradient Tool. Select a “Start” vertex and an “End” vertex to create a perfectly linear falloff. This is the best practice for long capes or dresses, as it ensures the simulation physics transition smoothly from the anchored shoulders to the loose edges.

5. Configure Physics Asset Collisions

Cloth simulation relies heavily on the Physics Asset assigned to the Skeletal Mesh. Within the clothing properties, ensure you have correctly mapped the collision capsules. If the capsules are too large, they will “eliminate” the natural folds of the cloth; if they are too small, the cloth will “clip” through the character’s body.

6. Optimize with LODs (Levels of Detail)

Simulation is computationally expensive. The ClothingSystemEditor allows you to define different simulation meshes for different LOD levels. For distant characters, you should “eliminate” the cloth simulation entirely or use a much lower-resolution simulation proxy to maintain high frame rates in crowded scenes.

7. Backstop and Friction Settings

Beyond Max Distance, use the Backstop properties to prevent cloth from pushing too far into the character’s body. Additionally, adjusting Friction is vital for preventing cloth from sliding off shoulders or getting stuck in unnatural positions against the skin.

8. Dataflow Workflow (UE 5.3+)

In recent versions, the engine has moved toward a Dataflow (node-based) approach for cloth. The ClothingSystemEditor module now interacts with the Chaos Cloth Asset editor. Use this new workflow for more complex, non-destructive cloth setups that can be shared across multiple different Skeletal Meshes.

Common Workflow Checklist
Asset Creation: Create the Cloth Asset from a Mesh Section.
Apply Clothing: Right-click the section again to “Apply Clothing Data.”
Painting: Open the Clothing Panel (Window > Clothing) and click “Activate Cloth Paint.”
Physics: Assign the correct Physics Asset for collision.
Validation: Use the “Simulate” button in the Skeletal Mesh Editor to test the physics in real-time.
Performance Tip

If your cloth is jittering or “exploding,” check the Gravity Scale and Stiffness values. Excessive stiffness values combined with a high gravity scale can “eliminate” the stability of the Chaos solver, leading to visual artifacts.