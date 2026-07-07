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

ides a platform-independent interface for monitoring the operating system’s filesystem. Its primary role is to track changes—such as files being added, modified, or removed—within specific directories in real-time.

It is the core technology behind many of the Unreal Editor’s most reactive features, such as the Content Browser automatically updating when you move files in Windows Explorer, or the Hot Reload/Live Coding systems detecting source code changes to trigger a recompile.

Practical Usage Tips and Best Practices
1. Scope to Developer or Editor Targets

Because the DirectoryWatcher depends on OS-level hooks that are typically only relevant during development, it is located in the Developer folder.

Best Practice: Only include this module in your Build.cs when targeting the Editor or specialized developer tools. Ensure any code using it is wrapped in #if WITH_EDITOR to eliminate compilation errors when packaging your final “Shipping” build.
2. Access via the Module Singleton

You do not instantiate the watcher directly. Instead, you must request the interface from the module manager.

Tip: Access the system using FDirectoryWatcherModule& Manager = FModuleManager::LoadModuleChecked<FDirectoryWatcherModule>("DirectoryWatcher");. This ensures the underlying OS hooks are properly initialized, eliminating potential null pointer crashes.
3. Manage Delegate Handles Carefully

When you register a directory to be watched, the system returns an FDelegateHandle.

Action: You must store this handle and use it to unregister the directory when your object is destroyed or the module shuts down. Failing to unregister will eliminate the engine’s ability to clean up the memory, leading to “zombie” callbacks that crash the editor.
4. Filter Specific Change Types

The callback provides an EFileAction enum (Added, Modified, Removed, Renamed).

Best Practice: Check the action type immediately in your callback. Many OS operations (like saving a file) trigger multiple “Modified” events in rapid succession. Implementing a small “debounce” or filtering for only specific actions will eliminate redundant processing and performance hitches.
5. Handle Callbacks on the Game Thread

File system notifications often arrive from an asynchronous OS thread.

Tip: If your reaction to a file change involves modifying an Actor or a UI element, ensure you wrap that logic in AsyncTask(ENamedThreads::GameThread, ...). This helps eliminate race conditions and thread-safety violations within the engine.
6. Avoid Watching Root or Deeply Nested Paths

Watching a root directory (like C:/) or a folder with tens of thousands of files can significantly impact CPU usage as the OS struggles to report every minor change.

Action: Be as specific as possible with the paths you watch. Instead of watching the entire /Content/ folder, watch only the specific subfolder your system cares about. This helps eliminate unnecessary overhead and keeps the editor responsive.
7. Use for External Sidecar Data

This module is ideal for projects that use “sidecar” files (like external XML or JSON configs) that live outside the .uasset system.

Tip: Use the DirectoryWatcher to automatically re-parse these external files whenever they are saved in an external editor. This creates a seamless “Live Edit” workflow for designers, eliminating the need for manual “Import” button clicks.
8. Clean Up in ‘ShutdownModule’

If you are implementing this within a custom Editor Plugin:

Best Practice: Always call IDirectoryWatcher::UnregisterDirectoryChangedCallback inside your plugin’s ShutdownModule(). This ensures that if the plugin is disabled or reloaded, the OS hooks are cleanly released, eliminating potential file-lock issues that prevent the engine from closing properly.