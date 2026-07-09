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

ine that enables the engine to access files over a network connection rather than from the local disk. It is the core technology behind the Network File Server (NFS) and the Cook-on-the-fly (COTF) systems.

This module is primarily used during development to stream cooked assets from a powerful workstation (the “Cook Server”) to a target device (like a mobile phone or console). This allows developers to iterate on assets and see changes on the device without having to repackage and redeploy the entire build.

Practical Usage Tips & Best Practices
1. Use for Rapid Iteration on Consoles and Mobile

The primary benefit of this module is the elimination of the “Package-Deploy-Install” cycle, which can take several minutes or even hours for large projects.

Best Practice: Launch your game with the -filehostip=XX.XX.XX.XX command line argument. This directs the target device to request assets via the NetworkFileSystem module from your PC, allowing for near-instant updates when you modify a texture or blueprint.
2. Prefer Ethernet over Wi-Fi

Since the NetworkFileSystem module must transfer high-resolution textures and meshes in real-time as the game requests them, network latency is a critical factor.

Tip: Always use a wired Ethernet connection for both your PC and the target device. This results in the elimination of “hitching” or “asset popping” that occurs when the network bandwidth is insufficient to keep up with the game’s loading demands.
3. Manage the “Cook-on-the-fly” Cache

The NetworkFileSystem module works in tandem with a running instance of the Unreal Editor acting as a server.

Best Practice: If you notice assets are not updating on the device, use the recompile or clearcache commands on the server. Cleaning the server-side cache ensures the elimination of stale data being sent to the client.
4. Configure Firewall Exceptions for NFS Ports

The module typically communicates over specific ports (often 41899 for the File Server).

Tip: Ensure your workstation’s firewall has explicit inbound rules for the Unreal Editor and its network file services. Proper port configuration leads to the elimination of “Connection Timed Out” errors when the target device attempts to initialize the network file system.
5. Monitor Network I/O with “Stat Net”

If the game feels sluggish while using the NetworkFileSystem, you need to determine if the bottleneck is the network or the disk.

Best Practice: Use the console command stat net or stat file on the target device. Visualizing the data transfer rates facilitates the elimination of guesswork when diagnosing why a specific level is taking a long time to stream from the server.
6. Utilize Zen Server for Improved Performance

In newer versions of Unreal Engine (5.x), the NetworkFileSystem often interfaces with the Zen Server for optimized data delivery.

Tip: Ensure Zen Server is enabled in your project settings for cooked output. Utilizing Zen’s streaming capabilities results in the elimination of redundant file compression steps, making the network file streaming process significantly faster.
7. Isolate the “Development” Network

In a studio environment, having dozens of devices requesting assets simultaneously can saturate the office network.

Best Practice: Use a dedicated local subnet or a high-speed switch specifically for development kits. Isolating this traffic leads to the elimination of network congestion that could otherwise slow down the rest of the team’s internet access and version control syncing.
8. Verify UECommandLine.txt on Device

For the NetworkFileSystem to initialize, the target device needs to know it should look for a network server rather than local .pak files.

Tip: Check the UECommandLine.txt file on your device’s storage. Ensuring the -filehostip argument is correctly written there facilitates the elimination of “Black Screen” launches where the device fails to find any boot assets because it is looking in the wrong location.