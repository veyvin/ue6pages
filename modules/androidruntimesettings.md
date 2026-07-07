---
layout: default
title: AndroidRuntimeSettings
---

<!-- ai-generation-failed -->

<h1>AndroidRuntimeSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Android/AndroidRuntimeSettings/AndroidRuntimeSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioPlatformConfiguration, Core, CoreUObject, Engine, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e that manages the configuration and serialization of Android-specific project settings. It acts as the C++ backend for the Project Settings > Platforms > Android menu.

Description and Purpose

This module defines the UAndroidRuntimeSettings class, which stores all the data required to package an Android application, such as the Android Manifest settings, build architectures (ARM64, x86_64), and Google Play Services integration. Its primary purpose is to provide a unified interface for the Unreal Build Tool (UBT) and the Unreal Editor to read project-specific Android configurations and apply them during the cooking and packaging process.

Practical Usage Tips and Best Practices
Accessing Settings in C++
To read Android settings in your own C++ code (e.g., checking the app version or package name), you can access the default object. Make sure to wrap this in an #if WITH_EDITOR guard or a platform check, as this module is primarily for the editor/build pipeline:
C++
	#include "AndroidRuntimeSettings.h"

	const UAndroidRuntimeSettings* Settings = GetDefault<UAndroidRuntimeSettings>();

	FString PackageName = Settings->PackageName;
Copy code
Automate Manifest Additions
Instead of manually editing the XML, use the “Extra Settings for <application> section” within the UI provided by this module. This allows you to inject custom Android Activities or Services directly into the AndroidManifest.xml via the editor, ensuring they are preserved during engine updates.
Architectural Optimization
In the settings managed by this module, ensure you only enable the architectures your target devices require (e.g., uncheck Support armv7 and keep Support arm64 for modern devices). This significantly reduces the size of your final .apk or .aab file.
Use the Config Rules System
This module supports the “Config Rules” system. You can define a configrules.txt file in your Build/Android directory to override hardware settings at runtime based on the specific device model or GPU vendor detected, allowing for granular performance scaling.
Eliminate Bloat with “Package Game Data inside .apk”
For smaller projects, enabling “Package game data inside .apk” simplifies distribution. However, for larger AAA titles, uncheck this to generate an .obb file or use Android App Bundles (.aab) to comply with Google Play Store size limits.
Handle Redactable Information
Be careful when checking settings into version control. If you are using the module to store sensitive Google Play License Keys, ensure your DefaultEngine.ini (where these settings are saved) is properly managed. For teams, it is better to use the “Distribution Signing” settings to point to a local .keystore file that is not part of the public repository.
Validate Target SDK Levels
Always keep the “Target SDK Version” aligned with the current Google Play requirements (e.g., SDK 34 or higher). Using this module to precisely set the “Minimum SDK Version” ensures you eliminate support for outdated, insecure Android versions that could cause your app to be rejected from the store.
Iterate Faster with “Smallest APK”
During development, use the “Support OpenGL ES3.2” and “Support Vulkan” toggles within the settings to test different rendering paths. Disabling the one you aren’t currently testing can speed up the “Launch On” deployment time to your connected Android device.