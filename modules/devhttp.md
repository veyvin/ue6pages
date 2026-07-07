---
layout: default
title: DevHttp
---

<!-- ai-generation-failed -->

<h1>DevHttp</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/DevHttp/DevHttp.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, HTTP, SSL, XCurl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

facing HTTP features) provides a lightweight, embedded HTTP server within the Unreal Engine process.

Description and Purpose

This module is designed to enable external communication with a running instance of Unreal Engine (Editor, Standalone, or Dedicated Server) via standard HTTP requests. Its primary purpose is to facilitate tooling, automation, and remote monitoring. It allows developers to create REST-like endpoints to query engine stats, trigger console commands, or interface with external web-based dashboards. In recent versions, it serves as the backbone for features like the Remote Control API and PerfCounters, enabling a “headless” way to interact with the engine without a traditional UI or gameplay connection.

Practical Usage Tips and Best Practices
Bind Custom Routes for Automation
Use IHttpServerModule::Get().CreateHttpRouter(Port) to register custom GET or POST handlers. This is ideal for CI/CD pipelines where you need to trigger a specific event—such as an automated elimination test suite—and receive a JSON response confirming the results.
Manage Listener Lifecycles Carefully
Listeners started by this module do not always shut down automatically when a world ends. You should explicitly stop your listeners in EndPlay or ShutdownModule to eliminate port-binding conflicts (e.g., “Address already in use”) when restarting a PIE session or reloading a level.
Security and Network Exposure
By default, this server can be exposed to your local network. Always wrap your HTTP server logic in #if WITH_EDITOR or #if !UE_BUILD_SHIPPING blocks. This ensures you eliminate potential security vulnerabilities by preventing production builds from listening for external web requests.
Use for Dedicated Server Monitoring
On headless dedicated servers, use DevHttp (via the PerfCounters module) to expose a health-check endpoint. You can query this via curl to see the number of active players or the current server FPS, allowing you to eliminate the need for a full game client just to check server status.
Leverage JSON for Complex Data
When sending data back to a web dashboard, use the FJsonObject and FJsonSerializer classes. This module works best when paired with JSON, allowing you to transform complex engine structs—like a list of recent elimination events—into a format that external web apps can easily parse and graph.
Handle Requests on the Correct Thread
HTTP requests usually arrive on a background thread. If your handler needs to interact with UObjects or the World (e.g., to eliminate an actor via a web command), you must use AsyncTask(ENamedThreads::GameThread, [=](){ ... }) to move the logic to the Game Thread and eliminate potential race conditions and crashes.
Utilize the Remote Control Web Interface
Before writing a custom HTTP server from scratch, check if the Remote Control API (which utilizes this module’s underlying tech) already meets your needs. It provides a robust, pre-built way to call BlueprintCallable functions via HTTP, helping you eliminate redundant boilerplate code.
Set Explicit Ports to Avoid Conflicts
If running multiple instances of the engine on one machine (like a local multiplayer test), ensure each instance uses a unique port for its HTTP server. Hard-coding a single port can lead to initialization failures; using a command-line argument to offset the port will eliminate these collisions.