---
layout: default
title: CookOnTheFly
---

<!-- ai-generation-failed -->

<h1>CookOnTheFly</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/CookOnTheFly/CookOnTheFly.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Networking, Sockets</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ed for rapid iteration. Unlike “Cook by the Book,” which converts all assets before launching the game, COTF allows a packaged or staged build to request assets from a host PC (the Cook Server) over a network connection as they are needed at runtime.

This module is primarily used by developers working on consoles or mobile devices to avoid the lengthy process of re-packaging and re-deploying the entire project every time a single texture or material is modified.

Practical Usage Tips and Best Practices
1. Start the Cook Server via Command Line

To use COTF, you must run the Unreal Editor as a standalone cook server. Use the following command-line argument with the editor executable to begin listening for client requests: UnrealEditor-Cmd.exe [Project.uproject] -run=cook -targetplatform=[Platform] -cookonthefly This initializes the server and keeps it ready to deliver assets to any connected client.

2. Configure the Client Connection

The packaged game (the “Client”) needs to know where the Cook Server is located. Pass the IP address of your workstation to the game executable using the -filehostip flag: MyGame.exe -filehostip=192.168.1.10 Without this flag, the client will fail to connect and may crash due to the elimination of its access to required content.

3. Use a Wired Network Connection

Because COTF streams raw asset data over the network, bandwidth is a major bottleneck. Always use a wired Ethernet connection for both the server and the target device. Relying on Wi-Fi often leads to significant hitches or the elimination of the connection during high-bandwidth asset loads (like high-res textures).

4. Enable “Iterative” Cooking

The COTF module is most effective when paired with the -iterate flag. This ensures the cook server only re-processes assets that have changed since the last request. This results in the elimination of wasted CPU time on the server, making asset updates nearly instantaneous.

5. Monitor the Cook Server Logs

The Cook Server window provides real-time logs of which assets are being requested. If your game hangs while loading a level, check the server logs to see if a specific asset is failing to cook. This is the fastest way to ensure the elimination of broken or incompatible source assets.

6. Use for Mobile and Console Debugging

COTF is essential for platforms with slow file-transfer speeds. Instead of waiting 20 minutes for a 5GB build to copy to a tablet or console, you can deploy a tiny 100MB executable once and stream the 5GB of content on-demand. This facilitates the elimination of hours of downtime during a typical workday.

7. Combine with Zen Store for Speed

In UE 5.3+, COTF can leverage the Zen Store (Unreal’s high-performance data server). When configured correctly, the Zen Store caches cooked data more efficiently, leading to the elimination of redundant cooking operations across different team members or build sessions.

8. Avoid COTF for Performance Profiling

Since COTF loads data over a network, it introduces artificial latency and CPU overhead that wouldn’t exist in a final build. Never use COTF mode for frame-rate or load-time profiling. For accurate performance data, you must perform a full “Cook by the Book” to ensure the elimination of network-related performance variables.