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

Unreal Engine’s advertising interface for Apple’s iOS devices.

Description and Purpose

This module serves as a bridge between the engine’s generic advertising framework and the native iOS SDKs. Its primary purpose is to manage the lifecycle of ad banners and full-screen ads on iPhone and iPad. It implements the IAdvertisingProvider interface, allowing developers to call universal Blueprint nodes (like Show Ad Banner) while the module handles the underlying Objective-C calls to display the content. It is essential for developers looking to monetize mobile games through ad networks that integrate with the standard iOS advertising workflows.

Practical Usage Tips and Best Practices
Implement App Tracking Transparency (ATT) First
Since iOS 14, you must request permission to track users before serving personalized ads. You must trigger the “Request Platform Tracking Authorization” flow before the advertising module can successfully fetch relevant ads. Failing to do this will often eliminate your ability to receive high-value ad fills.
Configure the “Additional Shipping Linker Flags”
In your iOS Project Settings, ensure you include the necessary frameworks (like AdSupport or AppTrackingTransparency) in the linker flags. If these are missing, the module will fail to initialize at runtime, which will eliminate all ad functionality in your shipping build.
Use Ad Banner Delegates for UI Layout
Do not assume an ad is always visible. Bind to the OnAdOpened and OnAdClosed delegates to adjust your game’s UI. For example, shift your bottom-aligned buttons upward when a banner appears to eliminate overlapping interactive elements.
Manage Ad Visibility During Game States
Always call Hide Ad Banner during intensive gameplay or cinematic sequences. This helps you eliminate distractions for the player and ensures that the CPU/GPU resources used for ad rendering do not cause frame rate hitches during critical moments.
Verify the Provider ID in C++
If you are using C++, ensure you check that the advertising provider is correctly set to "IOSAdvertising". Use IAdvertisingProviderModule::Get().GetDefaultProvider() to validate the module is loaded. This helps you eliminate null pointer crashes when calling ad functions on non-iOS platforms.
Account for Safe Areas on Notched Devices
iOS devices with notches or “Dynamic Islands” require specific padding. The advertising module generally places banners at the extreme top or bottom. Verify your “Safe Area” settings in UMG to eliminate instances where the ad banner covers vital gameplay information or system gestures.
Test with Apple’s “Limit Ad Tracking” Setting
Always test your game on a physical device with “Limit Ad Tracking” enabled in the iOS system settings. This allows you to verify that your game’s logic doesn’t break when the advertising module returns an empty ad, helping you eliminate soft-locks in your monetization flow.
Include SKAdNetwork IDs in Info.plist
Modern iOS ad integration requires a list of SKAdNetworkIdentifier entries in your Info.plist. Use the “Extra Info.plist Provisions” section in Project Settings to add these. This is required to eliminate issues with ad attribution and ensures you are correctly credited for ad impressions.