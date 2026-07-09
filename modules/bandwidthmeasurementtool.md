---
layout: default
title: BandwidthMeasurementTool
---

<!-- ai-generation-failed -->

<h1>BandwidthMeasurementTool</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/Experimental/BandwidthMeasurementTool/BandwidthMeasurementTool.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">BandwidthDebugDelegates, Core, CoreUObject, HTTP</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rofiling subsystems) is a specialized utility used to track, analyze, and simulate network traffic in Unreal Engine. It provides high-level data on how much data is being sent and received per frame, broken down by Actor, RPC, and Property.

It is primarily used for Network Optimization, helping developers identify “bandwidth hogs” that may cause lag, packet loss, or high server costs in multiplayer games.

1. Module Configuration

While much of this tool is accessible via console commands, you can interface with it programmatically in your Build.cs to create custom telemetry or automated network performance tests.

C#
	// MyProject.Build.cs

	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "NetCore", "Engine", "NetworkReplayStreaming" });

	}
Copy code
2. Practical Usage Tips & Best Practices
Use the Network Profiler (nprof)

To get a visual breakdown of your bandwidth, use the command netprofile enable. This generates a .nprof file in your Saved/Profiling folder. Open this with the Network Profiler tool (located in Engine/Binaries/DotNET/NetworkProfiler.exe) to see exactly which replicated properties are consuming the most bytes.

Identify “Chatty” RPCs

Check the “All RPCs” tab in the profiler to find functions being called too frequently. If an RPC is firing every tick, it will quickly saturate a client’s downstream. “Eliminate” excessive bandwidth usage by converting frequent RPCs into RepNotify variables, which only send data when the value actually changes.

Leverage Iris for Scalability (UE 5.3+)

If your bandwidth measurement reveals bottlenecks in the legacy replication system, consider enabling Iris. Iris is the next-generation replication system designed to “eliminate” overhead by processing replication in parallel, significantly reducing the bandwidth footprint for games with thousands of networked actors.

Simulate Bandwidth Spikes

Use the console command net.GeneratePeriodicBandwidthSpike <Kb> <Seconds> to stress-test your game’s behavior under poor network conditions. This helps you verify if your game “eliminates” the player experience (via crashes or disconnects) or handles the congestion gracefully through interpolation.

Monitor Replication Graph Performance

If you use the Replication Graph, use the measurement tools to ensure your “Grid Cells” and “Always Relevant” lists are optimized. If too many actors are being gathered for a single connection, your bandwidth per client will spike. Use the tool to find the “sweet spot” for culling distances.

Enable Net Trace for Real-Time Analysis

Use net.Trace 1 (with Unreal Insights enabled) to get a real-time, frame-by-frame view of network packets. This is more granular than the standard profiler and allows you to see the “Packet Overhead” vs. “Actual Content,” helping you “eliminate” waste in your custom NetSerialize implementations.

Optimize Property Replication (Push Model)

If the measurement tool shows that a large actor is being checked for changes every frame even when it hasn’t moved, implement Push Model replication (MARK_DIRTY_CHANNEL). This ensures the engine only spends bandwidth on that actor when you explicitly tell it a change occurred, “eliminating” unnecessary comparison CPU cycles.

Profile on the Server

Always record your bandwidth measurements on the Server (Dedicated or Listen Server). Clients only see the data they receive, whereas the server provides the true “Total Outgoing” bandwidth perspective. Measuring on the server is the only way to accurately predict your hosting costs and maximum player capacity.