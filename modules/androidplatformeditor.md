---
layout: default
title: AndroidPlatformEditor
---

<!-- ai-generation-failed -->

<h1>AndroidPlatformEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Android/AndroidPlatformEditor/AndroidPlatformEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AndroidDeviceDetection, AndroidRuntimeSettings, AudioSettingsEditor, Core, CoreUObject, DesktopPlatform, DesktopWidgets, EditorWidgets, Engine, InputCore, MainFrame, MaterialShaderQualitySettings, MaterialShaderQualitySettingsEditor, PropertyEditor, RHI, RenderCore, ShaderPlatformConfigEditor, SharedSettingsWidgets, Slate, SlateCore, SourceControl</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

that provides the user interface and logic for managing Android-specific project settings. It acts as the backend for the Project Settings > Platforms > Android and Android SDK panels, handling the configuration of the Android Manifest, APK packaging settings, and the integration of the Android toolchain (SDK, NDK, and JDK).

This module is primarily used by developers to configure app permissions, distribution signing (keystores), and hardware-specific optimizations like Vulkan support or screen orientation.

Practical Usage Tips and Best Practices
1. Use the “Configure Now” Button

When first setting up a project for Android, always use the Configure Now button in the Project Settings. This action allows the module to generate the necessary Build/Android directory and platform-specific files. Without this, the engine cannot correctly package your project or handle elimination of unused resources during the build process.

2. Manage Keystores via Project Settings

Avoid manually moving .keystore files into the engine folders. Use the Distribution Signing section provided by this module to point to your keystore. Ensure the “Key Alias,” “Key Store Password,” and “Key Password” match exactly what you generated via keytool. If these are incorrect, the editor will fail to sign the APK for Google Play distribution.

3. Customize the Android Manifest via Extra Tags

Instead of trying to manually edit the AndroidManifest.xml (which is overwritten every build), use the Advanced APK Packaging section. You can add “Extra Tags for <manifest> node” or “Extra Settings for <application>” directly in the editor. This ensures your custom permissions or hardware requirements persist through every build.

4. Leverage Turnkey for SDK Setup

In modern versions of UE (5.x), the AndroidPlatformEditor integrates with Turnkey. Use the Platforms > SDK Management menu to let the engine automatically detect and install the verified versions of the SDK and NDK. This prevents common “NDK not found” errors during the compilation of C++ projects.

5. Environment-Specific SDK Overrides

If you have a specialized build machine or multiple versions of the NDK, you can override the global paths within the Android SDK section of the Project Settings. This is useful for pinning a specific NDK version (e.g., r25b) for a single project without affecting your other engine installations.

6. Optimize via Quality Presets

Use the Target Hardware and Mobile Render settings within the Android settings panel to toggle features like “Support Bloom” or “Support Desktop Forward Shading.” Disabling unnecessary high-end features here will lead to a significant elimination of shader compile time and improve the frame rate on mid-range Android devices.

7. Use UPL (Unreal Plugin Language) for Deep Integration

If you need to inject Java code or modify the GameActivity.java for third-party SDKs, the AndroidPlatformEditor processes UPL XML files. Instead of modifying engine source code, create a UPL script in your plugin to safely inject code into the Android build pipeline.

8. Verify App Bundles (AAB) for Google Play

Google Play requires .aab (Android App Bundle) files rather than .apk for new apps. Ensure the Generate Bundle (AAB) checkbox is enabled in the Android settings. This allows the module to package your game in a way that Google can optimize for different device configurations, reducing the download size for your players.