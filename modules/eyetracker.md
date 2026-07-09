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

real Engine designed to interface with eye-tracking peripherals (such as Tobii, Vive Pro Eye, or HoloLens 2). It provides a standardized C++ interface, IEyeTracker, and a set of Blueprint nodes to access gaze data, including gaze origin, direction, and fixation points. This module is essential for implementing “Gaze and Commit” mechanics, social avatar eye-mapping, and performance-saving techniques like Foveated Rendering.

Practical Usage Tips & Best Practices
1. Validate Connection Before Logic

Gaze tracking depends entirely on specialized hardware that may be disconnected or obscured.

Best Practice: Always use the IsEyeTrackerConnected node or check IEyeTracker::IsEyeTrackerConnected() before running any gaze-dependent code. This ensures the elimination of log spam or null pointer crashes when the user is not wearing a compatible headset.
2. Distinguish Between Head and Eye Gaze

Developers often confuse the forward vector of the HMD (head gaze) with the actual focal point of the pupils (eye gaze).

Tip: Use the GetGazeData node to get the specific vector of the eyes. This allows for the elimination of “stiff” interactions where a player is forced to move their whole head just to highlight a small UI element.
3. Implement Gaze Smoothing

Raw eye-tracking data is extremely “jittery” because human eyes perform tiny, rapid movements called saccades.

Best Practice: Apply a FInterp (Float Interp) or a weighted moving average to the gaze origin and direction. Smoothing the data leads to the elimination of flickering highlights on interactive objects, providing a much more comfortable user experience.
4. Optimize via Fixed/Variable Foveated Rendering

Eye tracking can be used to tell the GPU to only render the area the player is looking at in full resolution.

Tip: Combine the EyeTracker module with the Variable Rate Shading (VRS) settings in the project. This facilitates the elimination of wasted GPU cycles on peripheral pixels that the user cannot see clearly, significantly boosting frame rates in VR.
5. Use Gaze for “Intent” in AI and Interaction

Eye tracking can detect what a player is interested in before they ever press a button.

Best Practice: Use gaze duration (dwell time) to “prime” an object for interaction. For example, if a player stares at a door, you can begin pre-loading the room behind it. This leads to the elimination of visible loading hitches and creates a “magical” feel to the world.
6. Calibrate for Every User

Eye shapes and inter-pupillary distances vary significantly between individuals.

Tip: Always provide a way to trigger the hardware’s native calibration sequence (usually via the XR system’s overlay). Proper calibration ensures the elimination of accuracy drift where the “laser” of the eye gaze appears several inches away from where the user is actually looking.
7. Handle Blink Detection for “Gaze and Commit”

The EyeTracker module can often report when tracking is lost, which usually indicates a blink.

Best Practice: Use a brief “False” return from GetGazeData to detect a blink event. You can map a double-blink to a “select” action, which assists in the elimination of the need for bulky handheld controllers in certain VR/AR simulations.
8. Respect Global and Local Coordinate Spaces

Gaze data is typically returned in “Tracking Space” (relative to the headset) rather than World Space.

Tip: Use the GetWorldSpaceGazeData helper or manually transform the gaze vector by the Camera’s World Transform. Correct coordinate transformation is vital for the elimination of bugs where the gaze line-trace points in the wrong direction when the player rotates their character.