---
layout: default
title: IOSAdvertising
---

<!-- ai-generation-failed -->

<h1>IOSAdvertising</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Advertising/IOS/IOSAdvertising/IOSAdvertising.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Advertising, ApplicationCore, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

engine’s generic advertising interface to Apple’s native iOS advertising frameworks. While historically rooted in the now-deprecated iAd service, it currently serves as the backend for displaying ad banners and handling the mandatory App Tracking Transparency (ATT) workflow required by Apple for any app that uses an advertising identifier (IDFA).

Practical Usage Tips & Best Practices
1. Configure Build.cs Dependencies Correctly

To use the advertising interface in C++, you must include the module in your build script. Since it is platform-specific, it should be wrapped in a target platform check.

Best Practice: Add "iosadvertising" to your PublicDependencyModuleNames within an if (Target.Platform == UnrealTargetPlatform.IOS) block. This ensures the elimination of linker errors when compiling for other platforms like Android or Windows.
2. Implement Mandatory App Tracking Transparency (ATT)

Ads will fail to serve—and your app may be rejected—if you do not explicitly request permission to track the user via the ATT prompt.

Tip: Add the NSUserTrackingUsageDescription key to your Additional Plist Data in the iOS Project Settings. Providing a clear explanation for tracking ensures the elimination of ad revenue loss caused by blocked identifiers.
3. Use the Generic Advertising Interface

Rather than calling FIOSAdvertisingModule directly, utilize the engine’s abstracted IAdvertisingProvider interface for better code portability.

Best Practice: Use FAdvertising::Get().ShowAdBanner() in C++ or the Show Ad Banner node in Blueprints. This approach allows for the elimination of platform-specific code in your gameplay logic, as the engine routes calls to the correct module at runtime.
4. Manage Banner Positioning and Safe Zones

Ad banners can overlap critical UI elements, especially on modern devices with notches or home indicators.

Tip: The ShowAdBanner function accepts a boolean for “Show on Bottom.” Always verify your UMG safe zones on an actual device to ensure the elimination of layout overlap between your game’s HUD and the ad banner.
5. Hide Ads During High-Intensity Gameplay

Visible ads can distract players during critical moments, leading to accidental clicks and a poor user experience.

Best Practice: Call HideAdBanner at the start of gameplay levels and only call ShowAdBanner in menus or “Game Over” screens. Proactive management leads to the elimination of accidental clicks that pull the player out of the game.
6. Test with “Limit Ad Tracking” Enabled

Many users disable tracking globally in their iOS system settings, which affects how the module behaves.

Tip: Test your UI flow with “Allow Apps to Request to Track” turned off in the iOS Settings app. Ensuring your game remains stable when the module cannot retrieve an IDFA facilitates the elimination of crashes or hangs during the initialization phase.
7. Verify Third-Party Plugin Compatibility

Many developers use external SDKs (like AdMob or AppLovin) which may have their own iOS implementations.

Best Practice: If using a third-party plugin, check if it conflicts with the built-in iosadvertising module. Sometimes you must disable the default engine module to ensure the elimination of symbol collisions during the Xcode compilation process.
8. Monitor Console Logs via Xcode

Standard Unreal Engine logs may not capture specific error codes returned by the iOS system frameworks.

Tip: Run your project directly from Xcode and filter the output for [Advertising]. This provides low-level feedback from the native side, such as “No Inventory” or “Invalid Bundle ID,” which is essential for the elimination of guesswork when ads fail to display.