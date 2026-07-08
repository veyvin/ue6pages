---
layout: default
title: AppFramework
---

<!-- ai-generation-failed -->

<h1>AppFramework</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AppFramework/AppFramework.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, InputCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

t provides a suite of high-level Slate widgets and application-level utilities. It acts as a bridge between the low-level SlateCore (which handles basic rendering/events) and the specific needs of complex desktop applications and engine tools.

Description

This module is used to construct the “infrastructure” of a user interface. It contains complex, multi-component widgets that are common across the Unreal Editor and standalone tools, such as color pickers, window management logic, undo history views, and error reporting dialogs. If you are building an Editor Utility Widget, a custom engine plugin, or a standalone Slate application, AppFramework provides the professional-grade controls necessary for a standard user experience.

Practical Usage Tips and Best Practices
1. Configure Build Dependencies

To utilize the widgets in this module within your C++ project, you must explicitly include it in your *.Build.cs file. It is often used alongside Slate and SlateCore.

C#
	// In YourProject.Build.cs

	PrivateDependencyModuleNames.AddRange(new string[] { "Slate", "SlateCore", "AppFramework" });
Copy code
2. Leverage the SColorPicker

Instead of building a color selection tool from scratch, use the SColorPicker. It is the same robust tool used throughout the Unreal Editor, supporting RGB, HSV, Hex input, and alpha channels. It also handles sRGB conversions correctly, which is vital for maintaining visual consistency across different displays.

3. Use SWindow for Standalone Tools

If you are creating a popup or a secondary tool window, use SWindow from this module. It provides built-in support for title bars, resizing handles, and modal behavior. When spawning a new window, always ensure you set the bSimplifyWindow property to true if you want a clean, borderless look for minimal utility overlays.

4. Implement Standard Header Rows

For complex data views (like a list of items or logs), use the SHeaderRow widget. This allows you to create columns that users can resize, hide, or sort. It is the standard way to present organized data in the engine, providing a familiar interface for anyone used to the Unreal Editor’s “Details” or “Content Browser” panels.

5. Utilize the Undo History Widget

If your tool supports the UTransactor system (Unreal’s Undo/Redo framework), you can use the SUndoHistory widget to display a visual list of the undo stack. This is a best practice for complex tools where users need to track their changes and revert specific actions without guesswork.

6. Graceful Error Handling with SErrorReporting

The module provides the SErrorReporting widget, which is ideal for validating user input in real-time. Instead of using intrusive popup dialogs, you can embed this widget in your UI to show a red warning icon and a tooltip when a setting is invalid, effectively helping to eliminate user errors during tool operation.

7. Standardize with Framework Styles

Avoid hard-coding colors and padding for your widgets. AppFramework relies on the FAppStyle class. By using FAppStyle::Get().GetBrush("StandardBrush") or similar calls, your custom UI will automatically inherit the look and feel of the Unreal Editor (e.g., dark mode vs. light mode), ensuring a professional integration.

8. Manage Application Lifecycle

Use the utilities in this module to respond to application-level events, such as the window gaining or losing focus. This is particularly useful for custom tools that need to pause background processing or save data when the user clicks away, helping to eliminate potential data loss during a crash or unexpected elimination of the application process.