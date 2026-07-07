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

w Unreal Engine interacts with the Android platform. It implements the ITargetPlatform interface, providing the engine with the necessary logic to cook assets into Android-specific formats (like ASTC textures), deploy builds to devices via ADB (Android Debug Bridge), and manage settings specific to the Android ecosystem.

While this module is strictly for the Editor and Build Tools, it is the fundamental “bridge” that allows Unreal to translate generic project data into a functional Android package (.apk or .aab).

Practical Usage Tips & Best Practices
1. Module Dependency Constraints

The AndroidTargetPlatform module is Editor-only. Never attempt to include it in a runtime/game module. If you are writing a custom build tool or an editor extension, ensure the dependency is wrapped in a target type check in your Build.cs:

C++
	#include "Interfaces/ITargetPlatformManagerModule.h"

	 

	ITargetPlatformManagerModule* TPM = GetMoviePlayer()->GetTargetPlatformManager();

	const ITargetPlatform* AndroidPlatform = TPM->FindTargetPlatform(TEXT("Android"));

	if (AndroidPlatform)

	{

	    // Query platform-specific capabilities here

	}

	```

	 

	#### 3. Leverage Config Rules for Device Filtering

	One of the most powerful features managed via this module's logic is the `configrules.txt` system. Place this file in `Build/Android/` to perform runtime hardware checks. You can set variables based on GPU vendor or memory and then query them in C++:

	```cpp

	#if PLATFORM_ANDROID

	FString GpuVendor = FAndroidMisc::GetConfigRulesVariable(TEXT("SRC_GpuVendor"));

	if (GpuVendor.Contains(TEXT("Adreno"))) { /* Optimize for Adreno */ }

	#endif

	```

	 

	#### 4. Optimize Texture Compression (ASTC)

	The `AndroidTargetPlatform` module handles the texture cooking pipeline. Modern Android development should prioritize **ASTC** (Adaptive Scalable Texture Compression). Ensure your project is configured to cook for ASTC primarily, as it provides the best balance of quality and memory footprint, and is supported by virtually all modern Android devices.

	 

	#### 5. Manage Target SDK and Minimum SDK

	Through the settings exposed by this module in **Project Settings > Android**, always keep your **Target SDK** updated to the latest Google Play requirement (e.g., API 34+). However, keep the **Minimum SDK** as low as your features allow (typically API 26 or 28) to maximize your potential install base.

	 

	#### 6. Use Turnkey for SDK Management

	Instead of manually managing environment variables (`ANDROID_HOME`), use the **Turnkey** system integrated into this module. Clicking "Install SDK" in the Platforms menu triggers the logic within this module to verify your SDK/NDK/JDK versions against the specific requirements of your Unreal Engine version.

	 

	#### 7. Multi-ABI Packaging

	For production, use the module's settings to package for **arm64-v8a**. While 32-bit (armeabi-v7a) support is still available, Google Play requires 64-bit support. Disabling 32-bit in your project settings will significantly reduce your final APK/AAB size and speed up the cooking process.

	 

	#### 8. Debugging via "Cook on the Fly"

	If you are iterating rapidly on UI or materials, use the **Cook on the Fly** server. This module facilitates the communication between the Editor and the Android device, allowing the device to request only the assets it needs over the network, bypassing the long "Package and Install" cycle.
Copy code
2. Leverage Config Rules for Hardware Filtering

One of the most powerful features managed by this module’s logic is the configrules.txt system. By placing this file in Build/Android/, you can define variables based on the device’s GPU, memory, or CPU and query them in C++ at runtime. This allows you to eliminate performance bottlenecks by disabling heavy features on low-end devices.

C++
	#if PLATFORM_ANDROID

	FString GpuVendor = FAndroidMisc::GetConfigRulesVariable(TEXT("SRC_GpuVendor"));

	if (GpuVendor.Contains(TEXT("Mali"))) { /* Apply Mali-specific optimization */ }

	#endif
Copy code
3. Optimize Texture Compression (ASTC)

The module handles the texture cooking pipeline. Modern Android development should prioritize ASTC (Adaptive Scalable Texture Compression). It provides the best balance of quality and file size. In your Project Settings, ensure you are cooking for ASTC to ensure compatibility with virtually all modern Android hardware.

4. Manage Multi-ABI Packaging

Through the settings exposed by this module, you can control which architectures to support. While 32-bit (armeabi-v7a) is still available, Google Play requires 64-bit (arm64-v8a) support. Disabling 32-bit in your project settings will significantly reduce your final build size and speed up the cooking process.

5. Use Turnkey for Automated Setup

Instead of manually configuring environment variables like ANDROID_HOME or JAVA_HOME, use the Turnkey system (found under Platforms > Android > Install SDK). This module utilizes Turnkey to verify that your SDK, NDK, and JDK versions match the specific requirements of the Unreal Engine version you are using.

6. Access Platform Settings Programmatically

If you need to query Android platform settings within an Editor utility, use the ITargetPlatformManagerModule to find the Android target without hard-linking the module:

C++
	ITargetPlatformManagerModule* TPM = GetMoviePlayer()->GetTargetPlatformManager();

	const ITargetPlatform* AndroidPlatform = TPM->FindTargetPlatform(TEXT("Android"));
Copy code
7. Utilize “Cook on the Fly” for Rapid Iteration

The AndroidTargetPlatform module facilitates the Cook on the Fly server. This allows an Android device to request assets directly from your PC over the network as they are needed, rather than requiring a full package and install cycle. This is a best practice for iterating on UI or materials.

8. Respect Target and Minimum SDK Levels

Always keep your Target SDK updated to the latest Google Play requirement (e.g., API 34+). However, keep your Minimum SDK as low as your features allow (typically API 26 or 28) to maximize your potential install base and prevent the elimination of older devices from your supported list.