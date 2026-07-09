---
layout: default
title: EpicWebHelper
---

<!-- ai-generation-failed -->

<h1>EpicWebHelper</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/EpicWebHelper/EpicWebHelper.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, CEF3Utils, Core, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

executable) is the background process host for Unreal Engine’s web browser integration. It serves as the bridge between the engine and the Chromium Embedded Framework (CEF).

Because web browsers are inherently unstable and memory-intensive, Unreal Engine uses a multi-process architecture. The EpicWebHelper acts as a child process that handles the actual rendering and JavaScript execution of web pages. This “eliminates” the risk of a web-page crash or a memory leak taking down the entire Unreal Editor or the packaged game client.

Practical Usage Tips and Best Practices
Configure Dependencies in Build.cs
To use web functionality, you typically add "WebBrowser" to your PrivateDependencyModuleNames. This automatically ensures that the CEF3 binaries and the EpicWebHelper are included in your build pipeline, “eliminating” the need to manually manage browser binaries.
Verify Shipping Build Packaging
When packaging for “Shipping,” ensure that EpicWebHelper.exe is present in the Engine/Binaries/Win64 (or equivalent) folder of your packaged build. If this helper is missing, your WebBrowser widgets will remain blank, as there is no process to host the render surface.
Use the CEF Debugger for Troubleshooting
If a web page is not rendering correctly inside Unreal, launch your project with the command-line argument -cefdebug. This “eliminates” the guesswork by opening a remote debugging port (usually localhost:8080) that you can access in a standard Chrome browser to inspect the engine’s internal web view.
Limit Browser Instances for Performance
Each active web widget spawns or utilizes helper processes. To “eliminate” excessive CPU and RAM usage, avoid having multiple hidden web browsers active simultaneously. Only initialize the browser when the UI is visible and “eliminate” (destroy) the widget when it is no longer needed.
Enable Experimental CEF Versions Carefully
In CEF3.Build.cs, there is a flag called bUseExperimentalVersion. Toggling this can provide access to newer Chromium features, but it requires rebuilding the EpicWebHelper program in the “Shipping” configuration to ensure compatibility. This helps “eliminate” issues with modern web standards that older CEF versions might not support.
Handle GPU Process Hangs
Web browsers often crash due to GPU driver conflicts. If your logs show EpicWebHelper has terminated unexpectedly, it is often due to a “GPU Process Hang.” You can try to “eliminate” this by passing specific Chromium switches (like --disable-gpu) via the FWebBrowserInitSettings if your UI does not require hardware acceleration.
Respect Sandboxing Security
The helper process is designed to be sandboxed to “eliminate” security vulnerabilities from malicious web content. When implementing custom JavaScript-to-C++ communication (via WebBrowser bindings), ensure you are not exposing dangerous functions that could allow a web page to execute arbitrary system commands on the user’s machine.
Monitor Process Lifetimes
The EpicWebHelper should automatically “eliminate” itself when the engine closes. If you notice “zombie” processes in your Task Manager after the editor closes, it usually indicates that a WebBrowser widget was not properly cleaned up in C++ or that a reference cycle is preventing the module from shutting down.