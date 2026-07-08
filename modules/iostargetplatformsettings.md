---
layout: default
title: IOSTargetPlatformSettings
---

<!-- ai-generation-failed -->

<h1>IOSTargetPlatformSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/IOS/IOSTargetPlatformSettings/IOSTargetPlatformSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, Engine, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

s such as bundle identifiers, supported orientations, and hardware requirements.

It acts as the “source of truth” for the Unreal Build Tool (UBT) and the Target Platform Manager. By centralizing these variables, it ensures that the engine can eliminate configuration discrepancies when switching between different build machines or CI/CD pipelines.

Practical Usage Tips and Best Practices
Access Settings via C++ for Automation
If you are writing a custom build script or an Editor Utility, you can access these settings by getting the UIOSRuntimeSettings object via GetDefault<UIOSRuntimeSettings>(). This allows you to programmatically check or modify values like the version number, helping you eliminate manual entry errors during version increments.
Implement Configuration Overrides
This module reads from DefaultEngine.ini. You can use platform-specific overrides (e.g., [IOS TargetSettings]) to define different bundle IDs for “Development” vs. “Shipping” builds. This practice helps you eliminate the risk of accidentally overwriting your production app on a tester’s device.
Configure Frame Pacing for Battery Life
Use the FramePacing settings within this module to set a target FPS (e.g., 30, 60, or Max). Setting a sensible default for mobile devices helps eliminate excessive thermal throttling and rapid battery drain during extended play sessions.
Validate ‘Minimum iOS Version’ for Plugins
Many modern plugins (like those for ARKit or advanced haptics) require a specific iOS version. Ensure the Minimum iOS Version in these settings is high enough to support your dependencies; this helps you eliminate cryptic linker errors that occur when a plugin calls an API not present in the target SDK.
Include Module in Build.cs for Target Logic
If you are developing a tool that needs to query if the current project is configured for iOS (e.g., checking if Bitcode is enabled), add "IOSTargetPlatformSettings" to your PrivateDependencyModuleNames. This ensures your code has access to the specialized UObject definitions for iOS.
Manage Remote Build Server Settings
For developers on Windows, this module stores the “Remote Server Name” and “Rsync” paths. If your team uses multiple Mac build minis, you can point this to a load balancer or a specific machine IP to eliminate build queue bottlenecks in a studio environment.
Set ‘Automatic Signing’ for Rapid Iteration
The module supports the “Automatic Signing” flag. When enabled, it allows the engine to request Xcode to handle the provision/certificate matching. This helps eliminate the “Certificate Not Found” headache for developers who are frequently adding new test devices to their Apple account.
Define Background Execution Modes
If your game requires background audio or location updates, use the Extra Background Modes array in these settings. This ensures the module correctly injects the necessary keys into the generated Info.plist, which helps you eliminate the app being suspended by the OS when the user minimizes it.