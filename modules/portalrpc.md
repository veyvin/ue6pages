---
layout: default
title: PortalRpc
---

<!-- ai-generation-failed -->

<h1>PortalRpc</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Portal/Rpc/PortalRpc.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, MessagingRpc</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

within Unreal Engine. It is designed to facilitate communication between the Unreal Engine Editor (or a running game instance) and external Epic services, most notably the Epic Games Launcher (historically referred to as the “Portal”).

Unlike gameplay RPCs that handle networking between a server and a client, PortalRpc uses the engine’s internal MessageBus system to send commands and data across different local processes. It is primarily used for tasks like managing game installs, handling launcher-driven updates, and coordinating the “Launch” flow from the store to the engine.

Practical Usage Tips and Best Practices
1. Distinguish from Gameplay Networking

It is critical to understand that PortalRpc has nothing to do with multiplayer replication or Server/Client function specifiers.

Best Practice: Never attempt to use PortalRpc for in-game player actions. Use it strictly for “Launcher-to-App” logic, such as checking for an available update or notifying the launcher that the game has successfully booted. This helps you eliminate confusion in your networking architecture.
2. Manage Dependency via Build.cs

Since this module is often used for platform-level integration, it must be included correctly in your C++ project.

Action: Add "PortalRpc" and "PortalServices" to your PrivateDependencyModuleNames in your *.Build.cs file. Ensure these are wrapped in an Editor or Developer target check if you do not need them in your final shipping build, effectively eliminating unnecessary bloat in your game executable.
3. Use IPortalRpcLocator for Discovery

To communicate with the launcher, your code needs to “find” the active portal process.

Tip: Utilize the IPortalRpcLocator interface to identify the available RPC endpoints. This automated discovery system helps you eliminate the need to hardcode port numbers or process IDs when trying to talk to the Epic Games Launcher.
4. Leverage for Custom Launcher Tools

If you are building a custom pipeline tool that needs to trigger a “Verify” or “Update” command within the Epic ecosystem:

Action: Send a message through the PortalRpc bus to the launcher’s service handlers. This allows your internal studio tools to trigger launcher actions directly, eliminating the manual steps usually required by developers to refresh their build environments.
5. Monitor via the Messaging Debugger

Because PortalRpc relies on the MessageBus, you can visualize its traffic in the editor.

Tip: Open the Messaging Debugger (Window > Developer Tools > Messaging Debugger). You can see the heartbeat and data packets sent between the engine and the launcher, which helps you eliminate guesswork when debugging why a “Launch Game” command isn’t responding.
6. Handle Async Responses Correctly

IPC communication is inherently asynchronous. The launcher may not respond immediately to a request from the engine.

Best Practice: Always implement a timeout or a “Promise/Future” pattern when calling PortalRpc functions. This prevents the Game Thread from hanging while waiting for an external process, eliminating potential “Application Not Responding” (ANR) errors.
7. Ensure MessageBus Is Enabled

PortalRpc cannot function if the engine’s messaging system is disabled.

Action: If you are running a command-line tool or a standalone build, ensure you pass the -messaging flag. This initializes the bus that PortalRpc uses, eliminating silent failures where messages are sent but never received by the launcher.
8. Respect Cross-Process Security

PortalRpc is designed to be secure and only communicate with verified Epic processes.

Tip: Avoid trying to “inject” custom messages into the PortalRpc channel from unauthorized third-party apps. Stick to the provided API to eliminate the risk of security violations or being flagged by anti-cheat systems that monitor suspicious inter-process traffic.