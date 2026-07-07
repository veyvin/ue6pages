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

terface (IDesktopPlatform) for interacting with the host operating system’s desktop environment. It serves as an abstraction layer for OS-level tasks that fall outside the scope of the core engine’s runtime, such as opening native file/folder picker dialogs, detecting engine installations, and managing project files (e.g., generating project files or building the editor).

Since it invokes native OS UI elements like the Windows Explorer or macOS Finder, it is primarily used in the Unreal Editor, standalone developer tools, and custom build scripts.

Practical Usage Tips and Best Practices
1. Native File and Folder Dialogs

The most common use for this module is providing a familiar OS experience for selecting files.

Best Practice: Always use IDesktopPlatform::OpenFileDialog or OpenDirectoryDialog instead of trying to build a custom Slate-based file browser. This ensures your tool feels native to the user and handles OS-specific features like “Quick Access” or network drives, which helps eliminate user confusion.
2. Scope to Editor or Developer Targets

Because this module is located in the Developer folder, it is not available in “Shipping” builds or on non-desktop platforms (Mobile/Console).

Action: Always wrap your DesktopPlatform code in #if WITH_EDITOR or include it only in Editor-specific modules. Failure to do so will eliminate your ability to package the game for non-desktop platforms, as the linker will be unable to find the module.
3. Accessing the Singleton Interface

Unlike most runtime modules, you access this module via a specialized singleton pattern.

Tip: Use FDesktopPlatformModule::Get() to retrieve the IDesktopPlatform* pointer. This is a reliable, thread-safe way to access platform utilities without having to manually call LoadModuleChecked every time, which helps eliminate redundant boilerplate code.
4. Pass the Parent Window Handle

When invoking a dialog, the first parameter is the ParentWindowHandle.

Best Practice: Use FSlateApplication::Get().GetActiveTopLevelWindow() to retrieve the native handle. Passing this handle ensures the file picker stays “modal” (on top) of the Unreal Editor. This prevents the editor from appearing frozen if the dialog window gets lost behind the main window, effectively eliminating potential user frustration.
5. Programmatic Engine Detection

If you are writing a tool that needs to know where Unreal Engine is installed on a user’s machine (e.g., a custom launcher or a multi-project build script):

Action: Use IDesktopPlatform::GetEngineInstallations. It queries the OS registry or configuration files to return a map of all installed engine versions and their local paths. This helps you eliminate the need for users to manually input installation paths.
6. Automate Project File Generation

This module provides the GenerateProjectFiles method, which programmatically triggers the logic used when you right-click a .uproject file.

Tip: If you are building an internal studio tool that modifies .uplugin or .uproject files, call this method to refresh Visual Studio or Xcode projects automatically. This helps eliminate manual “Refresh Project” steps for your engineering team.
7. Handle Multi-Selection Arrays

When using OpenFileDialog, you can set the EFileDialogFlags::Multiple flag.

Action: The result is returned as a TArray<FString>. Always check if the function returns true and if the array is not empty before processing. This helps you eliminate “Index Out of Bounds” crashes that occur if a user cancels the dialog.
8. Project Path Normalization

IDesktopPlatform methods often require absolute paths rather than relative engine paths.

Best Practice: Use FPaths::ConvertRelativePathToFull() before passing paths to this module. Native OS dialogs do not understand Unreal’s ../../../ relative notation, so normalizing these paths will eliminate “File Not Found” errors during OS-level operations.