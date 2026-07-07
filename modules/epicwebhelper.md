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

rting module that acts as the sub-process for the Chromium Embedded Framework (CEF) within Unreal Engine. Because modern web browsers are highly complex and prone to significant memory usage or instability, Unreal Engine uses a multi-process architecture to run web content.

When you use the WebBrowser widget in UMG or the Editor, the engine doesn’t run the browser logic inside the main game thread; instead, it spawns EpicWebHelper as a separate OS process to handle rendering, JavaScript execution, and network requests for web pages.

Practical Usage Tips and Best Practices
1. Ensure EpicWebHelper is Packaged

If your game uses the Web Browser widget, the EpicWebHelper.exe (or the equivalent for Mac/Linux) must be included in your packaged build.

Best Practice: Verify your staging settings to ensure the helper executable is in the Engine/Binaries/Win64 (or similar) folder of your distribution. If this file is missing, the web browser will remain a black screen, effectively eliminating the web functionality for your end users.
2. Scope Resources to Prevent Memory Bloat

Every instance of a web browser can spawn multiple helper processes (for GPU acceleration, plugins, and tab handling).

Tip: Close browser widgets when they are not in use rather than just hiding them. This allows the engine to terminate the associated EpicWebHelper processes and eliminate unnecessary RAM consumption on the user’s machine.
3. Use ‘Shipping’ Configuration for Best Performance

The EpicWebHelper is built in different configurations (Debug, Development, Shipping).

Action: When deploying your game, ensure you are using the Shipping version of the helper. This version has all debugging hooks removed and is highly optimized, which helps eliminate performance hitches and reduces the CPU footprint of web-based UI elements.
4. Monitor Process Crashes

Since EpicWebHelper runs as a separate process, it can crash independently of the main game.

Tip: In C++, you can bind to the OnConsoleMessage or use the browser’s error-handling delegates to detect when a page fails to load or the renderer process hangs. This allows you to restart the browser or display an error message, helping you eliminate “silent failures” where the UI just stops responding.
5. Handle GPU Acceleration Conflicts

EpicWebHelper uses the GPU to render web content, which can sometimes conflict with the main game’s RHI (Render Hardware Interface).

Action: If you notice flickering or black boxes in your web widgets, try using the -DisableLibUV or -DisableGPU command-line arguments (via the browser settings). This forces the helper into software rendering mode, which can eliminate graphical artifacts on older or incompatible hardware drivers.
6. Sanitize JavaScript Communication

The WebBrowser module allows you to communicate between C++ and JavaScript within the EpicWebHelper process.

Best Practice: Always sanitize data passed via ExecuteJavascript or WebBrowserObject. Since the helper process is essentially a gateway to the internet, proper data validation helps eliminate potential security vulnerabilities like Cross-Site Scripting (XSS) within your game UI.
7. Build the Helper for Custom Engine Versions

If you are using a source build of Unreal Engine and have modified the CEF binaries or settings:

Action: You must manually rebuild the EpicWebHelper project in your Visual Studio solution. If the version of the helper does not match the engine’s WebBrowser module version, the process will fail to initialize, eliminating your ability to display web content.
8. Respect Firewall and Sandbox Restrictions

On some platforms, the OS might see EpicWebHelper as a separate application trying to access the internet.

Tip: When testing your game, ensure your firewall allows the helper process to communicate. For console or restricted desktop environments, you may need to configure the browser’s “Sandboxing” settings to eliminate connection blocks that prevent web pages from loading correctly.