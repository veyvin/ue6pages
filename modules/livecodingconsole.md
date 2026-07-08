---
layout: default
title: LiveCodingConsole
---

<!-- ai-generation-failed -->

<h1>LiveCodingConsole</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/LiveCodingConsole/LiveCodingConsole.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, Json, LiveCodingServer, MessageLog, Projects, Slate, SlateCore, SourceCodeAccess, StandaloneRenderer, VisualStudioDTE, VisualStudioSourceCodeAccess, XCodeSourceCodeAccess</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

er for the Live Coding system (powered by Live++). While the core LiveCoding module handles the low-level binary patching and compilation, the LiveCodingConsole is responsible for spawning and managing the standalone external window that displays build progress, compilation errors, and status logs.

This module is essential for the C++ iteration workflow, providing immediate feedback when you trigger a recompile. It allows you to see exactly why a build failed without having to switch back to your IDE (Visual Studio, Rider, or VS Code), helping you eliminate dead time during the “Code-Compile-Test” loop.

Practical Usage Tips and Best Practices
Trigger with the Global Hotkey
The most efficient way to interact with this module is via the Ctrl + Alt + F11 shortcut while the Editor is in focus. This avoids the need to manually click the “Compile” button and immediately brings the Live Coding Console to the foreground if it was hidden, helping you eliminate unnecessary mouse clicks.
Keep the Console Visible for Error Catching
In Editor Preferences > General > Live Coding, ensure “Show Console on Startup” or “Auto-Show Console” is enabled. This ensures that if a background compilation fails due to a syntax error, the window pops up immediately to notify you, which helps you eliminate the frustration of testing code that hasn’t actually updated.
Avoid Header Changes
The Live Coding Console will often report success even if you change a .h file, but structural changes (like adding new UFUNCTION or UPROPERTY macros) cannot be hot-patched into the running engine. Only use it for logic changes inside .cpp files to eliminate potential memory corruption or crashes that occur when the class layout changes at runtime.
Restart for Constructors
Changes made to default values inside a C++ constructor will often not reflect on existing actors already placed in the level. If your logic changes aren’t appearing, use the console to verify the build finished, then recreate the actor in the scene to eliminate stale data issues.
Disable “Edit and Continue” in IDEs
To prevent conflicts between your IDE and the LiveCodingConsole, disable “Edit and Continue” in Visual Studio settings. This ensures the two systems don’t fight over the same debug symbols, which helps you eliminate “File in use” or “Access Denied” errors during compilation.
Use for Rapid Gameplay Tuning
The console is perfect for tweaking values like movement speed, damage numbers, or “elimination” logic timers while the game is running in Play In Editor (PIE). You can change a variable in your .cpp, hit the hotkey, and see the result instantly without stopping the session, helping you eliminate the need to restart the game for minor balance tweaks.
Monitor for ‘Module Not Enabled’ Warnings
If the console log shows that a specific module is “not enabled for live coding,” check your .uproject file. You may need to explicitly add the module to the project’s dependency list to eliminate it being skipped during the live patching process.
Clear the Log Regularly
If you are performing hundreds of iterations in a single session, the console log can become cluttered. Right-clicking inside the Live Coding Console and clearing the output helps you eliminate old error messages that might confuse you when troubleshooting a fresh compilation failure.