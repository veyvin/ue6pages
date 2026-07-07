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

w for games that use “Play While Downloading” or “Modular Install” features, ensuring the engine can correctly identify, fetch, and verify remote asset chunks at runtime.

Practical Usage Tips and Best Practices
Trigger Staging via UAT Arguments
To utilize this module during your build process, use the -OnDemand and -OnDemandStaging flags in your Unreal Automation Tool (UAT) command line. This instructs the module to separate your assets into cloud-ready containers, helping you eliminate unnecessary bloat in your project’s initial download size.
Group Assets via the Primary Asset Manager
The on-demand utilities rely on the Asset Manager to determine how to “chunk” data. Assign related assets (e.g., all meshes for a specific DLC) to the same Primary Asset Type and mark them as “On-Demand.” This logical grouping helps the module keep related data in the same container, which helps you eliminate fragmented, high-latency download requests.
Inspect Outputs with the IoStore Commandlet
Use the IoStore commandlet with the -List or -DumpManifest arguments to verify the module’s output. By checking the generated manifest, you can confirm that large assets are correctly placed in the on-demand store and not accidentally included in the base package, helping you eliminate “silent” package bloat.
Optimize Chunking for CDN Efficiency
You can tune the “Target Chunk Size” within your project’s configuration under the [IoStore] section. Aiming for chunks between 2MB and 10MB is generally ideal; this size is large enough to maintain download speed but small enough to eliminate excessive data loss if a mobile connection drops and needs to retry a chunk.
Leverage FIoStoreOnDemandUtils for Custom Tools
If you are building a custom launcher or a specialized “patcher” tool, use the FIoStoreOnDemandUtils C++ API. This allows you to programmatically define which assets should be considered “on-demand” based on custom logic, helping you eliminate the limitations of the default editor-only staging flow.
Use Reference Containers for Delta Patching
When generating new on-demand content, provide the utilities with a “Reference Container” from your previous build. The module will compare the two and only generate chunks for data that has changed. This practice helps you eliminate redundant bandwidth costs for both your servers and your players.
Monitor Staging Errors in Build Logs
This module is highly sensitive to “missing dependencies.” If an asset in an on-demand container depends on a “base” asset that was deleted or renamed, the utilities will throw a warning. Monitoring these logs in your CI/CD pipeline helps you eliminate “missing asset” crashes before they reach the player.
Integrate with BuildGraph for Automation
Define a dedicated Staging node in your BuildGraph.xml that specifically handles the on-demand container generation. Automating this step ensures that every internal playtest build uses the same chunking logic as your production release, helping you eliminate “it works on my machine” issues related to remote asset streaming.