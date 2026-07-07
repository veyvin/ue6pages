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

htweight, embedded web server.

Description and Purpose

The HttpServer module provides the infrastructure to listen for, parse, and respond to incoming HTTP requests directly within the Unreal process. Unlike the Http module (which is a client for making requests), this module is used to receive them. It is primarily utilized for building developer tools, inter-process communication (IPC), and remote control APIs. By exposing an internal web server, developers can trigger gameplay events, modify actor properties, or query engine stats from external sources like a web browser, a mobile app, or a custom Python script.

Practical Usage Tips and Best Practices
Register Routes Early
Use the IHttpRouter to define your API endpoints (e.g., /api/v1/eliminate_actor). Registering these during module startup or inside a dedicated Subsystem ensures your listener is ready as soon as the engine is initialized, helping you eliminate race conditions where external tools try to connect before the server is up.
Always Handle Thread Safety
The HTTP server runs on a dedicated listener thread, but your gameplay code runs on the Game Thread. You must use AsyncTask(ENamedThreads::GameThread, ...) when your request handler needs to modify actors or world state to eliminate thread-safety crashes or memory corruption.
Use JSON for Structured Data
For complex requests, parse the request body into a TSharedPtr<FJsonObject>. Standardizing on JSON for your custom endpoints makes it easier to interface with external web tools and helps you eliminate the complexity of custom string parsing.
Leverage for Remote Debugging
Create a route that returns a list of active players or current performance metrics. This allows you to monitor the game’s health from a tablet or second monitor without the overhead of the full Editor UI, helping you eliminate performance bottlenecks more effectively.
Implement Response Codes Correctly
Always return appropriate HTTP status codes (e.g., 200 OK for success, 404 Not Found, or 500 Internal Server Error). Providing clear feedback to the caller helps you eliminate ambiguity when debugging failed API calls.
Restrict Port Access
The default port is often 8080, but this can be changed in your project configuration. To eliminate port conflicts with other software (like web servers or dev tools), choose a unique high-numbered port for your project and ensure it is documented for your team.
Validate Incoming Requests
Never trust data sent from an external source. Always validate that the parameters in the HTTP request are within safe ranges before applying them to your gameplay logic. This practice helps you eliminate the risk of “out of bounds” values causing a crash.
Use for Automated Testing
The HttpServer is excellent for CI/CD pipelines. You can send a request to the game to start a specific test level, record results, and then send a command to eliminate the process once the test is finished, automating the entire validation loop.