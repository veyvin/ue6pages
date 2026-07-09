---
layout: default
title: Launch
---

<!-- ai-generation-failed -->

<h1>Launch</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Launch/Launch.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AgilitySDK, ApplicationCore, AudioMixerAndroid, AutomationWorker, BuildSettings, ClothingSystemRuntimeInterface, ClothingSystemRuntimeNv, CookOnTheFly, Core, CoreUObject, DerivedDataCache, DesktopPlatform, DeveloperToolSettings, EditorFramework, Engine, FunctionalTesting, HeadMountedDisplay, InputCore, InstallBundleManager, Json, LauncherCheck, MRMesh, MainFrame, MediaUtils, MoviePlayer, MoviePlayerProxy, NetworkFile, Networking, OpenGLDrv, Overlay, PakFile, PreLoadScreen, Projects, RHI, RenderCore, SandboxFile, Serialization, SessionServices, Settings, Slate, SlateCore, Sockets, SourceControl, StorageServerClient, StorageServerClientDebug, StreamingFile, TraceLog, UnixCommonStartup, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rapping” code that bridges the operating system’s main function (like WinMain on Windows or main on Linux/Android) to the engine’s internal loop.

Its primary purpose is to initialize the hardware environment, set up the memory allocators, and trigger the GuardedMain function. By abstracting the startup sequence into this module, Unreal “eliminates” the complexity of managing platform-specific initialization for every project, providing a unified path to launch the engine across PC, consoles, and mobile devices.

Practical Usage Tips and Best Practices
Understand the GuardedMain Entry Point
Most of the logic in the Launch module resides in Launch.cpp and LaunchEngineLoop.cpp. If you are debugging a crash that happens before any window appears, look into GuardedMain. This is where the engine “eliminates” unhandled exceptions during the very early boot phase.
Leverage Command-Line Arguments
The Launch module is responsible for parsing all startup parameters. Use FCommandLine::Get() to access raw arguments passed to the executable. This allows you to “eliminate” hardcoded debug flags by using custom arguments like -MyDebugMode directly in your C++ logic.
Initialize Global Subsystems via Delegates
Because this module runs before the UEngine object exists, you cannot use standard Actors or Components here. Instead, use the FCoreDelegates provided by the engine. Subscribing to FCoreDelegates::OnPreMainLoop allows you to “eliminate” initialization race conditions for low-level third-party libraries.
Manage Early Logging
If you need to log messages during the boot process, ensure you use UE_LOG as early as possible. The Launch module initializes the FOutputDevice very early. If the engine fails before this module completes, it “eliminates” your ability to see standard log files, often requiring you to check the stdout or the debugger’s output window.
Optimize Startup with Preloading
The Launch module handles the “PreLoadingScreen” phase. If your game has a long initial load, use this module’s hooks to “eliminate” a black screen by triggering a splash screen or a video player before the heavy UObject and Shader systems are fully initialized.
Monitor Engine Loop Heartbeat
The FEngineLoop class within this module contains the Tick() function that drives the entire engine. While you should never modify this directly, understanding its structure helps “eliminate” confusion regarding the order of operations between the Frame Sync, the Render Thread, and the Game Thread.
Custom Launch Parameters for Tools
When writing a Commandlet or a standalone tool, the Launch module determines which “Mode” the engine runs in. By passing specific flags to the executable, you can “eliminate” the loading of the Slate UI or the Renderer, creating a lightweight “headless” version of your game for automation or data processing.
Identify Platform-Specific Entry Points
If you are developing for mobile or consoles, the Launch module contains the specific platform wrappers (like LaunchAndroid.cpp or LaunchiOS.cpp). Studying these files can help “eliminate” issues related to app lifecycle events, such as what happens when a user minimizes the app or a system-level interrupt occurs.