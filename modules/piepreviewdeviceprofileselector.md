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

manages the application of device-specific configurations and hardware limitations during a Play-In-Editor (PIE) session.

Description and Purpose

This module allows developers to emulate the graphical constraints and performance settings of specific hardware (such as an iPhone, an Android tablet, or a Nintendo Switch) directly within the Unreal Editor viewport. Its primary purpose is to swap the active Device Profile and its associated Console Variables (CVars) at runtime when a “Preview” session is launched. By using this module, you can eliminate the need to constantly package and deploy to a physical device just to see how your UI scales or how your materials look under mobile-specific shader limitations.

Practical Usage Tips and Best Practices
Access via the Performance and Scalability Menu
In UE 5.6, you can access these settings by clicking the “Speedometer” icon (Performance and Scalability) in the viewport toolbar. Use the Preview Platform sub-menu to select a specific device. This is the fastest way to eliminate visual discrepancies between your PC development environment and the target hardware.
Generate Platform JSON from Physical Devices
A powerful feature in recent versions is the ability to connect a physical device via USB and select Generate Platform JSON. This captures the exact settings of that device. Loading this JSON via the selector module helps you eliminate guesswork by providing a 1:1 match for the device’s actual capabilities and limits.
Enable Mobile PIE with Preview Devices
In Editor Settings under the Experimental section, ensure “Mobile PIE with preview devices” is enabled. This allows the module to not only change the resolution but also emulate mobile-specific behaviors like touch-screen input and safe-zone boundaries, helping you eliminate UI overlapping issues.
Monitor Shader Recompilation
When you switch to a different device profile (e.g., from Android GLES 3.1 to Android Vulkan), the engine will trigger a shader recompile for that specific feature level. To eliminate wasted time, stay in one profile for long sessions and only switch when you need to verify final look-and-feel.
Use for Half-Precision (FP16) Debugging
Mobile GPUs often use FP16 math for efficiency, which can cause “jittering” or vertex “exploding” that isn’t visible on PC. The preview selector can trigger Half-Precision Shader Emulation. This is a best practice to eliminate precision bugs in your materials before they ever reach the device.
Test Screen Aspect Ratios and Safe Zones
Use the device selector to cycle through different aspect ratios (e.g., iPad 4:3 vs. modern 21:9 phones). This module helps you eliminate “notched” screen issues where critical gameplay UI might be hidden under a camera punch-hole or rounded corner.
Validate Scalability Buckets (Low/Med/High)
Instead of just selecting a specific phone, use the selector to swap between your project’s custom scalability profiles. This is the best way to eliminate performance hitches on low-end devices by ensuring your “Low” profile correctly disables expensive features like high-quality shadows or complex Niagara effects.
Combine with “Standalone Game” for Accuracy
While the viewport preview is fast, launching as a “Standalone Game” with a selected device profile provides the most accurate memory and performance simulation. This helps you eliminate editor-specific overhead and gives a clearer picture of how the elimination of certain rendering features impacts the actual frame rate.