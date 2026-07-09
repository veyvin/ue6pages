---
layout: default
title: PIEPreviewDeviceProfileSelector
---

<!-- ai-generation-failed -->

<h1>PIEPreviewDeviceProfileSelector</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/PIEPreviewDeviceProfileSelector/PIEPreviewDeviceProfileSelector.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, EditorFramework, Engine, Json, JsonUtilities, MaterialShaderQualitySettings, PIEPreviewDeviceSpecification, RHI, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

iew Platform” feature in the Unreal Editor. It provides the functionality to swap the active Device Profile (and its associated scalability settings and console variables) while running a game in Play-In-Editor (PIE) or viewing the viewport.

This module is essential for cross-platform development, as it allows developers to simulate the rendering constraints and performance profiles of specific hardware (like an iPhone 15 or an entry-level Android device) directly on a high-end development PC.

Practical Usage Tips & Best Practices
1. Simulate Mobile Scaling with MobileContentScaleFactor

Different mobile devices use different resolution scales. This module allows you to preview how your UI and 3D scene look at non-native resolutions.

Best Practice: Use the Preview Platform menu to switch to an “Android Low” or “iOS” profile. This facilitates the elimination of UI layout bugs where elements are too small or blurry on devices with high pixel density but low performance.
2. Generate Platform JSON for Physical Devices

In UE 5.5+, you can export the exact settings from a physical device to a JSON file.

Tip: Connect a target mobile device to your PC and use the Generate Platform Json option in the Preview Platform menu. Importing this file ensures the elimination of “visual drift” by matching the editor’s CVars exactly to the physical hardware.
3. Manage Shader Compilation Wait Times

Switching a preview profile via this module triggers a re-compilation of shaders for the target platform’s rendering level (e.g., Vulkan or Metal).

Best Practice: Only switch profiles when necessary, as the initial compilation can take several minutes. Once compiled, the editor caches these shaders, leading to the elimination of future wait times when switching back to that specific device profile.
4. Test “Quality Switch” Material Nodes

Many materials use the Quality Switch or Feature Level Switch nodes to simplify logic for lower-end devices.

Tip: Use the Material Quality Level selector alongside the device profile. This results in the elimination of shader performance bottlenecks by verifying that the “Low” version of a material correctly replaces expensive nodes like blurred glass or complex displacement.
5. Verify Memory Buckets and Texture Pools

Device profiles often override r.Streaming.PoolSize to match the limited VRAM of mobile devices.

Best Practice: Enable stat streaming while using a preview profile. Monitoring the texture pool facilitates the elimination of “blurry texture” issues that occur when a mobile device’s restricted memory bucket causes textures to never reach their highest MIP level.
6. Debug Platform-Specific CVars

Some device profiles include specific workarounds, such as r.RenderTargetSwitchWorkaround=1.

Tip: Use the console command CVarName (without a value) to see the current value and which profile set it. This leads to the elimination of confusion when a rendering feature is unexpectedly disabled because of a rule in the DefaultDeviceProfiles.ini.
7. Combine with Mobile Emulators

UE 5.6 integrated Android emulators directly into the editor workflow.

Best Practice: Use the PIEPreviewDeviceProfileSelector to set the editor viewport to the same profile as the running emulator. This results in the elimination of discrepancies between what you see in the editor and what the actual APK renders on the emulated hardware.
8. Use for Performance Profiling (Soft Targets)

While the editor cannot emulate hardware-specific driver bugs, it can simulate the amount of work being sent to the GPU.

Tip: Use stat unit while a low-end profile is active. If the “Draw” time is high even on a powerful PC, it indicates that your draw call count is too high for the target platform, allowing for the elimination of performance issues before ever deploying to the actual device.