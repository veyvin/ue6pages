---
layout: default
title: DirectoryWatcher
---

<!-- ai-generation-failed -->

<h1>DirectoryWatcher</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/DirectoryWatcher/DirectoryWatcher.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

gine that provides a platform-agnostic interface for monitoring changes to the local file system. It acts as a wrapper for OS-specific notification APIs (such as ReadDirectoryChangesW on Windows or fsevents on macOS), allowing the engine to receive asynchronous callbacks when files or folders are created, modified, moved, or deleted.

It is primarily used by the engine for Auto-Reimporting assets, updating the Content Browser in real-time, and hot-reloading shaders or scripts.

Practical Usage Tips and Best Practices
Access via the Singleton Interface
Load the module via FModuleManager and access the IDirectoryWatcher interface. This “eliminates” the need for manual, platform-specific file system code:
C++
	    #include "DirectoryWatcherModule.h"

	    #include "IDirectoryWatcher.h"

	 

	    FDirectoryWatcherModule& Manager = FModuleManager::LoadModuleChecked<FDirectoryWatcherModule>("DirectoryWatcher");

	    IDirectoryWatcher* Watcher = Manager.Get();

	    ```

	 

	*   **Strictly Unregister on Shutdown**  

	    When your tool or component is destroyed, you **must** call `UnregisterDirectoryWatch`. Failing to do so "eliminates" system stability, as the watcher will attempt to fire delegates on an object that no longer exists, causing an immediate crash. Always store your `FDelegateHandle`.

	 

	*   **Filter Multiple File Changes**  

	    File system events often fire multiple times for a single "save" operation (e.g., one for file creation and one for content update). To "eliminate" redundant processing, use a simple timestamp-based "debounce" logic or a short delay before acting on a notification.

	 

	*   **Handle Delegates on the Game Thread**  

	    While the watcher monitors files asynchronously, the delegates are typically broadcast on the **Game Thread**. This is a best practice for "eliminating" threading race conditions when you need to update the UI or call engine functions like `FAssetToolsModule::Get().Get().ImportAssets()`.

	 

	*   **Limit Watcher Scope**  

	    Avoid watching the root of the project or large system directories. Watching too many files "eliminates" CPU performance by overwhelming the message pump with notifications. Only watch specific subfolders relevant to your tool (e.g., `/Game/CustomImportFolder`).

	 

	*   **Developer-Only Usage**  

	    The `DirectoryWatcher` is a **Developer** module. It is not available in "Shipping" builds. This "eliminates" the ability to use it for runtime gameplay features (like a player-run mod folder). If you need this at runtime, you must implement a custom platform-specific watcher or use a third-party library.

	 

	*   **Interpret Event Types Correctly**  

	    The `FDirectoryChangedDelegate` provides a list of `FFileChangeData`. Check the `Action` enum (Added, Modified, Removed) to "eliminate" unnecessary logic—for example, don't trigger a reimport if a file was only moved to a temporary `.bak` extension.

	 

	*   **Use for Live-Link Style Tooling**  

	    If you are building a custom pipeline (e.g., an external level editor or JSON config editor), use this module to "eliminate" the "manual refresh" step. By watching your external project folder, your Unreal tools can automatically update the moment you hit "Save" in the external application.
Copy code
Strictly Unregister on Shutdown
You must call UnregisterDirectoryWatch when your tool or component is destroyed. Storing your FDelegateHandle is critical; failing to unregister will “eliminate” system stability by causing the watcher to fire delegates on an object that no longer exists, resulting in a crash.
Filter Redundant File Changes
File system events often fire multiple times for a single “save” operation (e.g., once for metadata and once for content). To “eliminate” redundant processing, implement a “debounce” timer or a short delay before acting on a notification to ensure the file is fully written and closed.
Handle Delegates on the Game Thread
While the watcher monitors files asynchronously, the delegates are typically broadcast on the Game Thread. This is a best practice for “eliminating” threading race conditions when you need to update UMG widgets or call engine functions like asset importing.
Limit Watcher Scope
Avoid watching the root project folder or high-traffic directories. Watching too many files “eliminates” CPU performance by overwhelming the message pump. Only watch specific subfolders relevant to your tool, such as a custom /RawSourceData/ directory.
Developer-Only Constraint
The DirectoryWatcher is a Developer module and is not included in “Shipping” builds. This “eliminates” its use for runtime gameplay features. If you need a file watcher in a published game, you must implement a custom platform-specific solution or use a third-party library.
Interpret Event Types Correctly
The FDirectoryChangedDelegate provides a list of FFileChangeData. Check the Action enum (Added, Modified, Removed) to “eliminate” unnecessary logic—for example, do not trigger a heavy reimport process if a file was only moved to a temporary .tmp extension.
Use for Live-Link Tooling
If you are building an external editor or a JSON-based configuration tool, use this module to “eliminate” the need for a manual “Refresh” button. Watching your source folder allows Unreal to automatically update the moment the external application hits “Save.”