---
layout: default
title: MacPlatformEditor
---

<!-- ai-generation-failed -->

<h1>MacPlatformEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Mac/MacPlatformEditor/MacPlatformEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AudioSettingsEditor, Core, CoreUObject, DesktopPlatform, Engine, InputCore, MacTargetPlatformControls, MacTargetPlatformSettings, MainFrame, MaterialShaderQualitySettings, PropertyEditor, RHI, RenderCore, SettingsEditor, ShaderPlatformConfigEditor, SharedSettingsWidgets, Slate, SlateCore, SourceControl, TargetPlatform, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e User Interface and specialized configuration logic for macOS development within the Unreal Editor. It is the bridge between the high-level engine settings and the macOS-specific requirements for packaging, code signing, and distribution. This module handles the “Modern Xcode” workflow, allowing developers to manage Apple Developer certificates and provisioning profiles directly within the Unreal interface, ensuring the elimination of manual plist editing and complex command-line builds for most project needs.

Practical Usage Tips & Best Practices
1. Enable Modern Xcode Workflow

In modern versions of Unreal (5.3+), the engine has shifted to a project-per-platform structure that aligns with Apple’s native development patterns.

Best Practice: Ensure bUseModernXcode=true is set in your BaseEngine.ini. This results in the elimination of the monolithic workspace, providing separate, optimized Xcode workspaces for Mac, iOS, and tvOS, which improves build stability and IDE performance.
2. Utilize Automatic Code Signing

Managing Apple Developer certificates can be the most time-consuming part of Mac development.

Tip: Use the Mac Platform settings provided by this module to select your Development Team ID. When “Automatic Signing” is active, Unreal communicates with Xcode to handle certificate generation, leading to the elimination of “Missing Private Key” or “Invalid Certificate” errors during packaging.
3. Configure Universal Binaries (ARM64 + x86_64)

Apple Silicon (M-series) and Intel Macs require different instruction sets for native performance.

Best Practice: In the Mac Platform settings, set the Targeted Architecture to arm64+x86_64. This creates a Universal Binary, ensuring the elimination of performance penalties caused by Rosetta 2 translation on Apple Silicon devices.
4. Manage the “Quarantine Bit” and Notarization

macOS Gatekeeper will block apps that are not properly signed and notarized when shared between team members via Slack or Perforce.

Tip: If an app won’t open, use the xattr -d com.apple.quarantine <app_path> command via the terminal. To prevent this for end-users, use the Mac platform settings to provide your App Store Connect credentials for automatic notarization, resulting in the elimination of the “App cannot be opened because the developer cannot be verified” warning.
5. Optimize for Apple Silicon Rendering

Mac-specific rendering features like Metal 3 and Nanite (beta on M2+) are managed through this module’s RHI settings.

Best Practice: Under the Mac platform settings, ensure Vulkan is disabled and Metal is the prioritized RHI. This ensures the elimination of shader compatibility issues and allows the engine to utilize hardware-specific features like “Metal Mesh Shaders.”
6. Use “Designed for iPad” for Rapid Testing

If you are developing a mobile game, you can run the iOS version of your app natively on your Mac.

Tip: In the iOS settings managed by this module, enable Supports iPad. You can then select “My Mac (Designed for iPad)” as a launch target, which facilitates the elimination of long deployment times to physical devices for UI and logic testing.
7. Handle P8 Team Keys for Build Machines

For automated build pipelines, logging into a personal Apple ID on a remote server is often impossible.

Best Practice: Use the App Store Connect API Key (P8 file) support within the Mac platform settings. Checking this file into your source control allows the build machine to authenticate with Apple, leading to the elimination of manual login requirements on headless build nodes.
8. Proactive “Elimination” of Entitlement Errors

Advanced features like “Extended Virtual Addressing” or “Increased Memory Limits” require specific entitlements in the app’s sandbox.

Tip: Use the Extra Entitlements text box in the Mac platform settings to add custom keys. Properly defining these ensures the elimination of runtime crashes when your game tries to access protected system resources or high amounts of RAM.