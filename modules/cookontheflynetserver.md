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

Fly (COTF) workflow by facilitating data transfer between a host Cook Server and a target client.

Description and Purpose

This module provides the networking backbone for the “Cook on the Fly” system. In this workflow, a game client (running on a console, mobile device, or PC) does not have all its assets locally. Instead, it requests them over the network from a machine running the Unreal Editor as a Cook Server. The CookOnTheFlyNetServer manages these requests, ensuring the server cooks the requested asset for the specific target platform and streams the resulting data back to the client. Its primary purpose is to eliminate the need for long, full-project cook times during rapid iteration, allowing developers to see content changes on a device almost instantly.

Practical Usage Tips and Best Practices
Configure the File Host IP
For the client to communicate with the server, you must pass the host machine’s IP address to the client’s command line using -filehostip=XXX.XXX.X.X. Without this configuration, the client will fail to connect and will be unable to load any network-streamed assets.
Use with Non-Shipping Build Configurations
COTF and this network server module are intended for Development, Debug, and Test builds. Do not attempt to use this for Shipping builds, as the communication overhead and security implications are not suitable for end-users. Always eliminate COTF dependencies before final packaging.
Monitor Zen Server Integration
In UE 5.6, the Cook-on-the-Fly system is increasingly integrated with Zen Server. Ensure that your local Zen Server is running and accessible, as the CookOnTheFlyNetServer often retrieves the cooked blobs from the Zen Store to stream them to the client.
Enable Iterative Cooking
Combine COTF with the -iterate flag on your server. This ensures that the server only re-cooks assets that have actually changed since the last request, further helping to eliminate idle wait times during your playtesting sessions.
Verify Network Stability
COTF is highly sensitive to network interruptions. If your office or home network is unstable, the client may “hang” while waiting for an asset. Use a wired connection whenever possible to eliminate timeouts and “Asset Not Found” errors during critical debugging.
Stress Test Elimination VFX
When testing heavy assets—such as a complex Niagra effect for a player elimination—use COTF to tweak the effect in the editor and immediately trigger it on the device. The server will re-cook the modified effect and stream it to the client for the next elimination event, providing a near-instant feedback loop.
Check Port Availability
The Cook Server typically listens on a specific port (defaulting to 41002). Ensure your firewall or router is not blocking this traffic. If the client cannot reach the CookOnTheFlyNetServer, it will be unable to boot, so you must eliminate any network blockages before starting your session.
Use for “Map-Only” Iteration
If you are only changing level layouts and not base assets, use the -MAPSONLY flag on your server command line. This narrows the scope of what the CookOnTheFlyNetServer has to manage, making the streaming process even more efficient for level designers.