---
layout: default
title: HardwareSurvey
---

<!-- ai-generation-failed -->

<h1>HardwareSurvey</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/HardwareSurvey/HardwareSurvey.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

capacity, and operating system versions across a player base.

This module provides the IHardwareSurvey interface, which “eliminates” the need for developers to write platform-specific code (such as DirectX queries on Windows or Metal queries on macOS) to identify hardware specifications. This data is critical for making informed decisions regarding “min-spec” targets and scalability defaults.

Practical Usage Tips and Best Practices
Access via the Module Manager
To use the survey features, access the singleton instance using FModuleManager::LoadModuleChecked<IHardwareSurveyModule>("HardwareSurvey").Get(). This “eliminates” manual object management and ensures the hardware detection logic is correctly initialized for the current platform.
Validate Minimum Specifications
Use the FHardwareSurveyResults struct to check the player’s hardware against your game’s required specs during the first launch. If the hardware is insufficient, you can “eliminate” a poor player experience by providing a clear warning or suggestion to update drivers before the game crashes.
Add Module Dependencies
In your Build.cs file, add "HardwareSurvey" to your PrivateDependencyModuleNames. This “eliminates” linker errors. Note that as a developer module, you should typically wrap its usage in #if WITH_EDITOR or !UE_BUILD_SHIPPING if you only intend to use it for internal telemetry during playtests.
Sync with Scalability Settings
Combine the results of the hardware survey with the GameUserSettings system. By identifying specific GPU models or VRAM limits, you can “eliminate” the guesswork in auto-detecting quality levels, ensuring the game defaults to “Low” on integrated graphics and “Epic” on high-end cards.
Respect Privacy and GDPR
While this module collects hardware IDs, you must “eliminate” the collection of personally identifiable information (PII). Ensure that any data sent to your backend is anonymized and that you have acquired the necessary user consent via an opt-in toggle in your UI, adhering to legal and platform requirements.
Use for Performance Profiling Analysis
When collecting automated performance traces or crash reports, include the hardware survey summary in the metadata. This “eliminates” ambiguity when analyzing “outlier” performance spikes, as you can see if the issues are isolated to specific hardware configurations or driver versions.
Identify Specialized Features
The survey can detect support for specific instruction sets or hardware features (like Ray Tracing or specific shader models). Use this to “eliminate” the execution of heavy rendering code on hardware that physically cannot support it, preventing driver-level “Device Removed” errors.
Review Results via Analytics
The engine can be configured to automatically pipe these results to an Analytics Provider. This “eliminates” the need for manual data mining; you can view a dashboard of your community’s hardware trends directly through your analytics platform’s interface.