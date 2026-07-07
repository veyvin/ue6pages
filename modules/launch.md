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

Init” (starting the game or editor), and “Tick” (the main loop) phases, while also handling platform-specific requirements like command-line parsing and crash reporting.

Practical Usage Tips and Best Practices
1. Understand the GuardedMain Loop

The core of the Launch module is a function called GuardedMain. This function wraps the entire engine execution in a massive try-catch or platform-specific exception handler.

Action: If you are debugging a crash that occurs before any of your actors are spawned, look at the call stack in the Launch module. This helps you eliminate confusion by identifying whether the failure occurred during early Engine PreInit or during actual gameplay initialization.
2. Master Command-Line Arguments

The Launch module is responsible for parsing the FCommandLine.

Tip: You can pass custom arguments to your game executable (e.g., MyGame.exe -MyCustomFlag). Use FParse::Param in your code to detect these. This allows you to toggle debug features or bypass intro videos, effectively eliminating manual code changes for different testing scenarios.
3. Respect the Loading Phases

The Launch module loads engine modules in a specific order: Earliest, PreDefault, Default, and PostDefault.

Best Practice: If your custom module needs to intercept engine startup (like a custom renderer or a low-level memory profiler), set your LoadingPhase to PreDefault in the .uplugin or .uproject file. This ensures your logic is active before the Launch module starts the main game loop, eliminating initialization order conflicts.
4. Handle Platform Entry Points Carefully

In C++, the Launch module defines the platform-specific entry macros (e.g., IMPLEMENT_PRIMARY_GAME_MODULE).

Action: Never attempt to write your own WinMain or main function in an Unreal project. Doing so will conflict with the Launch module’s existing architecture. Relying on the engine’s macros helps you eliminate build errors across multiple platforms.
5. Monitor PreInit for Startup Speed

Most “startup hitches” occur during the GEngineLoop.PreInit() phase within the Launch module.

Tip: Use the -llm (Low Level Memory) and -trace=loadtime command-line flags. This helps you see which modules the Launch module is struggling to load, allowing you to eliminate unnecessary plugin dependencies that are slowing down your game’s boot time.
6. Utilize the Unreal Engine Commandlet Mode

The Launch module can boot the engine in “Commandlet” mode (using -run=CommandletName). This allows you to run headless tasks like baking lightmaps or exporting data without spawning a window.

Action: Use commandlets for automated build pipelines. This helps you eliminate the overhead of the GPU and UI, making your data-processing tasks much faster.
7. Debugging via Launch Settings

When debugging in Visual Studio, you can set “Command Arguments” in the project properties.

Tip: Common flags like -windowed -resx=1280 -resy=720 are handled immediately by the Launch module. Using these helps you eliminate the need to navigate in-game menus to change resolutions or display modes during rapid iteration.
8. Avoid Blocking the Main Thread During Init

Since the Launch module runs the main loop on a single thread during startup, performing long synchronous file IO in a module’s StartupModule() function will “freeze” the splash screen.

Best Practice: Use asynchronous loading or the Task Graph system for heavy initialization tasks. This keeps the Launch sequence fluid and helps you eliminate the appearance of the game being “unresponsive” during boot-up.