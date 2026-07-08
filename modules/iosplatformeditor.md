---
layout: default
title: IOSPlatformEditor
---

<!-- ai-generation-failed -->

<h1>IOSPlatformEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/IOS/IOSPlatformEditor/IOSPlatformEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioSettingsEditor, Core, CoreUObject, DesktopPlatform, Engine, FreeImage, GameProjectGeneration, IOSRuntimeSettings, InputCore, MacTargetPlatformControls, MacTargetPlatformSettings, MainFrame, MaterialShaderQualitySettings, MaterialShaderQualitySettingsEditor, PropertyEditor, RHI, RenderCore, ShaderPlatformConfigEditor, SharedSettingsWidgets, Slate, SlateCore, SourceControl, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

s menu in the Unreal Editor.

This module is responsible for handling Apple-specific requirements, such as mobile provisioning profiles, signing certificates, app icons, and splash screens. By centralizing these platform-specific tasks, it helps eliminate the complexity of manually editing .plist files or managing build settings that would otherwise require deep knowledge of Xcode.

Practical Usage Tips and Best Practices
Manage Provisions and Certificates Directly
Use the iOS Project Settings (powered by this module) to import your .mobileprovision and .p12 files. The module provides a status indicator (green/red) for each; ensure both are valid to eliminate “Code Signing Error” failures during the packaging process.
Configure Automatic Icon Generation
Rather than manually creating dozens of specific icon sizes in Photoshop, provide a single high-resolution source image (usually 1024x1024) within the settings. The module will handle the resizing and manifest creation, helping you eliminate the risk of missing a specific icon size required by the App Store.
Define Custom Plist Entries
If your project requires specific iOS permissions—such as Camera, Location, or Bluetooth access—use the “Additional Plist Data” field. This allows the module to inject the necessary NSUsageDescription strings into the final Info.plist, which helps you eliminate immediate app rejections by Apple’s automated scanners.
Optimize Frame Rate via ‘Max Metal Shader Standard’
Within the module’s settings, you can specify the Metal Shader Standard. For modern devices, choosing a higher version (like Metal 2.1 or 3.0) can eliminate performance bottlenecks by allowing the engine to use more advanced GPU features and optimizations.
Toggle Remote Shader Compiling
If you are developing on Windows, this module facilitates the connection to a “Remote Mac” for shader compilation and code signing. Ensure the SSH credentials and IP are correctly configured in the settings to eliminate “Unable to connect to remote server” errors during the build.
Set the Correct Bundle Identifier
Ensure your Bundle Identifier matches exactly what is registered in your Apple Developer Portal. The module uses this string to verify against your provisioning profiles; a mismatch will eliminate your ability to deploy the app to a physical device.
Configure Supported Hardware Tiers
Use the “Minimum iOS Version” and “Supported Devices” checkboxes to filter out older hardware. This helps you eliminate support requests from users with devices that do not meet your game’s memory or GPU requirements.
Utilize the Launch Screen Storyboard
Modern iOS apps require a .storyboard file for the launch screen rather than static images. Use the module’s settings to point to your custom storyboard file, which helps you eliminate the “black bars” or incorrect aspect ratio issues seen on newer iPhones and iPads.