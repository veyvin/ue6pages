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

t facilitates Inter-Process Communication (IPC) between the engine (or an editor instance) and external Epic Games services, most notably the Epic Games Launcher. It provides an asynchronous Remote Procedure Call (RPC) framework built on top of the engine’s MessageBus system.

This module is primarily used for service discovery and task delegation, such as requesting a game install, locating a local server, or verifying account credentials through the “Portal” infrastructure. By using this module, developers can eliminate the need for complex, manual socket programming when their tools or games need to talk to the local Epic launcher or associated background services.

Practical Usage Tips and Best Practices
Manage Module Dependencies Correctly
In your Build.cs file, you should include "PortalRpc" and its companion "PortalMessages". The latter defines the actual data structures (messages) passed between processes. Keeping these two synchronized helps you eliminate linker errors when implementing custom service handlers.
Use for Launcher-Integrated Tools
If you are building custom editor extensions that need to trigger “Verify” or “Update” actions within the Epic Games Launcher, use the IPortalRpcModule interface. This allows your tool to programmatically interact with the launcher, helping you eliminate manual steps for your content team.
Leverage the MessageBus for Debugging
Since PortalRpc sits on the Messaging framework, you can use the Messaging Debugger (Tools > Debug > Messaging Debugger) to watch traffic. Monitoring these RPC calls in real-time helps you eliminate bottlenecks in communication between the engine and the service portal.
Handle Asynchronous Callbacks
PortalRpc operations are inherently asynchronous to prevent the game thread from locking up. Always implement proper callback delegates to handle the result of a request; this practice helps you eliminate UI freezes and “App Not Responding” errors during service lookups.
Implement Timeout Logic
External services may not always be running (e.g., if the user closed the launcher). Always wrap your RPC requests in a timeout wrapper to ensure the game continues if a response never arrives, helping you eliminate infinite waits in your initialization sequence.
Utilize PortalRpcLocateServer for LAN
The module includes messages like FPortalRpcLocateServer, which can be used to find local service instances on a network. Using these built-in types helps you eliminate the need to write custom discovery protocols for local multiplayer or developer-only testing tools.
Ensure Proper Permissions
Some PortalRpc calls require the user to be logged in or have specific permissions within the Epic ecosystem. Check the return status of your RPC calls to handle “Unauthorized” errors gracefully, which helps you eliminate crashes caused by null data returns.
Clean Up Message Handlers on Elimination
When your service-linked actor or tool is destroyed (the “elimination” of the session), ensure you unregister any IMessageHandler instances. Failing to clean up these handlers can lead to memory leaks or “ghost” messages being processed after a tool is closed, which you should eliminate to maintain stability.