---
layout: default
title: ApplicationCore
---

<!-- ai-generation-failed -->

<h1>ApplicationCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ApplicationCore/ApplicationCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">BackgroundHTTPFileHash, BackgroundHttpIOS, BuildSettings, Core, CoreUObject, WindowsD3D</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

hardware abstraction layer (HAL) for the operating system’s windowing and application systems. It is the bridge between the high-level Slate UI/Engine logic and the low-level platform APIs (such as Win32, Cocoa, or Wayland).

It handles essential OS-level tasks including window creation, cursor management, clipboard access, screen resolution queries, and the initial reception of raw input events before they are passed to the Slate application.

Practical Usage Tips & Best Practices
1. Correct Module Dependency

When working with low-level windowing or clipboard logic in C++, you must add ApplicationCore to your Build.cs. Because this module is required for the application to run, it should be a public or private dependency depending on your header exposure:

C++
PublicDependencyModuleNames.AddRange(new string[] { "Core", "ApplicationCore" });
Copy code
2. Access the Platform Application

To interact with the OS (e.g., checking if the app is minimized), access the global FPlatformApplication via the FSlateApplication. Do not attempt to create a new instance; use the existing singleton provided by the engine:

C++
	if (FSlateApplication::Get().GetPlatformApplication().IsValid())

	{

	    bool bIsHidden = FSlateApplication::Get().GetPlatformApplication()->IsCursorDirectlyOverSlot();

	}
Copy code
3. Cross-Platform Clipboard Management

Use FPlatformApplicationMisc::ClipboardCopy and FPlatformApplicationMisc::ClipboardPaste for text operations. This ensures your “Copy to Clipboard” features work across Windows, Mac, and Linux without platform-specific #if PLATFORM_WINDOWS blocks.

4. Manage System Cursor State

When creating custom UI or minigames that require specific cursor behavior (like a custom aiming reticle), use the ICursor interface provided by this module. This allows you to programmatically show, hide, or lock the cursor to a window bounds at the OS level, which is more robust than simply hiding the widget.

5. Handle Display Metrics

To correctly scale UI or calculate window positions, query FDisplayMetrics. This structure, populated by ApplicationCore, provides the “Safe Zones,” screen resolution, and DPI scaling of the user’s monitor. This is critical for ensuring your HUD isn’t partially eliminated by the edges of an ultra-wide or mobile display.

6. Low-Level Window Messaging

If you are building a tool that needs to react to OS messages (like the “Power Plugged In” notification or “Window Resized”), you can register a IWindowsMessageHandler (on Windows) through this module. This is an advanced technique for tools that need to respond to events the engine doesn’t wrap by default.

7. Avoid Heavy Logic in Input Routing

Input events flow from the OS through ApplicationCore to Slate. If you are overriding OnKeyChar or similar low-level functions, keep the logic extremely lightweight. Blocking this thread or performing heavy calculations here will cause “input lag” and potentially lead to the elimination of a smooth user experience.

8. Coordinate with GenericPlatform

When writing code intended for multiple platforms, always look at FGenericPlatformApplication first. This base class defines the interface for all platforms; if a function exists there, it is safe to use in cross-platform code. Only use platform-specific subclasses (like FWindowsApplication) if you are writing code that will strictly never run on other OSs.