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

Engine IoStore (Input/Output Store) system, designed to handle asset streaming over HTTP.

Description and Purpose

This module provides a specialized HTTP client that connects the engine’s IoStore architecture to remote data sources, specifically ZenServer. Its primary purpose is to enable Zen Streaming, an experimental but powerful iteration workflow where a target device (such as a mobile phone or console) streams cooked assets directly from a host PC’s memory or disk via a network socket. By using this module, developers can eliminate the need to package, stage, and deploy massive .pak files to a device every time a small content change is made, allowing the game to pull only the data it needs over a local network.

Practical Usage Tips and Best Practices
Utilize Zen Streaming for Rapid Iteration
Enable Zen Streaming in your Project Settings > Packaging by turning on “Use ZenServer as cooked output store.” This utilizes the IoStoreHttpClient to fetch assets on demand, which helps you eliminate the “Deploy to Device” bottleneck during daily content iteration.
Configure the ue.projectstore File
The client relies on a ue.projectstore file located in the staged build folder. This file contains the IP address and port of your host PC. Ensure your workstation’s firewall is configured to allow traffic on the ZenServer port (default 13400) to eliminate connection timeout errors on the target device.
Monitor Throughput with zen.showgraphs
While the game is running on the target device, use the console command zen.showgraphs 1. This displays a real-time plot of the network streaming performance, helping you eliminate performance mysteries by identifying if hitches are caused by network latency or asset size.
Override Host Settings via Command Line
If your host PC’s IP address changes frequently, you can bypass the ue.projectstore file by passing -ZenStoreHost=<IP_ADDRESS> as a launch argument to the game. This flexibility allows you to eliminate the need to re-stage the build just to update a network address.
Use on Trusted Local Networks Only
The IoStoreHttpClient is optimized for high-speed, low-latency local connections. Using it over a slow VPN or unstable Wi-Fi can lead to significant loading hitches. For the best experience, use a wired connection or high-performance 5GHz Wi-Fi to eliminate streaming-induced stutter.
Validate Asset Availability in the Hub
If assets are failing to stream, check the Zen Dashboard on your host PC. Ensure the project is correctly “indexed.” If the dashboard shows no active project, the client will have nothing to pull, leading to an elimination of all textures and meshes in the level.
Optimize for Non-Shipping Configurations
This module and the streaming workflow it supports are intended for Debug and Development builds. Ensure you switch back to standard File/Pak system for Shipping builds to eliminate any dependency on a host workstation and to ensure maximum security for your end-users.
Check Module Dependencies in Build.cs
If you are writing custom engine extensions that interact with remote I/O, ensure you add IoStoreHttpClient to your PrivateDependencyModuleNames in your .Build.cs file. This ensures the necessary HTTP protocols for IoStore are linked, helping you eliminate “Unresolved External Symbol” errors during compilation.