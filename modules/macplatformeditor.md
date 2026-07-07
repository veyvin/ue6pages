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

le for managing macOS-specific project settings and providing a bridge between the Unreal Editor and Apple’s development ecosystem.

Description and Purpose

This module implements the user interface and backend logic for the Project Settings > Platforms > macOS panel. Its primary purpose is to allow developers to configure the unique requirements of the macOS operating system, such as application icons, bundle identifiers, and Metal graphics settings. It acts as a wrapper for the Modern Xcode Workflow, ensuring that the engine correctly handles codesigning, entitlements, and .plist generation. By utilizing this module, developers can eliminate the need to manually open Xcode to configure basic application metadata, streamlining the path from editor to packaged app.

Practical Usage Tips and Best Practices
Configure Modern Code Signing Ensure “Use Modern Code Signing” is enabled in the macOS settings. This allows the engine to interface directly with your Apple Developer Team ID and helps you eliminate “Command PhaseScriptExecution failed” errors that frequently occur during the packaging and distribution phase.
Set Application Display Name for Archives To change the name of the final .app bundle, use the Application Display Name field in this module (which updates the MacEngine.ini). Correctly setting this early helps you eliminate the confusion of having multiple builds named after the generic .uproject filename in your Finder.
Utilize Universal Binaries (arm64 + x86_64) In the macOS target architecture settings, select the option for Universal Binaries. This allows the module to package “slices” for both Intel and Apple Silicon Macs into a single executable, which is the best way to eliminate compatibility issues for players on different hardware generations.
Manage Frame Pacing with Metal Settings The module provides settings for the Metal RHI, such as “Wait for VSync.” Configuring these specifically for macOS helps you eliminate screen tearing and ensures that the game’s frame pacing is consistent with the ProMotion displays found on modern MacBook Pro models.
Customize the Info.plist Template If your game requires specific permissions (like Microphone or Camera access), you can specify a custom Info.plist template within this module. This allows the engine to merge your requirements into the final build automatically, helping you eliminate manual post-build edits in Xcode.
Optimize App Icons via ICNS Use the module’s icon section to upload your .icns or high-resolution PNGs. The module will handle the scaling for Retina displays, which helps you eliminate blurry or pixelated icons in the macOS Dock and Launchpad.
Verify Xcode Version Compatibility The module often displays warnings if the installed version of Xcode is incompatible with the current engine version. Checking this status within the macOS platform settings is a proactive way to eliminate build failures caused by outdated SDKs or command-line tools.
Enable “Designed for iPad” for Apple Silicon If you are developing a mobile game, use the macOS settings to enable the “Designed for iPad” mode. This allows you to launch and test your iOS project directly as a windowed macOS app on M1/M2/M3 Macs, which can eliminate the overhead of deploying to a physical mobile device during rapid iteration.