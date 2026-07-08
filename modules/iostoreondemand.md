---
layout: default
title: IoStoreOnDemand
---

<!-- ai-generation-failed -->

<h1>IoStoreOnDemand</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/IoStore/OnDemand/IoStoreOnDemand.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, DownlinkBandwidthManager, IndexedCacheStorage, IoStoreHttpClient, IoStoreOnDemandCore, Json, PlatformWriteMonitor, RSA, S3Client, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tore architecture designed to revolutionize iteration on target platforms. It allows a game running on a console or mobile device to stream cooked asset data over a network directly from a host workstation’s Zen Server.

What it is and What it’s used for

Located within the Zen Store infrastructure, this module facilitates a “streaming-to-target” workflow. Traditionally, testing on a device required “Staging” (copying all assets) and “Deploying” (transferring them to the device), which is a slow process for large projects. IOStoreOnDemand eliminates the need for these steps by leaving the assets on the developer’s PC and fetching them only when the game requests them.

Primary uses include:

Rapid Iteration: Launching a game on a target device in seconds because only the executable and a tiny ue.projectstore config file are deployed.
Network Asset Streaming: Fetching cooked .uasset data from the Zen Server on demand via TCP/HTTP during runtime.
Storage Optimization: Running massive projects on devices with limited storage (like mobile phones) since the bulk of the data remains on the workstation.
Practical Usage Tips and Best Practices
1. Use on Trusted, High-Speed Networks

Because assets are being fetched over the network, bandwidth is critical. Always use a wired Ethernet connection for both the host PC and the target console. This ensures the elimination of “Network Hitching” that can occur if the game thread stalls while waiting for a large asset to stream over Wi-Fi.

2. Validate Connection via ue.projectstore

The game looks for a ue.projectstore file to know where the Zen Server is. If the game fails to connect, verify that your workstation’s IP address and port (default 13580) are correctly defined in this JSON file. Correct configuration ensures the elimination of “Asset Not Found” errors at runtime.

3. Monitor Streaming with zen.showgraphs

While the game is running on the target, use the console command zen.showgraphs 1. This displays an on-screen plot of the streaming throughput. It is a best practice for identifying if a specific scene is loading too slowly due to network congestion rather than disk I/O.

4. Override Host with Command Line Arguments

If your workstation IP changes frequently, you don’t need to rebuild the project. You can override the connection parameters by passing -ZenStoreHost=<Your_IP> as a launch argument. This provides flexibility and the elimination of redundant staging phases when moving between different network environments.

5. Limit Usage to Non-Shipping Builds

This module is strictly for Debug and Development configurations. It relies on a local server that will not exist in a retail environment. Ensure you never include “On Demand” logic in a Shipping build to prevent the elimination of game functionality for the end-user.

6. Coordinate with the Cooker

The assets must be cooked into the Zen Store (standard in UE 5.4+) for this module to work. If you modify an asset, simply run a “Cook” in the Editor; the Zen Server updates its internal database, and the target device will automatically stream the new version on the next load without a redeploy.

7. Profile for “Zen Server Streaming” Text

When the system is active, you should see “ZenServer streaming from [IP]” in the top-left corner of the screen. If this text is missing, the game has likely fallen back to local storage. Checking for this visual cue is the fastest way to confirm your iteration cycle is optimized.

8. Strategic Elimination of Staged Data

If you switch back to a standard “Packaged” workflow, manually clear your Saved/StagedBuilds/[Platform] folder. Residual metadata from the IOStoreOnDemand module can sometimes cause the engine to look for the Zen Server instead of local .pak files, leading to the elimination of asset loading stability during final testing.