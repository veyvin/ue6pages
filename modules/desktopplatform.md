---
layout: default
title: DesktopPlatform
---

<!-- ai-generation-failed -->

<h1>DesktopPlatform</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/DesktopPlatform/DesktopPlatform.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

interface for interacting with the host operating system’s desktop environment. It serves as an abstraction layer for tasks that fall outside the standard gameplay loop but are essential for editor functionality and pipeline automation, such as opening file explorer dialogs, managing project files, and discovering engine installations.

Its primary role is to provide the IDesktopPlatform interface, which allows C++ code to invoke OS-native features (like Windows Explorer or macOS Finder dialogs) without writing platform-specific code in the main application logic. This helps eliminate the need for multiple #ifdef blocks when handling basic desktop interactions.

Practical Usage Tips and Best Practices
Access via the Module Manager
To use this module, you must load it through the FDesktopPlatformModule. Always check if the pointer is valid before calling functions to eliminate crashes in environments where the desktop platform might not be available (such as server builds).
C++
	IDesktopPlatform* DesktopPlatform = FDesktopPlatformModule::Get();

	if (DesktopPlatform) { /* ... */ }
Copy code
Wrap in Editor-Only Guards
The DesktopPlatform module is intended for developer tools and the Unreal Editor. Ensure that any code referencing it is wrapped in #if WITH_EDITOR or is contained within an Editor-specific module. This ensures the dependency is eliminated from shipping builds, which do not support these desktop interactions.
Standardize File Selection Dialogs
Use OpenFileDialog or SaveFileDialog for custom editor tools. These functions provide a native OS experience for the user. By utilizing the EFileDialogFlags, you can eliminate user error by enforcing single-file selection or specific file extensions (e.g., .json, .csv).
Discover Engine Root Directories
If you are writing a tool that needs to find where the engine is installed on a user’s machine, use GetEngineRootDir. This helps eliminate hard-coded paths in your scripts, making your developer tools portable across different team members’ workstations.
Open Native OS Folders
Use the ExploreFolder function to open a specific directory in the OS file manager. This is a common “quality of life” feature for editor utility widgets, allowing users to eliminate the manual search for export folders or log directories on their hard drive.
Monitor External Processes
The module provides functions like GetNativeProcessHandle. When launching external command-line tools (such as texture compressors or build scripts), use these handles to track if the process is still running. This allows your tool to eliminate “zombie” processes that could otherwise hang in the background.
Distinguish from Generic HAL
Do not confuse IDesktopPlatform with FPlatformProcess (from the HAL). Use DesktopPlatform for UI-facing desktop tasks (like dialogs) and FPlatformProcess for low-level system tasks (like thread management). Keeping these concerns separate will eliminate architectural confusion in your codebase.
Handle Multi-User Path Logic
When saving paths returned by the desktop dialogs, always convert them to relative paths using FPaths::MakeStandardFilename. This ensures that paths shared between team members (e.g., in a data table) work correctly on everyone’s machine, helping to eliminate “Path Not Found” errors in collaborative environments.