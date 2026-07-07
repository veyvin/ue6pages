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

t plugin) is a specialized utility within Unreal Engine designed to track and report the amount of data transmitted over the network during a game session. It provides a structured way to measure real-time bandwidth consumption, specifically for identifying spikes in traffic caused by replication and RPCs.

It is primarily used by network engineers to profile multiplayer performance, establish baseline bandwidth requirements for different game states, and debug “network saturation” issues where too much data is being sent at once.

Practical Usage Tips and Best Practices
1. Enable via Plugin and Command Line

This module is typically disabled by default to save resources. To use it, you must enable the Bandwidth Measurement plugin in the editor. Once enabled, you can start a recording session by passing -bandwidthmeasurement=true as a command-line argument when launching your server or client.

2. Monitor via the Network Profiler

The data captured by this module is best viewed using the Network Profiler (found in Engine/Binaries/DotNET/NetworkProfiler.exe). It allows you to see exactly which actors or properties are responsible for the most traffic, helping you focus your optimization efforts on the “heaviest” objects.

3. Use “stat net” for Real-Time Overviews

While the BandwidthMeasurementTool provides deep historical data, you can use the stat net console command for a high-level, real-time look at current bandwidth usage. This is useful for identifying the immediate impact of specific gameplay actions, such as spawning a large group of enemies or triggering a complex RPC.

4. Identify Burst Traffic

One of the best uses of this tool is the elimination of network hitches by identifying “bursts.” If your bandwidth graph shows sharp, vertical spikes, it often indicates that too many actors are losing “Dormancy” at the same time. Use the tool to find which frame the spike occurred and cross-reference it with your gameplay logic.

5. Optimize via NetUpdateFrequency

If the tool reveals that a specific actor class is consuming a disproportionate amount of bandwidth, consider lowering its NetUpdateFrequency. By reducing how often an actor checks for changes, you can perform a significant elimination of unnecessary packet overhead without noticeably impacting gameplay.

6. Profile Server-Side for Accuracy

Always prioritize recording bandwidth data on the Server. While clients can record data, they only see what is sent to them. The server-side profile provides the most accurate “total” picture of the bandwidth being distributed to all players, which is critical for determining server hosting costs and scalability.

7. Leverage Dormancy to Save Bandwidth

Use the measurement data to verify that your Actor Dormancy is working correctly. If an actor is supposedly “Dormant” but the tool shows it is still contributing to the bandwidth total, it means the actor is being “woken up” prematurely. Proper dormancy is the most effective way to reach the elimination of idle network traffic.

8. Verify Quantization Benefits

If you implement Net Quantization (like FVector_NetQuantize) to compress your data, use the BandwidthMeasurementTool before and after the change. This provides concrete metrics on how many bits were saved per packet, allowing you to justify the reduction in precision for the sake of better network performance.