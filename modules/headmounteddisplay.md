---
layout: default
title: HeadMountedDisplay
---

<!-- ai-generation-failed -->

<h1>HeadMountedDisplay</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/HeadMountedDisplay/HeadMountedDisplay.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, EngineSettings, InputCore, RHI, RenderCore, Renderer</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

eving a user’s position and orientation, it helps eliminate the need to write separate code for every specific headset on the market.

Practical Usage Tips and Best Practices
Transition to the OpenXR Standard
As of UE 5.1+, the HeadMountedDisplay module relies heavily on the OpenXR plugin. Instead of using vendor-specific APIs (like the deprecated Oculus or SteamVR plugins), always use the generic OpenXR implementation. This practice helps you eliminate platform fragmentation and ensures your project is compatible with all modern XR runtimes.
Set Tracking Origin via Blueprint or C++
Use the SetTrackingOrigin node early in your logic (usually in BeginPlay). Choosing between Floor Level and Eye Level is critical for player height calibration. Correctly setting this helps eliminate “floating” players or players who are stuck inside the floor geometry.
Leverage Late Latching for Performance
In your Project Settings, ensure that Late Latching is enabled for supported platforms (like Quest). This allows the engine to update the HMD transformation data at the very last moment before rendering, helping to eliminate “swimming” or latency-induced motion sickness.
Use ‘GetDeviceWorldPose’ for Accurate Tracking
When you need the absolute position of the headset in your level, use the GetDeviceWorldPose function. This function returns the pose in world space rather than local tracking space, which helps eliminate complex manual coordinate transformations when placing UI or effects relative to the player’s head.
Include Module Dependency in Build.cs
To access HMD functions in C++, you must add "HeadMountedDisplay" to your PublicDependencyModuleNames in your *.Build.cs file. Additionally, include the "XRBase" module if you need to use the common base classes for XR components, which helps eliminate linker errors during compilation.
Check ‘IsHeadMountedDisplayConnected’ Before Initialization
Always verify that a headset is actually active using IsHMDConnected before executing XR-specific logic. This allows your game to gracefully fall back to a standard 2D monitor view if no VR hardware is detected, helping to eliminate crashes or “black screen” issues on startup.
Manage Viewport Scaling and HMD Density
Use the vr.PixelDensity console variable to dynamically adjust the render resolution based on the user’s hardware performance. Lowering the density slightly can eliminate dropped frames and stuttering in demanding scenes without completely sacrificing visual clarity in the HMD.
Handle HMD Recentering Gracefully
Players often need to recenter their view during a session. Subscribe to the OnHMDPoseRecentered event to reposition your player pawn or UI elements accordingly. This ensures the player’s forward direction remains aligned with your game’s intended orientation, helping to eliminate physical discomfort and disorientation.