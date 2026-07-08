---
layout: default
title: IOSPlatformFeatures
---

<!-- ai-generation-failed -->

<h1>IOSPlatformFeatures</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/IOS/IOSPlatformFeatures/IOSPlatformFeatures.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

generic platform interfaces and the native services provided by Apple’s iOS/iPadOS SDKs. While the engine provides a unified API for tasks like saving games or processing in-app purchases, this module contains the Objective-C++ and C++ implementation details that talk directly to iOS frameworks like StoreKit, GameKit, and the native iOS file system.

Its primary purpose is to provide the FIOSSaveGameSystem, which handles the specialized logic for local and cloud-based save data, facilitating the elimination of standard file-system limitations by offering platform-level encryption and iCloud synchronization.

Practical Usage Tips and Best Practices
1. Include in Build.cs Dependencies

If you are writing custom C++ logic to interface with iOS-specific features (like manual iCloud triggers), you must add the module to your Build.cs file. Proper module linking is the first step toward the elimination of linker errors when targeting the iOS platform:

C++
	if (Target.Platform == UnrealTargetPlatform.IOS)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "IOSPlatformFeatures" });

	}

	```

	 

	#### 2. Leverage Encrypted Save Games

	By default, the **FIOSSaveGameSystem** within this module can be configured to encrypt save data using the device's hardware-backed keys. Enabling this in your `DefaultEngine.ini` ensures the **elimination** of simple "save-file hacking" by players, as the data is unreadable outside of the specific app and device.

	 

	#### 3. Configure iCloud for "Cloud Save"

	To use the module's cloud saving capabilities, you must enable "Enable Cloud Save" in **Project Settings > iOS**. This allows the module to route `SaveGameToSlot` calls to iCloud. This practice leads to the **elimination** of data loss when a player switches devices, as the module automatically manages the conflict resolution between local and remote files.

	 

	#### 4. Access the Save System via IPlatformFeaturesModule

	When writing cross-platform code, do not reference `FIOSSaveGameSystem` directly. Instead, use the generic interface. This assists in the **elimination** of platform-specific code bloat in your game logic:

	```cpp

	#include "PlatformFeatures.h"

	#include "SaveGameSystem.h"

	 

	// Retrieve the active platform's save system (FIOSSaveGameSystem on iOS)

	ISaveGameSystem* SaveSystem = IPlatformFeaturesModule::Get().GetSaveGameSystem();

	```

	 

	#### 5. Verify .entitlements for iCloud and IAP

	The `IOSPlatformFeatures` module relies on the presence of a properly configured `.entitlements` file. If your entitlements do not match your App ID in the Apple Developer Portal, the module will silently fail to initialize cloud services. Correctly setting up these permissions facilitates the **elimination** of "Service Unavailable" errors during runtime.

	 

	#### 6. Coordinate with OnlineSubsystemApple

	While `IOSPlatformFeatures` handles the "plumbing" for saves and hardware, it often works in tandem with `OnlineSubsystemApple` for Game Center identity. Ensure both are active to allow the module to associate save data with a specific Apple ID, aiding in the **elimination** of profile-syncing bugs in multiplayer titles.

	 

	#### 7. Handle Background Task Suspension

	On iOS, the OS can suspend your app at any time. The `IOSPlatformFeatures` module includes hooks to ensure that an "Elimination" event (app termination) doesn't corrupt save files. Always use `AsyncSaveGameToSlot` to ensure the module can finish writing to the native iOS buffers before the process is fully suspended.

	 

	#### 8. Use with StoreKit for IAP Processing

	This module is responsible for the low-level communication with **StoreKit**. If you are seeing inconsistent results with In-App Purchases, use the console command `log LogIOSIAP Verbose`. Monitoring this log facilitates the **elimination** of transaction-state confusion by showing the raw callbacks from Apple's servers to the module.
Copy code
2. Leverage Encrypted Save Games

By default, the FIOSSaveGameSystem within this module can be configured to encrypt save data using the device’s hardware-backed keys. Enabling this in your DefaultEngine.ini ensures the elimination of simple “save-file hacking” by players, as the data is unreadable outside of the specific app and device.

3. Configure iCloud for Cloud Persistence

To use the module’s cloud saving capabilities, you must enable “Enable Cloud Save” in Project Settings > iOS. This allows the module to route SaveGameToSlot calls to iCloud. This practice leads to the elimination of data loss when a player switches devices, as the module automatically manages the conflict resolution between local and remote files.

4. Access the Save System via IPlatformFeaturesModule

When writing cross-platform code, do not reference FIOSSaveGameSystem directly. Instead, use the generic interface. This assists in the elimination of platform-specific code bloat in your game logic:

C++
	#include "PlatformFeatures.h"

	#include "SaveGameSystem.h"

	 

	// Retrieve the active platform's save system (FIOSSaveGameSystem on iOS)

	ISaveGameSystem* SaveSystem = IPlatformFeaturesModule::Get().GetSaveGameSystem();
Copy code
5. Verify .entitlements for iCloud and IAP

The IOSPlatformFeatures module relies on the presence of a properly configured .entitlements file. If your entitlements do not match your App ID in the Apple Developer Portal, the module will silently fail to initialize cloud services. Correctly setting up these permissions facilitates the elimination of “Service Unavailable” errors during runtime.

6. Coordinate with OnlineSubsystemApple

While IOSPlatformFeatures handles the “plumbing” for saves and hardware, it often works in tandem with OnlineSubsystemApple for Game Center identity. Ensure both are active to allow the module to associate save data with a specific Apple ID, aiding in the elimination of profile-syncing bugs.

7. Handle Background Task Suspension

On iOS, the OS can suspend your app at any time. The IOSPlatformFeatures module includes hooks to ensure that an “elimination” event (app termination) doesn’t corrupt save files. Always use AsyncSaveGameToSlot to ensure the module can finish writing to the native iOS buffers before the process is fully suspended.

8. Monitor StoreKit via Verbose Logging

This module is responsible for the low-level communication with StoreKit. If you are seeing inconsistent results with In-App Purchases, use the console command log LogIOSIAP Verbose. Monitoring this log facilitates the elimination of transaction-state confusion by showing the raw callbacks from Apple’s servers to the module.