---
layout: default
title: ClothingSystemRuntimeNv
---

<!-- ai-generation-failed -->

<h1>ClothingSystemRuntimeNv</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ClothingSystemRuntimeNv/ClothingSystemRuntimeNv.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ClothingSystemRuntimeCommon, ClothingSystemRuntimeInterface, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the implementation for the NVIDIA PhysX (APEX) Clothing system. While Unreal Engine 5 has moved to Chaos Cloth as its primary simulation engine, this module remains in the engine to ensure backwards compatibility for projects upgrading from UE4 that still rely on legacy cloth assets. It handles the simulation of cloth particles, collision detection against physics assets, and the skeletal mesh deformation based on the PhysX solver.

Practical Usage Tips & Best Practices
1. Distinguish from Chaos Cloth

It is important to understand that this module is entirely separate from the modern Chaos Cloth system.

Best Practice: Do not attempt to mix NVIDIA and Chaos cloth components on the same character. For new UE5 projects, you should avoid this module in favor of ClothingSystemRuntimeChaos to ensure long-term support and access to modern features like the Cloth Panel Editor.
2. Respect the 32-Collision Limit

A hard limitation of the NVIDIA cloth solver is that it can only consider a maximum of 32 collision primitives (spheres, capsules, etc.) per cloth piece.

Tip: If you exceed this limit, the solver may randomly ignore certain bones, causing the cloth to clip through the body. Prioritize collisions for the torso and legs, and consider the elimination of finger or minor limb collisions to stay under the budget.
3. Use Backstop for Clipping Prevention

Backstop is a critical parameter in the NVIDIA runtime that defines a “no-go zone” for cloth particles relative to their animated bone position.

Best Practice: Use Backstop to prevent the cloth from pushing too far into the character’s mesh. This is often more performant than increasing solver iterations and is highly effective at the elimination of “jittering” caused by cloth getting stuck inside a high-poly collision body.
4. Manage LODs for Performance

NVIDIA cloth simulation cost scales with the number of simulated vertices.

Tip: Always set up Clothing LODs. In the Skeletal Mesh editor, you can disable clothing simulation for lower LODs (further away). This ensures the elimination of expensive physics calculations for characters that are only a few pixels wide on the screen.
5. Proper Mask Painting

The runtime relies on “Max Distance” and “Stiffness” masks painted in the editor.

Best Practice: Ensure your “Max Distance” values are 0 for vertices attached directly to the body (like a waistband). This “pins” the cloth in place. Improperly painted masks are the leading cause of cloth falling off the character or stretching infinitely.
6. Handle Character Elimination Events

When a character undergoes elimination, the cloth simulation can sometimes “explode” if the physics asset is instantly disabled or if the actor is moved to a distant location for pooling.

Best Practice: Set the Clothing Simulation Mode to Disabled or Teleport and Reset when an actor is eliminated to ensure the solver stops cleanly and doesn’t consume CPU cycles on an invisible mesh.
7. Profile with “stat clothing”

To see the performance impact of this module, use the console command stat clothing. This provides a breakdown of how many cloth assets are currently simulating and the total time taken by the NVIDIA solver. Use this to identify if “background” NPCs are accidentally simulating cloth, leading to the elimination of wasted frame time.

8. Plan for Migration

Because NVIDIA PhysX is no longer the default physics engine for Unreal, this module is considered legacy.

Tip: If your project requires high-fidelity cloth and long-term stability, use the built-in migration tools to convert your assets to Chaos. While ClothingSystemRuntimeNv is stable, it will not receive new features or optimizations in future UE5 releases.