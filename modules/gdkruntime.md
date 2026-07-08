---
layout: default
title: GDKRuntime
---

<!-- ai-generation-failed -->

<h1>GDKRuntime</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Microsoft/GDKRuntime/GDKRuntime.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, GRDK</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Game Development Kit (GDK) within Unreal Engine. It provides the necessary runtime environment to bridge Unreal’s engine systems with the specific APIs required to ship games on Xbox consoles and the Windows Store (PC).

What it is and What it’s used for

Located in Engine/Source/Runtime/GDKRuntime, this module acts as a hardware abstraction layer. It wraps the Microsoft GDK SDK, allowing the engine to communicate with the Xbox OS and the Windows Gaming environment.

Primary uses include:

Platform Initialization: Bootstrapping the GDK environment and handling the “Lazy Initialization” of Microsoft gaming services.
System Integration: Managing platform-specific features like User Identity, Xbox Live connectivity, and Title-specific metadata.
Online Subsystem Support: Providing the underlying architecture for OnlineSubsystemGDK, which handles matchmaking, achievements, and cloud saves.
Device Awareness: Identifying the specific hardware target (e.g., Xbox Series X vs. Series S vs. PC) to apply correct performance profiles and rendering constraints.
Practical Usage Tips and Best Practices
1. Distinguish Between Win64 and WinGDK

When targeting Windows, you can build for standard Win64 (Steam/Epic Games Store) or WinGDK (Microsoft Store/Xbox App). Use the GDKRuntime to detect if the game is running as a packaged Microsoft Store app. This is critical for the elimination of errors when calling Xbox-specific APIs on non-GDK Windows builds.

2. Configure Lazy Initialization

In your DefaultEngine.ini, you can manage how the GDK runtime starts up. By default, bLazyInitialize is set to true. This delays the initialization of gaming services until they are actually needed, which can significantly improve your initial boot-up time and splash screen performance.

3. Use the GDKSaveGameSystem

For Xbox and Microsoft Store builds, you should use the module’s dedicated save system. In your WindowsEngine.ini (under the GDK sub-folder), set SaveGameSystemModule=GDKSaveGameSystem. This ensures that your local save data is correctly synchronized with the Xbox Live Cloud Storage service.

4. Leverage Remote Deployment via Xbox PC Remote Tools

The GDKRuntime supports remote deployment, allowing you to push builds from your dev PC to a remote Windows machine or Xbox. Ensure you have the Xbox PC Toolbox App installed and your devices registered in your UserEngine.ini to allow for rapid iteration and the elimination of manual transfer steps.

5. Handle Game Input Correctly

For games using the Game Input for Windows plugin (which relies on GDKRuntime), ensure you set IncludeRedistFiles=True in your config. This allows the engine to bundle the GameInputRedist.msi, which is a best practice to ensure the physical input devices (like specialized controllers) function correctly on the end-user’s machine.

6. Manage Additional Modules via MSGameOSSSelector

If your project uses custom GDK-specific modules, you can use the MSGameOSSSelector to load them conditionally. Add +AdditionalModulesToLoad=MyCustomModule in your MSGameOSS configuration. This ensures that platform-specific C++ logic only loads when the GDK environment is fully active.

7. Monitor GDK-Specific Logs

During development, keep a close watch on LogGamingRuntime. This log category provides detailed feedback on whether the GDK SDK was initialized successfully. If you encounter “D3D Device Removed” errors or authentication failures, these logs are the primary place to look for the GDK-specific error codes.

8. Strategic Elimination of Future Content Questions

When working with GDKRuntime, only implement features supported in the current Unreal Engine version (e.g., UE 5.6 or 5.7). Avoid attempting to implement future Xbox API features that are not yet exposed by the engine’s GDK wrapper, as this can lead to build instability and certification failures.