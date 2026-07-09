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

gine that manages the data structures and logic for Android-specific platform settings. It defines the UAndroidRuntimeSettings class, which stores the variables found in Project Settings > Platforms > Android. This module is critical for controlling APK packaging, manifest generation, SDK versions, and hardware-specific optimizations (like Vulkan support or orientation) directly from the engine.

Practical Usage Tips & Best Practices
1. Add Build.cs Dependency for Automation

If you are writing Editor Utility Widgets or automation scripts that need to programmatically modify Android settings (e.g., changing the Version Code during a build pipeline), you must include the module in your Build.cs.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AndroidRuntimeSettings");

	}
Copy code
2. Access Settings via C++ Singleton

To read or modify Android settings in code, access the UAndroidRuntimeSettings default object. This is useful for checking if specific features, like high-end graphics or specific orientation locks, are enabled before executing platform-specific logic.

C++
	#include "AndroidRuntimeSettings.h"

	 

	const UAndroidRuntimeSettings* Settings = GetDefault<UAndroidRuntimeSettings>();

	if (Settings && Settings->bSupportVulkan)

	{

	    // Execute Vulkan-specific logic

	}
Copy code
3. Use “Don’t Bundle Libraries” for Rapid Iteration

For C++ developers, the “Don’t Bundle Libraries into APK” setting (found in this module’s settings) is essential. When enabled, the engine excludes heavy assets from the package, allowing you to deploy only code changes. This significantly reduces the time spent waiting for a device deploy after a code fix.

4. Configure ProGuard and Small-So for Optimization

Within the Android Runtime Settings, enable “Build Shipping config with hidden visibility” (Small-So). This results in smaller binary sizes by stripping symbols. Additionally, use the ProGuard settings to further minimize the final APK size, which is vital for meeting app store requirements.

5. Manage Permissions for Elimination Events

If your game uses social features or cloud saving to track player stats (like an elimination leaderboard), you must add the necessary permissions (e.g., android.permission.INTERNET) in the Extra Permissions array within these settings. This ensures the Android Manifest is correctly generated with the required security access.

6. Utilize Config Rules (configrules.txt)

The Android Runtime Settings system supports a configrules.txt file (placed in Build/Android). This allows you to define variables based on the device hardware (e.g., GPU family or RAM). You can then query these variables in C++ using FAndroidMisc::GetConfigRulesVariable to scale your game’s quality dynamically.

7. Override SDK/NDK Versions per Project

While Unreal uses global settings by default, you can use the Project SDK Override section in this module to pin a specific project to an older NDK or a specific SDK level. This is helpful when maintaining a legacy project that is not yet ready for the latest Android API requirements.

8. Verify App Bundles (AAB) for Play Store

Always ensure “Generate Bundle (AAB)” is enabled in these settings when preparing for a production release. Google Play requires AABs rather than standard APKs. This module handles the logic of splitting the assets into the correct format for Google’s dynamic delivery system.