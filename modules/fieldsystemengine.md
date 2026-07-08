---
layout: default
title: FieldSystemEngine
---

<!-- ai-generation-failed -->

<h1>FieldSystemEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/FieldSystem/Source/FieldSystemEngine/FieldSystemEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Chaos, ChaosSolverEngine, Core, CoreUObject, Engine, PhysicsCore, RHI, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

for

Located in Engine/Source/Runtime/FieldSystemEngine, this module manages the containers and logic used to define “Fields.” These are mathematical regions (spheres, boxes, or planes) that apply forces, strain, or state changes to Chaos particles. Unlike traditional physics volumes, Field Systems provide high-frequency, per-particle control over the simulation.

Primary uses include:

Chaos Destruction Control: Breaking Geometry Collections by applying “External Strain” or anchoring pieces in place using “Anchor Fields.”
Dynamic Force Application: Pushing or pulling fractured debris using Radial or Directional forces (Linear/Angular Velocity).
Particle Interaction: Passing spatial data to Niagara systems to influence particle behavior (e.g., dust rising only where a building collapses).
Simulation Management: Using “Disable Fields” to put moving physics objects to sleep, ensuring the elimination of unnecessary CPU overhead from jittering debris.
Practical Usage Tips and Best Practices
1. Choose the Correct Field Lifetime

The module supports three distinct execution methods. Use the right one for your specific goal:

Transient: Created, executed once, and destroyed (e.g., an explosion).
Construction: Set in the Blueprint Construction Script (e.g., static anchors for a building).
Persistent: Evaluated every tick (e.g., a “gravity well” or a permanent wind zone).
2. Master the Use of Culling Fields

To optimize performance, always use a Culling Field (typically a Sphere or Box) to bound your logic. This restricts the math to a specific volume, ensuring the elimination of expensive physics calculations for particles that are outside the intended area of effect.

3. Use “External Strain” for Realistic Breaks

Instead of just applying force to break a Geometry Collection, apply External Strain. If the strain value exceeds the “Damage Threshold” defined in the Geometry Collection, the object will fracture. This allows for more surgical destruction, like a bullet hole, rather than a whole object shattering at once.

4. Optimize with Sleep and Disable Fields

For large-scale destruction, use a Disable Field to stop the simulation of debris once it has settled. This tells the Chaos solver to stop calculating movement for those specific particles, which is critical for maintaining high frame rates in scenes with thousands of fractured pieces.

5. Influence Materials via World Fields

By setting a Field System to “World,” you can sample it inside the Material Editor. This is a best practice for visual polish; for example, you can change the vertex offset or color of a material based on the proximity of a Physics Field, making the environment look “singed” or “impacted” where an explosion occurred.

6. Combine Noise and Falloff

Purely mathematical fields look artificial. Use the NoiseField and UniformScalar nodes to add randomness to your forces. Combining a Radial Falloff with a Perlin Noise modifier creates more organic, jagged destruction patterns that mimic real-world physics.

7. Use Anchor Fields for Structural Integrity

To prevent a building from falling over immediately when the simulation starts, use an Anchor Field in the Construction Script. This marks specific clusters as “Kinematic” (immovable) until a high enough force or strain is applied, allowing you to create stable but destructible structures.

8. Strategic Elimination of Physics Latency

If fields seem to trigger “late,” check the Physics Tick Group. Since Field Systems interact with the Chaos Solver, ensuring your logic runs during the PrePhysics or DuringPhysics phase is essential. For complex interactions, verify that your Field System Component is not set to tick if it only uses Transient fields.