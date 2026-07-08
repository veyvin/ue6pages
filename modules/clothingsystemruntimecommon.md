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

ayer for the Unreal Engine clothing simulation pipeline. It acts as the bridge between the high-level Engine classes (like USkeletalMeshComponent) and the low-level physics solvers (like Chaos Cloth).

Its primary role is to provide the base classes—such as UClothingAssetCommon and UClothingSimulationCommon—that store simulation data, handle cloth-to-mesh skinning, and manage the lifecycle of a simulation. By separating the simulation data from the solver implementation, it allows the engine to “eliminate” dependencies on specific physics backends, making the clothing system modular and extensible.

Practical Usage Tips and Best Practices
Explicit Module Dependency When writing C++ tools that programmatically create or modify clothing assets, you must include ClothingSystemRuntimeCommon and ClothingSystemRuntimeInterface in your Build.cs. This ensures your code can access the core classes needed to “eliminate” compilation errors related to clothing types.
Separate Render and Simulation Meshes Always use a simplified “Sim Mesh” for your clothing logic while keeping a high-poly “Render Mesh” for visuals. The module handles the mapping between the two. This is the best way to “eliminate” performance bottlenecks, as simulating every vertex of a high-fidelity character mesh is computationally prohibitive.
Utilize Clothing Asset Reuse Because this module decouples clothing from the Skeletal Mesh, you can share a single UClothingAssetCommon across multiple characters with similar skeletons. This helps “eliminate” redundant data and simplifies the management of shared garments like uniforms or capes.
Leverage Mask-Based Parameter Control Use the painting tools in the editor to define masks for parameters like “Max Distance” and “Backstop.” These masks are processed by the Common module to “eliminate” clipping. For example, setting a “Max Distance” of 0 at the waist of a skirt ensures it stays fixed to the character’s hips.
Optimize with Long Range Attachment (LRA) Enable “Tethers” (Long Range Attachment) within your cloth asset settings. This allows the module to “eliminate” the “stretchy” look often found in low-iteration simulations by anchoring distant vertices directly to kinematic bones.
Implement LOD-Specific Simulation You can disable clothing simulation at lower Levels of Detail (LODs) or use a much simpler Sim Mesh. The Common module automatically handles the transition, allowing you to “eliminate” the CPU cost of clothing for characters that are far from the camera.
Monitor Solver Performance Use the console command stat ChaosCloth to see how much time the simulation is consuming. If the “Clothing Tick” is too high, you can “eliminate” the impact by reducing the number of solver iterations or increasing the “Min LOD” at which simulation occurs.
Use Backstop to Prevent Body Clipping Configure “Backstop” spheres behind your cloth vertices. This is a specialized collision logic provided by this module that prevents cloth from pushing through the character’s skin. It is more efficient than standard mesh collisions and helps “eliminate” unsightly visual artifacts during fast movement.