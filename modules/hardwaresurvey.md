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

ons.

This module is primarily used for Analytics and Hardware Targeting. It allows developers to understand the hardware landscape of their player base, helping them eliminate guesswork when deciding which minimum specifications to support or which scalability settings should be the default for specific hardware tiers.

Practical Usage Tips and Best Practices
Initialize the Survey Module Correctly
To begin gathering data, you must access the FHardwareSurveyModule through the Module Manager. Ensure you call the survey functions asynchronously to eliminate any potential hitching on the main thread while the module queries the system API for hardware details.
Use for Data-Driven Scalability
Leverage the collected hardware data to automatically assign players to a specific Device Profile. By matching GPU identifiers against your own database, you can eliminate the risk of a high-end card being defaulted to “Low” settings due to an unrecognized hardware ID.
Monitor Driver Version Compliance
The module can retrieve specific GPU driver versions. Use this information to trigger a warning UI if a player is using a driver version known to cause crashes in your game. This proactive check helps you eliminate a large volume of “stability” bug reports that are actually caused by outdated external software.
Anonymize Data for Privacy Compliance
When sending hardware survey results to your backend analytics (such as Epic Analytics or a custom solution), ensure you do not collect personally identifiable information (PII). This helps you eliminate legal risks associated with GDPR or other data privacy regulations while still gathering useful technical telemetry.
Identify Performance Bottlenecks Across the Player Base
Compare the hardware survey data with frame-rate telemetry from your game. If players with a specific CPU architecture are consistently seeing lower performance, you can use that data to eliminate specific code paths or optimize certain systems (like physics or animation) specifically for those processors.
Wrap in Preprocessor Guards for Shipping
While hardware surveys are useful for telemetry, you may want to disable the active polling of hardware in certain build configurations. Wrap your survey calls in #if !UE_BUILD_SHIPPING or use a configurable flag to eliminate unnecessary background processing in the final consumer version of the game.
Include Module Dependency in Build.cs
To utilize this module in C++, you must add "HardwareSurvey" to your PrivateDependencyModuleNames in your *.Build.cs file. Using a private dependency is a best practice to eliminate unnecessary exposure of hardware-querying headers to other parts of your game logic.
Verify Platform Support
Not all platforms provide the same level of hardware detail (e.g., consoles have fixed hardware, while PC is highly variable). Use the module to check the TargetPlatform first; this allows you to eliminate redundant hardware checks on platforms where the specifications are already known and constant.