---
layout: default
title: LinuxTargetPlatformControls
---

<!-- ai-generation-failed -->

<h1>LinuxTargetPlatformControls</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/Linux/LinuxTargetPlatformControls/LinuxTargetPlatformControls.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, Engine, LinuxTargetPlatformSettings, Projects, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rovides the User Interface and configuration logic for Linux-based platforms within the Unreal Engine Project Settings. While the LinuxTargetPlatform module handles the actual heavy lifting of cooking and packaging, LinuxTargetPlatformControls acts as the bridge between the developer and the engine’s configuration files. It exposes Linux-specific properties—such as Targeted RHIs (Vulkan), splash screens, icons, and audio settings—allowing developers to customize their Linux builds through a visual interface rather than manual .ini file editing.

Practical Usage Tips & Best Practices
1. Configure Targeted RHIs (Vulkan)

Linux builds primarily rely on Vulkan for high-performance rendering. This module provides the checkboxes to enable or disable specific Vulkan versions.

Best Practice: Only enable the RHIs your target hardware supports. For modern desktop Linux, ensure “Vulkan” is checked. Selecting only the necessary RHIs leads to the elimination of bloated shader cache files and reduces initial compile times for your players.
2. Manage Platform-Specific Splash Screens and Icons

Linux desktops (GNOME, KDE, etc.) handle window icons and startup splashes differently than Windows.

Tip: Use the settings provided by this module to upload a dedicated PNG for the Linux icon and a splash image. Properly setting these assets ensures the elimination of the default Unreal Engine logo appearing in the taskbar or during the loading sequence of your packaged game.
3. Select Audio Plugins for Linux Compatibility

Not all spatialization or reverb plugins are cross-platform.

Best Practice: Use the Audio section under Linux Project Settings to specify which plugins (like Resonance Audio or Epic’s Built-in Spatialization) should be used. Setting this correctly results in the elimination of “Audio Device Failures” when the game initializes on a Linux system with specific driver requirements.
4. Optimize for Steam Deck via Project Settings

The Steam Deck runs on SteamOS (Linux). Settings managed by this module directly affect how the game performs on this handheld.

Tip: If targeting the Steam Deck, use the Linux settings to ensure the Vulkan RHI is prioritized. This proactive configuration facilitates the elimination of compatibility issues when the game is run through the Proton layer or as a native Linux build.
5. Verify Toolchain Detection

This module’s backend helps the editor determine if the Linux cross-compiler is correctly installed on a Windows host.

Best Practice: If the “Package Project > Linux” option is grayed out, check the Linux platform settings in the editor. This module will often display a warning if the toolchain is missing, aiding in the elimination of confusion regarding why Linux is not an available build target.
6. Use for Architecture-Specific Packaging

Unreal supports both x86_64 and ARM64 for Linux. The controls module allows you to toggle which architectures are included in a “Multi” cook.

Tip: If you are only deploying to desktop PCs, uncheck the ARM64 architecture. This leads to the elimination of unnecessary cooking time and reduces the size of your final build by omitting unused binaries.
7. Coordinate with DefaultEngine.ini

Changes made through the Linux Target Platform Controls UI are saved into your project’s Config/DefaultEngine.ini under the [/Script/LinuxTargetPlatform.LinuxTargetSettings] section.

Best Practice: When working in a team, ensure these .ini changes are committed to version control. This ensures the elimination of “local-only” configuration discrepancies where the build machine uses different settings than the developer’s workstation.
8. Proactive “Elimination” of Legacy RHIs

Older versions of Unreal allowed for OpenGL on Linux, which is now deprecated in favor of Vulkan.

Tip: Use the controls UI to ensure OpenGL is disabled for modern projects. Eliminating legacy RHIs ensures that the engine doesn’t waste resources attempting to compile shaders for outdated graphics APIs that your target hardware no longer utilizes.