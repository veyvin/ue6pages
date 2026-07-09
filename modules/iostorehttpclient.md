---
layout: default
title: IoStoreHttpClient
---

<!-- ai-generation-failed -->

<h1>IoStoreHttpClient</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/IoStore/HttpClient/IoStoreHttpClient.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, OpenSSL, TraceLog, nghttp2</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ader (the engine’s modern I/O system). It serves as the bridge between the local IoStore and a remote ZenServer. Its primary purpose is to allow a game running on a target device (such as a console or mobile phone) to request and stream cooked assets directly from a developer’s workstation over HTTP. This bypasses the need to bake, package, and deploy full builds for every small content change.

Practical Usage Tips & Best Practices
1. Enable Zen Streaming for Iteration

The most common use for this module is during the “Connect to Zen” workflow, where the game pulls data over the network instead of reading from a local .ucas or .utoc file.

Best Practice: Use this module in Development or Test builds on your local office network. This facilitates the elimination of long deployment times, as you only need to push the executable once while streaming assets on demand.
2. Configure the Zen Server IP Address

The client needs to know where the ZenServer is hosted (typically your PC).

Tip: Ensure the ue.projectstore file on the target device contains the correct host IP and port. Setting this correctly ensures the elimination of “Connection Refused” errors when the game attempts to initialize the HTTP I/O stream.
3. Use on Trusted, Low-Latency Networks

Because this module handles asset loading over HTTP, network stability is critical for engine performance.

Best Practice: Only use iostorehttpclient over a wired LAN or high-speed 5GHz Wi-Fi. Utilizing a stable connection leads to the elimination of hitches and stalls that occur when the game thread is waiting for a critical asset to arrive over a slow network.
4. Monitor I/O Performance via Insights

You can track how much data is being pulled through the HTTP client using Unreal Insights.

Tip: Look at the I/O Overview tab in Insights to see the latency of HTTP requests. Analyzing these metrics assists in the elimination of bottlenecks by identifying assets that are too large to be streamed effectively during live gameplay.
5. Verify Module Dependencies in Build.cs

If you are writing custom engine-level tools that interact with the I/O store, you must explicitly include this module.

Best Practice: Add "iostorehttpclient" to your dependencies only for non-shipping targets. This ensures the elimination of unnecessary bloat in your final shipping executable, where remote HTTP loading is typically disabled for security.
6. Coordinate with the Cooker

The assets requested by the client must exist in the Zen Cache on the host machine.

Tip: Keep the editor or a “Cook on the Fly” server running while testing. This ensures the elimination of “Asset Not Found” errors, as the iostorehttpclient can only retrieve what the server has successfully cooked.
7. Handle Network Timeouts Gracefully

If the workstation goes to sleep or the network drops, the game will likely hang or crash when it hits a “must-load” asset.

Best Practice: Ensure your workstation’s power settings prevent sleep during a playtest session. Proactive power management results in the elimination of frustrating “connection lost” crashes during long-running soak tests.
8. Secure Your Zen Port

Since this module communicates over standard HTTP, the port used by ZenServer is technically open to your local network.

Tip: Use a firewall to restrict the ZenServer port to authorized device IPs only. This security measure contributes to the elimination of unauthorized access to your cooked game data by other users on the same corporate or home network.