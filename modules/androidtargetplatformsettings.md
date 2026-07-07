---
layout: default
title: AndroidTargetPlatformSettings
---


<h1>AndroidTargetPlatformSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Android/AndroidTargetPlatformSettings/AndroidTargetPlatformSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, Engine, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

hat defines the configuration data structures and properties for the Android platform. It provides the back-end logic and property definitions that populate the Project Settings > Platforms > Android menu.

While the AndroidRuntimeSettings module defines how settings behave at runtime (stored in UAndroidRuntimeSettings), the AndroidTargetPlatformSettings module acts as the bridge between the Unreal Editor’s user interface and the underlying build system (UBT), ensuring that your Android-specific configurations are correctly serialized and passed to the packaging tools.

Practical Usage Tips and Best Practices
1. Access Settings via C++

You can programmatically read or modify Android project settings by accessing the UAndroidRuntimeSettings object. This is useful for build automation scripts or custom editor tools that need to verify configuration before a build starts.

C++
	#include "AndroidRuntimeSettings.h"

	 

	// Retrieve the current Android settings

	const UAndroidRuntimeSettings* Settings = GetDefault<UAndroidRuntimeSettings>();

	 

	if (Settings->bBuildForArm64)

	{

	    UE_LOG(LogTemp, Log, TEXT("Project is configured for Arm64 builds."));

	}

	```

	*Note: Ensure you include the `AndroidRuntimeSettings` module in your `.Build.cs` (Editor-only logic recommended).*

	 

	#### 2. Standardize SDK/NDK Versions for Teams

	The module manages the `SDKConfig` section. To ensure consistent builds across a team, avoid using "latest" in the SDK/NDK fields.

	*   **Best Practice:** Specify exact API levels (e.g., NDK `25.1.8937393` and SDK `34`) in the settings. This prevents the "it builds on my machine" problem when different developers have different Android Studio versions installed.

	 

	#### 3. Use Manifest Additions for Native Integration

	Instead of manually editing the `AndroidManifest.xml` (which is overwritten during builds), use the **Extra Settings for <application> section** provided by this module.

	*   **Tip:** If you are integrating a third-party SDK (like an ad network or custom hardware API), add the required `<meta-data>` or `<activity>` tags directly in the Project Settings. This keeps your configuration source-controlled within the `.ini` files.

	 

	#### 4. Leverage "Configure Now" for New Projects

	When first setting up Android, the module displays a "Project is not configured for the Android platform" warning.

	*   **Best Practice:** Always click the **Configure Now** button. This does more than just clear the warning; it generates the necessary directory structure in `Build/Android/` and populates the default `proguard-project.txt` and permission files required for a valid APK.

	 

	#### 5. Optimization: Architecture Selection

	The module allows you to toggle `Support armv7` and `Support arm64`. 

	*   **Best Practice:** For modern projects (Google Play Requirement), enable **Support arm64** and disable **Support armv7**. This significantly reduces the size of your final `.aab` (Android App Bundle) and speeds up the packaging process by eliminating the need to compile the engine twice.

	 

	#### 6. Manage Distribution Signing Securely

	The module provides fields for the Key Store, Alias, and Passwords.

	*   **Security Tip:** Do not check your `.keystore` password into a public repository. The module stores these in `DefaultEngine.ini`. For professional projects, leave the password fields blank in the UI and provide them via Environment Variables or a build-machine-specific `OptionalAndroidRuntimeSettings.ini` that is excluded from source control.

	 

	#### 7. Control Render Surface Settings

	Within the settings, you can toggle "Render to offscreen surface."

	*   **Tip:** Only enable this if you specifically need UMG background blur or specialized post-processing effects that require an offscreen buffer. Disabling this allows the engine to render directly to the backbuffer, which provides a measurable performance boost and reduced latency on lower-end Android devices.

	 

	#### 8. Use Turnkey for Automated Setup

	This module interacts with Unreal's **Turnkey** system to validate your environment.

	*   **Best Practice:** Use the **Platforms > SDK Management > Android > Install SDK** flow. The module uses this data to automatically populate the SDK/NDK/JDK paths, ensuring that the editor is perfectly synced with the versions verified by Epic for your specific engine release.
Copy code

Note: Ensure you include the AndroidRuntimeSettings module in your .Build.cs (Editor-only logic recommended).

2. Standardize SDK/NDK Versions for Teams

The module manages the SDKConfig section. To ensure consistent builds across a team, avoid using “latest” in the SDK/NDK fields.

Best Practice: Specify exact API levels (e.g., NDK 25.1.8937393 and SDK 34) in the settings. This prevents the “it builds on my machine” problem when different developers have different Android Studio versions installed.
3. Use Manifest Additions for Native Integration

Instead of manually editing the AndroidManifest.xml (which is overwritten during builds), use the Extra Settings for <application> section provided by this module.

Tip: If you are integrating a third-party SDK (like an ad network or custom hardware API), add the required <meta-data> or <activity> tags directly in the Project Settings. This keeps your configuration source-controlled within the .ini files.
4. Leverage “Configure Now” for New Projects

When first setting up Android, the module displays a “Project is not configured for the Android platform” warning.

Best Practice: Always click the Configure Now button. This does more than just clear the warning; it generates the necessary directory structure in Build/Android/ and populates the default proguard-project.txt and permission files required for a valid APK.
5. Optimization: Architecture Selection

The module allows you to toggle Support armv7 and Support arm64.

Best Practice: For modern projects (Google Play Requirement), enable Support arm64 and disable Support armv7. This significantly reduces the size of your final .aab (Android App Bundle) and speeds up the packaging process by eliminating the need to compile the engine twice.
6. Manage Distribution Signing Securely

The module provides fields for the Key Store, Alias, and Passwords.

Security Tip: Do not check your .keystore password into a public repository. The module stores these in DefaultEngine.ini. For professional projects, leave the password fields blank in the UI and provide them via Environment Variables or a build-machine-specific OptionalAndroidRuntimeSettings.ini that is excluded from source control.
7. Control Render Surface Settings

Within the settings, you can toggle “Render to offscreen surface.”

Tip: Only enable this if you specifically need UMG background blur or specialized post-processing effects that require an offscreen buffer. Disabling this allows the engine to render directly to the backbuffer, which provides a measurable performance boost and reduced latency on lower-end Android devices.
8. Use Turnkey for Automated Setup

This module interacts with Unreal’s Turnkey system to validate your environment.

Best Practice: Use the Platforms > SDK Management > Android > Install SDK flow. The module uses this data to automatically populate the SDK/NDK/JDK paths, ensuring that the editor is perfectly synced with the versions verified by Epic for your specific engine release.