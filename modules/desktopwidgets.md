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

s specialized widgets for desktop-specific application workflows. Unlike standard gameplay UI (UMG), this module contains professional-grade interface elements designed for tools, editors, and standalone utility applications.

It is primarily used to build desktop-centric features such as file/directory pickers, window title bars, and platform-specific dialogs that feel native to the operating system.

Practical Usage Tips and Best Practices
1. Implement Native Directory Picking

Instead of building a custom file browser, use the SDirectoryPicker widget from this module. It provides a standard, professional interface for users to select paths on their local machine. This ensures the elimination of “non-standard” UI patterns that can confuse users in professional toolsets.

2. Use SWindowControlButtons for Custom Titles

If you are creating a custom-styled window (like the Unreal Editor’s own title bar), use SWindowControlButtons. This widget handles the standard Minimize, Maximize, and Close logic, facilitating the elimination of manual window state management code.

3. Conditional Module Inclusion

Since this module is intended for developer tools and desktop applications, avoid including it in mobile or console shipping builds. In your Build.cs, wrap the dependency to ensure the elimination of unnecessary bloat in your runtime executable:

C#
	if (Target.Platform == UnrealTargetPlatform.Win64 || Target.Platform == UnrealTargetPlatform.Mac)

	{

	    PrivateDependencyModuleNames.Add("DesktopWidgets");

	}
Copy code
4. Combine with DesktopPlatform for Full Functionality

The DesktopWidgets module provides the visual elements (UI), but the DesktopPlatform module provides the actual OS-level hooks. Use them together to create a seamless workflow: the widget collects the user intent, and the platform module executes the file operation, resulting in the elimination of platform-specific C++ logic in your UI code.

5. Utilize SBreadcrumbTrail for Navigation

For tools that involve deep folder hierarchies or complex nested settings, use the SBreadcrumbTrail widget. It provides a clickable path (e.g., Project > Assets > Characters) that allows users to jump back to previous levels, ensuring the elimination of navigation fatigue in complex desktop tools.

6. Leverage Desktop-Specific Styling

The widgets in this module are designed to look consistent with the Unreal Editor “Dark” theme. When building a custom tool, using these pre-styled widgets ensures the elimination of visual discrepancies, making your tool feel like an integrated part of the Unreal ecosystem.

7. Handle Window Dragging with STitleBar

If you are building a “borderless” window, use the STitleBar widget to define the draggable area of your UI. This widget communicates directly with the underlying SWindow, leading to the elimination of manual mouse-delta calculations for moving windows around the desktop.

8. Prioritize Slate over UMG for Tooling

While UMG is excellent for game HUDs, the DesktopWidgets module is built for Slate. For complex desktop applications or editor extensions, stick to Slate to leverage these advanced widgets. This architectural choice leads to the elimination of performance overhead associated with the UMG-to-Slate wrapper in high-density data tools.