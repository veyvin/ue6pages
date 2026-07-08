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

ngine that manages the metadata, build parameters, and platform-specific behaviors for Android applications. It defines the UAndroidRuntimeSettings class, which acts as the C++ backend for the Project Settings > Platforms > Android menu in the Unreal Editor.

Description

This module is responsible for bridging the gap between Unreal’s project configuration and the final Android environment. It handles everything from AndroidManifest.xml generation and permissions to SDK/NDK version targeting and OpenGL/Vulkan rendering toggles. It ensures that the settings defined in your DefaultEngine.ini are correctly translated into the Gradle build system during the packaging process.

Practical Usage Tips and Best Practices
1. C++ Access to Settings

To read Android-specific settings in your C++ code (for example, to check the current Version Code or Package Name), you can access the CDO (Class Default Object) of the settings class. Ensure you include the module in your Build.cs:

C++
	#include "AndroidRuntimeSettings.h"

	 

	// Accessing the settings

	if (const UAndroidRuntimeSettings* Settings = GetDefault<UAndroidRuntimeSettings>())

	{

	    FString PackageName = Settings->PackageName;

	}
Copy code
2. Automate Versioning via Build Scripts

Instead of manually incrementing the “Store Version” in the Editor, use the AndroidRuntimeSettings properties in conjunction with a CI/CD pipeline. You can use a command-line switch to override the VersionDisplayName and VersionCode during the build process to ensure every build has a unique, traceable ID.

3. Manage Permissions Safely

The module allows you to add “Extra Permissions” to the manifest. Best practice is to keep this list minimal. Adding unnecessary permissions can lead to app rejection or user distrust. For events like recording audio during a match, ensure the permission is only added if the feature is active in your build configuration.

4. Optimize Manifest with UPL

While the module handles standard settings, use Unreal Plugin Language (UPL) for advanced manifest surgery. If you need to add specific <intent-filter> tags or third-party SDK activities that the standard settings don’t cover, the AndroidRuntimeSettings will incorporate your UPL XML instructions into the final build.

5. Configure Distribution Signing

Within these settings, you must configure your Key Store, Alias, and Passwords. Security Tip: Never check your keytool passwords directly into a public version control system. Use the module’s support for environment variables or localized DefaultEngine.ini files that are excluded from your repository.

6. Handle Application Elimination Behavior

In the Advanced section of the settings, you can toggle the “Terminate on Exit” behavior. For many Android games, setting this to true is a common practice to ensure all resources are cleared and to eliminate potential “Application Not Responding” (ANR) errors when a user attempts to restart the app quickly after closing it.

7. Architecture Targeting

Use the settings to specify which CPU architectures to support (typically arm64-v8a). To minimize your APK/AAB size, disable any architectures you do not intend to support. This is the most effective way to eliminate “bloat” from your final package for the Google Play Store.

8. Verify Vulkan/OpenGL Support

The module controls which graphics APIs are bundled. For modern devices, enabling Vulkan can significantly improve performance and reduce thermal throttling. Use the “Detection” settings to ensure the game falls back to OpenGL ES 3.2 only if Vulkan support is not found on the user’s device.