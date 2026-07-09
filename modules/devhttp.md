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

rovides the infrastructure for hosting a lightweight, internal web server within the Unreal Editor. It is the primary engine component responsible for the Remote Control API, allowing external web applications, tablets, or custom scripts to communicate with a running instance of Unreal Engine. By exposing engine functions and properties via standard HTTP/REST endpoints, it enables the creation of custom web-based control panels used extensively in virtual production, broadcast, and automated testing pipelines.

Practical Usage Tips & Best Practices
1. Activate via Console Commands

The server is not active by default to ensure editor performance and security.

Best Practice: Use the console command WebControl.StartServer to initialize the listener. You can also use WebControl.EnableServerOnStartup to ensure the server is ready every time you open the project, facilitating the elimination of manual setup steps for your remote team.
2. Restrict to Local Network Environments

The DevHttp module is designed for developer convenience and does not include robust encryption or public-facing security protocols.

Tip: Always operate the server behind a firewall on a trusted local area network (LAN). Proper network isolation ensures the elimination of unauthorized remote access to your project’s memory and assets.
3. Use in Non-Shipping Builds Only

This module is located in the Developer folder of the engine source, meaning it is intended for use in the Editor or special “Development” builds.

Best Practice: Do not attempt to package this module for final consumer release. It is designed for internal iteration; its removal from the final executable ensures the elimination of unnecessary overhead and potential security vulnerabilities in the shipping product.
4. Manage Port Conflicts

By default, the DevHttp server typically listens on port 30010.

Tip: If you have multiple instances of Unreal Engine running on the same machine, or if another application is using that port, you can change it in the Project Settings under Web Control. Assigning unique ports to different instances leads to the elimination of connection collisions.
5. Leverage JSON Utilities for Payloads

Communication with the DevHttp server relies heavily on JSON formatting for both requests and responses.

Best Practice: When writing external scripts (like Python or JavaScript) to interact with the server, use standard JSON libraries. Ensuring your payloads match the expected Unreal reflection structure is key to the elimination of “400 Bad Request” errors.
6. Identify Objects via Object Path

To modify a property or call a function via HTTP, you must provide the full path to the object (e.g., /Game/Maps/Main.Main:PersistentLevel.CineCameraActor_1).

Tip: You can right-click any actor in the World Outliner and select “Copy Reference” to get the path. Using precise paths ensures the elimination of ambiguity when targeting specific actors in a complex level.
7. Combine with Remote Control Presets

While you can call any reflected function, using the Remote Control Preset asset (which uses DevHttp under the hood) is more efficient.

Best Practice: Group the most-used properties into a Preset. This provides a simplified, flat list of endpoints, which results in the elimination of deep, complex nested JSON queries for your web developers.
8. Monitor via the Output Log

The DevHttp module logs connection attempts and request status directly to the Unreal Output Log.

Tip: If your remote dashboard isn’t responding, check the LogRemoteControl category in the editor. Monitoring these logs is the fastest way to achieve the elimination of connectivity bugs or malformed API calls.