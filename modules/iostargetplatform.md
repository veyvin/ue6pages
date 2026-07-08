---
layout: default
title: IOSTargetPlatform
---


<h1>IOSTargetPlatform</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/IOS/IOSTargetPlatform/IOSTargetPlatform.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DesktopPlatform, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nd the Apple iOS/iPadOS ecosystem. It handles the specific logic required to package, cook, and deploy projects to iPhone and iPad devices.

What it is and What it’s used for

Located in Engine/Source/Developer/IOSTargetPlatform, this module is an editor-only extension of the ITargetPlatform interface. It provides the engine with the necessary metadata and toolchain hooks to treat iOS as a valid build target.

Primary uses include:

Asset Cooking: Managing the conversion of engine assets into formats optimized for mobile hardware (e.g., converting textures to ASTC format).
Deployment Orchestration: Interfacing with the Unreal Automation Tool (UAT) and Xcode to push builds to connected devices via USB or Wi-Fi.
Configuration Management: Handling iOS-specific settings found in Project Settings, such as Bundle Identifiers, Version Strings, and Provisioning Profiles.
Device Discovery: Detecting and listing connected Apple hardware so they appear as valid targets in the “Launch” menu.
Practical Usage Tips and Best Practices
1. Use the Modernized Xcode Workflow (UE 5.3+)

In recent versions, Unreal has moved toward a “Modern” Xcode integration. Ensure your project is set to use the modern workflow in Project Settings > iOS. This allows Xcode to manage frameworks and code signing more natively, leading to the elimination of many legacy “Certificate Not Found” errors.

2. Automate Provisioning with “Automatic Signing”

Manually managing .mobileprovision files can be tedious. If you are using a Mac, enable Automatic Signing in the iOS Project Settings. This allows the IOSTargetPlatform module to communicate with Xcode to generate and refresh the necessary profiles automatically, ensuring the elimination of expired certificate issues.

3. Optimize Texture Cooking with ASTC

iOS devices primarily use ASTC (Adaptive Scalable Texture Compression). In your project’s Target Platform settings, ensure you are only cooking for ASTC rather than older formats like PVRTC. This reduces build size and ensures the elimination of redundant texture data in your final .ipa package.

4. Configure Privacy Manifests (Required for App Store)

As of 2024, Apple requires Privacy Manifests (PrivacyInfo.xcprivacy). The IOSTargetPlatform module now looks for this file in your project’s Build/IOS/Resources/ directory. Including this file correctly is a best practice to ensure the elimination of App Store rejection notices during the submission process.

5. Leverage “Remote Building” from Windows

If your primary development machine is a PC, you can still use this module by setting up a Remote Build Server (an networked Mac). The IOSTargetPlatform module will securely SSH into the Mac to handle the final compilation and signing, allowing for the elimination of the need to switch workstations constantly.

6. Utilize the “Launch On” Feature for Fast Iteration

Instead of a full “Package Project,” use the Launch On dropdown in the Toolbar. This uses a “Cook on the Side” method where the IOSTargetPlatform module only sends changed assets to the device. This provides a massive speed boost and the elimination of long wait times between mobile gameplay tests.

7. Define Per-Configuration App Names

Unreal now supports different Display Names for different build configurations (e.g., “MyGame-Dev” vs “MyGame”). Use this feature in the iOS settings to easily distinguish between different versions of the app on your testing device, aiding in the elimination of confusion when testing multiple branches.

8. Strategic Elimination of Unused Architectures

Older iOS devices used armv7, but modern ones use arm64. Ensure your project settings are only targeting the architectures you actually intend to support (usually just arm64 for modern UE5 projects). This reduces binary size and leads to the elimination of unnecessary compilation time during the packaging phase.