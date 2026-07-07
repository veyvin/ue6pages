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

al Engine’s abstract Advertising framework for the Android OS. It acts as the bridge between the engine’s generic “Show Ad” commands and the Google Play Services (AdMob) SDK.

This module is responsible for initializing the mobile ad SDK, managing the lifecycle of ad banners and interstitials, and communicating with the Android activity to overlay advertisements on top of the game’s OpenGL or Vulkan surface.

Practical Usage Tips & Best Practices
1. Include in Target.cs

Because this is a platform-specific provider, simply adding it to a Build.cs dependency is not enough for the engine to package it correctly. You must explicitly add it to your project’s .Target.cs file within the Android platform check:

C#
	if (Target.Platform == UnrealTargetPlatform.Android)

	{

	    ExtraModuleNames.Add("AndroidAdvertising");

	    // Often paired with the online subsystem

	    ExtraModuleNames.Add("OnlineSubsystemGooglePlay"); 

	}
Copy code
2. Configure AdMob IDs in Project Settings

Navigate to Project Settings > Platforms > Android > Google Play Services. Here, you must check Enable Google Play Support and populate the Ad Mob Ad Unit IDs array. The order of IDs in this array corresponds to the “Ad Index” used in Blueprint nodes like Show Ad Banner.

3. Handle Permission Requirements

For the ad module to function and communicate with Google’s servers, ensure your Android manifest includes the necessary permissions. In Project Settings > Android, add com.android.vending.BILLING to the Extra Permissions array if you plan to use rewarded ads or in-app purchases alongside the advertising module.

4. Use “Configure Now” for Google Play

The AndroidAdvertising module relies on a properly configured Android environment. If you see a red bar in the Android or Google Play Services section of your Project Settings, click Configure Now. This generates the necessary XML files and folders in your project’s Build/Android directory required for the SDK to initialize.

5. Leverage the Eyedropper for Placement

While the AndroidAdvertising module handles the logic, the visual placement is handled by the engine’s viewport. Use the Show Ad Banner node’s “Show on Bottom” boolean to toggle position. To ensure ads don’t cover critical HUD elements (like an elimination feed), design your UMG layout with a buffer at the top or bottom of the screen.

6. Always Use Test IDs for Development

Google Play Services is highly sensitive to “invalid traffic.” When testing your Android builds, use Google’s dedicated test Ad Unit IDs (e.g., ca-app-pub-3940256099942544/6300978111 for banners). Only swap to your production IDs from the AdMob console right before uploading your .aab to the Google Play Console.

7. Monitor the Logcat for Debugging

If ads are not appearing on your device, use Android Studio’s Logcat or the adb logcat command. Filter for “Ads” or “Unreal” to see specific error codes. Common issues include ERROR_CODE_NO_FILL (meaning the ad network has no ads for your region/app) or ERROR_CODE_NETWORK_ERROR.

8. Graceful Fallbacks for Offline Users

The AndroidAdvertising module cannot fetch data without a connection. Before calling ad functions, check for network availability. This prevents the game from waiting for a timeout and ensures you can provide an alternative UI state, such as a “No Ads Available” message, rather than a broken button.