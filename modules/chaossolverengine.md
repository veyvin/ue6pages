---
layout: default
title: ChaosSolverEngine
---

<!-- ai-generation-failed -->

<h1>ChaosSolverEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/ChaosSolverEngine/ChaosSolverEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ChaosVDRuntime, Core, CoreUObject, DataflowCore, DataflowEngine, DataflowSimulation, DeveloperSettings, Engine, Messaging, RHI, RenderCore, RigidPhysics, TraceBasedDebuggers</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

gh-level framework (Actors and Components) and the low-level Chaos Physics library. It provides the engine-side implementation for managing physical simulations, handling the lifecycle of the physics solver, and exposing solver settings to the Editor and Blueprints.

While the Chaos module contains the raw math and simulation logic, ChaosSolverEngine defines the AChaosSolverActor, which allows developers to create specialized physics “islands” with unique properties (like different gravity or tick rates) within a single level.

1. Optimize with Solver Iterations

The solver’s accuracy and stability are determined by its iteration counts (Position, Velocity, and Projection).

Best Practice: For performance-heavy scenes, lower the Position Iterations (default 8) and Velocity Iterations (default 1). If you have complex joint chains or ragdolls that jitter, increase these values specifically on a dedicated Solver Actor rather than globally.
2. Leverage Dedicated Solver Actors

By default, all physics objects use the “World Solver.” However, you can place a ChaosSolverActor in your level and assign specific actors to it.

Tip: Use a dedicated solver for localized, high-fidelity physics (like a complex machine or a hero destruction event). This isolates the performance cost and allows you to use higher quality settings without affecting the rest of the world.
3. Tuning Sleep Thresholds

Chaos puts objects to “sleep” when their movement falls below a certain velocity to save CPU cycles.

Best Practice: Adjust the Linear Sleep Threshold and Angular Sleep Threshold in the Solver settings. Increasing these values will eliminate micro-jitters in resting objects and improve performance by putting bodies to sleep sooner.
4. Use Async Physics Ticking

Unreal Engine 5 supports “Async Physics,” which runs the simulation on its own thread at a fixed frequency, independent of the game’s frame rate.

Tip: Enable p.Chaos.Thread.DesiredHz (usually set to 60 or 120). This ensures physics behavior remains consistent even if the game’s rendering frame rate fluctuates, which is critical for vehicles and competitive gameplay.
5. Debug with Chaos Visual Debugger (CVD)

The Chaos Visual Debugger (found in Tools > Chaos Visual Debugger) is the most powerful way to inspect this module’s output.

Best Practice: Use CVD to record a simulation and step through it frame-by-frame. You can see every collision contact, constraint force, and “island” partition, allowing you to identify exactly why a simulation is underperforming or exploding.
6. Control Substepping for High-Speed Objects

If fast-moving objects are tunneling through walls, you may need substepping.

Tip: Instead of enabling substepping globally, use the Solver’s Async Physics mode. Because it runs at a fixed, high frequency (e.g., 120Hz), it inherently provides the benefits of substepping by checking for collisions more frequently than the render thread.
7. Manage Collision Cull Distance

The solver checks for potential collisions within a certain radius.

Best Practice: Lower the Collision Cull Distance in the project settings or solver properties. This reduces the number of “Narrow Phase” collision checks the solver has to perform each tick, significantly improving performance in dense environments.
8. Use Continuous Collision Detection (CCD) Sparingly

While CCD prevents fast objects from passing through geometry, it is computationally expensive for the solver.

Tip: Only enable CCD on the specific MeshComponent of high-speed projectiles or hero characters. Never enable it globally on the solver unless your game logic relies entirely on high-speed physical interactions. Use MACD (Motion-Aware Collision Detection) for a more performant middle-ground.