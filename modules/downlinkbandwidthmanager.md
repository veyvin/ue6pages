---
layout: default
title: DownlinkBandwidthManager
---

<!-- ai-generation-failed -->

<h1>DownlinkBandwidthManager</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/Experimental/DownlinkBandwidthManager/DownlinkBandwidthManager.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">BandwidthDebugDelegates, BandwidthMeasurementTool, Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ity within Unreal Engine designed to monitor and manage incoming data flow from a server or external source to a client. It is primarily utilized in systems where stable, real-time data streaming is critical, such as Pixel Streaming, large-scale multiplayer networking, or background content delivery.

This module acts as a governor for data reception, providing metrics and logic to handle network congestion and ensuring the elimination of client-side hitches caused by saturating the user’s download capacity.

Practical Usage Tips and Best Practices
1. Implement for Adaptive Pixel Streaming

When using Pixel Streaming, leverage this module to monitor the client’s actual download speed. By feeding this data back to the encoder, you can dynamically adjust the video bitrate. This prevents buffer overflows and leads to the elimination of visual “stutter” or high-latency spikes during playback.

2. Configure Congestion Control Thresholds

Use the manager to set “High Watermark” and “Low Watermark” thresholds for incoming data packets. When the download rate hits the high watermark, you can trigger logic to temporarily pause non-essential data (like background cosmetic updates), facilitating the elimination of packet loss for critical gameplay data.

3. Monitor via BandwidthDebugDelegates

The module works closely with BandwidthDebugDelegates. By hooking into these delegates, you can create on-screen debug HUDs that show real-time downlink health. This is a best practice for the elimination of guesswork when developers are testing their game on limited or throttled network connections.

4. Prioritize Critical Game State

In complex multiplayer environments, use the bandwidth manager’s metrics to inform your Iris (UE5’s high-performance replication system) or legacy replication settings. If the downlink is saturated, you can prioritize actor replication over property replication, aiding in the elimination of desync between the client and server.

5. Graceful Degradation for Background Downloads

If your game uses background patching or asset streaming (like OODLE or Bink video streaming), use this module to throttle those downloads during intense gameplay. This ensures the elimination of “lag spikes” that occur when a background download competes with the primary game networking.

6. Utilize for Mobile Network Handling

Mobile devices often experience fluctuating signal strength. Configure the DownlinkBandwidthManager to detect rapid drops in bandwidth. You can then trigger a UI notification to the player or switch to a lower-fidelity network mode, leading to the elimination of unexpected disconnections during transitions between 5G and Wi-Fi.

7. Integrate with ClientPilot for Testing

When running automated performance tests using ClientPilot, use the bandwidth manager to simulate “poor” network conditions. Artificially limiting the downlink allows you to observe how the game handles extreme congestion, which is essential for the elimination of crashes or infinite loading loops in the final product.

8. Analyze Logs for “Silent” Throttling

Regularly check logs associated with this module to see if the engine is frequently “clamping” incoming data. Persistent clamping indicates that your server is sending more data than the client’s pipe can handle. Adjusting your replication frequency or LODs based on these logs assists in the elimination of inefficient bandwidth usage.