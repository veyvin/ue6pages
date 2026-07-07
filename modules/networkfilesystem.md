---
layout: default
title: NetworkFileSystem
---

<!-- ai-generation-failed -->

<h1>NetworkFileSystem</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/NetworkFileSystem/NetworkFileSystem.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CookOnTheFly, CookOnTheFlyNetServer, Core, CoreUObject, DesktopPlatform, Engine, Projects, SandboxFile, Sockets, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

he engine to serve and access files over a network connection, primarily used to support “Cook-on-the-Fly” (COTF) and remote file streaming.

Description and Purpose

This module acts as the backend for the Unreal File Server, allowing a host PC (the server) to send cooked game assets to a target device (the client, such as a console or mobile phone) in real-time. Instead of packaging the entire game and deploying a massive build, the target device requests only the files it currently needs as the player moves through the level. This workflow is essential for rapid iteration, as it allows developers to eliminate the long wait times associated with full deployment cycles when testing changes on physical hardware.

Practical Usage Tips and Best Practices
Implement via -filehostip Command
To connect a target device to your workstation’s file server, launch the client application with the -filehostip=XXX.XXX.X.X parameter. This tells the NetworkFileSystem client where to request assets, helping you eliminate the need to manually copy .pak files to the device storage during development.
Open Required Ports in Firewalls
The Network File Server typically communicates over ports 41000 to 41099. Ensure these ports are open on your host machine’s firewall. Proper port management is the best way to eliminate “Connection Timed Out” errors when the target device attempts to reach the host.
Utilize Zen Server for Streaming
In UE 5.x, the NetworkFileSystem logic often integrates with the Zen Server. When using Zen for streaming cooked output, ensure your network is “Trusted” (LAN/VPN). This allows for high-granularity data transfer and helps you eliminate redundant data transformations between the cook and stage phases.
Ensure Network Stability on Mobile
When using the network file system with mobile devices, a stable 5GHz Wi-Fi or a wired Ethernet connection is highly recommended. Frequent packet loss can cause the engine to hitch while waiting for assets, so a solid connection is a best practice to eliminate false performance readings during mobile optimization.
Combine with Cook-on-the-Fly (COTF)
Use the -cookonthefly flag on your editor command line to start the server. This module will then monitor your project for changes; if you modify a texture and reload the level on your device, the server will re-cook just that asset and send it over, allowing you to eliminate the need to restart the server or the client app.
Monitor Server Logs for Request Failures
Keep the File Server console window visible. It will log every file request made by the client. If the game crashes on the device, checking the last requested file in the log is the fastest way to eliminate guesswork and identify a corrupted or missing asset.
Exclude Shipping Builds
The NetworkFileSystem and its associated servers are unauthenticated and intended for trusted local environments only. Never include these protocols in a Shipping build configuration. This security practice helps you eliminate potential data leaks or unauthorized file access in public releases.
Use for Rapid UI Iteration
The network file system is particularly effective for UI/UX designers. Since UMG and texture changes can be pushed to the device via the network file server almost instantly, it allows you to eliminate the friction of testing touch-screen layouts on the actual hardware.