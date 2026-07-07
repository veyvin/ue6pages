---
layout: default
title: SceneDepthPickerMode
---

<!-- ai-generation-failed -->

<h1>SceneDepthPickerMode</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/SceneDepthPickerMode/SceneDepthPickerMode.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, Engine, InputCore, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

a dedicated interaction mode for sampling world-space depth and distance values directly from the 3D viewport.

Description and Purpose

This module implements the logic for the “Eyedropper” or “Picker” tool used in various cinematic and rendering properties. Its primary purpose is to allow artists and designers to click on a 3D object in the scene to automatically retrieve the exact distance between the camera and that specific point. It is most commonly used to set the Focal Distance in Cinematic Cameras or to define the focus point for Post-Process effects. By providing a pixel-perfect sampling method, it helps eliminate the “trial and error” guesswork involved in manually typing numeric depth values to achieve a sharp image.

Practical Usage Tips and Best Practices
Bind to Camera Focus Settings
The most common use case is in the Cine Camera Actor. Click the “eyedropper” icon next to the Focus Settings > Manual Focus Distance property. This activates the module, allowing you to click your character’s eyes to eliminate blurry renders in your cinematics.
Sample Through Translucency
The picker is designed to respect depth-writing. If you need to focus on an object behind a glass window, ensure the glass material is not writing to the CustomDepth or that you are clicking on a opaque section. This helps you eliminate focus errors where the camera accidentally focuses on the glass surface instead of the subject.
Use with Post-Process Volumes
When setting up Depth of Field (DoF) in a Post-Process Volume, use this mode to find the “Near” and “Far” transition points. Sampling the ground at different distances is a best practice to eliminate harsh transitions between focused and unfocused areas of the map.
Identify World Space vs. Screen Space
This module returns values in Unreal Units (cm). When using the sampled value in a Material or a Blueprint, ensure your math accounts for this scale. This helps you eliminate logic bugs where a sampled depth of 500 (cm) is incorrectly interpreted as a 0.0–1.0 normalized value.
Validate Collision with the Picker
If the picker fails to return a value or snaps to the “infinite” background, it usually means the object you clicked lacks a valid collision mesh or a depth-rendering pass. Use this behavior to eliminate invisible or “ghost” objects that might cause issues for other systems like AI or line traces.
Combine with Sequencer Keyframes
When creating a “rack focus” in Sequencer, move the playhead to your first frame, use the picker to set the distance, and set a key. Move to the next frame, pick the new subject, and key again. This workflow is the fastest way to eliminate drift and ensure the focus transition is perfectly timed with the action.
Check for Viewport Scaling Issues
If you are using a high-DPI monitor or a custom UI scale, ensure your clicks align with the visual subject. If the sampled depth seems “off,” try resetting your viewport resolution scale to 100% to eliminate coordinate offset errors during the picking process.
Utilize in Material Editor Previews
In some instances, the picker can be used to set parameters in Material Instance Constants that rely on distance-based effects (like a “Distance Fade”). Using the picker here is a best practice to eliminate seams between different materials that are meant to blend at a specific world-depth.