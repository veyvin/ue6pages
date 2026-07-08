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

Engine used to manage and evaluate Device Profiles. It acts as the logic layer that maps specific hardware (like an iPhone 15 Pro, a specific Android GPU, or a high-end PC) to a collection of configuration overrides, such as texture resolution limits, shadow quality, and other scalability console variables (CVars).

Its primary role is to handle the matching logic that determines which profile should be active on the current device. By using this module, developers can eliminate the need for platform-specific branching in gameplay code, instead relying on a centralized system that automatically applies the correct performance and quality settings based on the hardware detected at startup.

Practical Usage Tips and Best Practices
Use the Device Profile Manager for Runtime Access
To interact with profiles in C++, access the UDeviceProfileManager via the module. This allows you to query which profile is currently active, helping you eliminate uncertainty when debugging why specific scalability settings are applied to a user’s device.
Implement Hierarchical Profiles
Leverage the “BaseProfileName” feature to create a hierarchy (e.g., Android_High inheriting from Android). This allows you to define global settings in the parent and only override specific values in the child, which helps eliminate redundant entries and makes your DefaultDeviceProfiles.ini much easier to maintain.
Leverage Memory Buckets
Use the [PlatformMemoryBuckets] configuration within your profiles to adjust settings based on available RAM. For example, you can set r.Streaming.PoolSize_Smallest for 3GB devices and r.Streaming.PoolSize_Largest for 12GB devices. This helps eliminate out-of-memory (OOM) crashes on lower-end mobile hardware.
Test with the dp.Override Command
During development, you can use the console command dp.Override [ProfileName] to force the engine to adopt a different profile. This is an essential tool to eliminate the need for packaging and deploying to multiple physical devices just to verify how your UI or materials look on “Low” vs “High” settings.
Optimize Texture LOD Groups
Within a device profile, you can override TextureLODGroups to cap the MaxLODSize for specific categories like “World” or “Character.” Doing this at the profile level allows you to eliminate high-resolution textures on mobile devices where they would otherwise waste VRAM and impact performance.
Utilize Data-Driven CVars
Instead of hard-coding performance toggles, use the +CVars= array in your device profile. This allows you to eliminate complex C++ logic for feature toggling; if a feature is too expensive for a specific device, you simply set its associated CVar to 0 in that device’s profile.
Preview in Editor via Target Platforms
Use the “Device Profiles” window (Tools > Platforms > Device Profiles) to select a mobile or console profile and “Set as Active.” This updates the viewport in real-time, helping you eliminate visual artifacts and performance bottlenecks early in the production cycle without leaving the editor.
Check for Profile Matching Errors
If the engine cannot find a specific match for a device, it defaults to a generic profile (like Android or Windows). Regularly check your logs for “Device Profile not found” warnings to eliminate situations where a high-end device is accidentally running on baseline “Low” settings due to a naming mismatch in your config files.