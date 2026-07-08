---
layout: default
title: MacTargetPlatformSettings
---

<!-- ai-generation-failed -->

<h1>MacTargetPlatformSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Mac/MacTargetPlatformSettings/MacTargetPlatformSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CookedEditor, Core, CoreUObject, DesktopPlatform, Engine, RHI, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the configuration and management of macOS-specific project settings. It acts as the bridge between the Unreal Editor and the build pipeline, exposing the UMacTargetSettings class to define how a project is compiled, packaged, and signed for the Mac.

With the introduction of the Modern Xcode Workflow in recent versions, this module has become the primary hub for aligning Unreal projects with standard Apple development practices. It centralizes everything from bundle identifiers to architecture choices, helping developers eliminate manual configuration errors when targeting the macOS ecosystem.

Practical Usage Tips and Best Practices
Enable the Modern Xcode Workflow
In UE 5.3+, ensure bUseModernXcode is set to true in your BaseEngine.ini or via the project settings. This modernizes the project structure to be more consistent with native Apple apps and helps you eliminate cluttered, monolithic workspaces by creating per-platform Xcode projects.
Target Universal Binaries
To support both Intel-based Macs and Apple Silicon (M-series) in a single distribution, set your architecture to arm64+x86_64. This allows you to eliminate the need for separate builds and ensures that players on either hardware type receive the best possible performance.
Configure Automatic Code Signing
Use the ModernSigningTeam and ModernSigningPrefix settings. By entering your Apple Team ID and a reverse-domain prefix, the module allows Xcode to handle provisioning and entitlements automatically. This helps you eliminate the “Profile Not Found” errors common with manual signing.
Optimize Targeted RHIs (Metal)
Since Apple has deprecated OpenGL, ensure that Metal is the only selected RHI in the Mac settings. As of recent engine updates, rendering support for Intel-based Macs has been refined to focus on Metal, helping you eliminate shader compatibility issues on modern macOS versions.
Utilize Per-Configuration App Names
The Mac platform settings allow you to specify different application display names for different build configurations. Using a suffix like “(Dev)” for development builds helps you eliminate confusion when multiple versions of your app are installed on the same testing machine.
Custom Info.plist Templates
Instead of modifying the engine’s default files, place a custom Template.plist in your project’s Build/Mac folder. The module will automatically use this as a base, allowing you to add custom keys (like camera or microphone permissions) while helping you eliminate the risk of your changes being overwritten during engine updates.
Manage Frameworks via Build.cs
When your project requires macOS-specific system frameworks (like AppKit or CoreVideo), add them to your Build.cs. The MacTargetPlatformSettings system ensures these are correctly mapped into the generated Xcode project, helping you eliminate linker errors when the app is packaged.
Access Settings Programmatically in Tools
If you are building custom editor utilities or automation scripts, you can access these settings in C++ using GetDefault<UMacTargetSettings>(). This allows you to verify packaging settings before starting a build, helping you eliminate failed automation runs due to missing bundle IDs or team credentials.