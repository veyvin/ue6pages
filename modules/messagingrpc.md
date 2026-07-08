---
layout: default
title: MessagingRpc
---

<!-- ai-generation-failed -->

<h1>MessagingRpc</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/MessagingRpc/MessagingRpc.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, MessagingCommon</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the Unreal Message Bus (Messaging module). It allows for Remote Procedure Calls (RPCs) between different processes—such as the Unreal Editor, standalone game instances, or external command-line tools—without requiring a traditional network connection (like a socket-based server/client).

It is primarily used for inter-process communication (IPC) within tools and multi-process architectures. By providing a “request-response” pattern over the message bus, it facilitates the elimination of complex manual message-tracking logic, allowing developers to call functions on remote instances as if they were local.

Practical Usage Tips and Best Practices
1. Define Request and Response Structs

MessagingRpc relies on USTRUCT definitions to pass data. For every RPC, you should define a “Request” struct and a “Response” struct. Keeping these structs minimal and focused on data only leads to the elimination of serialization overhead and reduces the latency between the calling process and the responder.

2. Use for Multi-Process Tooling

If you are developing a tool where an external application (like a custom Python script or a separate C++ utility) needs to trigger actions inside the Unreal Editor, use IMessageRpcServer and IMessageRpcClient. This setup facilitates the elimination of “polling” mechanisms, as the RPC system will notify your code immediately when a command is received.

3. Implement Timeout Handling

RPCs over the message bus are asynchronous and can fail if the remote process is busy or disconnected. Always implement a timeout handler when calling CallRpc. This practice leads to the elimination of “hanging” logic where your tool waits indefinitely for a response that will never arrive.

4. Ensure Thread Safety

Message bus callbacks often occur on a background thread (the Messaging thread). If your RPC response needs to modify the level or update the UI, you must wrap that logic in an AsyncTask(ENamedThreads::GameThread, ...) block. This is a critical best practice for the elimination of race conditions and editor crashes.

5. Target Specific Endpoints

The Message Bus can be noisy if multiple instances of the editor are open on the same network. When calling an RPC, use the FMessageAddress of a specific recipient rather than broadcasting to everyone. This precision assists in the elimination of “duplicate execution” bugs where multiple processes try to respond to the same request.

6. Register RPC Handlers in StartupModule

To ensure your system is ready to receive commands as soon as the process starts, register your IMessageRpcServer handlers in your module’s StartupModule() function. This leads to the elimination of “lost messages” that occur if a client tries to communicate with a server that hasn’t finished its internal setup.

7. Audit Message Bus Traffic

If your RPCs involve large amounts of data (like sending mesh buffers or high-res textures), monitor the message bus performance. Excessive traffic can saturate the bus and slow down other engine services like Live Link. Optimizing your data payload leads to the elimination of network-induced frame drops in the editor.

8. Validate Struct Reflection

Since MessagingRpc uses the engine’s reflection system to serialize data, all structs must be marked with USTRUCT() and all members with UPROPERTY(). Forgetting these macros leads to the elimination of the data during transport, resulting in empty or “zeroed out” requests arriving at the destination.