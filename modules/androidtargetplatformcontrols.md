---
layout: default
title: AndroidTargetPlatformControls
---

<!-- ai-generation-failed -->

<h1>AndroidTargetPlatformControls</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Android/AndroidTargetPlatformControls/AndroidTargetPlatformControls.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AndroidDeviceDetection, AndroidTargetPlatformSettings, AudioPlatformConfiguration, Core, CoreUObject, DesktopPlatform, Engine, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

as the primary “Front-end” interface and logic layer for Android-specific configuration within Unreal Engine. It manages the UI elements and underlying data validation found in the Project Settings > Platforms > Android and Android SDK categories.

This module is responsible for bridging the gap between high-level project settings and the low-level requirements of the Android build process. It handles tasks such as SDK license acceptance, manifest requirement validation, and the configuration of APK packaging settings (like Minimum and Target SDK versions).

1. Ensure SDK License Acceptance

The most critical function of this module is managing the Android SDK License. If you see a warning stating “Project is not configured for the Android platform,” you must click the Configure Now button provided by this module. This generates the necessary platform files and enables the Accept SDK License button, which is a mandatory step before any build can proceed.

2. Validate Package Names

The module enforces strict naming conventions for the Android Package Name (e.g., com.YourCompany.[ProjectName]).

Best Practice: Avoid using underscores or special characters in the package name, as the module’s validation logic may flag these, leading to failures during the manifest generation phase. Use only alphanumeric characters and dots.
3. Manage Manifest Requirements and Permissions

The module provides a UI for adding “Extra Permissions” and “Extra Settings” to the AndroidManifest.xml. Instead of manually editing the manifest file, use the fields provided in the Project Settings (managed by this module). This ensures that your permissions are correctly formatted and injected during the build process without manually editing intermediate files.

4. Configure Architecture Support

Through this module’s interface, you can select which architectures to include in your build (e.g., Support arm64-v8a or Support x86_64).

Tip: To reduce iteration time during development, enable only the specific architecture of your test device. Enabling all architectures increases the final APK/AAB size and significantly lengthens the packaging time.
5. Utilize Turnkey for SDK Setup

In modern versions of Unreal Engine (5.x+), the AndroidTargetPlatformControls module integrates with Turnkey to simplify toolchain installation. Use the Platforms > SDK Management > Android > Install SDK menu option. This allows the module to automatically download and configure the exact versions of the NDK, JDK, and SDK verified for your engine release, eliminating manual path errors.

6. Set Target and Minimum SDK Levels

This module allows you to define the Minimum SDK Version and Target SDK Version.

Best Practice: Always check the current Google Play Store requirements for the Target SDK level. If your Target SDK is too low, the module will allow the build, but the resulting package will be rejected by the Play Store.
7. Configure Texture Format Priorities

Inside the Android settings managed by this module, you can configure the Texture Format Priority for packaging. This determines which texture compression (like ASTC or DXTC) is prioritized when the “Multi” variant is selected. Correctly ordering these can ensure the best visual quality for your target hardware.

8. Handling Google Play Services

The module includes a toggle for Enable Google Play Support. If you are integrating Leaderboards, Achievements, or In-App Purchases, clicking Configure Now in the Google Play Services section of the settings is required to enable the module to write the necessary google-services.json metadata into your project.