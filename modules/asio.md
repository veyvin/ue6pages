---
layout: default
title: Asio
---

<!-- ai-generation-failed -->

<h1>Asio</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/asio/Asio.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, OpenSSL</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rary, a cross-platform header-only library for network and low-level I/O programming. In Unreal Engine 5.6, it is located under Engine/Source/ThirdParty/Asio.

Description and Purpose

Asio provides a consistent asynchronous model for networking and concurrency that is often more robust and flexible than standard socket wrappers. In Unreal Engine, it is not used for primary gameplay networking (which relies on UNetDriver and FSocket). Instead, it is a critical low-level dependency for third-party integrations and peripheral protocols. Systems like Pixel Streaming (via WebRTC), LiveLink, and certain OSC implementations rely on Asio to handle high-frequency, non-gameplay data streams without taxing the Unreal Game Thread.

Practical Usage Tips and Best Practices
Link via Third-Party Logic in Build.cs
Asio is a header-only library, but you should still link it properly through the engine’s build system to ensure include paths are correctly resolved across different platforms:
AddEngineThirdPartyPrivateStaticDependencies(Target, "Asio");
Define ASIO_STANDALONE
Unreal’s version of Asio is typically configured to run in “standalone” mode, meaning it does not require Boost. Ensure your project’s Build.cs or private header defines this macro to avoid accidental dependencies on non-existent Boost headers:
PublicDefinitions.Add("ASIO_STANDALONE=1");
Isolate Asio in an FRunnableThread
The asio::io_context::run() function is blocking. Never call it on the Game Thread. Instead, wrap your Asio logic inside an FRunnable and create a dedicated FRunnableThread. This ensures that your network I/O loop runs concurrently and does not cause frame rate hitches.
Use asio::post for Thread Safety
When you need to send data from the Game Thread (e.g., a player’s coordinate) to an Asio-managed socket, use asio::post. This safely queues the work for the Asio background thread, eliminating the need for complex mutex-based locking between Unreal and Asio logic.
Namespace Management (absl vs asio)
Because Asio is often used alongside the Abseil module (especially in WebRTC contexts), be mindful of namespace overlap. Always use explicit asio:: and absl:: prefixes. Avoid using namespace directives to prevent naming collisions with Unreal’s Core types.
Prefer Task Graph for Event Dispatch
If an Asio callback (like receiving a packet) needs to update a gameplay element (like a UI text block), do not modify the UObject directly from the Asio thread. Use AsyncTask(ENamedThreads::GameThread, [...]() { ... }); to jump back to the Game Thread safely.
Standardize Elimination Reporting
If you are using Asio for a custom telemetry or spectator system, use its async timers to batch data. For instance, when an elimination occurs, don’t send a packet immediately; use an asio::steady_timer to collect all elimination data over a 100ms window and send them in a single compressed burst to reduce overhead.
Proper Shutdown Handling
Always stop the io_context and join the background thread in your module’s ShutdownModule or an Actor’s EndPlay. Failing to stop a running Asio loop will prevent the Unreal Editor from shutting down cleanly or lead to “Zombie” processes in the Task Manager.