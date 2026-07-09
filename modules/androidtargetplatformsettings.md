---
layout: default
title: AndroidTargetPlatformSettings
---

<!-- ai-generation-failed -->

<h1>AndroidTargetPlatformSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Android/AndroidTargetPlatformSettings/AndroidTargetPlatformSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, Engine, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

for managing the configuration, validation, and UI representation of Android-specific project settings. It serves as the bridge between the Unreal Engine Editor and the underlying .ini configuration files (specifically DefaultEngine.ini) that define how an Android application is built, packaged, and signed.

This module provides the logic for the Platforms > Android section in the Project Settings, handling everything from SDK/NDK path validation to the generation of the AndroidManifest.xml and Proguard rules.

Practical Usage Tips and Best Practices
Access Settings via C++ for Automation
If you are building custom editor tools or build scripts, you can access the Android settings directly via the UAndroidRuntimeSettings class. This is useful for programmatically updating version codes or package names before a build.
C++
	// Required Module: AndroidTargetPlatformSettings

	#include "AndroidRuntimeSettings.h"

	 

	 

	UAndroidRuntimeSettings* Settings = GetMutableDefault<UAndroidRuntimeSettings>();

	Settings->VersionDisplayName = TEXT("1.0.5");

	Settings->SaveConfig();
Copy code
Validate SDK/NDK via Turnkey Integration
The module interfaces with Unreal Turnkey. Always use the “Platforms > SDK Management” menu to let this module verify your environment. If the module cannot find the correct paths, it will “eliminate” your ability to package, even if the files exist on disk.
Utilize “Extra Tags” for Manifest Customization
Instead of manually editing the AndroidManifest.xml (which the engine overwrites), use the Advanced APK Packaging section provided by this module. You can add “Extra Tags for <application>” or “Extra Permissions” directly in the UI to ensure they are correctly injected during the build process.
Use Per-Project SDK Overrides
If you are working on multiple projects that require different NDK versions (e.g., one project requires a specific Vulkan feature), use the Project SDK Override section. This allows this module to point to a specific NDK path for one project without affecting your global system environment variables.
Configure Distribution Signing Early
The module provides fields for Keystore files and aliases. It is a best practice to set these up in a protected Local/ or Secure/ folder. Ensure the “For Distribution” checkbox is managed correctly; failing to do so will result in an APK that the Google Play Store will “eliminate” during the upload process.
Optimize Architecture Stripping
In the settings managed by this module, you can toggle support for arm64-v8a and x86_64. To reduce build times and package size during development, disable architectures you aren’t currently testing on. Only enable both when preparing the final shipping “elimination” of bugs for production.
Manage Texture Compression Formats
This module determines which texture formats (ETC2, ASTC, DXTC) are included in your Android build. For modern devices, prioritize ASTC. You can use the “Build” settings to “eliminate” unneeded formats, significantly reducing the final size of the .obb or App Bundle.
Handle Permissions via Module Logic
The module allows you to toggle “Enable Remote Notifications” and “Enable Cloud Messaging.” When these are checked, the module automatically adds the necessary library dependencies and manifest requirements. Always check these toggles here first before attempting to manually add Android libraries to your Build.cs.