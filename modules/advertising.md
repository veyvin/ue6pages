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

ate mobile advertisements into your project. It acts as an abstraction layer between the engine and platform-specific SDKs, such as Google AdMob for Android and various providers for iOS.

What it is and What it’s used for

The module provides a unified interface to trigger ad banners and interstitial ads without requiring the developer to write native JNI (Android) or Objective-C (iOS) code. It is primarily used for:

Monetization: Displaying banner ads at the top or bottom of the screen.
Interstitials: Showing full-screen ads during natural breaks in gameplay (e.g., between levels).
Revenue Generation: Integrating ad unit IDs directly from provider dashboards into the engine configuration.
Practical Usage Tips and Best Practices
1. Implement Platform-Specific Dependencies

The Advertising module is a wrapper and requires the actual platform modules to function. In your C++ project’s .Build.cs file, ensure you include the necessary modules conditionally so they do not affect non-mobile builds:

C++
	// In YourProject.Build.cs

	if (Target.Platform == UnrealTargetPlatform.Android || Target.Platform == UnrealTargetPlatform.IOS)

	{

	    PrivateDependencyModuleNames.Add("Advertising");

	}

	```

	 

	#### 2. Verify Provider Availability

	Before calling ad functions in C++, always ensure a provider is actually loaded. The engine might fail to initialize the ad SDK due to missing config or network issues. Use the `IAdvertisingModule` interface to check the default provider.

	 

	```cpp

	#include "IAdvertisingModule.h"

	#include "Interfaces/IAdvertisingProvider.h"

	 

	IAdvertisingProvider* AdProvider = IAdvertisingModule::Get().GetDefaultProvider();

	if (AdProvider)

	{

	    AdProvider->ShowAdBanner(0, true); // Show first ad unit at bottom

	}

	```

	 

	#### 3. Account for UI Layout "Dead Zones"

	A common mistake is forgetting that `Show Ad Banner` **does not resize the game viewport**. The ad banner is drawn as an overlay on top of your Slate/UMG UI. 

	*   **Best Practice:** Design your mobile UI with "Safe Zones" at the top and bottom. If a banner is active, shift your HUD elements or menus so they aren't obscured by the advertisement.

	 

	#### 4. Manage Banner Lifecycle

	Avoid leaving banners active during intense gameplay or narrative cutscenes where they might distract the player or cause accidental clicks.

	*   **Tip:** Use the `Hide Ad Banner` node (or `AdProvider->HideAdBanner()`) when entering gameplay and only show it in menus, "Game Over" screens, or victory transitions.

	 

	#### 5. Use Test Ad IDs During Development

	Never use your real Production Ad Unit IDs while testing your game in the editor or on a device. Google and Apple are strict about "Invalid Click" activity, and self-clicking your ads can lead to account suspension.

	*   **Best Practice:** Use the standard Google/Apple test IDs until the final release build.

	 

	#### 6. Handle Multiple Ad Unit IDs

	The Project Settings (Platforms > Android/iOS) allow you to define an array of Ad Unit IDs. 

	*   **Tip:** Use index `0` for your main banner, index `1` for secondary ads, etc. In code/Blueprints, the `Ad ID Index` parameter refers directly to the order in these arrays. This allows you to switch between different ad providers or campaigns easily.

	 

	#### 7. Combine with OnlineSubsystem

	For a professional implementation, the Advertising module should work alongside the `OnlineSubsystem`. For example, use the Online Subsystem to check if a player has purchased a "Remove Ads" IAP (In-App Purchase). If the purchase is verified, ensure your logic globally disables all `ShowAdBanner` calls.

	 

	#### 8. Debug via Device Logs

	The Advertising module provides very little feedback in the Unreal Editor since the actual SDKs (AdMob/AppLovin) only run on mobile hardware. 

	*   **Best Practice:** Use `adb logcat` (Android) or the Xcode console (iOS) and filter for "Ads" or "Unreal" to see why an ad might fail to load (e.g., "No Fill," "Invalid Configuration," or "Network Timeout").
Copy code
2. Use Test Ad Unit IDs During Development

Always use the dedicated test IDs provided by AdMob or your chosen provider during the development phase. Never use production IDs while testing on your own devices, as clicking your own ads can lead to account suspension for “invalid activity.”

3. Respect the UI Safe Zones

Ad banners are overlaid on top of the game viewport and do not automatically resize your UI. Design your UMG widgets with flexible anchors or “Safe Zones” so that critical gameplay buttons or HUD elements are not obscured when a banner is called via the Show Ad Banner node.

4. Manage the Ad Lifecycle

Banners consume screen real estate and processing power. Use the Hide Ad Banner node to eliminate the ad display during intensive gameplay or cinematic sequences. Only call Show Ad Banner during menus, shop screens, or pause states to improve the player experience and performance.

5. Verify Provider Availability

Before attempting to show an ad in C++, always verify that the advertising provider is valid. Access the module via IAdvertisingModule::Get().GetDefaultProvider() and perform a null check. This prevents crashes if the SDK fails to initialize due to a lack of internet connectivity.

6. Toggle Ads via Player State

If you offer a “Remove Ads” In-App Purchase (IAP), store a boolean variable in your SaveGame or PlayerState. Wrap your advertisement logic in a branch that checks this variable before calling any display functions to ensure paying users are not bothered by ads.

7. Design for Interstitial Timing

Interstitial ads should only be shown during “natural” pauses, such as after a character is eliminated or when transitioning between levels. Sudden full-screen ads during active movement can frustrate players and lead to poor app store ratings.

8. Monitor Performance and “No-Fill” Events

Advertisements rely on network calls that can fail. Ensure your game logic does not “hang” while waiting for an ad to load. Use the built-in system events to detect if an ad failed to load (a “No-Fill” event) so you can gracefully skip the ad and let the player continue.