---
layout: default
title: IrisCore
---

<!-- ai-generation-failed -->

<h1>IrisCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Net/Iris/IrisCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, NetCore, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

l Engine’s modern, high-performance replication system. Introduced to address the limitations of the legacy OOD (Object Oriented Design) replication, IrisCore provides a “push-based” architecture designed to scale to massive player counts (100+) and highly interactive worlds.

Its primary purpose is to “eliminate” the CPU bottlenecks associated with the traditional replication system, which relies on polling every replicated actor every frame. Instead, IrisCore uses a data-centric approach that separates game thread data from replication data, significantly reducing server frame times and memory overhead.

Practical Usage Tips and Best Practices
Explicitly Enable in Target and Build Files
Iris is opt-in and is not active by default in the runtime. You must set bUseIris = true; in your project’s *.Target.cs file and call SetupIrisSupport(Target); in your *.Build.cs file. This “eliminates” the inclusion of the legacy replication path for those modules.
Switch to Push Model Replication
To gain the full performance benefits of IrisCore, you must enable the Push Model. Set net.IsPushModelEnabled=1 and net.Iris.PushModelMode=1 in your DefaultEngine.ini. This “eliminates” the need for the engine to poll properties, as the system is only notified when data actually changes.
Utilize Iris Filtering and Prioritization
IrisCore replaces the legacy AActor::IsNetRelevantFor() with a new NetObjectFilter API. Instead of using virtual functions that are called thousands of times, use the Iris API to set static filters or dynamic prioritizers. This “eliminates” redundant relevancy checks on the game thread.
Handle Custom Struct Serialization
If you have structs with custom NetSerialize functions, IrisCore will log a warning because it prefers reflection-based descriptors. To “eliminate” these warnings, add your structs to the SupportsStructNetSerializerList in DefaultEngine.ini under [/Script/IrisCore.ReplicationStateDescriptorConfig].
Beware of Replication Graph Incompatibility
IrisCore and the Replication Graph plugin are mutually exclusive. You cannot use both simultaneously. If you are migrating a project, you must “eliminate” your Replication Graph implementation and replace its logic with Iris Prioritizers and Filters.
Use NetUpdateFrequency Sparingly
In IrisCore, polling frequency is handled differently than in the legacy system. Because the system is push-based, setting high update frequencies on objects that don’t change often won’t hurt performance as much, but you should still tune frequencies to “eliminate” unnecessary packet overhead.
Verify with Iris-Specific Debugging
IrisCore includes specialized console commands for profiling. Use net.Iris.ShowDiagnostics 1 to visualize how objects are being replicated. This “eliminates” the guesswork when trying to determine why a specific actor is not appearing on the client or is consuming too much bandwidth.
Implement BeginReplication Overrides
When using Iris, you should use the BeginReplication lifecycle event to set up your filters (e.g., bAlwaysRelevant, bOnlyRelevantToOwner). This “eliminates” the need for per-frame logic, as the Iris system caches these states to process replication more efficiently in the background.