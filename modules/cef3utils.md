---
layout: default
title: CEF3Utils
---

<!-- ai-generation-failed -->

<h1>CEF3Utils</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/CEF3Utils/CEF3Utils.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

m Embedded Framework (CEF) integration within Unreal Engine. It provides essential helper functions and lifecycle management tools for the WebBrowser plugin, which allows developers to embed web content directly into Slate and UMG widgets.

Its primary role is to bridge the gap between the Unreal Engine application and the external Chromium subprocesses. It handles command-line argument construction, subprocess path resolution, and the initialization/shutdown logic required to run a Chromium-based browser within the engine’s memory space.

1. Module Dependency and Setup

To use CEF features in C++, you must ensure that your Build.cs includes the WebBrowser and CEF3Utils modules. Note that CEF is primarily supported on Windows, macOS, and Linux; it is not available for mobile or console platforms.

C#
	if (Target.Platform == UnrealTargetPlatform.Win64 || Target.Platform == UnrealTargetPlatform.Mac)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "CEF3Utils", "WebBrowser" });

	}
Copy code
2. Manage the Subprocess Path

CEF runs as a separate process to ensure that a web crash does not eliminate the main game process.

Best Practice: Always ensure the UnrealCEFSubProcess.exe (on Windows) is correctly packaged. CEF3Utils uses the FCEF3Utils::GetCEFSubProcessPath() function to find this executable. If you are using a custom build or launcher, verify this path to avoid “Browser failed to initialize” errors.
3. Customize Command Line Arguments

You can pass custom flags to the underlying Chromium engine via the CEF3Utils logic.

Tip: If you need to enable hardware acceleration or ignore certificate errors for local testing, you can modify the command line before the browser is initialized. Use the --disable-gpu flag if you encounter rendering flickering in specific hardware environments.
4. Handle Lifecycle and Shutdown

Chromium requires a clean shutdown to release file locks on its cache and cookies.

Best Practice: The engine handles most of this via FCEF3Utils::UnloadCEF(). If you are manually loading/unloading the module in a tool or plugin, ensure you call the unload function during the module’s ShutdownModule phase to prevent memory leaks or zombie processes.
5. Managing Cache and Cookies

CEF3Utils helps determine where Chromium stores its persistent data.

Tip: You can specify a custom CachePath in your browser settings. If you want a “private” session that clears all data when the game closes, ensure the cache path is either empty or points to a temporary directory that you eliminate upon application exit.
6. Synchronize with Slate Ticking

Because CEF renders on its own schedule, CEF3Utils assists in synchronizing the web frame buffers with Slate’s rendering.

Best Practice: Avoid trying to force-tick the browser from the Game Thread. Let the CEF3Utils and WebBrowser module handle the internal message loop to prevent deadlocks between the Slate UI thread and the Chromium render thread.
7. Monitor Subprocess Health

The module provides hooks to detect if the subprocess has crashed.

Tip: If your web widget suddenly turns white or disappears, use the OnConsoleMessage or OnLoadError delegates (exposed via the WebBrowser module but powered by CEF utilities) to log the specific Chromium error code. This is essential for debugging localized network or rendering issues.
8. Use Experimental Versions with Caution

As of Unreal Engine 5.6⁄5.7, the engine supports newer versions of CEF.

Warning: To use an experimental version of CEF, you must rebuild the EpicWebHelper program. Always test your web-based UI thoroughly after a version bump, as Chromium updates can change how CSS or JavaScript is interpreted, potentially breaking existing UMG layouts.