---
layout: default
title: Advertising
---

<!-- ai-generation-failed -->

<h1>Advertising</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Advertising/Advertising/Advertising.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

r integrating mobile advertisements—primarily banner ads and full-screen interstitials—into your project. It abstracts platform-specific SDKs (like AdMob for Android or iAd/AdMob for iOS) into a unified C++ and Blueprint API, allowing you to monetize mobile games with minimal platform-specific branching.

Practical Usage Tips and Best Practices
1. Implement Platform-Specific Build Dependencies

The Advertising module is only functional on mobile platforms. To avoid linker errors on Windows or Mac builds, wrap the module dependency in your Build.cs file with a platform check:

C#
	if (Target.Platform == UnrealTargetPlatform.Android || Target.Platform == UnrealTargetPlatform.IOS)

	{

	    PublicDependencyModuleNames.Add("Advertising");

	}

	```

	 

	#### 2. Manage the Ad Lifecycle with UI

	Do not leave ad banners active during gameplay unless your UI is specifically designed for it. Banners can overlap critical HUD elements or touch controls. Always call `HideAdBanner()` when transitioning from menus to active gameplay or cinematic sequences.

	 

	#### 3. Handle Provider Availability

	Before attempting to show an ad, verify that a valid provider exists. Not all regions or devices will have active ad services. Use `IAdvertisingModule::Get().GetDefaultProvider()` and check for null before calling methods.

	 

	#### 4. Optimize Z-Order and Safe Zones

	Ad banners are often rendered as a native overlay on top of the Unreal viewport. Ensure your UMG layout accounts for the "Safe Zone" at the top or bottom of the screen to prevent the ad from covering important buttons, especially on devices with notches (like iPhone).

	 

	#### 5. Respect User Privacy (GDPR/CCPA)

	The advertising module itself is a bridge. You are still responsible for ensuring you have obtained user consent before initializing the ad provider if you are targeting regions with strict privacy laws. You may need to delay ad initialization until the user accepts your privacy policy.

	 

	#### 6. Use Interstitials for Natural Breaks

	Save interstitial (full-screen) ads for natural "down-time" in the loop, such as between levels or after a player dies. Showing an interstitial unexpectedly during active play is a leading cause of negative user reviews and uninstalls.

	 

	#### 7. Test with "Test Mode" IDs

	Never use your real AdMob Ad Unit IDs during development. Google and Apple may ban your account if they detect "invalid clicks" from your own development devices. Use the standard Test IDs provided in the AdMob documentation until you are ready for a production release.

	 

	#### 8. Monitor Memory and Latency

	Loading ads, especially video interstitials, can cause a brief hitch on lower-end mobile devices. Pre-load your ads during a loading screen or a period of low CPU activity to ensure the transition to the ad is seamless.

	 

	---

	 

	### C++ Implementation Example

	 

	To interact with the advertising system in C++, you must access the `IAdvertisingModule` and its provider interface.

	 

	**Required Headers:**

	```cpp

	#include "Advertising.h"

	#include "IAdvertisingModule.h"

	#include "Interfaces/IAdvertisingProvider.h"

	```

	 

	**Implementation Logic:**

	```cpp

	void UMyAdManager::ShowBannerAd()

	{

	    // 1. Get the Advertising Module

	    IAdvertisingModule& AdModule = IAdvertisingModule::Get();

	 

	    // 2. Access the platform-default provider (e.g., AdMob)

	    TSharedPtr<IAdvertisingProvider> AdProvider = AdModule.GetDefaultProvider();

	 

	    if (AdProvider.IsValid())

	    {

	        // 3. Show the banner at the bottom (index 1 usually denotes bottom)

	        // Note: The specific integer meaning can vary by provider implementation

	        const int32 AdShowBottom = 1;

	        AdProvider->ShowAdBanner(AdShowBottom);

	        

	        UE_LOG(LogTemp, Log, TEXT("Ad Provider found. Requesting Banner."));

	    }

	    else

	    {

	        UE_LOG(LogTemp, Warning, TEXT("No valid Advertising Provider found for this platform."));

	    }

	}

	 

	void UMyAdManager::HideBannerAd()

	{

	    TSharedPtr<IAdvertisingProvider> AdProvider = IAdvertisingModule::Get().GetDefaultProvider();

	    if (AdProvider.IsValid())

	    {

	        AdProvider->HideAdBanner();

	    }

	}

	```

	 

	### Debugging & Tools

	*   **Logcat (Android) / Console (iOS):** Look for tags like `Ads` or `GMA` (Google Mobile Ads) to see why an ad failed to load (e.g., "No Fill").

	*   **Project Settings:** Ensure `Enable Google Play Support` is checked under **Platforms > Android** for AdMob to function.

	*   **Build Logs:** Verify that the `AndroidAdvertising` or `IOSAdvertising` plugins are being correctly packaged during the build process.
Copy code
2. Manage Ad Visibility via UI Lifecycle

Do not allow ads to persist during active gameplay unless the UI is specifically designed for it. Always call Hide Ad Banner during transitions from menus to gameplay. Failure to hide ads can lead to accidental clicks, which may result in account “elimination” from ad providers due to suspected fraud.

3. Account for Safe Zones and Notches

Ad banners are typically native overlays that sit on top of the Unreal viewport. Ensure your UMG layouts utilize Safe Zone widgets so that critical game buttons or health bars are not obscured by the ad banner, especially on devices with camera notches.

4. Use Interstitials for Natural Breaks

Save full-screen (interstitial) ads for natural pauses in the game loop, such as moving between levels or after a player elimination. Avoid showing these during active interaction, as it creates a poor user experience and high bounce rates.

5. Verify Provider Validity

In C++, always check if the default advertising provider is valid before attempting to call functions. Not all devices or regions will have a provider initialized.

C++
	IAdvertisingModule& AdModule = IAdvertisingModule::Get();

	TSharedPtr<IAdvertisingProvider> Provider = AdModule.GetDefaultProvider();

	if (Provider.IsValid()) { /* Show Ad */ }
Copy code
6. Use Test Ad Unit IDs During Development

Never use your production Ad Unit IDs while testing in the editor or on dev devices. Repeatedly loading and clicking your own live ads can lead to your account being flagged. Use the generic Test IDs provided by Google AdMob or Apple during the implementation phase.

7. Handle Network Connectivity Gracefully

Mobile users often have intermittent internet. Use the advertising delegates to detect if an ad failed to load. If an ad fails, ensure your UI doesn’t leave a blank gap where the banner was expected, and avoid spamming the “Show” request immediately.

C++ Implementation Recipe

To interact with ads in code, you must include the module headers and access the singleton provider.

Header Includes:

C++
	#include "Interfaces/IAdvertisingProvider.h"

	#include "IAdvertisingModule.h"
Copy code

Implementation Logic:

C++
	void UMyGameInstance::ShowBanner()

	{

	    // Access the module singleton

	    IAdvertisingModule& AdModule = IAdvertisingModule::Get();

	    

	    // Get the platform-specific provider (AdMob, etc.)

	    TSharedPtr<IAdvertisingProvider> AdProvider = AdModule.GetDefaultProvider();

	 

	    if (AdProvider.IsValid())

	    {

	        // Parameter 1 usually defines the ad index/location

	        AdProvider->ShowAdBanner(0);

	        UE_LOG(LogTemp, Log, TEXT("Ad Banner Requested."));

	    }

	}

	 

	void UMyGameInstance::HideBanner()

	{

	    TSharedPtr<IAdvertisingProvider> AdProvider = IAdvertisingModule::Get().GetDefaultProvider();

	    if (AdProvider.IsValid())

	    {

	        AdProvider->HideAdBanner();

	    }

	}
Copy code
Performance & Optimization
Avoid Tick: Never check for ad status inside a Tick function. Use Event Dispatchers or Delegates to respond to ad-loading success or failure.
Memory Management: The advertising module uses TSharedPtr for providers; ensure you are not creating circular references if you store the provider pointer in a custom class.
Asset Footprint: Be aware that including advertising SDKs via this module will increase your final APK/IPA package size.