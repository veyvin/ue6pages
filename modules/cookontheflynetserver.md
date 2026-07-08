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

thin Unreal Engine that manages the communication between a host (typically a PC running the Editor or a dedicated Cooker) and a target device (such as a console, mobile phone, or secondary PC) during a “Cook on the Fly” (COTF) session.

Description

In traditional workflows, all assets must be “cooked” (converted to platform-native formats) and packaged before they can be played on a device. CookOnTheFlyNetServer eliminates this bottleneck by allowing the game client to request and receive assets over the network in real-time as they are needed. This module implements the server-side protocol that listens for asset requests, triggers the cooking process for the requested file, and streams the binary data back to the client. It is the core engine component that enables rapid iteration on-target without full re-packaging.

Practical Usage Tips and Best Practices
1. Ideal for Iterating on Mobile and Consoles

Use this module when you are fine-tuning materials, textures, or Blueprints on a physical device. Instead of waiting several minutes for a full build/deploy cycle, the CookOnTheFlyNetServer ensures that as soon as you save an asset in the Editor, the next time the game loads it on the device, it will pull the updated version automatically.

2. Configure the File Host IP

To establish a connection, you must tell the target device where the server is located. When launching your game on the target, use the command-line argument -filehostip=XX.XX.XX.XX (replacing with your PC’s IP address). This allows the client to find the CookOnTheFlyNetServer instance running on your workstation.

3. Use a Wired Connection

Streaming assets over Wi-Fi is often slow and prone to packet loss, which can cause the game to hitch or hang while waiting for data. For the best experience, use a wired Ethernet connection between your development PC and the target device to eliminate latency and ensure a stable stream of cooked data.

4. Monitor via the Output Log

The CookOnTheFlyNetServer prints detailed logs to the “Output Log” window in the Editor. If an asset fails to load on the device, check the logs for “COTF” entries. It will tell you if the server failed to cook the asset or if the network connection was reset, which is essential for troubleshooting connectivity issues.

5. Verify Firewalls and Ports

Since this is a network-based service, ensure your OS firewall is not blocking the engine’s ports. The server typically communicates over port 41002 (though this can vary). If the device fails to connect, disabling the firewall temporarily is a common step to determine if a port block is preventing the server from being reached.

6. Combine with Zen Store for Performance

In Unreal Engine 5.5 and 5.6, the COTF protocol has been significantly enhanced by the Zen Store. While CookOnTheFlyNetServer handles the communication, the Zen Store acts as the high-speed backend. Ensure Zen is running in your system tray to provide the fastest possible data throughput to your target device.

7. Handle Asset Elimination Safely

If you delete or “eliminate” an asset from your project while a COTF session is active, the server may still have a cached version or the client may crash when it fails to find the asset it was expecting. If you perform a major cleanup or elimination of project files, it is a best practice to restart both the Editor (server) and the game client to ensure the network manifests are synchronized.

8. Use for Shader Iteration

One of the most powerful uses of this module is iterating on complex shaders. When you change a node in a Material and hit Apply, the CookOnTheFlyNetServer will detect the change and re-cook the shader for the target platform. The device will then hitch momentarily as it receives the new shader bytecode, allowing you to see the visual change on the final hardware almost instantly.