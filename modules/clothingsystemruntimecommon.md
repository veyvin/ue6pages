---
layout: default
title: ClothingSystemRuntimeCommon
---

<!-- ai-generation-failed -->

<h1>ClothingSystemRuntimeCommon</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ClothingSystemRuntimeCommon/ClothingSystemRuntimeCommon.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ClothingSystemRuntimeInterface, Core, CoreUObject, Engine, Slate</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

loth.

Unlike the solver-specific modules (like ClothingSystemRuntimeInterface), this module handles the “common” tasks: managing clothing assets, handling the skinning of simulation meshes to the underlying skeleton, and coordinating how the simulation results are applied back to the render mesh. It is the core engine that allows characters to have dynamic capes, skirts, and loose garments.

Practical Usage Tips and Best Practices
1. Add to Build Dependencies

If you are implementing custom clothing logic, such as a custom UClothingAsset or a specialized simulation component in C++, you must include this module in your Build.cs.

C++
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "ClothingSystemRuntimeCommon", "ClothingSystemRuntimeInterface" });
Copy code
2. Optimize Simulation Mesh Density

The performance of the clothing system is directly tied to the number of vertices in the simulation mesh, not the render mesh.

Best Practice: Use a simplified, low-poly proxy mesh for simulation and “wrap” the high-poly render mesh onto it. This helps eliminate unnecessary CPU overhead while maintaining high visual fidelity.
3. Leverage Long Range Attachment (Tethers)

When iterations are kept low for performance, cloth can often appear overly stretchy or “elastic.”

Tip: Use the Long Range Attachment (Tether) settings within the clothing properties. Tethers connect dynamic vertices directly to kinematic “anchor” points, which helps eliminate the “stretchy rubber” look without requiring expensive solver substeps.
4. Configure Substeps and Iterations Carefully

These two parameters on the SolverConfig node are the primary “knobs” for balancing quality and performance.

Best Practice: Increase Substeps to improve collision accuracy and prevent clipping through the character’s body. Use Iterations to increase the stiffness of the cloth. Balancing these allows you to eliminate clipping artifacts while maintaining a stable frame rate.
5. Use Tapered Capsules for Limbs

Standard capsules often fail to accurately represent the tapering of a character’s arms or legs, leading to gaps or clipping in clothing.

Tip: Use the Tapered Capsule shape in the Physics Asset. This module supports capsules with different radii at each end, which helps eliminate unsightly intersections between the character’s mesh and the simulated cloth.
6. Implement Backstop to Prevent Clipping

“Backstop” is a distance-based constraint that prevents cloth vertices from moving too far back into the character’s body.

Action: Paint Backstop distance and radius masks on your clothing asset. This limits the “travel” of a vertex toward the bone, effectively eliminating the most common clipping issues during extreme animations.
7. Profile with Stat Commands

To understand the performance impact of your characters’ clothing in a live scene, use the built-in profiling tools.

Command: Use stat ChaosClothPerformance in the console. This provides an overview of the simulation time and vertex counts. Monitoring this helps you identify which characters need optimization to eliminate frame rate hitches.
8. Utilize the ‘One Sided Collision’ for Capes

For garments like capes that only ever exist on one side of a character (the back), standard collision can sometimes be jittery.

Tip: For UE 5.6+, use the One Sided Collision option on capsules. This forces cloth vertices toward the capsule’s +X direction, which is extremely useful for eliminating clipping in capes or wrapped garments where the cloth should never enter the body volume.