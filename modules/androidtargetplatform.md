---
layout: default
title: AndroidTargetPlatform
---


<h1>AndroidTargetPlatform</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Android/AndroidTargetPlatform/AndroidTargetPlatform.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AndroidDeviceDetection, AudioPlatformConfiguration, Core, CoreUObject, DesktopPlatform, Engine, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

editor’s platform abstraction layer. It defines how the engine perceives, interacts with, and packages content specifically for the Android operating system.

What it is and What it’s used for

This module implements the ITargetPlatform interface for Android. It is an Editor-only module that provides the engine with the necessary logic to handle Android-specific hardware configurations, texture compression formats, and deployment rules.

Primary uses include:

Device Discovery: Detecting connected Android devices via ADB (Android Debug Bridge) for “Launch On” functionality.
Cooking & Packaging: Translating generic engine assets into Android-optimized formats (e.g., ASTC textures).
Platform Settings: Exposing Android-specific project settings in the Editor, such as SDK/NDK paths, screen orientations, and manifest requirements.
Feature Support Querying: Informing the editor which rendering features (like Vulkan or OpenGL ES) are supported by the target mobile hardware.
Practical Usage Tips and Best Practices
1. Manage Multi-Texture Formats

Android supports various texture compression formats (ASTC, DXT, ETC2). Use the AndroidTargetPlatform settings to prioritize ASTC for modern devices. This ensures the best balance between visual quality and memory footprint, which is critical to avoid crashes on lower-end hardware.

2. Utilize Config Rules (configrules.txt)

You can control device-specific behavior without changing C++ code by using the configrules.txt system. This allows you to set variables based on the device model or GPU vendor. For example, you can disable high-end post-processing if a specific mobile GPU is detected to prevent performance degradation.

3. Optimize via Per-Platform Overrides

In the Project Settings, look for the small “plus” icon next to properties like “Max FPS” or “Resolution Scale.” The AndroidTargetPlatform module allows you to override these values specifically for Android, ensuring your game doesn’t overheat the device while maintaining high quality on PC.

4. Configure SDK/NDK/Java Paths Correctly

The most common failure in this module is a mismatch in environment paths. Always ensure your Android SDK, NDK, and JDK paths are set in Project Settings > Platforms > Android SDK. Use the versions recommended for your specific Unreal Engine version (e.g., UE 5.5 generally prefers NDK r25b or r26b).

5. Leverage “Launch On” for Iteration

Instead of full packaging, use the Launch button in the toolbar. The AndroidTargetPlatform module handles the incremental cook and deploy, only sending modified files to the device. This drastically reduces iteration time compared to a full APK build.

6. Use Device Profiles for Scalability

The module interacts with the Device Profiles system. Create specific profiles for different Android tiers (e.g., Android_Low, Android_Mid, Android_High). You can adjust r.MobileContentScaleFactor and other CVar settings to ensure a smooth frame rate across the fragmented Android ecosystem.

7. Monitor Device Output with Logcat

If a game fails to start on the device, use the Android Logcat window in the Unreal Editor (Window -> Developer Tools). This module pipes the device’s system logs directly into the editor, allowing you to see why a process was eliminated or if a shader failed to compile on the mobile GPU.

8. Validate Permissions in the Manifest

The module generates the AndroidManifest.xml during the build process. Ensure you only check the permissions your game actually needs in Project Settings > Android. Excessive permissions (like “Read Contacts”) can lead to store rejection and unnecessary privacy concerns for your users.