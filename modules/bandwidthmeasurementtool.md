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

hts and Network Profiler frameworks) is a specialized diagnostic suite used to monitor, analyze, and optimize data transmission between a server and its clients. Its primary purpose is to identify “network-heavy” actors, properties, and RPCs (Remote Procedure Calls) that consume excessive bandwidth, which can lead to latency spikes or packet loss.

This tool is essential for multiplayer developers aiming for the total elimination of network congestion and ensuring a smooth experience on limited-bandwidth connections, such as mobile networks or high-latency internet.

Practical Usage Tips and Best Practices
1. Enable via Command Line or Console

To begin recording data for the tool, you must start your game instance with the -trace=net command-line argument or use the netprofile console command during runtime. This generates an .nprof or .utrace file that can be opened in the Unreal Insights or the standalone Network Profiler application.

2. Prioritize “Hot” Replicated Properties

Use the tool to identify properties that change every frame. If a variable is consuming high bandwidth but doesn’t need perfect precision, implement a NetQuantize struct (e.g., FVector_NetQuantize100) or increase the NetUpdateFrequency. This leads to a significant elimination of unnecessary bit-stream overhead.

3. Analyze RPC Overhead

The tool will show you exactly how many bits each RPC call consumes. Frequent, small RPCs are often more expensive than occasional large ones due to header overhead. If the tool shows a high count for a specific RPC, consider batching that data into a single struct or using a replicated variable with RepNotify instead.

4. Monitor Packet Saturation

In the Networking Insights panel, look for red bars in the packet timeline. This indicates packet saturation where the data sent exceeds the MaxClientRate defined in your BaseEngine.ini. If saturation occurs, the engine will drop lower-priority packets, which can cause the elimination of critical gameplay updates.

5. Profile on the Server Side

While clients can record traces, the most accurate bandwidth data comes from the server. The server tracks all outgoing replication data for every connected client. Always perform your primary bandwidth audits on a Dedicated Server build to see the true cost of actor relevancy and global replication.

6. Identify “Network Relevant” Culprits

Use the tool to find actors that are replicated even when they are far away from the player. If an actor shows high bandwidth usage but isn’t visible, adjust its NetCullDistanceSquared. This ensures the elimination of data transmission for actors that do not affect the local player’s immediate experience.

7. Use CSV Profiler for Correlation

Run the CSVProfile command alongside your bandwidth measurement. This allows you to correlate network spikes with CPU hitches. Often, a large burst of replicated data (like when first joining a match) can cause a CPU stall as the client attempts to spawn dozens of actors simultaneously.

8. Validate Fast Array Replication

If you are replicating large lists of data, use the tool to compare standard TArray replication against Fast Array Serializer. The tool will demonstrate how Fast Arrays provide a better elimination of redundant data by only sending the specific elements that have changed, rather than the entire array.