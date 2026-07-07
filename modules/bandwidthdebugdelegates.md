---
layout: default
title: BandwidthDebugDelegates
---

<!-- ai-generation-failed -->

<h1>BandwidthDebugDelegates</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/Experimental/BandwidthDebugDelegates/BandwidthDebugDelegates.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ty module that provides a centralized system of delegates for tracking and reacting to bandwidth telemetry. Instead of requiring developers to poll the UNetDriver or manually parse network logs, this module exposes broadcast events that trigger when specific bandwidth thresholds are met or when network traffic data is updated.

It is primarily used to build custom in-game performance HUDs, telemetry logging systems, or adaptive quality systems that can eliminate network congestion by lowering game fidelity when a player’s bandwidth is throttled.

Practical Usage Tips and Best Practices
1. Add to Build Dependencies

To use these delegates in your C++ classes, you must include the module in your Build.cs. It is generally used in Client or Editor builds and is often omitted from specialized Server builds to save memory.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.Add("BandwidthDebugDelegates");
Copy code
2. Implement Adaptive Quality Logic

Use the delegates to trigger “Lite” versions of gameplay effects when bandwidth is restricted.

Best Practice: Bind a function to the bandwidth update delegate to toggle the visibility of cosmetic actors or high-frequency VFX. By eliminating non-essential traffic during high-latency spikes, you preserve the reliability of critical gameplay RPCs.
3. Create Custom Debug Overlays

While Unreal has built-in stat net commands, they are not always accessible to QA or end-users on consoles.

Tip: Use this module’s delegates to feed a UMG-based “Network Health” widget. This allows non-technical testers to report bandwidth usage and packet information without needing to open the console or use external profiling tools.
4. Monitor for Bandwidth “Saturation”

The module is excellent for detecting when the NetServerMaxTickRate or MaxClientRate is being exceeded.

Best Practice: If a delegate reports that the outbound buffer is consistently full, trigger a logic check to eliminate redundant property replication (e.g., increasing the NetUpdateFrequency of distant actors).
5. Integrate with Network Insights

This module works in tandem with Unreal Insights (Networking Insights).

Tip: Use the delegates to “mark” the network stream when specific gameplay events occur (like a large explosion). This makes it easier to find those specific frames in a .utrace file, helping you identify which replicated properties are consuming the most bits.
6. Bind/Unbind During Level Transitions

Network drivers are often torn down and recreated during a “Seamless Travel” or level load.

Best Practice: Always ensure you unbind your custom functions from these delegates when an actor is being eliminated or when the EndPlay event is called. Failing to unbind can lead to “hanging” delegates that attempt to call code on garbage-collected objects.
7. Use for Automated Stress Testing

In an automation environment, you can use these delegates to validate that a new feature doesn’t exceed a “Bandwidth Budget.”

Action: Create a functional test that monitors the bandwidth delegate during a high-action scene. If the bits-per-second exceed your budget, the test can automatically fail the build, eliminating the risk of shipping a network-heavy update.
8. Verify Packet Overhead

The delegates provide insights into “overhead” (packet headers) versus “payload” (your actual data).

Tip: If the overhead is significantly higher than the payload, it indicates that you are sending too many small “bunches.” Use this information to combine multiple RPCs into a single struct or array to eliminate redundant header data in the stream.