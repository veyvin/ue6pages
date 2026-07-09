---
layout: default
title: DeviceProfileServices
---

<!-- ai-generation-failed -->

<h1>DeviceProfileServices</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DeviceProfileServices/DeviceProfileServices.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, EditorFramework, Engine, Json, JsonUtilities, PIEPreviewDeviceSpecification, TargetPlatform, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine used to manage and evaluate Device Profiles at runtime. It provides the logic for the Device Profile Selection process, which allows the engine to determine which hardware-specific settings (like texture quality, resolution scales, or shader complexities) should be applied to a specific physical device.

This module is the engine’s primary tool for handling cross-platform scalability. It “eliminates” the need for hard-coding hardware checks by providing a rule-based matching system that maps device characteristics (like GPU family, OS version, or RAM capacity) to specific configuration buckets.

Practical Usage Tips and Best Practices
Define Hierarchical Profiles
The module follows a parent-child inheritance structure. Always define a base profile (e.g., Android) and then specialized children (e.g., Android_Adreno6xx). This “eliminates” redundancy, as child profiles only need to override specific CVars that differ from the base platform settings.
Use Matching Rules for Precise Targeting
Leverage the DeviceProfileMatchingRules in your BaseDeviceProfiles.ini. You can use SRC_GPUFamily or SRC_DeviceModel with CMP_Regex to “eliminate” performance issues on specific problematic hardware by automatically applying lower settings to those devices.
Leverage Device Profile Fragments
Use Device Profile Fragments to inject specific CVar overrides into existing profiles without creating a whole new class. This is a best practice for “eliminating” crashes on specific GPU/Driver combinations discovered late in development by appending a fragment containing fix-oriented CVars.
Implement Memory Buckets
Configure Memory Buckets (e.g., Smallest, Smaller, Default) within the module to scale the r.Streaming.PoolSize. This helps “eliminate” Out-of-Video-Memory (OOM) errors on lower-tier mobile devices by automatically capping memory usage based on the device’s total RAM.
Test with the Device Profile Previewer
In the Editor, go to Tools > Platforms > Device Profiles. Use the Previewer to see which profile your current machine matches. This “eliminates” the guesswork of whether your .ini rules are correctly written before you deploy a build to actual hardware.
Utilize MobileContentScaleFactor
For mobile development, use the r.MobileContentScaleFactor CVar within your profiles. This allows the module to “eliminate” rendering bottlenecks by downscaling the internal render resolution while keeping the UI crisp at the device’s native resolution.
Validate via Console Commands
At runtime, use the command DPNode.DumpActiveDeviceProfile to see which profile was selected. This is a critical debugging step to “eliminate” confusion if a device is performing poorly because it accidentally matched a “High” profile instead of a “Low” one.
Minimize Hard-Coded Platform Checks
Instead of using if (IsAndroid()) in C++, use the module to set a custom CVar in the profile, then check that CVar in your code. This “eliminates” code fragility and allows you to tune feature “elimination” or activation entirely through configuration files without recompiling.