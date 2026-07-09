---
layout: default
title: HTTPServer
---

<!-- ai-generation-failed -->

<h1>HTTPServer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Online/HTTPServer/HttpServer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, HTTP, Sockets</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

real Engine instance to function as a lightweight web server. While the “Remote Control” plugin is the most well-known user of this module, HTTPServer can be used independently to build custom REST APIs, inter-process communication (IPC) bridges, or live-data ingestion pipelines directly within your game or editor.

Practical Usage Tips & Best Practices
1. Dispatch Work to the Game Thread

HTTP requests are received on a background listener thread. If your C++ handler needs to spawn an actor, modify a property, or call a Blueprint event, you must move that logic to the main thread.

Best Practice: Use AsyncTask(ENamedThreads::GameThread, [=]() { ... }); inside your handler. This ensures the elimination of race conditions and crashes that occur when interacting with UObjects from a background thread.
2. Register Unique Routes via IHttpRouter

The IHttpRouter is the primary interface for defining your API’s endpoints.

Tip: Access the router using FHttpServerModule::Get().GetHttpRouter(Port). Use specific paths (e.g., /api/v1/status) rather than generic ones to ensure the elimination of route collisions if other plugins or engine systems also utilize the HTTP server.
3. Use Asynchronous Response Callbacks

Handlers in this module use a FHttpResultCallback pattern. This allows you to process requests without blocking the listener.

Best Practice: Do not perform heavy computation directly in the handler. Capture the OnComplete callback and trigger it only once your data is ready. This approach results in the elimination of “Request Timeout” errors on the client side during heavy frame-time spikes.
4. Manage Module Dependencies Correctly

Because this is a developer-centric module, it is often not included by default in runtime builds.

Tip: Add "HttpServer" to your PublicDependencyModuleNames in your project’s Build.cs. If your tool is for internal use only, wrap the logic in #if WITH_EDITOR to ensure the elimination of linker errors when packaging a shipping build.
5. Implement Basic Authentication and IP Filtering

The HTTPServer module is “naked” by default and does not provide built-in SSL or advanced security.

Best Practice: If your tool is exposed to a network, manually inspect the FHttpServerRequest headers for a custom “Auth-Key” or verify the PeerAddress. This is a critical step toward the elimination of unauthorized remote execution vulnerabilities in your development environment.
6. Leverage JSON for Structured Data

Most modern web tools communicate via JSON, and Unreal’s Json module pairs perfectly with the HTTPServer.

Tip: Convert the incoming Request.Body (a TArray<uint8>) into an FString and parse it using FJsonSerializer. This standardized workflow assists in the elimination of fragile string-parsing logic when handling complex command parameters.
7. Handle Port Conflicts Gracefully

If you run multiple instances of your game on the same machine (e.g., for multiplayer testing), the second instance will fail to bind to the default port.

Best Practice: Use a configuration variable or command-line argument to set the port dynamically. Implementing a “retry on next available port” logic during initialization leads to the elimination of “Address already in use” errors during local playtests.
8. Ensure Object Lifetime Safety

Since handlers are delegates, they can outlive the class that registered them if the level changes or an actor is destroyed.

Tip: When binding a route to a class member, use TWeakObjectPtr to check for validity or ensure you call UnbindRoute in EndPlay or ShutdownModule. This ensures the elimination of “dangling pointer” crashes when a request is received after its owner has been garbage collected.