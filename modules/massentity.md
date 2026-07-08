---
layout: default
title: MassEntity
---

<!-- ai-generation-failed -->

<h1>MassEntity</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MassEntity/MassEntity.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

iented Entity Component System (ECS). It is designed to handle the simulation of tens of thousands of entities simultaneously by decoupling data from logic.

Instead of using heavy AActor objects, MassEntity uses Entities (IDs), Fragments (minimal data structs), and Processors (logic that operates on batches of Fragments). This architecture facilitates the elimination of CPU bottlenecks associated with traditional Object-Oriented programming, making it ideal for large-scale crowds, traffic systems, and complex environmental simulations.

Practical Usage Tips and Best Practices
1. Group Fragments into Archetypes

MassEntity automatically groups entities with the same set of fragments into Archetypes. To ensure the elimination of memory fragmentation, try to keep your fragment compositions consistent. Entities in the same Archetype are stored contiguously in memory “Chunks,” which maximizes CPU cache hits during processing.

2. Use “Assorted Fragments” for Requirements

When creating a Mass Entity Config Asset, you may encounter validation errors where a trait requires a specific piece of data (like a TransformFragment). Use the Assorted Fragments Trait to manually add these missing fragments. This practice leads to the elimination of “Missing Fragment” crashes when the simulation begins.

3. Batch Changes with the CommandBuffer

Never modify an entity’s composition (adding/removing fragments or tags) directly inside a processor’s main loop. Instead, use the MassCommandBuffer. The server will batch these requests and execute them between processing phases, which assists in the elimination of data corruption and race conditions during multi-threaded execution.

4. Leverage Tags for Efficient Filtering

Use Tags (empty fragments) to represent states like bIsEliminated, bIsMoving, or bIsWaiting. Processors can use these tags in their EntityQuery to instantly include or exclude large groups of entities. This facilitates the elimination of expensive branch logic (if-statements) inside your heavy simulation loops.

5. Minimize “Tick” with StateTrees

Avoid running complex logic every frame in a Mass Processor. Instead, use the StateTree module in conjunction with Mass. This allows entities to stay “dormant” until a specific event occurs, leading to the elimination of unnecessary CPU cycles for agents that aren’t currently performing meaningful actions.

6. Optimize with ChunkFragments

If you have data that is identical for every entity in a specific memory chunk (such as a shared weather constant or a global gravity multiplier), use a ChunkFragment. Reading data once per chunk rather than once per entity leads to the elimination of redundant memory access and improves overall throughput.

7. Validate Configs Before PIE

Always use the Validate Entity Config button within your Mass Entity Config Assets. This built-in tool checks for dependency cycles and missing required fragments. Regular validation is a best practice for the elimination of “silent failures” where entities spawn but fail to move or render because of a configuration error.

8. Use Mass LOD for Visualization

To maintain high frame rates, use the MassLODCollectorProcessor. This system calculates the distance between the camera and entities, allowing you to swap between high-detail actors, low-detail static meshes, or simple vertex animation textures. This leads to the elimination of rendering bottlenecks when displaying thousands of agents on screen.