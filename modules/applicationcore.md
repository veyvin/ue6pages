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

eal Engine that provides a platform-agnostic interface for interacting with the operating system. It sits directly above the hardware/OS layer and below the high-level Engine and Slate modules.

What it is and What it’s used for

ApplicationCore acts as a wrapper for OS-specific functionality like window creation, cursor management, and hardware input processing. Instead of writing separate code for Windows (Win32), Mac (Cocoa), or Linux, developers interact with the generic classes in this module.

Primary uses include:

Window Management: Creating, resizing, and managing the lifecycle of the application windows.
Input Handling: Capturing raw HID (Human Interface Device) events like mouse movement, key presses, and gamepad input before they are passed to the Slate UI system.
Display Metrics: Querying monitor resolution, DPI scales, and safe zones (crucial for mobile and console).
Clipboard & System Services: Interacting with the system clipboard and OS-level message boxes.
Practical Usage Tips and Best Practices
1. Accessing Display Metrics

When you need to know the physical dimensions of the user’s screen or the current DPI scale for UI layout, use FDisplayMetrics. This is more accurate for low-level calculations than high-level UMG functions.

C++
	FDisplayMetrics DisplayMetrics;

	FDisplayMetrics::RebuildDisplayMetrics(DisplayMetrics);

	// Access DisplayMetrics.PrimaryDisplayWidth, etc.
Copy code
2. Handle Custom Input via IMessageHandler

If you are building a custom window or a specialized tool that doesn’t use the standard Gameplay Framework, you must implement IMessageHandler. This interface allows your class to receive raw OS events (like OnKeyDown or OnControllerAnalog) directly from the GenericApplication.

3. Manage the System Clipboard

The FPlatformApplicationMisc class within this module is the standard way to interact with the OS clipboard. Use ClipboardCopy and ClipboardPaste to allow users to move text between your game/tools and other applications.

4. Use GenericApplication for Platform Logic

Avoid using #if PLATFORM_WINDOWS whenever possible. Instead, use the methods provided by FSlateApplication::Get().GetPlatformApplication(). This returns a GenericApplication pointer that handles the platform-specific logic internally, making your code cleaner and more portable.

5. Monitor Window Focus Events

Use this module to detect when the application loses focus (Deactivate) or is minimized. This is the ideal time to pause the game, throttle the frame rate to save power, or mute audio to improve the user’s experience when they tab out.

6. Coordinate with SlateCore

ApplicationCore and SlateCore work in tandem. ApplicationCore gathers the raw events, and SlateCore processes them into UI interactions. If you are developing a standalone application using Unreal’s slate framework, ensure both modules are included in your *.Build.cs to handle the window-to-UI pipeline correctly.

7. Handle High-DPI Scaling

With the prevalence of 4K monitors, always check the Scale factor provided by the windowing logic in this module. Ensure your application window isn’t created with a hardcoded pixel size, but rather one that accounts for the OS-level scaling factor to eliminate blurry text and tiny icons.

8. Graceful Elimination of Application Windows

When shutting down specific windows in a multi-window editor tool, use the CloseWindow methods within the GenericWindow class. This ensures that the OS-level resources are freed correctly and that the application doesn’t hang or leave “ghost” processes in the task manager.