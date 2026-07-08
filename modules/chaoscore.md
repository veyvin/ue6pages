---
layout: default
title: ChaosCore
---

<!-- ai-generation-failed -->

<h1>ChaosCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/ChaosCore/ChaosCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, IntelISPC</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

osCore provides the base architectural components. This includes core types for particles, evolution (the “solver” logic), spatial acceleration structures (AABBs), and foundational math utilities. It is designed to be a high-performance, multithreaded framework that manages how physical data is stored and updated over time. Effectively, it is the “engine within the engine” for physical calculations.

Practical Usage Tips and Best Practices
1. Minimize Raw Access to Particles

In the Chaos architecture, physical entities are represented as “Particles.” While ChaosCore provides the headers to access these, you should generally interact with them through the FPhysicsCommand or FChaosScene interfaces. Direct, uncontrolled access to core particles can lead to race conditions since Chaos runs on its own async physics thread.

2. Optimize Broad Phase with Proper Mobility

Chaos uses spatial structures defined in this module to determine which objects might be colliding. To keep the Broad Phase efficient, ensure all non-moving objects are set to Static. This allows ChaosCore to place them in a stable AABB tree that doesn’t require constant refitting, significantly reducing CPU overhead.

3. Tune Iteration Settings for Stability

The accuracy of the physics solver is determined by the Position and Velocity iterations (configured in Project Settings but executed via ChaosCore logic). If you notice “jitter” or objects clipping through floors, increasing these counts slightly can help. However, keep them as low as possible to eliminate unnecessary performance hits.

4. Use the Chaos Visual Debugger (CVD)

Because ChaosCore handles the “hidden” math of physics, debugging can be difficult. Use the Chaos Visual Debugger (Tools > Chaos Visual Debugger) to record a simulation. This tool allows you to scrub through time and see the exact contact points and constraints that ChaosCore is calculating, which is essential for troubleshooting unstable simulations.

5. Leverage Sleep Thresholds

To save CPU cycles, Chaos puts objects to “sleep” when their linear or angular velocity falls below a certain threshold. If you have many small debris items, ensure their sleep thresholds are tuned correctly. This allows ChaosCore to stop updating those particles, which helps eliminate performance bottlenecks in scenes with many simulated objects.

6. Profile with “Stat Chaos” Commands

Use the console command stat Chaos or stat ChaosCounters to see a real-time breakdown of what the core is doing. This shows the number of active particles, collision contacts, and joint constraints. Monitoring these counters is the best way to identify when a specific scene has become too physically complex for the target hardware.

7. Handle Safe Cleanup on Elimination

When an Actor or Component is eliminated from the game world, the corresponding physical proxy in ChaosCore must be removed. In C++, always ensure you are calling the appropriate destruction methods on your physics handles. Improper cleanup of Chaos particles during an actor’s elimination can lead to “ghost collisions” where objects hit invisible remnants of deleted actors.

8. Prefer Async Physics for Consistency

For high-precision gameplay (like vehicles or fighting games), enable Async Physics. This allows ChaosCore to run at a fixed tick rate independent of the variable game frame rate. This ensures that physics-heavy events—like the physics-driven elimination of a destructible wall—behave identically regardless of whether the player is running at 30 FPS or 120 FPS.