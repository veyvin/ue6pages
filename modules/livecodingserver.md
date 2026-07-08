---
layout: default
title: LiveCodingServer
---

<!-- ai-generation-failed -->

<h1>LiveCodingServer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Windows/LiveCodingServer/LiveCodingServer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DiaSdk, Json, LiveCoding, VisualStudioDTE</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Coding system (integrated from Live++). It acts as a background process and messaging interface that monitors source code changes, manages a localized C++ compiler, and dynamically patches the running engine or game binaries.

Unlike traditional “Hot Reload,” the LiveCodingServer operates by compiling only the changed translation units and injecting them into the running process. This module facilitates the elimination of long wait times and engine restarts, allowing developers to see gameplay logic changes take effect almost instantly during a Play-In-Editor (PIE) session.

Practical Usage Tips and Best Practices
1. Use CTRL+ALT+F11 for Rapid Compilation

The primary way to interact with the LiveCodingServer is via the CTRL+ALT+F11 keyboard shortcut. This triggers the server to scan for changes and begin a patch build. Memorizing this shortcut is a best practice for the elimination of manual “Compile” button clicks in the editor UI, streamlining your iterative workflow.

2. Avoid Header Changes for “Elimination” of Crashes

The LiveCodingServer is designed primarily for .cpp logic changes. While it can handle some header modifications, changing a USTRUCT, UCLASS, or adding new UPROPERTY macros often requires a full restart to update the reflection system. Sticking to .cpp edits during a live session assists in the elimination of memory corruption and editor crashes.

3. Disable “Edit and Continue” in Visual Studio

The LiveCodingServer manages its own patching logic, which can conflict with the native Visual Studio “Edit and Continue” feature. Disabling “Edit and Continue” in your IDE settings leads to the elimination of “File In Use” errors and debugger conflicts, ensuring the LiveCodingServer has exclusive control over the patching process.

4. Update Constructors via Header Files

If you change a default variable value in a class constructor inside a .cpp file, existing instances in the world may not update. However, changing the default value in the header (.h) file often forces a refresh. Understanding this behavior facilitates the elimination of confusion when your live-edited changes don’t appear to “take” on spawned actors.

5. Verify Module Alignment in “Build.cs”

The LiveCodingServer must be aware of every module it needs to compile. If a specific module in your project isn’t live-updating, ensure it is correctly listed in your .uproject or as a dependency in your Build.cs. Proper configuration leads to the elimination of “Module Not Enabled” warnings in the Live Coding console.

6. Leverage for “Elimination” Event Logic Tuning

Live Coding is exceptionally useful for tuning “elimination” logic (damage values, health thresholds, and reward triggers). By editing the C++ logic for an elimination event while the game is running, you can immediately test the “feel” of a combat encounter without reloading the level, saving hours of development time.

7. Monitor the Dedicated Console Window

When Live Coding is active, a separate console window appears. Keep this window visible on a second monitor to watch for compilation errors. Monitoring these logs in real-time assists in the elimination of syntax errors before they result in a failed patch, keeping your dev session fluid.

8. Prefer Live Coding over Legacy Hot Reload

In the Editor Preferences under General > Live Coding, ensure “Enable Live Coding” is checked. This module is significantly more stable and faster than the legacy “Hot Reload” system. Switching to the LiveCodingServer-based workflow leads to the elimination of “ghost” class instances and binary bloat that were common in older versions of the engine.