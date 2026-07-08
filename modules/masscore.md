---
layout: default
title: MassCore
---

<!-- ai-generation-failed -->

<h1>MassCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Mass/MassCore/MassCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

, Unreal Engine’s highly optimized, data-oriented Entity Component System (ECS). It is designed to handle the simulation of tens of thousands of agents or objects with minimal CPU overhead.

What it is and What it’s used for

Located in Engine/Source/Runtime/MassCore, this module implements the core ECS architecture. It replaces the traditional “one Actor per object” approach with Entities (IDs), Fragments (pure data structs), and Processors (logic that operates on batches of data).

Primary uses include:

Massive Crowd Simulation: Running AI logic and movement for thousands of characters, as seen in the Matrix Awakens city sample.
High-Performance Calculations: Performing stateless, parallel operations on large datasets that would otherwise choke the AActor ticking system.
Data-Oriented Design (DOD): Ensuring data is stored contiguously in memory (“Chunks”) to maximize CPU cache hits and minimize memory latency.
Practical Usage Tips and Best Practices
1. Keep Fragments Small and POD-like

Fragments are the “Components” of the Mass system. A best practice is to keep these structs as small as possible and avoid using UObject pointers inside them. Small, Plain Old Data (POD) structs ensure that more entities fit into a single CPU cache line, leading to the elimination of memory access bottlenecks.

2. Minimize Logic in Processors

Mass Processors should be stateless and focused on tight loops. Avoid heavy C++ branching or complex object-oriented patterns inside the Execute function. Moving complex decision-making to StateTrees while keeping the Processor for raw data updates helps in the elimination of CPU stalls.

3. Leverage Tags for Efficient Filtering

Use Mass Tags (empty fragments) to categorize entities (e.g., FIsWalkingTag, FIsEliminatedTag). The Mass system can filter archetypes based on these tags at the “Chunk” level. This allows the engine to skip entire blocks of memory that don’t match the query, resulting in the elimination of wasted processing cycles.

4. Use Command Buffers for Structural Changes

Structural changes (adding/removing fragments or the elimination of an entity) are expensive because they move data between archetypes. Always use the FMassCommandBuffer to queue these changes. This ensures the engine performs all moves in a single batch at the end of the frame, leading to the elimination of redundant memory reallocations.

5. Avoid Tick Whenever Possible

Even in Mass, constant ticking has a cost. Use the Mass Signals system to wake up entities only when an event occurs (like receiving damage). Transitioning from a polling-based model to a signal-based model is a primary strategy for the elimination of idle CPU usage.

6. Optimize Archetype Composition

An “Archetype” is defined by the unique combination of fragments an entity possesses. Having too many unique archetypes with only a few entities each reduces the efficiency of the ECS. Aim for common fragment combinations to ensure the elimination of fragmented memory chunks.

7. Use Pure Processors for Parallelization

If your processor does not depend on the results of other Mass systems in the same phase, mark it as “Pure.” This allows the Mass Executor to run the processor in parallel across multiple threads. This is essential for the elimination of frame-time spikes in projects with extreme entity counts.

8. Monitor Performance via Mass Debugger

Use the mass.Debug console commands and the Mass Debugger tool in the editor. These tools allow you to visualize entity counts and archetype distribution. Regular monitoring is a best practice for the elimination of “data bloat” and identifying processors that are consuming more time than expected.