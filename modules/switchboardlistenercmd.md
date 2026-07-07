---
layout: default
title: SwitchboardListenerCmd
---

<!-- ai-generation-failed -->

<h1>SwitchboardListenerCmd</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/SwitchboardListener/SwitchboardListenerCmd/SwitchboardListenerCmd.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">SblCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rtual Production ecosystem, providing the command-line interface and logic for the Switchboard Listener application.

Description and Purpose

The Switchboard Listener is a standalone companion application that must run on every remote machine in a cluster (such as nDisplay nodes, Render Nodes, or Multi-User workstations). The SwitchboardListenerCmd module handles the network communication between the main Switchboard operator and these remote machines. Its primary purpose is to act as a remote executor: it receives commands via TCP/IP to launch the Unreal Engine, sync files from Perforce, monitor system performance, and manage logs. By using this listener, a single operator can eliminate the need to manually log into multiple PCs to start a synchronized session.

Practical Usage Tips and Best Practices
Run Outside the Editor Environment
The listener is a lightweight console application. You should run it as a standalone executable (found in Engine/Binaries/Win64/SwitchboardListener.exe) rather than through the editor. This is a best practice to eliminate the overhead of the Unreal Editor UI on your render nodes.
Assign Static IP Addresses
For stable production environments, ensure every machine running the listener has a static IP address. This allows the main Switchboard application to reliably find and connect to every node, helping you eliminate connection failures caused by DHCP lease changes.
Configure Firewall Exceptions
The listener typically communicates over port 2980. Ensure your Windows Firewall or network security software has an explicit inbound rule for this port. Proper configuration will eliminate “Connection Timed Out” errors when trying to deploy a cluster.
Add to OS Startup Tasks
On a professional stage, add the Switchboard Listener to the Windows “Startup” folder or create a Scheduled Task to launch it on login. This ensures the nodes are ready to receive commands as soon as the PC boots, which helps to eliminate manual setup time during a shoot.
Monitor the Listener Console for Crashes
If an Unreal instance fails to launch, check the console window of the Switchboard Listener on the target machine. It often captures low-level OS errors or “File Not Found” exceptions that are eliminated from the main Switchboard UI, providing vital debugging info.
Use the “-ip” and “-port” Arguments
If a machine has multiple network adapters (e.g., one for management and one for a high-speed data plane), use the -ip command-line argument when launching the listener. This forces it to bind to the correct network, helping you eliminate traffic routing issues.
Maintain Version Parity
Always ensure the version of the SwitchboardListenerCmd module matches the version of the main Switchboard application. Using mismatched versions can cause protocol errors; keeping them in sync will eliminate “Invalid Command” or serialization errors during cluster orchestration.
Integrate with Perforce (P4)
The listener can handle Perforce workspace syncing directly. Ensure the P4 command-line tools are installed on the remote nodes. This allows the operator to trigger a “Sync and Build” command, which helps to eliminate version mismatches across the entire cluster.