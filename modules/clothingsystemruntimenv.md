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

Engine has moved toward Chaos Cloth as the default, this module remains in the engine to maintain backward compatibility for older projects and to support pipelines specifically optimized for NVIDIA’s cloth solvers.

Practical Usage Tips and Best Practices
1. Understand the 32-Collider Limit

One of the most critical constraints of the NVCloth system is the collision budget. It has a hard limit of 32 collision objects per cloth asset. Exceeding this limit can cause unpredictable behavior or result in specific body parts (like legs or arms) losing collision entirely. To eliminate this issue, only assign the most essential capsules and spheres in the Physics Asset to the cloth simulation.

2. Use Tapered Capsules for Limbs

When setting up collisions for NVCloth, prioritize Tapered Capsules over standard capsules. Standard capsules have a uniform radius, which often leads to clipping at the wrists or ankles. Tapered capsules allow for different radii at each end, providing a much tighter fit to the character’s geometry and reducing the chance of the cloth penetrating the mesh.

3. Optimize the Simulation Mesh (Sim Mesh)

The mesh you simulate does not have to be the high-poly mesh you render. Use the Clothing Proxy workflow to simulate a lower-resolution version of the garment. This reduces the number of particles the NV solver must process each frame, which is the most effective way to eliminate performance bottlenecks in scenes with multiple clothed characters.

4. Balance “Max Distance” and “Backstop”

The Max Distance mask controls how far a vertex can move from its skinned position, while Backstop prevents vertices from moving into the character. A common mistake is setting Max Distance too high without a proper Backstop. Always paint a Backstop distance and radius to ensure that even during fast movement, the cloth is pushed away from the body rather than clipping through it.

5. Monitor Performance with “Stat Cloth”

Use the console command stat cloth to monitor the CPU time spent on NVCloth simulations. If you see high MS (milliseconds) values, check if you have multiple characters on screen simulating high-vertex-count garments. Consider using Cloth LODs to disable simulation entirely at long distances, switching to standard skinning to save resources.

6. Utilize Wind Directional Sources

NVCloth reacts natively to the Wind Directional Source actor. To make clothing feel more realistic, add a wind actor to your level and tune the “Strength” and “Speed” parameters. In the cloth asset settings, you can adjust the Wind Adaptation value to control how much the fabric catches the breeze, which adds life to capes and loose garments without extra animation work.

7. Handle Transitions during Elimination

When a character is eliminated, it often transitions from a kinematic animation state to a ragdoll. Ensure that your cloth settings are tuned to handle these sudden changes in velocity. If the cloth “explodes” upon elimination, it is usually due to high stretch stiffness or collision overlaps. Lowering the stiffness slightly can help the cloth settle naturally as the character’s body falls.

8. Plan for Migration to Chaos

Since NVCloth is a legacy system, it is a best practice to evaluate a migration to the Chaos Cloth system (handled by the ClothingSystemRuntimeCommon and ChaosCloth modules). Chaos offers unlimited collision objects and better integration with the modern physics pipeline. While ClothingSystemRuntimeNv is stable, new features and performance optimizations are primarily targeted at the Chaos solver.