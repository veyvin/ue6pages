---
layout: default
title: MassSignals
---

<!-- ai-generation-failed -->

<h1>MassSignals</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Mass/MassSignals/MassSignals.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rk designed to provide a decoupled signaling system for Mass entities. Unlike traditional event systems that rely on direct object references or expensive per-frame polling, MassSignals allows a system to “notify” an entity that a specific event has occurred.

It is primarily used as a performance optimization tool to “wake up” specific processors or state machines (like Mass StateTree) only when necessary. By using named signals, you can trigger entity logic based on specific gameplay events—such as a player entering a radius or an agent reaching a destination—which helps you eliminate the CPU overhead of constantly checking conditions for thousands of entities every tick.

Practical Usage Tips and Best Practices
Subscribe Processors to Signal Names
In your UMassProcessor, use the FMassSignalName to subscribe to specific signals during initialization. This allows the MassEngine to skip your processor’s execution for a specific entity until that signal is explicitly raised, helping you eliminate wasted processing cycles on idle agents.
Use Signals to Drive StateTree Transitions
MassSignals is the primary mechanism for “waking up” a Mass StateTree. Instead of the StateTree evaluating its transition logic every frame, you can send a signal to the entity to force an immediate re-evaluation. This is essential to eliminate latency in AI reactions while keeping the simulation performant.
Access the MassSignalSubsystem in C++
To send a signal, retrieve the UMassSignalSubsystem from the world. Use the SignalEntity or SignalEntities (for batching) functions. Batching signals to multiple entities at once is a best practice to eliminate redundant function call overhead when an area-of-effect event occurs.
Avoid Overusing Unique Signal Names
Keep your FMassSignalName entries standardized (e.g., “DamageReceived”, “TargetLost”). Using a massive variety of unique strings can increase the overhead of the internal signal-tracking map. Reusing common signal names across different systems helps you eliminate memory fragmentation and keeps the signaling pipeline lean.
Combine with Tags for Logical Filtering
When a signal is received, your processor will run on that entity. Use Mass Tags (like FHasPendingActionTag) as a filter in your query to ensure that the processor only acts on the entities that actually require a state change. This dual-layer approach helps you eliminate “false positive” processing.
Eliminate Per-Frame Distance Checks
Instead of having 5,000 entities constantly check their distance to the player, use a single spatial query (like a Trigger Volume or an EQS query) to send a signal to entities as they enter the player’s vicinity. This shift from polling to signaling helps you eliminate one of the most common bottlenecks in large-scale AI.
Monitor Signal Traffic with ‘stat mass’
Use the console command stat mass or stat MassSignals to monitor how many signals are being dispatched per frame. If you see a massive spike in signal counts, it may indicate a “signaling loop” where processors are repeatedly triggering each other. High visibility here allows you to eliminate logic recursion bugs.
Prefer Signals over Fragment Data Changes for Triggers
While you could change a boolean in a Fragment to trigger behavior, that requires a processor to constantly read that Fragment to see the change. Raising a signal is more efficient because it tells the engine exactly which entity needs attention, allowing you to eliminate “read-heavy” polling loops.