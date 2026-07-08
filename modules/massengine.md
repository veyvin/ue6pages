---
layout: default
title: MassEngine
---

<!-- ai-generation-failed -->

<h1>MassEngine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Mass/MassEngine/MassEngine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Chaos, Core, CoreUObject, Engine, MassCore, MassEntity, MassSignals, RHI, RenderCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine’s highly optimized, data-oriented calculation system. While the MassEntity module provides the raw ECS (Entity Component System) architecture, the MassEngine module integrates this framework into the engine’s main loop and world systems.

It is primarily used for managing Mass Processors, handling the execution phases (how and when logic runs), and bridging the gap between data-oriented “Fragments” and the standard Unreal World. This module is the engine that drives thousands of autonomous agents, such as the crowds and traffic seen in The Matrix Awakens demo, helping you eliminate the CPU bottlenecks associated with traditional Actor-based ticking.

Practical Usage Tips and Best Practices
Group Processors into Phases
Mass logic is organized into Processing Phases (e.g., PrePhysics, DuringPhysics, PostPhysics). Use the MassEngine settings to place your logic in the correct phase. This helps you eliminate race conditions by ensuring that movement logic occurs before collision checks and visual updates.
Leverage Entity Queries for Cache Efficiency
In your C++ processors, use FMassEntityQuery to request only the specific Fragments you need. By processing small, contiguous blocks of data, you eliminate “cache misses,” allowing the CPU to process thousands of entities significantly faster than individual AActor ticks.
Use Traits for Modular Configuration
Instead of hard-coding entity logic, use Mass Traits in a MassEntityConfigAsset. Traits allow you to add “packages” of Fragments and Processors to an entity via the editor. This modularity helps you eliminate monolithic classes and makes it easy for designers to swap behaviors without C++ changes.
Batch Commands via MassCommandBuffer
If a processor needs to add a Tag or delete an entity (an “elimination” event), do not do it immediately. Use the FMassCommandBuffer. Commands are queued and executed at the end of the phase, which helps you eliminate memory corruption and iterator invalidation while looping through entities.
Utilize Tags for State Filtering
Tags are empty Fragments used as “flags.” Instead of checking a boolean inside a Fragment, use a Tag (e.g., FMassIsDeadTag). You can then configure your Processor’s query to skip any entity with that tag, which helps you eliminate unnecessary calculations for inactive or “eliminated” agents.
Avoid Using UObjects in Fragments
Fragments should ideally be “Plain Old Data” (POD) structs. Avoid placing UObject pointers inside Fragments, as the Garbage Collector can struggle with the sheer volume of Mass data. Keeping Fragments as simple math types helps you eliminate GC-related hitches and maintains high performance.
Optimize with Chunk Fragments
For data shared by all entities in a specific memory chunk (like a shared “Global Wind Direction”), use a Chunk Fragment. This allows every entity in that chunk to read the same memory address, helping you eliminate redundant data storage across thousands of individual agents.
Debug with ‘Mass Visualizer’
When testing thousands of entities that don’t have Actors, use the Mass Debug Visualization trait. This draws simple shapes (like cones or boxes) in the viewport to represent your entities. This visibility allows you to eliminate logic bugs in your simulation before you commit to high-fidelity mesh rendering.