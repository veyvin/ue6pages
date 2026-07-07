---
layout: default
title: IOSRuntimeSettings
---

<!-- ai-generation-failed -->

<h1>IOSRuntimeSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/IOS/IOSRuntimeSettings/IOSRuntimeSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioPlatformConfiguration, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ration values stored in your project’s DefaultEngine.ini. Its primary purpose is to manage the metadata and build-time instructions required to package an application for Apple devices. This includes bundle identifiers, supported orientations, version numbers, rendering APIs (Metal), and icon/launch screen references. When you package a project, the engine queries this module to generate the final Info.plist and build environment, helping you eliminate the need to manually edit complex XML configuration files in Xcode.

Practical Usage Tips and Best Practices
Configure a Unique Bundle Identifier
In the settings managed by this module, ensure your Bundle Identifier follows the reverse-DNS format (e.g., com.company.game). This is critical for code signing; an incorrect identifier will eliminate your ability to deploy to a physical device or the App Store.
Set the Minimum iOS Version Aggressively
Adjust the Minimum iOS Version to target only the hardware that supports your performance requirements. Targeting older versions unnecessarily can force you to include legacy code paths, whereas a higher minimum version helps you eliminate compatibility bugs with obsolete hardware.
Optimize Frame Pacing for Battery Life
Use the Frame Rate Lock settings within the iOS runtime settings to cap the game at 30 or 60 FPS. Mobile devices heat up quickly; capping the frame rate helps you eliminate thermal throttling and significantly extends the player’s battery life.
Manage Metal Shader Precision
Within the rendering section, you can toggle “Use Fast-Math” or force 32-bit floating-point precision. If you notice visual artifacts in your materials on certain devices, disabling “Fast-Math” can help you eliminate precision errors, though it may slightly impact performance.
Utilize Remote Build Settings for Windows Teams
If you are developing on Windows, the Remote Build section in these settings allows you to connect to a Mac for code signing and compilation. Properly configuring the Remote Server Name and SSH Key is the only way to eliminate the requirement of a local Mac for every developer.
Define Custom Launch Storyboards
Starting with recent iOS versions, static launch images are deprecated. Use the Launch Screen settings to point to a custom Storyboard file. This is a best practice to eliminate black screens during the initial application boot and ensures compliance with Apple’s App Store guidelines.
Customize the Info.plist for Permissions
The module provides an Extra Info.plist Provisions text box. Use this to add custom keys for privacy permissions (like Camera or Microphone access). Correctly providing these descriptions helps you eliminate App Store rejections due to missing usage strings.
Enable/Disable Specific Device Support
In the Supported Devices list, you can uncheck specific iPad or iPhone models. If your game requires high-end features like Lumen or Nanite (which have limited mobile support), use these checkboxes to eliminate the possibility of users with underpowered devices downloading the game and experiencing crashes.