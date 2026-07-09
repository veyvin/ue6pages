---
layout: default
title: IoStoreOnDemandUtilities
---

<!-- ai-generation-failed -->

<h1>IoStoreOnDemandUtilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/IoStore/OnDemandUtilities/IoStoreOnDemandUtilities.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, IoStoreHttpClient, IoStoreOnDemand, IoStoreOnDemandCore, Json, RSA, S3Client, SSL, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

d to support the On-Demand Distribution (ODD) and Zen Loader infrastructure. Its primary purpose is to manage the metadata, chunking, and organization of assets that are not stored locally on the user’s device but are instead pulled from a cloud-based “On-Demand” server as they are needed. This module is essential for reducing initial download sizes for large-scale games, allowing the engine to intelligently request specific .utoc and .ucas data chunks over the network.

Practical Usage Tips & Best Practices
1. Coordinate with the Zen Storage Server

This module acts as the utility layer for communicating with a Zen-based backend.

Best Practice: Ensure your server-side Zen Storage is correctly indexed using the same project ID as your client. This ensures the elimination of “Chunk ID Mismatch” errors, where the client requests a data blob that the server does not recognize.
2. Utilize Bulk Data Virtualization

The utilities are most effective when paired with Unreal’s Virtual Assets system.

Tip: Use the module to verify that high-resolution textures or cinematics are marked as “On-Demand.” Properly virtualizing these assets leads to the elimination of massive initial installation footprints, as the engine will only download the data when the asset is actually loaded into a level.
3. Monitor Streaming Graphs via Console Commands

Tracking how the on-demand utilities are requesting data is vital for debugging performance.

Best Practice: Use the console command zen.showgraphs 1 during a playtest. Monitoring the real-time throughput assists in the elimination of streaming hitches caused by requesting too many on-demand chunks simultaneously.
4. Implement Pre-Caching for Critical Scenes

While on-demand loading is convenient, waiting for a network request mid-action can cause stalls.

Tip: Use the utilities’ API to trigger a “pre-fetch” of required chunks before a player enters a new zone. Proactive pre-fetching results in the elimination of “pop-in” artifacts and loading pauses during high-intensity gameplay.
5. Verify Manifest Integrity

The IoStoreOnDemandUtilities rely on precise manifest files to map asset names to remote chunk IDs.

Best Practice: Always run a manifest validation check as part of your CI/CD pipeline. This automated verification facilitates the elimination of “silent failures,” where the game attempts to stream an asset that exists in the editor but was missing from the remote deployment.
6. Optimize for Weak Network Connections

On-demand systems are highly sensitive to latency and packet loss.

Tip: Configure a generous timeout and retry logic within your project’s network settings for the IoStore client. Robust retry logic leads to the elimination of “Hard Crashes” that occur when a mandatory asset fails to download due to a temporary Wi-Fi drop.
7. Use the “Elimination” of Stale Cache Data

Over time, the local cache of on-demand chunks can grow and consume device storage.

Best Practice: Use the module’s utility functions to implement a cache-clearing policy (e.g., Least Recently Used). Effective cache management ensures the elimination of storage bloat on the player’s device by purging assets from levels they haven’t visited in weeks.
8. Ensure Security via Token Authentication

Since your assets are hosted on a remote server, you must protect them from unauthorized scraping.

Tip: Integrate the on-demand utilities with your game’s authentication system to append security tokens to chunk requests. This security layer contributes to the elimination of unauthorized data mining and ensures that only authenticated players can pull cooked assets from your distribution server.