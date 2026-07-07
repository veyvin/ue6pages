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

t that provides the user interface and logic for managing Linux-specific build and deployment settings.

Description and Purpose

This module acts as the “bridge” between the Unreal Editor’s UI and the underlying Linux platform abstraction layer. Its primary purpose is to populate the Project Settings > Platforms > Linux section, allowing developers to configure parameters such as supported architectures (x86_64, ARM64), binary splash screens, and localized application names. By providing a centralized control surface, it allows developers to eliminate the need for manually editing .ini files when configuring how their project should be packaged and distributed for Linux environments.

Practical Usage Tips and Best Practices
Toggle Architecture Support via UI
Use the checkboxes provided by this module to enable or disable specific architectures like x86_64 or ARM64. Unchecking architectures you do not intend to support helps you eliminate accidental build time increases and prevents the generation of unnecessary binaries.
Configure the RHI Priority List
Within the Linux platform settings, you can define the priority for different Render Hardware Interfaces (RHIs), such as Vulkan or OpenGL. Ordering these correctly ensures the game defaults to the most performant API, helping you eliminate visual regressions on older Linux drivers.
Assign Custom Splash Screens
This module manages the file paths for Linux-specific splash images and icons. Ensure your images meet the recommended dimensions (typically 600x200 for splash) to eliminate distorted or missing graphics during the application’s initial boot sequence on Linux desktops.
Manage Packaging Settings for Steam Deck
If targeting the Steam Deck, use this module to ensure the “For Distribution” and “Shipping” configurations are correctly mapped to Linux-compatible file systems. Proper configuration here helps you eliminate permission errors when the game is installed via the Steam client.
Set Environment Variable Overrides
The controls module allows you to specify certain environment variables that should be set when the game launches. This is a best practice to eliminate issues with custom library paths (LD_LIBRARY_PATH) or to force specific driver behaviors for specialized hardware.
Validate Toolchain Status
This module often displays the status of your current Linux cross-compilation toolchain. Checking this section after an engine update is a good way to eliminate build failures; if the toolchain is reported as “not found,” you know you must update your LINUX_MULTIARCH_ROOT before proceeding.
Localize Application Titles
Use the “Project Name” and “Version” fields within the Linux controls to provide localized strings for the OS window manager. This helps you eliminate generic “UE5-Game” titles appearing in the Linux taskbar, providing a more professional and polished user experience.
Define Low-Level Test Configurations
For developers using the Functional Testing framework, this module provides options to configure how tests are packaged for Linux. Ensuring these are set to “Development” rather than “Shipping” helps you eliminate the exclusion of critical debug symbols needed for automated CI/CD pipelines.