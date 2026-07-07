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

tly on the game HUD without needing to switch to external tools like Unreal Insights.

This module is primarily used to identify “bursty” network traffic, such as massive RPC calls or property replication spikes, instantly during a play session.

Practical Usage Tips and Best Practices
1. Enable via Plugin and Dependency

To use this module in a C++ project, you must first enable the Bandwidth Measurement plugin. In your Build.cs file, ensure you gate the dependency so it is only included in non-shipping builds:

C#
	if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.Add("ClientBandwidthDebugVisualizer");

	}

	```

	 

	#### 2. Trigger with the Correct Console Command

	To toggle the on-screen graph, use the console command `net.BandwidthGraph 1`. This will display a rolling histogram in the top corner of the screen. You can use `net.BandwidthGraph 0` to hide it. This is significantly faster for quick checks than booting up **Unreal Insights**.

	 

	#### 3. Interpret the Color Coding

	The visualizer typically splits traffic into categories. Pay close attention to the **Total** (often white/gray) versus **Game Data** (usually green). If you see the Total line spike while Game Data remains flat, it often indicates "overhead" traffic such as Voice-over-IP (VoIP) or heavy control channel Handshaking rather than actual gameplay replication.

	 

	#### 4. Identify RPC "Spam" Instantly

	Because the graph updates every frame, it is the best tool for identifying "RPC Spam." If a specific player action (like firing a weapon or opening an inventory) causes a vertical green spike that hits the top of the graph, you have immediately identified a candidate for **Net Quantization** or bit-packing optimization.

	 

	#### 5. Use to Test NetUpdateFrequency

	When you lower an actor’s `NetUpdateFrequency` to save bandwidth, keep the visualizer open. You should see the "Game Data" line move from a jagged, high-frequency "sawtooth" pattern to a smoother, lower-frequency wave. This provides immediate visual confirmation that your optimization is working.

	 

	#### 6. Calibrate for Latency/Jitter

	The visualizer also tracks packet loss and jitter indirectly by showing the "gaps" in data arrival. If the histogram looks "stuttery" despite a high framerate, it indicates that the client is receiving packets in irregular clusters, which can lead to the **elimination** of smooth movement and cause "rubber-banding."

	 

	#### 7. Profile on Target Hardware (Consoles/Mobile)

	One of the biggest strengths of the `ClientBandwidthDebugVisualizer` is that it works on-device. Since it is an in-game HUD element, you can view bandwidth metrics on a mobile phone or a console devkit where connecting a PC-based profiler might be cumbersome or technically restricted.

	 

	#### 8. Combine with "stat net"

	While the visualizer gives you the *history* and *trend* of bandwidth, use the `stat net` command alongside it to get the *exact* numerical bit-counts. The visualizer tells you **when** the spike happened, and `stat net` tells you exactly **how big** (in bits per second) that spike was.
Copy code
2. Activate via Console Command

To toggle the visualizer overlay while the game is running, use the console command: net.BandwidthGraph 1 Set it to 0 to hide it. This is significantly faster for quick sanity checks than opening the full Network Profiler or Unreal Insights.

3. Interpret the Histogram Spikes

The visualizer displays a rolling histogram. Sharp vertical spikes in the graph indicate large “bunches” of data being sent in a single frame. This usually points to a specific event, such as a player spawning or a complex multicast RPC, which may require the elimination of unnecessary data to smooth out the traffic.

4. Distinguish Game Data from Overhead

The graph often differentiates between actual gameplay replication and protocol overhead (such as acks and handshakes). If you see high bandwidth usage but the “Game Data” portion is small, focus your optimization on the elimination of connection-level overhead rather than your Blueprint variables.

5. Use to Test NetUpdateFrequency

When you lower an actor’s NetUpdateFrequency, keep the graph open. You should see the “jagged” peaks spread further apart. This provides immediate visual confirmation that your frequency changes are effectively contributing to the elimination of congested network frames.

6. Debug “Saturation” in Real-Time

If the graph consistently hits the top of the display area, your client is likely reaching its bandwidth limit. This can lead to the elimination of reliable packets (causing latency) or the dropping of unreliable ones. Use this visual feedback to tune your DefaultMaxClientRate in the project settings.

7. Verify Net Quantization

If you implement FVector_NetQuantize to compress coordinates, the visualizer allows you to see the immediate reduction in bit-rate. Seeing the graph height drop after implementing quantization is the best way to prove the elimination of redundant precision that the player won’t notice.

8. Monitor Jitter and Packet Gaps

Inconsistent spacing between bars on the histogram indicates network jitter. If you see wide gaps followed by large clusters of bars, it means the client is receiving data in “clumps.” This is a primary cause of “rubber-banding” and should be addressed by checking the server’s tick rate or the stability of the network connection.