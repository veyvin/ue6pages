---
layout: default
title: HotReload
---

<!-- ai-generation-failed -->

<h1>HotReload</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/HotReload/HotReload.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, DesktopPlatform, DirectoryWatcher, Engine, Projects, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ine that allows developers to recompile and patch C++ code while the Unreal Editor is still running. It serves as a bridge between the IDE (Visual Studio, JetBrains Rider) and the Editor’s memory space.

What it is and What it’s used for

Located in Engine/Source/Developer/HotReload, this module manages the loading and unloading of Dynamic Link Libraries (DLLs) at runtime. When a developer compiles code without closing the Editor, the HotReload module detects the change, compiles a new version of the DLL (identifiable by a suffix like -0001), and redirects the engine’s function pointers and class metadata to the new version.

Primary uses include:

Rapid Iteration: Changing the internal logic of a .cpp file and seeing the results immediately without restarting the Editor.
Variable Adjustments: Modifying default values or constants within C++ classes during a Play-In-Editor (PIE) session.
Workflow Continuity: Maintaining the current Editor state (open levels, selected actors, undo history) while updating the underlying binary code.
Practical Usage Tips and Best Practices
1. Prioritize Live Coding Over Hot Reload

In modern Unreal Engine versions (5.0+), Live Coding (triggered via Ctrl+Alt+F11) is the preferred successor to Hot Reload. Live Coding is faster and more reliable because it patches memory directly. Use the HotReload module primarily for legacy systems or when Live Coding is explicitly disabled.

2. Avoid Header Changes During Hot Reload

Hot Reload is best suited for .cpp changes. Modifying .h files—specifically adding or removing UPROPERTY or UFUNCTION macros—often leads to memory corruption or “Ghost” variables. For structural changes, the best practice is the elimination of risks by closing the Editor and performing a clean build.

3. Address Blueprint Corruption Risks

Hot-reloading a native UActorComponent or USceneComponent that is currently being used in an open Blueprint can occasionally corrupt that Blueprint’s archetype. If you notice variables “resetting” to defaults or the “Reset to Default” yellow arrow disappearing, you must restart the Editor to prevent permanent data loss.

4. Manage DLL Buildup and Bloat

Each Hot Reload session creates a new DLL file in your Binaries/Win64 folder. Over a long development session, this can lead to dozens of redundant files. Periodically close the Editor and manually delete these suffixed DLLs (or run a “Clean” in your IDE) to ensure the elimination of binary bloat.

5. Use the “Reload Complete” Delegate

If you are writing custom Editor tools or UI (Slate), your widgets may not automatically refresh after a Hot Reload. You can bind your code to the FCoreUObjectDelegates::ReloadCompleteDelegate to trigger a manual UI refresh or a data re-cache whenever a module is successfully reloaded.

6. Perform Regular “Hard” Restarts

Hot Reload is a temporary bridge, not a permanent state. After several hours of hot-reloading, the engine’s internal class hierarchy can become fragmented. It is a best practice to restart the Editor at least once a day to ensure the elimination of subtle memory leaks or pointer instability.

7. Verify Hot Reload via the Log

Always keep the Output Log visible when compiling. The HotReload module will output status messages (e.g., Module 'MyGame' reloaded successfully). If you see a “Linker Error” or “Failed to load module,” do not continue working, as the Editor is likely in an unstable state.

8. Strategic Elimination of Hot Reload Crashes

If the Editor crashes during a Hot Reload, it is often due to a “Circular Reference” where the new DLL is trying to access a class that was destroyed in the old DLL. To prevent this, ensure that your BeginPlay and EndPlay logic is robust and that you are not storing raw pointers to objects that might be reinstanced during the reload process.