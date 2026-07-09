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

eal Engine that provides a cross-platform abstraction layer for hardware and operating system functionality. It sits just above the Core module and serves as the bridge between the engine’s high-level systems (like Slate or the Viewport) and the underlying platform APIs (Windows Win32, macOS Cocoa, Linux, etc.).

Its primary role is to handle window management, mouse/keyboard input events, clipboard operations, screen resolution, and OS-level messaging in a way that allows the rest of the engine to remain platform-agnostic.

Practical Usage Tips and Best Practices
1. Conditional Build Dependencies

ApplicationCore is essential for any code that interacts with the OS window or native hardware input. However, because it is a low-level dependency, you should ensure it is added correctly in your Build.cs. It is required if you are writing custom Editor tools or low-level input handlers.

C#
PublicDependencyModuleNames.AddRange(new string[] { "Core", "ApplicationCore" });
Copy code
2. Accessing Platform-Specific Information

Use the FPlatformApplicationMisc class within this module to query OS-level data that is not part of the standard gameplay framework. For example, you can check the device’s battery level, retrieve the OS version, or detect if the application has focus.

3. Native Clipboard Integration

If you are building a custom Editor tool or a game feature that requires copying/pasting text to and from the player’s operating system, use the GenericApplication interface provided by this module. This ensures your “Copy to Clipboard” logic works seamlessly across Windows, Mac, and Linux.

4. Managing Mouse Cursor State

While high-level input is usually handled via APlayerController, ApplicationCore allows you to control the native hardware cursor. Use this for “software cursor” implementations or to lock the mouse to a specific window bounds during intense gameplay to prevent accidental “elimination” of focus.

5. Handling Display Metrics

When building UI that needs to account for multi-monitor setups or high-DPI scaling, use FDisplayMetrics. This class provides accurate information about the usable area of the screen, including taskbar offsets and native resolutions, which is critical for correctly positioning pop-up windows.

6. Coordinate Platform-Level Input Devices

ApplicationCore manages the IInputDevice interface. If you are developing a driver for a custom piece of hardware (like a specialized flight stick or a VR controller), you will likely implement a class that inherits from IInputDevice within this module to pipe raw OS events into Unreal’s InputCore.

7. Monitor Application Heartbeat

The module handles the “Pump Messages” logic for the OS. In specialized C++ applications (like standalone commandlets), you can use FPlatformApplicationMisc::PumpMessages to ensure the application remains responsive to the OS and doesn’t get flagged as “Not Responding” during long processing tasks.

C++ Implementation Example: Accessing the Clipboard

To interact with the OS clipboard using ApplicationCore, you use the platform’s application instance:

C++
	#include "HAL/PlatformApplicationMisc.h"

	#include "GenericPlatform/GenericApplication.h"

	 

	void UMyPlatformUtils::CopyTextToOSClipboard(FString TextToCopy)

	{

	    // Copy a string to the native OS clipboard

	    FPlatformApplicationMisc::ClipboardCopy(*TextToCopy);

	}

	 

	FString UMyPlatformUtils::PasteTextFromOSClipboard()

	{

	    FString ClipboardContent;

	    // Retrieve text from the native OS clipboard

	    FPlatformApplicationMisc::ClipboardPaste(ClipboardContent);

	    return ClipboardContent;

	}
Copy code
Best Practices & Performance
Avoid Main Thread Blockage: Since ApplicationCore handles OS messages, blocking the main thread for too long will prevent the OS from processing “Close” or “Minimize” commands, leading to a “Hang” state.
Use Generic Interfaces: Always prefer the Generic versions of classes (e.g., GenericApplication) rather than platform-specific ones (e.g., WindowsApplication). This ensures your code remains portable.
Input Latency: When implementing custom input devices, ensure you are polling or receiving events as close to the hardware interrupt as possible via the ApplicationCore interfaces to minimize input lag.