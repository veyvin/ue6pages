---
layout: default
title: AndroidAdvertising
---

<!-- ai-generation-failed -->

<h1>AndroidAdvertising</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Advertising/Android/AndroidAdvertising/AndroidAdvertising.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Advertising, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Engine Advertising interface for the Android platform. While the generic Advertising module provides the high-level API, AndroidAdvertising contains the actual JNI (Java Native Interface) logic required to bridge Unreal Engine with Google Play Services and AdMob.

It handles the communication between the C++ engine code and the Android Java SDK to initialize ads, request banners or interstitials, and manage callback events from the Google servers.

Practical Usage Tips and Best Practices
1. Conditional Module Inclusion

To prevent build errors when compiling for other platforms (like Windows or iOS), you must conditionally include this module in your project’s Build.cs.

C#
	if (Target.Platform == UnrealTargetPlatform.Android)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "AndroidAdvertising", "OnlineSubsystemGooglePlay" });

	}

	```

	 

	#### 2. Enable Google Play Support in Project Settings

	Simply adding the module is not enough. You must go to **Project Settings > Platforms > Android > Google Play Services** and check **"Enable Google Play Support"**. Without this toggle, the `AndroidAdvertising` module will not be able to initialize the underlying Google SDKs.

	 

	#### 3. Required "Billing" Permission

	Even for free ads, the Google Play Services integration often requires the billing permission to function correctly with certain AdMob features. Add `com.android.vending.BILLING` to the **Extra Permissions** array in **Project Settings > Android > Advanced APKPackaging**.

	 

	#### 4. Manage Ad Unit ID Arrays

	Unreal Engine uses an array system for Ad IDs. In your Android Project Settings, you can define multiple Ad Mob Ad Unit IDs. When calling `ShowAdBanner(Index)`, the index corresponds to the element in this array. 

	*   **Tip:** Use Index `0` for Banners and Index `1` for Interstitials to keep your code organized.

	 

	#### 5. Always Use AdMob Test IDs

	During development, **never** use your real Ad Unit IDs. Clicking your own live ads—even accidentally—can lead to a permanent ban of your AdMob account. 

	*   **Best Practice:** Hardcode a "Debug/Test" ID mode in your C++ logic that uses Google’s universal test IDs (e.g., `ca-app-pub-3940256099942544/6300978111` for banners) unless the build is a `Shipping` build.

	 

	#### 6. Handle "Back" Button Behavior

	On Android, users expect the "Back" button to close interstitials. Ensure your UI logic doesn't conflict with the AdMob overlay. When an interstitial is active, the `AndroidAdvertising` module takes focus; once closed, ensure your game resumes its pause state or menu correctly.

	 

	#### 7. Verification of Provider Availability

	Since `AndroidAdvertising` is a concrete implementation of `IAdvertisingProvider`, always verify it was successfully loaded before calling it in C++. This avoids null pointer crashes if Google Play Services fail to initialize on a specific device.

	 

	---

	 

	### C++ Integration Example

	 

	The module is rarely accessed directly; instead, it registers itself as the default provider for the Android platform.

	 

	```cpp

	#include "IAdvertisingModule.h"

	#include "Interfaces/IAdvertisingProvider.h"

	 

	void AMyHUD::TriggerAndroidBanner()

	{

	#if PLATFORM_ANDROID

	    // Get the module

	    IAdvertisingModule& AdModule = IAdvertisingModule::Get();

	    

	    // This will return the AndroidAdvertising provider on Android devices

	    TSharedPtr<IAdvertisingProvider> AdProvider = AdModule.GetDefaultProvider();

	 

	    if (AdProvider.IsValid())

	    {

	        // Index 0 as defined in Project Settings -> Android

	        AdProvider->ShowAdBanner(0); 

	    }

	#endif

	}

	```

	 

	### Performance & Packaging

	*   **Proguard/R8:** If you use custom Proguard rules for your Android build, ensure you do not "obfuscate" the AdMob or Google Play classes, as this will cause the `AndroidAdvertising` module to crash at runtime when it fails to find the Java classes via JNI.

	*   **Multi-Dex:** Including advertising SDKs significantly increases the method count of your Android app. Ensure **"Enable Multi-Dex"** is checked in your Android Project Settings to avoid the 64k method limit error.
Copy code
2. Enable Google Play Support

Simply adding the module code is not enough. You must navigate to Project Settings > Platforms > Android > Google Play Services and check “Enable Google Play Support”. Without this toggle, the module will not be able to find the necessary Google libraries, and ad calls will fail silently.

3. Use Test Ad Unit IDs

During the development and testing phase, never use your real Ad Unit IDs from the AdMob console. Clicking your own live ads—even by accident—can lead to an account “elimination” by Google due to invalid traffic. Always use the universal Google test IDs (e.g., ca-app-pub-3940256099942544/6300978111 for banners) until you are ready for a Shipping build.

4. Configure Ad Unit Arrays

In the Android Project Settings, you define an array of Ad Mob Ad Unit IDs. The Show Ad Banner or Show Interstitial Ad functions reference these by index.

Best Practice: Keep a consistent index convention (e.g., Index 0 is always your main Banner, Index 1 is your Interstitial) to avoid showing the wrong ad type.
5. Handle the Billing Permission

Even if your ads are free, the Google Play Services library often requires the billing permission to function correctly with certain ad features. Add com.android.vending.BILLING to the Extra Permissions array in Project Settings > Android > Advanced APKPackaging.

6. Safe Zone Awareness

Android devices vary wildly in screen shapes and notches. Use the Safe Zone widget in UMG to ensure your ad banners do not overlap critical game UI. Note that the AndroidAdvertising module places banners at either the top or bottom of the screen; ensure your UI logic accounts for this screen real estate “elimination.”

7. Proguard and R8 Configuration

If you use Proguard or R8 for code shrinking in your Android builds, you must ensure the AdMob and Google Play Services classes are not obfuscated. If the Java classes are renamed during the build process, the C++ AndroidAdvertising module will fail to find them via JNI, causing the app to crash when an ad is requested.

C++ Usage Snippet

To trigger an ad on Android via C++, you typically use the IAdvertisingModule interface, which will automatically use the AndroidAdvertising provider on Android devices.

C++
	#include "IAdvertisingModule.h"

	#include "Interfaces/IAdvertisingProvider.h"

	 

	void AMyPlayerController::TriggerBannerAd()

	{

	#if PLATFORM_ANDROID

	    IAdvertisingModule& AdModule = IAdvertisingModule::Get();

	    TSharedPtr<IAdvertisingProvider> AdProvider = AdModule.GetDefaultProvider();

	 

	    if (AdProvider.IsValid())

	    {

	        // Index 0 as defined in Android Project Settings

	        AdProvider->ShowAdBanner(0); 

	    }

	#endif

	}
Copy code
Performance & Debugging
Logcat Monitoring: Use adb logcat -s UE5 while your device is connected to see JNI calls and any errors returned by the Google Play SDK.
Multi-Dex Support: Including AdMob adds a significant number of methods to your DEX file. If your build fails with a “64k method limit” error, enable Multi-Dex in the Android Project Settings.
Network Timeouts: The module handles requests asynchronously. If an ad fails to load due to no internet, the provider will trigger a failure delegate; use this to hide the ad slot so it doesn’t appear as a black bar.