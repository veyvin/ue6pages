---
layout: default
title: IoStoreOnDemandDebug
---

<!-- ai-generation-failed -->

<h1>IoStoreOnDemandDebug</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/IoStore/OnDemandDebug/IoStoreOnDemandDebug.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, IoStoreOnDemandCore, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

owgraphs 1 to enable on-screen plots of streaming data. This allows you to monitor real-time throughput from the ZenServer and helps you eliminate confusion regarding whether a slow load is caused by disk I/O on the host or network congestion.
Monitor Latency and Request Counts
The module tracks the number of pending requests and the latency of each asset fetch. If your game hitches during a transition, check these stats to determine if the network latency is too high, helping you eliminate performance bottlenecks in your office or home network setup.
Verify ‘ue.projectstore’ Connectivity
When using On-Demand streaming, the target device uses a ue.projectstore file to locate the ZenServer. Use the debug module’s logs to verify that the device has successfully parsed this file and established a handshake, which helps you eliminate “Connection Refused” errors during the initial launch.
Debug Missing Cooked Data
If an asset fails to appear on the target device, this module can report if the ZenServer actually contains the cooked version of that asset. This helps you eliminate the trial-and-error process of wondering if a specific mesh was included in the last cook or if the streamer simply failed to find it.
Validate Non-Shipping Configurations
On-Demand streaming is intended for Debug, Development, and Test configurations. Use the debug module to ensure that your build is correctly attempting to stream data rather than looking for local files, which helps eliminate “File Not Found” crashes when testing on-target iteration.
Analyze Cache Misses
The module provides insights into the local cache on the target device. By analyzing cache hits vs. misses, you can determine if the device is effectively reusing previously streamed data, helping you eliminate redundant network traffic for frequently accessed global assets.
Identify Heavy Assets for Optimization
By watching the live stream logs provided by this module, you can identify which specific assets (e.g., massive 4K textures) take the longest to arrive. This data allows you to eliminate unoptimized content that might be too large for efficient network streaming during a fast iteration cycle.
Use with ‘stat VirtualTexture’
If your project uses Virtual Textures, the On-Demand debug module works in tandem with VT stats. Monitoring both allows you to see how network streaming affects the “pop-in” of textures, helping you eliminate visual artifacts by adjusting your network priority or ZenServer settings.