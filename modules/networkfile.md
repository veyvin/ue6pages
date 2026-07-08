---
layout: default
title: NetworkFile
---

<!-- ai-generation-failed -->

<h1>NetworkFile</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/NetworkFile/NetworkFile.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CookOnTheFly, Core, CoreUObject, Sockets</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ile interface designed to redirect file system requests over a network. It primarily acts as a wrapper that allows a target device (such as a console or mobile phone) to “stream” game files directly from a host PC instead of reading them from local storage.

This module is the backbone of the Unreal Network File Server (UNFS). By enabling a connection between the runtime client and the editor/cooker, it facilitates the elimination of the time-consuming “package and deploy” cycle. Developers can modify assets in the editor and see the changes reflected on the physical device almost immediately, as the device fetches the updated files over the network on demand.

Practical Usage Tips and Best Practices
1. Use the -FileHostIP Command-Line Argument

To activate the NetworkFile system on a client device, you must launch the application with the -filehostip=XXX.XXX.XXX.XXX argument, where the IP points to your workstation. This tells the engine to initialize FNetworkPlatformFile, leading to the elimination of the default local file system in favor of the network-redirected path.

2. Ensure Network Port 57000 is Open

The Unreal Network File Server typically communicates over port 57000. Ensure that your workstation’s firewall is configured to allow inbound traffic on this port. Proper network configuration assists in the elimination of connection timeouts and “File Not Found” errors during the device boot process.

3. Optimize for High-Latency Connections

Streaming large assets like 4K textures or high-poly meshes over Wi-Fi can cause significant hitches. Whenever possible, use a wired connection (USB-to-Ethernet or a devkit LAN port). This practice facilitates the elimination of stalls during loading screens while the NetworkFile module waits for data packets to arrive.

4. Combine with Iterative Cooking

The NetworkFile module works best when paired with Iterative Cooking. By only cooking the assets that have changed and serving them via the network, you ensure the elimination of redundant data transfers, making the iteration loop as fast as possible for designers and artists.

5. Monitor Network Traffic via Unreal Insights

If you experience performance drops while using network streaming, use Unreal Insights to audit file I/O. The NetworkFile module’s activity will appear in the traces, helping you identify which specific assets are causing bottlenecks. This data is essential for the elimination of assets that are too large for efficient network streaming.

6. Use the -StreamingHostIP for Audio/Video

For specialized media streaming that bypasses standard file logic, you may also need to set -streaminghostip. While NetworkFile handles general bulk data, ensuring both IPs are set leads to the elimination of desync issues between your game logic and streamed media assets.

7. Verify Sandbox Path Permissions

On mobile platforms like Android, the NetworkFile module needs permission to write to its local sandbox for caching purposes. If permissions are missing, the module may fail to initialize. Checking your Project Settings for appropriate storage access leads to the elimination of startup crashes when running in network-file mode.

8. Disable for Shipping Builds

The NetworkFile module is a development tool and should never be active in a production environment. The engine’s build system is designed for the elimination of this module during the “Shipping” configuration to prevent security vulnerabilities and ensure the game only reads from local, authenticated pak files.