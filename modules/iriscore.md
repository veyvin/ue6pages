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

ration networking framework. Introduced as a high-performance alternative to the legacy replication system, Iris is designed to handle massive player counts and dense, interactive worlds (such as those in Fortnite).

Iris transitions from a polling-based model to a fully push-based, data-oriented architecture. It separates gameplay data from the replication internal state, using a “Replication Bridge” to marshal data. This allows the engine to eliminate the expensive overhead of per-object virtual function calls during serialization and significantly reduces server CPU usage.

Practical Usage Tips and Best Practices
Enable via Target and Build Files
To use Iris, you must opt-in by adding bUseIris = true; to your project’s *.Target.cs file. Additionally, call SetupIrisSupport(Target); in your *.Build.cs to eliminate manual dependency management and ensure the correct private and public modules are linked.
Transition to Push-Model Replication
While Iris can poll for changes, it is optimized for the Push Model. Use the MARK_PROPERTY_DIRTY_FROM_NAME macros or similar patterns to notify the system only when data actually changes. This helps you eliminate the CPU cost of scanning thousands of actors every frame to see if their properties are “dirty.”
Implement Custom Filters and Prioritizers
Iris replaces the “Replication Graph” with a more modular system of Filters and Prioritizers (found in NetObjectFilter.h and NetObjectPrioritizer.h). Use these to define exactly which connections should receive specific actors (e.g., a “Team-Only” filter), which helps eliminate unnecessary network traffic to irrelevant clients.
Leverage Quantization for Efficiency
Iris performs Quantization (transforming source data into a network-ready format) once per object per update, rather than once per connection. Ensure your custom data types implement efficient quantization logic to eliminate redundant calculations when sending the same data to 100 different players.
Avoid Virtual Function Overrides for Networking
In Iris, logic previously handled by virtual functions like GetNetPriority() or IsNetRelevantFor() is moved to the API. Shift your logic to the BeginReplication() setup phase to eliminate the performance penalty of per-frame virtual calls across thousands of replicated objects.
Use Unreal Insights for Network Profiling
Iris is deeply integrated with Unreal Insights. Use the “Networking” traces to visualize exactly how much bandwidth each “Replication Fragment” is consuming. This visibility allows you to eliminate bandwidth spikes caused by unoptimized property updates or oversized arrays.
Ensure NetRefHandle Validity
When interacting with the Iris API, you will often use FNetRefHandle instead of direct Actor pointers. Always validate these handles before use to eliminate null-pointer crashes in asynchronous or multi-threaded networking code.
Verify Sub-Object Replication
Iris handles sub-objects (like components or custom UObjects) more strictly than the legacy system. Ensure your sub-objects are correctly registered with the replication bridge during the Actor’s initialization to eliminate “missing data” bugs on the client side.