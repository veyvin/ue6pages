---
layout: default
title: IoStoreOnDemandTests
---

<!-- ai-generation-failed -->

<h1>IoStoreOnDemandTests</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/IoStore/Tests/IoStoreOnDemandTests.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TestModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, IoStoreOnDemand</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

eal Engine designed to validate the functionality of IoStore On-Demand (also known as Zen Store streaming). This system allows games to stream cooked assets directly from a Zen Server (or a cloud-based distribution point) to a target device (PC, Console, or Mobile) over a network, rather than reading them from a local .pak or .utoc file.

This module provides automated unit and functional tests to ensure the reliability of the network transport layer, the integrity of streamed data, and the elimination of potential crashes or corruption that could occur during real-time asset delivery.

Practical Usage Tips and Best Practices
1. Use to Validate “On-Target” Iteration

If you are using Zen Streaming to test your game on a mobile device without a full deployment, run these tests first. They facilitate the elimination of connectivity issues between your workstation and the device, ensuring that the ue.projectstore configuration is correctly routing data over your local network.

2. Verify Cache Integrity and “Elimination”

IoStore On-Demand relies on a local persistent cache to store streamed chunks. Use the tests in this module to verify that the cache correctly handles “elimination” events—such as clearing out old data when the cache reaches its size limit—without corrupting the remaining assets.

3. Test Under Simulated Latency

The module includes logic to test how the engine behaves when the network is slow or unstable. Running these tests assists in the elimination of “infinite loading” bugs where the game might hang if an asset chunk fails to arrive from the Zen Server in a timely manner.

4. Audit “ue.projectstore” Generation

The streaming system requires a JSON-formatted ue.projectstore file to locate the server. Use the module’s validation logic to ensure your build pipeline is generating this file with the correct IP address and Port. This practice leads to the elimination of “Server Not Found” errors during development cycles.

5. Monitor Streaming Throughput

When running tests from this module, use the console command zen.showgraphs 1. This allows you to visualize the data transfer in real-time. Observing these graphs during automated tests leads to the elimination of performance bottlenecks caused by non-optimized network configurations.

6. Debug “Chunk Missing” Scenarios

If your game crashes during an On-Demand session because of a missing asset, run the module’s functional tests to check the Zen Store’s internal mapping. These tests help identify if an asset was skipped during the cook phase, aiding in the elimination of broken references in your streamed build.

7. Verify Build.cs for Custom Automation

If you are extending the engine’s build system to include custom streaming verification, you must add "IoStoreOnDemandTests" to your Build.cs in a Test or Editor configuration. Proper linking is required for the elimination of compiler errors when referencing the On-Demand test controller.

8. Ensure Non-Shipping Configuration Alignment

IoStore On-Demand is intended for Debug, Development, and Test builds, not Shipping builds. Use this module to verify that your “Test” configuration correctly falls back to local storage if the Zen Server is unavailable, facilitating the elimination of launch failures when testing your game in a standalone environment.