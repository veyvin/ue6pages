---
layout: default
title: LinuxPlatformEditor
---


<h1>LinuxPlatformEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Linux/LinuxPlatformEditor/LinuxPlatformEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, Engine, InputCore, LinuxTargetPlatformControls, LinuxTargetPlatformSettings, MainFrame, MaterialShaderQualitySettings, PropertyEditor, RenderCore, SharedSettingsWidgets, Slate, SlateCore, SourceControl, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e how their game behaves when running on Linux-based operating systems.

This module is primarily used to manage build-time configurations, such as selecting the targeted Rendering Hardware Interface (RHI) (e.g., Vulkan), setting up the Cross-Compile toolchain from Windows, and configuring platform-specific branding like icons and splash screens. By centralizing these settings, it helps eliminate the need for developers to manually edit .ini files for standard platform configurations.

Practical Usage Tips and Best Practices
Configure the Cross-Compile Toolchain
For developers working on Windows, this module is essential for setting up the LINUX_MULTIARCH_ROOT environment variable. Use the settings interface to verify your toolchain path; this helps you eliminate “Clang not found” errors when attempting to package Linux binaries from a Windows machine.
Target Vulkan for Modern Performance
Within the Linux settings provided by this module, ensure Vulkan is selected as the primary Targeted RHI. Since OpenGL is deprecated in many modern Linux environments, sticking to Vulkan helps you eliminate visual artifacts and ensures compatibility with the latest drivers from NVIDIA and AMD.
Set Up Splash Screens and Icons
Use the module’s UI to assign specific .png files for the Linux splash screen and window icons. Linux desktop environments (like GNOME or KDE) handle icons differently than Windows; providing these assets here helps you eliminate the generic “X” or “Unreal” icon appearing in the user’s taskbar.
Manage Audio Plugin Overrides
The Linux platform settings allow you to specify which spatialization, reverb, and occlusion plugins to use specifically for Linux. If a certain third-party audio plugin is unstable on Linux, you can use these settings to fall back to the Built-In Spatialization, helping you eliminate audio crashes on launch.
Optimize Frame Pacing
In the “Runtime” section of the Linux settings, you can configure the fixed frame rate or smoothing logic. For Linux-based dedicated servers, setting a stable frame pace is critical to eliminate CPU spikes and ensure consistent replication timing for all connected clients.
Utilize Custom Config Folders
The Linux editor module supports distribution-specific variants (e.g., Ubuntu vs. Rocky Linux). You can use the Config/Custom/ paths to override LinuxEngine.ini settings for specific hardware targets (like the Steam Deck), which helps you eliminate the need for multiple separate project files.
Verify RHI Version Requirements
When targeting newer engine features like Lumen or Nanite on Linux, check the “Minimum Vulkan Version” settings. Setting this correctly ensures the engine won’t attempt to run on outdated drivers, which helps you eliminate “Device Lost” crashes on startup for users with legacy hardware.
Use ‘stat Platform’ for Debugging
While working in the editor, you can use the console command stat Platform to see how the settings defined in this module are being applied to your current session. This visibility allows you to eliminate guesswork when troubleshooting why a specific Linux-only optimization isn’t active.