---
layout: default
title: DesktopWidgets
---

<!-- ai-generation-failed -->

<h1>DesktopWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/DesktopWidgets/DesktopWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, InputCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at provides specialized widgets for desktop platforms. While standard Slate widgets (found in the Slate and SlateCore modules) handle general UI like buttons and lists, DesktopWidgets provides the “glue” between the OS and the engine’s interface.

It is primarily used for creating native-feeling window frames, custom title bars, and platform-specific wrappers. It is a critical component for developers building standalone tools, editor extensions, or custom launchers that require deep integration with the host operating system’s windowing system.

Practical Usage Tips and Best Practices
1. Use SWindowTitleBar for Custom Editor Windows

If you are creating a standalone tool or a secondary editor window, use the SWindowTitleBar widget. It provides the standard minimize, maximize, and close buttons that match the Unreal Engine aesthetic. This ensures the elimination of “plain” or inconsistent window headers in your custom tools.

2. Implement SNativeWindowWrapper for Low-Level Control

When you need to wrap a native OS window handle (HWND on Windows) into a Slate-compatible format, use SNativeWindowWrapper. This allows Slate to “see” and interact with windows managed by the platform, assisting in the elimination of input conflicts between the OS and the engine.

3. Leverage SDesktopPlatform for File Dialogs

While not a widget itself, the DesktopWidgets module often works in tandem with the DesktopPlatform module to trigger native “Open File” or “Save Folder” dialogs. Use these to allow users to select assets outside the project directory, leading to the elimination of hard-coded file paths in your pipeline tools.

4. Optimize with SWindow Content Padding

When building a custom desktop window, pay attention to the SWindow content padding settings. Desktop-specific widgets often require specific margins to account for OS-level borders. Proper padding facilitates the elimination of “clipped” UI elements at the edges of the window frame.

5. Use SPrimaryButton for Consistent UX

The DesktopWidgets and related tool modules provide the SPrimaryButton. This is the blue “action” button seen in the Unreal Editor (e.g., the “Save” button). Using this in your desktop tools assists in the elimination of user confusion by highlighting the intended “Success” path in a dialogue.

6. Debug with the Slate Reflector

Since desktop widgets often deal with complex hierarchies and window-level offsets, use the Slate Reflector (Widget Reflector) to inspect them. This tool allows you to see exactly which DesktopWidgets class is responsible for a specific UI element, aiding in the elimination of layout bugs.

7. Handle Window Activation Events

When using widgets from this module, ensure you hook into window activation and deactivation events. This is a best practice for the elimination of “phantom” inputs—ensuring your custom desktop window doesn’t continue processing keyboard shortcuts when the user has clicked away to another application.

8. Modularize via DeveloperToolSettings

Many behaviors of desktop-specific widgets can be configured via the DeveloperToolSettings module. If your custom window needs to persist its position or size across sessions, use these settings to store the layout, which leads to the elimination of the need for users to manually resize their workspace every time the tool is opened.