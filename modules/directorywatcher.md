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

atform-independent API for monitoring filesystem changes in real-time. It allows the engine to detect when files or directories are created, modified, or deleted within specific watched paths.

This module is primarily used by the Content Browser to trigger asset reimports and by the Shader Compiler to detect changes in .usf or .ush files. Because it is a “Developer” module, its functionality is typically available in the Editor and Development builds but is eliminated from Shipping builds to minimize runtime overhead and security risks.

Practical Usage Tips and Best Practices
Access via FModuleManager To use the watcher, you must load the module and access the IDirectoryWatcher interface. Always verify the module is valid before use to eliminate null pointer crashes in specialized build environments.
C++
	FDirectoryWatcherModule& WatcherModule = FModuleManager::LoadModuleChecked<FDirectoryWatcherModule>("DirectoryWatcher");

	IDirectoryWatcher* Watcher = WatcherModule.Get();
Copy code
Handle Delegate Registration Carefully When registering a callback via RegisterDirectoryWatch, you receive an FDelegateHandle. You must store this handle and use it to unregister when your object is destroyed. Failing to do so will cause the engine to attempt to call a function on a deleted object, which you must eliminate to prevent memory corruption.
Understand the “Developer” Build Constraint Since this module is in the Developer folder, it is not included in Shipping builds. If your gameplay logic requires monitoring a save-game folder, do not use this module; instead, use IPlatformFile or platform-specific APIs to eliminate packaging errors.
Filter Bursts of Events Filesystem operations often trigger multiple events in rapid succession (e.g., a file being created, then written to, then closed). Implement a “debounce” or “cooldown” timer in your callback to eliminate redundant processing and prevent the engine from reimporting the same asset four times in one second.
Prefer Folder Watching over Deep Hierarchies Monitoring a root directory with thousands of subfolders can be resource-intensive depending on the OS. If possible, watch specific subdirectories to eliminate unnecessary CPU interrupts and file handle exhaustion on platforms with limited filesystem resources.
Use for Custom Tool Hot-Reloading If you are developing a custom plugin that loads external data (like a JSON config or a localization file), use DirectoryWatcher to trigger a reload automatically when the file is saved in an external editor. This eliminates the need for the user to manually restart the editor or click a “Refresh” button.
Check for Path Validity Before registering a watch, ensure the path exists using FPaths::DirectoryExists. Attempting to watch a non-existent directory can lead to silent failures; validating the path beforehand helps eliminate debugging frustration when your callbacks never trigger.
Thread Safety Considerations Callbacks from the DirectoryWatcher are typically executed on the thread that pumps the file system messages (often the Main/Game Thread in the Editor). Avoid performing heavy file I/O or complex asset processing directly inside the callback. Instead, queue the task to a background thread to eliminate UI freezes.