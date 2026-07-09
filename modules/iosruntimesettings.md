---
layout: default
title: IOSRuntimeSettings
---

<!-- ai-generation-failed -->

<h1>IOSRuntimeSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/IOS/IOSRuntimeSettings/IOSRuntimeSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioPlatformConfiguration, Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tifiers, orientation lock, and minimum OS versions—and serializes these settings into the DefaultEngine.ini file, which the Unreal Build Tool (UBT) later uses to generate the final Info.plist for the application.

Practical Usage Tips & Best Practices
1. Use a Unique Bundle Identifier

The Bundle Identifier is the “fingerprint” of your app. If it does not match the App ID created in your Apple Developer account, the build will fail.

Best Practice: Use the reverse-DNS format (e.g., com.OrganizationName.ProjectName). Setting this correctly in the iOS Runtime Settings ensures the elimination of “Provisioning Profile not found” errors during the packaging phase.
2. Configure Remote Build Settings for Windows Users

If you are developing on Windows, you must use a remote Mac to handle the final compilation and code signing via SSH.

Tip: Within the iOS settings, provide the Remote Server Name and RSync User. Properly configuring these fields leads to the elimination of connection timeouts and allows for a seamless “one-click” build process from a PC.
3. Optimize Performance via Frame Pacing (Power Usage)

Uncontrolled frame rates on mobile devices lead to rapid battery drain and thermal throttling.

Best Practice: Set the Frame Rate Limit (e.g., to 30 or 60 FPS) in the Power Usage section of the iOS settings. Utilizing the engine’s built-in frame pacer facilitates the elimination of jittery performance and keeps the device cool during extended play sessions.
4. Leverage the Modernized Xcode Workflow

In recent engine versions (5.3+), Unreal has streamlined how it communicates with Apple’s toolchain.

Tip: Enable Use Automatic Code Signing in the Xcode Projects section. This allows Unreal to automatically manage your certificates and profiles through your signed-in Xcode account, resulting in the elimination of manual profile management headaches.
5. Manage Launch Screen and Icon Assets

The module provides specific slots for different icon sizes required by various iPhone and iPad models.

Best Practice: Always provide high-resolution source images for every requested slot. Filling these correctly ensures the elimination of blurred icons on high-DPI “Retina” displays and prevents app rejection during the App Store review process.
6. Restrict Supported Orientations

Allowing a game to rotate freely can break UI layouts that are designed only for landscape or portrait.

Tip: In the orientation settings, uncheck the modes you do not support (e.g., “Portrait”). This ensures the elimination of accidental layout breaks that occur when a user tilts their device during gameplay.
7. Add Custom Plist Data for Permissions

If your game uses specific features like the camera, microphone, or local networking, you must provide “Usage Description” strings.

Best Practice: Use the Additional Plist Data text box to add these XML keys. Providing clear descriptions for these permissions assists in the elimination of “silent failures” where the OS blocks a feature because the required description is missing.
8. Set the Minimum iOS Version Proactively

Setting the minimum version too low can cause crashes if you use modern rendering features (like certain Metal features), while setting it too high limits your audience.

Tip: Verify the requirements for your target rendering level (e.g., Metal 2.0 vs 3.0) and set the Minimum iOS Version accordingly. Accurate version targeting results in the elimination of compatibility issues for users on older hardware.