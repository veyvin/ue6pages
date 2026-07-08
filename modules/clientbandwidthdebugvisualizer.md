---
layout: default
title: ClientBandwidthDebugVisualizer
---

<!-- ai-generation-failed -->

<h1>ClientBandwidthDebugVisualizer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/Experimental/ClientBandwidthDebugVisualizer/ClientBandwidthDebugVisualizer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">BandwidthDebugDelegates, Core, CoreUObject, Engine, EngineSettings</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ic module used to provide an on-screen, real-time HUD overlay of network traffic. Unlike the standalone Network Profiler which requires post-session analysis, this visualizer allows developers to see exactly how much data is being received by the client during active gameplay.

Its primary purpose is to provide “at-a-glance” visibility into bandwidth consumption, helping developers identify immediate spikes in data usage caused by specific gameplay events, such as spawning large numbers of actors or firing high-frequency RPCs.

Practical Usage Tips and Best Practices
1. Enable via Console Commands

To activate the visualizer during a play session (PIE or a development build), use the following console command: net.BandwidthDebugVisualizer 1 This will spawn the debug graph on the client’s screen. Setting it to 0 will result in the elimination of the overlay from the viewport.

2. Interpret the Scrolling Graph

The visualizer typically displays a scrolling bar graph where each bar represents a single network packet. The height of the bar indicates the size of the packet in bits. This is useful for identifying “jumbo” packets that might be approaching the MTU (Maximum Transmission Unit) limit, which can lead to the elimination of network efficiency through packet fragmentation.

3. Monitor “Burst” Events

Use the visualizer to monitor specific gameplay actions, like opening a complex inventory or entering a new “World Partition” cell. If you see a massive spike in the graph during these actions, it indicates that the server is sending too much initial state data at once. This insight allows for the elimination of hitches by staggering data transmission.

4. Correlate with Packet Loss

While the visualizer primarily tracks bandwidth, large gaps in the scrolling bars often indicate packet loss or severe latency. If the bars stop moving or disappear, it signals that the client is no longer receiving updates, potentially leading to the elimination of a stable connection.

5. Use in Combination with “stat net”

The visualizer provides a high-level visual representation, but for specific numbers, you should use it alongside the stat net command. stat net provides the raw KBs/sec and Ping values, while the visualizer shows the distribution of that data across individual packets.

6. Debugging Relevancy and Cull Distances

Move your character in and out of range of network-heavy actors. As actors become “relevant” and start replicating, you should see a corresponding increase in the visualizer’s bar heights. If a distant, “culled” actor is still causing spikes, you have identified a bug that requires the elimination of its network relevancy.

7. Profile on Target Hardware

Bandwidth processing has a CPU cost on the client. Use the visualizer on lower-end target devices (like mobile or older consoles) to ensure that the sheer volume of incoming packets isn’t overwhelming the client’s ability to de-serialize data, which can cause the elimination of frame-rate stability.

8. Verify RPC Frequency

If you have a “Fire” or “Move” RPC that is accidentally being called every frame, the visualizer will show a constant, thick wall of bars. This is a clear signal to implement better “throttling” or “quantization” logic to ensure the elimination of redundant network traffic.