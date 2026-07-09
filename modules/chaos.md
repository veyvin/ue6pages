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

lity destruction, cloth, and hair simulation.

It is primarily used to drive the physical world, including character movement, vehicular physics, and the Geometry Collection system for real-time environmental destruction.

1. Module Configuration

To access Chaos types or extend physics functionality in C++, you must add the module to your Build.cs. Because Chaos is divided into several sub-modules, you often need the core and solvers.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Chaos", "ChaosSolverEngine", "PhysicsCore" });
Copy code
2. Practical Usage Tips & Best Practices
Leverage Async Physics Ticking

Chaos supports Async Physics, which runs simulation logic on its own dedicated thread at a fixed frequency. This “eliminates” physics jitter caused by variable frame rates. To use this effectively in C++, use the OnPhysicsStep callback to apply forces, ensuring your gameplay logic remains deterministic regardless of the rendering FPS.

Optimize with Geometry Collection Clustering

When creating destructible environments, use Clustering. Instead of simulating 1,000 tiny fragments immediately, Chaos groups them into clusters that only break apart when a specific strain threshold is met. This “eliminates” unnecessary CPU overhead by only simulating complex interactions when the player actually destroys an object.

Use Physics Fields for Direct Control

Instead of manually iterating through actors to apply forces, use Physics Fields. These allow you to define regions of space that exert forces, break joints, or “eliminate” the velocity of physical objects. This is much more efficient than traditional “Radial Force” components for large-scale destruction events.

Master the Connection Graph

The Connection Graph determines how pieces of a Geometry Collection “stick” together. By fine-tuning the connection strength, you can create realistic structural integrity (e.g., a building corner stays standing until the base is “eliminated”). Use the DataFlow editor to procedurally generate these graphs for complex assets.

Implement Sleep and Disable States

To maintain high performance in scenes with many physical objects, ensure “Sleep” thresholds are correctly tuned. Chaos can “eliminate” the active simulation of an object once it comes to rest. For debris that the player can no longer reach, use Culling Fields to completely disable or remove the physics state after a certain time.

Optimize Collision Proxies

Complex concave meshes are expensive to simulate. For Chaos, always prefer Convex Hulls or simple primitives (Boxes/Spheres) for collision. In the Geometry Collection editor, use the “Proxy Mesh” setting to “eliminate” high-poly collision data while retaining high-poly visual data, significantly boosting collision detection speed.

Debugging with the Chaos Visual Debugger (CVD)

If objects are falling through the floor or jittering, use the Chaos Visual Debugger. It allows you to record a physics session and scrub through it frame-by-frame to see exactly where a solver conflict occurs. This “eliminates” the guesswork involved in debugging complex physical interactions or ragdoll “explosions.”

Control Damage Propagation

Use the Damage Propagation Factor to control how a shockwave travels through a fractured object. A high propagation value will cause an entire wall to collapse from a single hit, while a low value allows for localized “holes.” Balancing this is key to “eliminating” unrealistic “glass-like” shattering in materials like concrete or wood.