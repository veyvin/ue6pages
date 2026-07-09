---
layout: default
title: CookOnTheFlyNetServer
---

<!-- ai-generation-failed -->

<h1>CookOnTheFlyNetServer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/CookOnTheFlyNetServer/CookOnTheFlyNetServer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CookOnTheFly, Core, Networking, Sockets, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Cook-on-the-Fly (COTF) system. Its primary role is to act as a bridge between a development PC (the server) and a target device (the client, such as a console or mobile phone), allowing the game to request and receive cooked assets over a network connection in real-time. Instead of waiting for a full project cook and deployment, the engine only cooks assets as they are requested by the game during a session, significantly speeding up iteration for developers working on non-PC hardware.

Practical Usage Tips & Best Practices
1. Ideal for Mobile and Console Iteration

Use this module when working on platforms where deployment times are high. Instead of re-packaging a 10GB build to test a single texture change, the CookOnTheFlyNetServer allows the device to pull the updated texture instantly over the LAN. This facilitates the elimination of the “wait-for-build” bottleneck in the daily dev cycle.

2. Configure the File Host IP

For the client to find the server, you must provide the host’s IP address.

Best Practice: Launch your game with the command-line argument -filehostip=XXX.XXX.XXX.XXX. Ensure your development machine has a static IP or is correctly identified on the network to prevent connection failures.
3. Operate in a Trusted Network

As of the latest engine versions, the communication handled by this module is unauthenticated.

Best Practice: Only use COTF within a trusted office LAN or via a secure VPN. Because the server allows full read/write access to certain cooked data stores, using it on a public network could lead to data corruption or the elimination of project security.
4. Use with Non-Shipping Configurations

The CookOnTheFlyNetServer is designed for Debug, Development, and Test builds.

Tip: Do not attempt to use this system in Shipping builds, as the network hooks and the UCookOnTheFlyServer logic are typically compiled out or disabled for security and performance reasons.
5. Transition to Zen Streaming

In UE 5.4 and later, the engine is moving toward Zen Streaming via the Zenserver.

Tip: While the NetServer module is still vital for legacy workflows, check if your target platform supports Zen Streaming. Zen offers better de-duplication and faster data transfer, leading to the elimination of redundant asset cooking across multiple test devices.
6. Enable Iterative Cooking

To get the most out of the COTF server, ensure the -iterate flag is used. This tells the server to only re-cook assets that have actually changed since the last request. This results in the elimination of unnecessary CPU overhead on your workstation while the game is running.

7. Monitor for Network Latency

Since assets are being pulled over the wire, high network latency can cause hitches or “missing asset” pop-in during gameplay.

Best Practice: Use a high-speed wired connection whenever possible. If you experience long hitches, check the server logs to see if a specific large asset (like a 4K texture or a complex level) is taking too long to cook and send.
8. Graceful Asset Elimination and Reloading

The COTF system is highly sensitive to asset references. If you delete an asset in the Editor while a COTF session is active, the server must handle the elimination of that asset from its cache.

Tip: If you see “File Not Found” errors on the client after deleting assets, restart the COTF server to clear the internal manifest and ensure the client state is synchronized with the local project files.