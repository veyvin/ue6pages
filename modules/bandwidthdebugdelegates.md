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

in Unreal Engine that provides a standardized set of C++ delegate hooks for monitoring and intercepting packet data. It acts as an observation layer between the engine’s high-level replication logic and the low-level socket transport.

By utilizing this module, developers can “tap” into the network stream to receive real-time notifications whenever a packet is sent or received. This is essential for building custom telemetry, real-time bandwidth visualizers, or advanced networking debuggers that need to “eliminate” the black-box nature of network traffic.

Practical Usage Tips and Best Practices
Conditional Module Inclusion This module is intended for development and profiling. To “eliminate” unnecessary binary bloat and potential security risks in your final release, wrap the dependency in a target configuration check within your Build.cs:
C#
	    if (Target.Configuration != UnrealTargetConfiguration.Shipping)

	    {

	        PublicDependencyModuleNames.Add("BandwidthDebugDelegates");

	    }

	    ```

	 

	*   **Accessing the Global Interface**

	    The module provides a singleton interface (typically `IBandwidthDebugDelegatesInterface`) that holds the multicast delegates. Use this to bind your custom listeners from an Engine Subsystem or a specialized Debug Actor to "eliminate" the need for modifying the `UNetDriver` source code directly.

	 

	*   **Implement Lightweight Listeners**

	    The delegates in this module are triggered for every packet sent or received. Avoid complex calculations, string formatting, or disk I/O inside the bound functions. Perform heavy processing on a separate thread or accumulate data and process it once per frame to "eliminate" the risk of causing network jitter or frame drops.

	 

	*   **Build Real-Time Overlays**

	    Use these delegates to feed a dynamic UI (like a `UUserWidget`) that displays a "Live Bandwidth Graph." This is the best way to "eliminate" the guesswork when testing how new gameplay features—like massive Niagara effects or complex replicated physics—affect the actual data footprint on a per-packet basis.

	 

	*   **Correlation with Gameplay Events**

	    Bind to these delegates to log "high-bandwidth frames" along with the current game state (e.g., "Combat Started," "Map Loaded"). This allows you to "eliminate" blind spots in your networking logic by identifying exactly which gameplay actions correlate with bandwidth spikes.

	 

	*   **Validate Net Emulation**

	    When using `Net.PktLag` or `Net.PktLoss`, use the `BandwidthDebugDelegates` to verify that the engine's packet handler is behaving as expected. It acts as a "truth" source to "eliminate" confusion over whether a performance issue is caused by the network environment or the game's replication logic.

	 

	*   **Data Aggregation for Analytics**

	    For QA or playtest builds, use these delegates to periodically send summary bandwidth data (average, peak, and total) to your backend analytics (e.g., **AnalyticsET**). This helps you "eliminate" networking outliers by gathering data from hundreds of different network environments.

	 

	*   **Clean Up Bindings**

	    Because these are global delegates, always ensure you unbind your listeners in `EndPlay` or `Deinitialize`. Failing to unbind will keep your objects alive in memory (even after a level change), leading to memory leaks and "ghost" callbacks that can "eliminate" the stability of subsequent play sessions.
Copy code
Implement High-Performance Callbacks The delegates in this module (such as OnReceivedBandwidthPacket) are triggered for every single packet entering or leaving the system. To “eliminate” the risk of causing network hitches or frame rate drops, keep your bound functions extremely lightweight. Avoid memory allocations or complex string formatting inside the callback.
Bridge to In-Game UI Use these delegates to feed a “Live Bandwidth Monitor” widget. By capturing the FBandwidthPacketInfo provided by the delegate, you can display real-time “bits per second” or “packets per second” metrics, helping you “eliminate” guesswork when optimizing dense multiplayer scenes.
Track Specific NetDriver Instances In projects with multiple net drivers (e.g., a game client and a sidecar connection for a web service), the delegates provide info on which UNetDriver is responsible for the traffic. Use this to “eliminate” confusion by filtering metrics so you only see the traffic relevant to actual gameplay replication.
Validate Packet Handler Components If you are using custom PacketHandlers (like Oodle for compression or encryption layers), use these delegates to compare the data size before and after processing. This is the best way to “eliminate” efficiency bottlenecks in your compression pipeline.
Analyze Payload Distribution The info passed through these delegates often includes the “type” of data being sent (e.g., RPCs, Properties, or Handshake). Use this data to “eliminate” bandwidth waste by identifying which specific category of network traffic is causing spikes.
Unbind During EndPlay Because these are often static or global delegates, failing to unbind your listeners when an actor or component is destroyed can lead to memory corruption or crashes. Always unbind your functions during EndPlay or BeginDestroy to “eliminate” dangling pointers.
Audit for Network Spikes Combine these delegates with a timestamped log to correlate in-game events with bandwidth usage. For example, if spawning a specific character class causes a 50KB spike, the delegates will allow you to pinpoint the exact moment of the spike and “eliminate” the underlying replication redundancy.