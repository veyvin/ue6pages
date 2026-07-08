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

n of the Unreal Engine Advertising interface for the Android OS. It acts as the bridge between the engine’s generic advertising commands and the Google Play Services (AdMob) SDK.

What it is and What it’s used for

This module handles the low-level communication between Unreal Engine and the Android system to serve advertisements. It translates high-level Blueprint or C++ calls—such as showing a banner or an interstitial—into the specific JNI (Java Native Interface) calls required by the Android environment.

Primary uses include:

AdMob Integration: The default way to display Google-powered ads on Android devices.
Banner Management: Positioning and displaying persistent ads at the top or bottom of the mobile screen.
Interstitial Control: Managing full-screen ads that appear during gameplay transitions.
Ad Unit ID Mapping: Linking the unique strings provided by the AdMob console to the engine’s runtime.
Practical Usage Tips and Best Practices
1. Conditional Build Configuration

Since this module contains Android-specific code, it should only be loaded when targeting that platform. In your project’s *.Target.cs or *.Build.cs file, wrap the module dependency in a platform check to prevent compilation errors for Windows or iOS:

C#
	if (Target.Platform == UnrealTargetPlatform.Android)

	{

	    ExtraModuleNames.Add("AndroidAdvertising");

	}
Copy code
2. Configure Google Play Services

The module will not function unless Enable Google Play Support is checked in the Project Settings > Platforms > Android section. You must also enter your AdMob App ID and the specific Ad Unit IDs for banners and interstitials in the Google Play Services section for the module to initialize correctly.

3. Request Billing Permissions

To ensure the advertising ecosystem functions fully within the Android lifecycle, add com.android.vending.BILLING to the Extra Permissions array in the Advanced APKPackaging section of your Android Project Settings. This is often required for modern ad-driven monetization pipelines.

4. Handle Ad Overlays in UI Design

Android banners are rendered as an overlay on the game surface. Unlike some UI elements, they do not push the game viewport up. You must manually ensure that your UMG buttons and health bars are anchored away from the banner position (Top or Bottom) to prevent them from being obscured.

5. Use the “Show Ad Banner” Node

For most use cases, you do not need to call the module directly in C++. Once the module is configured in the Project Settings, you can use the standard Show Ad Banner Blueprint node. The Index pin corresponds to the order of Ad Unit IDs you entered in your Android Project Settings.

6. Strategize Interstitial Timing

Interstitials managed by this module take over the entire screen and pause the game’s rendering thread. Only trigger these when a player is in a safe state, such as after they have been eliminated or when they are navigating between levels, to avoid crashing the user experience during active play.

7. Verify Internet Connectivity

The AndroidAdvertising module requires a network connection to fetch ad content. Before calling an ad function, use the Is Network Available check. If a player is offline, your logic should gracefully skip the ad call to eliminate potential timeouts or lag spikes in the UI.

8. Monitor via Logcat

When debugging ad issues on a physical device, use Android Logcat (available in the Output Log or via command line). Filter for “Ads” or “Unreal” to see the specific error codes returned by the Google Play Services SDK if an ad fails to load, such as ERROR_CODE_NO_FILL.