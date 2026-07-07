---
layout: default
title: EyeTracker
---

<!-- ai-generation-failed -->

<h1>EyeTracker</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/EyeTracker/EyeTracker.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, Engine, InputCore, RHI, RenderCore, Renderer, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

in Unreal Engine that provides a standardized interface for accessing gaze and pupillary data from eye-tracking peripherals.

Description and Purpose

This module defines the IEyeTracker interface, which allows Unreal Engine to communicate with various hardware devices (such as Tobii, Varjo, Vive Pro Eye, or HoloLens 2) without requiring device-specific code for every implementation. It collects raw data regarding where a user is looking in 3D space, their gaze direction, and pupil dilation. This data is essential for Virtual Reality (VR) and Augmented Reality (AR), enabling features like foveated rendering, gaze-based UI interaction, and realistic eye movement for social avatars.

Practical Usage Tips and Best Practices
Implement Foveated Rendering to Boost Performance
Use the gaze data from this module to drive Variable Rate Shading (VRS) or Fixed Foveated Rendering. By rendering the area the player is looking at in higher detail and reducing quality in the periphery, you can significantly improve frame rates and eliminate GPU bottlenecks in high-resolution VR scenes.
Use “Gaze and Commit” for UI Interaction
Instead of relying solely on hand controllers, allow players to highlight buttons by looking at them and then pressing a trigger to confirm. This interaction model helps eliminate “arm fatigue” in long VR sessions and provides a more natural user experience for menu navigation.
Apply Data Smoothing (Interpolation)
Raw eye-tracking data is often “jittery” due to natural microsaccades (tiny involuntary eye movements). Use a Lerp or a custom exponential smoothing filter on the gaze vector to eliminate visual jitter when moving a reticle or a world-space cursor.
Always Include a Calibration Sequence
Every user’s eyes are unique. Before starting a gameplay session, trigger the hardware’s calibration routine via the IEyeTracker interface. Proper calibration is necessary to eliminate offset errors where the engine thinks the user is looking slightly to the side of their actual target.
Drive Social Avatar Realism
In multiplayer experiences, map the eye-tracker’s output to the Control Rig of a character’s skeletal mesh. Having an avatar’s eyes track other players or points of interest will eliminate the “blank stare” effect and make digital characters feel significantly more alive.
Design for “Gaze and Dwell” Accessibility
For players with limited mobility, implement “Dwell” logic where an action is triggered after staring at an object for a specific duration (e.g., 2 seconds). This allows players to trigger a character elimination or interact with the world using only their eyes, effectively eliminating the need for traditional inputs.
Validate Hardware Connection States
Always use the IsEyeTrackerConnected node or C++ check before attempting to read gaze data. Implementing a fallback to “Head Gaze” (using the HMD’s forward vector) when the eye tracker is unavailable will eliminate broken gameplay loops for users without compatible hardware.
Respect User Privacy and Data Security
Gaze data can be sensitive. Avoid logging raw gaze coordinates to external servers unless necessary for gameplay. By processing data locally and only sending high-level events (like “Target Acquired”), you eliminate potential privacy risks associated with tracking a user’s biometric data.