---
layout: default
title: Chaos
---

<!-- ai-generation-failed -->

<h1>Chaos</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/Chaos/Chaos.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AutoRTFM, ChaosCore, ChaosVDRuntime, Core, CoreUObject, Eigen, GeometryCore, IntelISPC, MeshDescription, NNE, TraceBasedDebuggers, TraceLog, Voronoi</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ruction engine, introduced as the successor to PhysX. It is a highly integrated, multi-threaded physics solver designed to handle large-scale simulations, rigid body dynamics, cloth, and cinematic-quality destruction.

In UE5, Chaos is the default physics engine. It powers everything from basic collision detection and character movement to complex Geometry Collections that can be fractured and destroyed in real-time.

Practical Usage Tips and Best Practices
1. Implement Geometry Collections for Destruction

To utilize Chaos destruction, you must convert static meshes into Geometry Collections. Use the Fracture Mode in the editor to define how the mesh breaks. This process creates a hierarchy of clusters, allowing the engine to optimize performance by only simulating the broken pieces when necessary.

2. Manage Performance with Chaos Fields

Use Chaos Fields (such as Anchor, Force, or Sleep fields) to control the behavior of simulated objects procedurally. For example, placing a Sleep Field on a pile of debris can force the elimination of active physics calculations once the objects settle, significantly saving CPU cycles in dense scenes.

3. Optimize via Build.cs Dependencies

When working with Chaos in C++, you must include the correct modules in your Build.cs. Depending on your needs, you might require Chaos, ChaosSolverEngine, and GeometryCollectionEngine.

C#
PublicDependencyModuleNames.AddRange(new string[] { "Chaos", "ChaosSolverEngine", "PhysicsCore" });
Copy code
4. Utilize the Chaos Visual Debugger (CVD)

For complex physics issues, open Tools > Chaos Visual Debugger. This tool allows you to record a physics simulation and scrub through it frame-by-frame. It is essential for identifying the cause of “explosive” jitter or finding why a specific collision failed to trigger an elimination event on a destructible actor.

5. Leverage Async Physics Ticking

In Project Settings, you can enable Async Physics. This runs the Chaos simulation on its own dedicated thread, separate from the Game Thread. This results in the elimination of physics-induced hitches on the main thread and provides a smoother, more consistent simulation frequency (e.g., a fixed 60Hz).

6. Use Simple Collision Proxies

For high-fidelity meshes, avoid using the “Use Complex Collision as Simple” setting. Instead, use the Physics Asset Editor to create a chain of simple primitives (spheres, capsules, boxes). This reduces the number of contact points the Chaos solver must process, which is vital for maintaining performance during character movement.

7. Control Destruction with Connection Graphs

Chaos uses Connection Graphs to determine how chunks of a fractured object are physically attached. By adjusting the “Damage Threshold” and “Connection Type,” you can ensure that structures don’t collapse too easily, allowing for a realistic “peeling” effect where only the impacted area undergoes elimination.

8. Optimize Cloth with Proxy Meshes

For character cloth simulation, never simulate the high-poly render mesh directly. Instead, create a low-resolution “Proxy” mesh that follows the same skinning. The Chaos Cloth solver will handle the low-poly physics and transfer the results to the high-poly mesh, preventing the elimination of your frame rate during heavy action sequences.