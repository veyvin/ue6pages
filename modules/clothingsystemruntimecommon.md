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

ng simulation meshes, property masks, and the weight-mapping data that tells the solver which parts of a mesh should behave like cloth versus which should stay attached to the character.

By providing a common interface for cloth data, it “eliminates” the need for different solvers to reimplement basic concepts like max distance, backstops, and tethering logic.

Practical Usage Tips and Best Practices
Implement LOD-Specific Sim Meshes
A best practice is to provide a simplified simulation mesh for lower LODs (Levels of Detail). Using the common runtime to swap to a lower-resolution sim mesh as the character moves away will “eliminate” significant CPU overhead while maintaining the visual silhouette of the clothing.
Master the Max Distance Mask
The “Max Distance” parameter is the most critical for performance. Any vertex with a value of 0 is effectively “eliminated” from the physics simulation and follows the skeletal animation perfectly. Use this for belts, collars, or waistbands to keep them stable while allowing the rest of the garment to flow.
Utilize Backstops to Prevent Clipping
Use the Backstop properties to “eliminate” the common issue of cloth clipping into the character’s body. A Backstop creates a virtual “safety sphere” behind each vertex based on its skinned position, preventing the cloth from moving too far inward toward the mesh.
Use Long Range Attachments (Tethers)
If your cloth appears to stretch unnaturally during fast movement, enable Long Range Attachments. This logic “eliminates” excessive stretching by creating a virtual tether between a simulated vertex and a fixed kinematic vertex, ensuring the cloth doesn’t “grow” beyond its intended length.
Optimize Collision Capsules
The common runtime works best when colliding against simple primitives. In the character’s Physics Asset, “eliminate” complex convex hulls in favor of Tapered Capsules for limbs. Tapered Capsules are specifically supported by the clothing system and are much more performance-efficient than standard capsules.
Check “Remove from Mesh” for Overlapping Geometry
When creating a cloth asset from a section of a skeletal mesh, you can enable “Remove from Mesh.” This “eliminates” the original rendering of those triangles from the base skeletal mesh, preventing Z-fighting between the simulation mesh and the original static pose.
Monitor Performance with Stat Commands
Use the console command stat ChaosCloth to see a real-time breakdown of simulation time. If a single character’s clothing is taking too long to solve, “eliminate” complexity by reducing the number of simulation particles or lowering the iteration count in the Cloth Config.
Leverage Multi-Threaded Simulation
The runtime is designed to run in parallel. Ensure that “Allow Parallel Cloth Task” is enabled in your Project Settings. This allows the engine to “eliminate” bottlenecks on the Game Thread by moving the clothing solver to available worker threads on the CPU.