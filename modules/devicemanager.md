---
layout: default
title: DeviceManager
---

<!-- ai-generation-failed -->

<h1>DeviceManager</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/DeviceManager/DeviceManager.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, InputCore, Slate, SlateCore, TargetPlatform, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

designed to discover, manage, and control target hardware for game deployment and testing. It serves as the primary interface for connecting the Unreal Editor to external devices like smartphones, consoles, and remote PCs.

What it is and What it’s used for

Located under the Platforms menu in the Unreal Editor, the Device Manager handles the communication layer between your development workstation and target platforms. It uses the Target Device Services to identify available hardware on your local network or via direct connection (USB).

Primary uses include:

Device Discovery: Automatically detecting Android, iOS, and console development kits connected to your network.
Claiming and Sharing: Reserving specific devices for your exclusive use so that other developers on the same network cannot accidentally deploy to them.
Remote Power Management: Powering on, rebooting, or shutting down target hardware directly from the Unreal Editor.
Process Monitoring: Viewing running processes and resource usage on a connected device to assist in performance profiling.
Practical Usage Tips and Best Practices
1. Claim Devices to Prevent Conflicts

When working in a team environment, always “Claim” your target device in the Device Manager. This marks the device as busy in the shared network pool. If you leave a device unclaimed, another developer might initiate a deployment to it, causing the elimination of your current testing session and potential data corruption.

2. Use “Connect to IP” for Remote Hardware

If a device (like an Apple TV or a dev kit in a different room) does not appear automatically, use the Connect to IP feature. This is especially critical for tvOS devices which lack USB ports. Ensure your workstation and the target device are on the same subnet to maintain a stable connection.

3. Integrate with the Project Launcher

The Device Manager works in tandem with the Project Launcher. Once a device is claimed and visible in the Device Manager, it will appear as a valid target in your custom Launch Profiles. Use this workflow to create specialized “Debug” or “Shipping” deployment profiles that target specific hardware groups.

4. Monitor Device Health and Details

Select a device and check the Device Details tab. This provides critical information such as the OS version, CPU architecture, and available storage. Verifying these details before a large deployment can help you avoid failures caused by insufficient disk space or unsupported firmware versions.

5. Leverage Horde for Large Device Pools

For studios with massive device farms, integrate with Horde. The Device Manager can interface with Horde to manage “Automation Pools.” This allows you to check out devices programmatically for automated testing, ensuring that devices are returned to the shared pool once the tests are completed.

6. Utilize the Context Menu for Quick Actions

Right-clicking a device in the list provides a context menu for quick commands like Reboot or Power Off. Using these commands from your PC is often faster than physically interacting with the hardware, which is essential for maintaining a high-speed development iteration loop.

7. Debug via “Running Processes”

If your game seems to be performing poorly on a mobile device, use the Running Processes tab in the Device Manager. This view provides a snapshot of the CPU and memory load of all active apps on the device. This helps you determine if a background system process is interfering with your game’s performance.

8. Strategic Elimination of Stale Connections

Over time, the Device Manager list can become cluttered with “Disconnected” or “Unauthorized” entries from old hardware. Periodically use the Remove button to clean your list. Keeping a clean device list reduces the chance of selecting the wrong target when performing a “Quick Launch” from the Platforms menu.