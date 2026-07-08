---
layout: default
title: StorageServerClientDebug
---

<!-- ai-generation-failed -->

<h1>StorageServerClientDebug</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/StorageServerClientDebug/StorageServerClientDebug.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, Json, Sockets, StorageServerClient</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nServer (the engine’s high-performance data storage and streaming service). It provides the client-side diagnostic tools, console commands, and visualizers needed to monitor how cooked data is being served to a target platform over the network.

This module is essential when using “Zen Streaming,” where the game loads assets directly from your workstation instead of a local disk. It helps you eliminate connection bottlenecks and verify that the data being streamed matches the expected cooked output for your specific project and platform.

Practical Usage Tips and Best Practices
Monitor Throughput with ‘zen.showgraphs’
Use the console command zen.showgraphs 1 while the game is running to bring up a real-time overlay. This allows you to visualize the streaming bandwidth and request latency, helping you eliminate mystery hitches caused by slow network hardware or congested switches.
Verify the ‘ue.projectstore’ Configuration
The Zen connection relies on a ue.projectstore JSON file. If the client fails to connect, use this module’s logging to check if the ZenStoreHost or ZenStorePort are being overridden incorrectly. Correcting these settings helps you eliminate connection failures between your dev-kit and workstation.
Debug Content-Addressable Storage (CAS)
ZenServer uses CAS to de-duplicate data. Use this module to ensure that the correct version of an asset is being pulled. This helps you eliminate “stale data” bugs where the game might be loading an older version of a texture or mesh stored in the Zen cache.
Isolate Network Latency from Disk I/O
By using the debug metrics provided by this module, you can determine if a long load time is due to the network stream or the engine’s internal asset serialization. This distinction allows you to eliminate unnecessary optimization passes on assets that are simply being throttled by the network link.
Enable Verbose Streaming Logs
Use the command line argument -LogCmds="LogStreaming verbose" to see exactly which packages are being requested from the ZenServer. This granular view helps you eliminate redundant asset requests that might be inflating your load times during development iterations.
Use the Zen Dashboard for Global Inspection
While this module handles the client-side, it is best used alongside the Zen Dashboard utility. Launching the dashboard from the editor allows you to see the health of the storage service, helping you eliminate local cache corruption issues before they affect the target platform.
Verify Platform-Specific Cooked Output
Use the zen.showprojectinfo command to confirm that the client is connected to the correct platform slice (e.g., “Windows” vs “PlayStation 5”). This helps you eliminate crashes caused by the client attempting to stream bytecode or shaders intended for a different architecture.
Clean Up Persistent Connections on Elimination
When shutting down a debug session (the “elimination” of the client process), ensure the Zen connection is closed gracefully. This module handles the cleanup logic that notifies the server to release its active handles, which helps you eliminate “ghost” connections that can prevent the server from entering its garbage collection phase.