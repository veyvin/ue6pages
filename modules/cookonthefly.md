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

content delivery system for Unreal Engine. Instead of packaging all game assets into a large .pak file before running the game, the COTF module allows the engine to request and “cook” (convert) assets from the Editor/PC to the target device (Console, Mobile, or another PC) in real-time as they are needed.

This module is the backbone of the “Enable cooking on the fly” workflow, significantly reducing iteration times by allowing developers to test changes on target hardware without a lengthy full-package and deployment cycle.

Practical Usage Tips and Best Practices
1. Enable via the Platforms Menu

To use this module, go to the Platforms menu in the Unreal Editor and check the Enable cooking on the fly box. When you “Launch” the game to a target device, the Editor will act as a File Server. This provides the elimination of the need to wait for a 20-minute cook-and-package process for every small tweak.

2. Configure the FileHostIP

When running a build on a mobile device or console, the client must know where the COTF server (your PC) is located. Use the command-line argument -filehostip=XX.XX.XX.XX (replacing with your local IP) when launching the client. This ensures the elimination of connection timeouts between the device and the content server.

3. Leverage Iterative Cooking

The COTF module is designed to work with Iterative Cooking. It checks the timestamps of assets; if you modify a material in the editor, only that material is re-cooked and sent to the device. This leads to the elimination of redundant data transfers and keeps your testing session fast.

4. Transition to Zen Server (UE5+)

In newer versions of Unreal Engine 5, the traditional COTF module is being superseded by the Zen Server and Zen Store. Zen Server provides a more robust, faster, and deduplicated data streaming service. If you encounter instability with legacy COTF, switching to a Zen-based workflow can assist in the elimination of asset corruption during transit.

5. Monitor Network Bottlenecks

Since assets are sent over the network, your Wi-Fi or Ethernet speed becomes your “disk read speed.” If the game hitches when entering a new area, check your network bandwidth. Using a wired connection for both the PC and the dev kit is a best practice for the elimination of streaming-induced lag.

6. Debugging with “LogCookOnTheFly”

If assets are failing to load on the device, check the output log in the Editor. The COTF module provides detailed logs under the LogCookOnTheFly category. Analyzing these logs helps in the elimination of “Missing Asset” errors by identifying if a file was skipped due to a platform-specific cooking error.

7. Combine with “Launch On”

The COTF module is most effective when used with the Launch On feature for rapid UI and gameplay iteration. Because the executable is already on the device, only the modified “uasset” files are pushed. This facilitates the elimination of downtime during daily development tasks.

8. Use for Low-Storage Devices

COTF is ideal for testing large projects on devices with limited storage (like older smartphones). Because assets are streamed on-demand rather than stored in a monolithic bundle, it allows for the elimination of “Out of Disk Space” errors during the development of massive levels.