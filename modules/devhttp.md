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

provides a lightweight HTTP server and client framework for internal engine tools and development-time communication.

Description

Unlike the standard HTTP module used for game-side network requests (like connecting to a REST API), DevHttp is designed to facilitate local or network-based communication between the Unreal Editor and external developer tools. It is primarily used to host small internal services, such as the Web Remote Control backend, performance profiling dashboards, or automated testing hooks. It allows external applications to “talk” to a running instance of Unreal Engine using standard web protocols. Because it is a “Developer” module, it is excluded from shipping builds to prevent security vulnerabilities in production environments.

Practical Usage Tips and Best Practices
1. Use for Local Development Dashboards

The DevHttp module is the best choice if you are building a custom web-based dashboard to monitor your game’s internal variables (like AI state or memory usage). You can set up a local listener that serves JSON data, allowing you to view project health in a standard web browser on a second monitor without adding overhead to the game’s UI.

2. Restrict to Development Configurations

Because this module is intended for internal use, always wrap your implementation code in #if WITH_EDITOR or #if !UE_BUILD_SHIPPING blocks. This ensures that any logic relying on DevHttp is completely stripped from the final executable, preserving security and reducing the final binary size.

3. Pair with WebControl.StartServer

The most common way developers interact with this module’s services is through the WebControl.StartServer console command. This initializes the listener on port 30010 by default. Use this to verify that your developer environment can successfully receive HTTP requests before writing custom C++ handlers.

4. Avoid Heavy Payloads

The server implemented within DevHttp is designed for lightweight command-and-control tasks, not for streaming large assets. If you need to send massive amounts of data (like high-res textures), consider using the CookOnTheFlyNetServer or a dedicated socket implementation instead to avoid blocking the engine’s main thread.

5. Implement Custom Request Handlers

You can extend the functionality of the developer server by registering custom IHttpRouter handlers. This allows you to define specific URL routes (e.g., http://localhost:30010/mytool/reset) that trigger specific C++ functions in your editor plugin, providing a bridge between external scripts (Python, JavaScript) and the engine.

6. Use Postman for Testing

When developing tools that rely on DevHttp, use an external API tester like Postman or Insomnia. This allows you to verify that your JSON payloads are correctly formatted and that the engine is returning the expected status codes (like 200 OK or 404 Not Found) without needing to write a frontend simultaneously.

7. Secure via Network Elimination

Since the DevHttp module does not typically include robust encryption (HTTPS) or complex authentication by default, it is a best practice to keep it bound to localhost (127.0.0.1). If you must open it to the local network, ensure your office firewall is configured to eliminate any incoming traffic from outside the trusted local subnet to prevent unauthorized remote execution of console commands.

8. Monitor for Port Conflicts

If you have multiple instances of the Unreal Editor open, or other web servers running on your machine, the DevHttp listener may fail to start due to a port conflict. Always check the Output Log for “Failed to bind to port” errors. You can often change the port in the DefaultEngine.ini or via command-line arguments to resolve these conflicts.