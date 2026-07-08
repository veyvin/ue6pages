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

r that enables communication between the engine and eye-tracking hardware, such as those found in the HoloLens 2, Vive Pro Eye, or specialized desktop trackers like Tobii.

Description

The EyeTracker module provides a standardized C++ interface (IEyeTracker) and a Blueprint library (EyeTrackingFunctionLibrary) to access gaze data. It abstracts away the hardware-specific SDKs, allowing developers to retrieve the user’s gaze origin and direction in a unified coordinate space. This data is essential for Virtual Production, XR Interaction, and Research Analytics, enabling mechanics like foveated rendering (optimizing performance where the user is looking), gaze-based UI interaction, and heat-map generation for user behavior studies.

Practical Usage Tips and Best Practices
1. Always Check Connection State

Eye-tracking hardware can be finicky or require user calibration. Before running any logic, always use the IsEyeTrackerConnected node (or IEyeTracker::IsEyeTrackerConnected() in C++). If the hardware is not detected, your code should fall back to a “Head Gaze” (the forward vector of the HMD/Camera) to prevent the elimination of player interaction capabilities.

2. Differentiate between Gaze and Head Tracking

Avoid using Eye Tracking for primary aiming in fast-paced shooters, as human eyes move too rapidly and “jitter” (saccades). A best practice is to use Head Gaze for broad targeting and Eye Gaze for subtle interactions, such as highlighting a specific UI button or selecting an object the user is already looking at to provide a “magical” feel.

3. Implement “Gaze and Dwell” for Hands-Free UI

A popular interaction pattern is Gaze and Dwell. When the gaze hits a UI element, start a timer. If the gaze remains on that element for a set duration (e.g., 1 second), trigger the action. This allows for the elimination of physical controllers, which is ideal for accessible design or medical/industrial simulations.

4. Handle “Blink” State to Prevent Data Gaps

When a user blinks, the eye tracker will return “False” or invalid data. You should implement a “Blink Buffer” that caches the last known valid gaze position for 0.15 to 0.2 seconds. This prevents the UI from flickering or the gaze-target from being “eliminated” every time the player blinks.

5. Transform Gaze to World Space Correctly

The raw gaze data is often provided in “Player Space” or “HMD Space.” To interact with the world, you must transform the Gaze Direction vector into World Space using the Camera’s location and rotation. Use a Line Trace by Channel starting from the Camera World Location in the direction of the transformed Gaze Vector to find what the user is looking at.

6. Enable Necessary Platform Capabilities

On platforms like HoloLens 2, eye tracking is protected by privacy permissions. You must navigate to Project Settings > Platforms > HoloLens and ensure the Gaze Input capability is checked. Without this, the EyeTracker module will return zeroed data, even if the hardware is functional.

7. Use for Foveated Rendering Performance

If your project is GPU-bound in VR, use the gaze data to drive Variable Rate Shading (VRS). By telling the GPU to render at full resolution only where the user is looking and lower resolution in the periphery, you can achieve a massive performance boost without the user noticing a loss in visual quality.

8. Calibrate Before Critical Data Collection

For research or high-precision tools, always trigger the hardware’s calibration routine via the EyeTracker module’s interface before starting a session. If the user shifts their headset, the gaze accuracy will drift; providing a “Recalibrate” button in your pause menu is a best practice to avoid the elimination of data accuracy over time.