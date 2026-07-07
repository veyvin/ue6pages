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

obile advertisement services into games. It provides a platform-agnostic interface that allows developers to communicate with mobile ad networks (such as AdMob on Android or iAd/StoreKit on iOS) to display banners and interstitial ads without writing platform-specific code for every implementation.

Practical Usage Tips & Best Practices
1. Configure Target.cs for C++ Projects

For C++ projects, simply adding the module to your Build.cs is often insufficient for mobile packaging. You must ensure the platform-specific advertising modules are included in your Target.cs file to ensure the engine links the correct provider:

C#
	if (Target.Platform == UnrealTargetPlatform.Android)

	{

	    ExtraModuleNames.Add("AndroidAdvertising");

	}
Copy code
2. Use Built-in Blueprint Nodes

For most standard implementations, avoid manual C++ calls and use the high-level Blueprint nodes: Show Ad Banner and Hide Ad Banner. These nodes are globally accessible and handle the communication with the IAdvertisingProvider interface automatically.

3. Manage Banner Visibility and Lifecycle

To optimize screen real estate and prevent performance overhead, only show banners when necessary.

Show Ad Banner during menus or “Game Over” screens.
Hide Ad Banner immediately when entering active gameplay to eliminate UI clutter and prevent accidental clicks during intense action.
4. Verify Google Play Services Configuration

On Android, the Advertising module relies on Google Play Services. In your Project Settings under Platforms > Android, you must:

Enable Google Play Support.
Include your App ID and Ad Unit IDs.
Add com.android.vending.BILLING to the Extra Permissions array if your monetization strategy involves both ads and in-app purchases.
5. Implement Event Dispatchers for Ad Success

If you are using ads to trigger rewards (such as “Revive on Eliminate”), ensure you verify the ad was actually watched. Use the OnUserClosedAd or similar delegates to check the status before granting rewards to prevent players from bypassing the monetization.

6. Test with “Test Ad” IDs

Never use your real Production Ad Unit IDs during development. Both Google and Apple have strict policies against clicking your own ads, which can lead to account suspension. Always use the standard “Test” Unit IDs provided by the ad network documentation until the final release build.

7. Handle Network Connectivity

Ad modules fail silently if there is no internet connection. Before attempting to show an ad, use the Online Subsystem or a simple network check to verify connectivity. If a connection is missing, you should have a fallback UI state so the “Show Ad” button does not appear broken to the user.

8. Respect Safe Zones

Ad banners are often placed at the top or bottom of the screen. Ensure your UMG widgets use Safe Zone anchors so that the ad banner does not overlap critical gameplay elements or UI buttons, which could lead to a poor user experience or “accidental click” violations from ad providers.