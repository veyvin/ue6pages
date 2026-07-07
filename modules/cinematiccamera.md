---
layout: default
title: CinematicCamera
---

<!-- ai-generation-failed -->

<h1>CinematicCamera</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/CinematicCamera/CinematicCamera.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperSettings, Engine, MovieScene, MovieSceneTracks, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Aperture (F-Stop), and advanced Focus Tracking systems.

It is the primary tool for creating cutscenes in Sequencer, virtual production, and high-end architectural visualization where realistic Depth of Field (DoF) and lens characteristics are required.

Practical Usage Tips & Best Practices
1. Module Dependency for C++

If you are programmatically spawning or manipulating cinematic cameras (e.g., custom camera rigs or spring arms), you must add the module to your Build.cs.

C#
PublicDependencyModuleNames.AddRange(new string[] { "CinematicCamera" });
Copy code

Header: #include "CineCameraActor.h" (or CineCameraComponent.h)

2. Utilize Filmback Presets

Avoid manually guessing sensor dimensions. The UCineCameraComponent includes a wide range of real-world Filmback Presets (e.g., 35mm Full Frame, Super 35, Micro Four Thirds). Selecting a preset ensures that your Focal Length and Aspect Ratio behave exactly like their real-world counterparts, providing an instant “cinematic” feel.

3. Master the Tracking Focus Method

For dynamic scenes, switch the Focus Method from Manual to Tracking. This allows you to pick an Actor (or a specific Component) to stay in focus regardless of camera or target movement.

Pro Tip: For Metahumans, create a small “focus target” actor parented to the character’s eyes. Tracking the root of a character often leads to the focus being at their feet, which can result in the facial features being out of focus.
4. Control Bokeh via Diaphragm Blade Count

To achieve specific aesthetic “Bokeh” shapes (the blurred light shapes in the background), adjust the Diaphragm Blade Count in the Lens Settings. A lower count (e.g., 5) creates pentagonal bokeh, while a higher count (e.g., 18) results in perfectly circular, smooth blurring.

5. Use the Focus Debug Plane

When setting focus manually, toggle the Draw Focus Debug Plane. This renders a translucent purple plane in the viewport representing exactly where the focus is sharpest. This is essential for ensuring that the subject is not “soft” due to a slightly misplaced focal point.

6. Optimize via Cinematic DoF Console Variables

High-quality Depth of Field can be performance-intensive. Use console variables to cap the cost during development:

r.DOF.Kernel.MaxBackgroundRadius: Limits the blur size of the background.
r.DOF.Scatter.MaxSpriteRatio: Controls the upper bound of scattered “bokeh” sprites to prevent GPU overdraw from causing the elimination of frame rate stability.
7. Anamorphic Squeeze Factor

If you are aiming for a widescreen “letterboxed” look, use the Squeeze Factor property under Lens Settings. Setting this to 2.0 (standard anamorphic) will stretch the bokeh vertically and change the lens flares, emulating the look of classic cinema lenses without needing to physically mask the viewport.

8. Prioritize Camera Post-Process Over Volume

While Post Process Volumes are great for global grading, use the Post Process Settings directly on the CineCameraActor for shot-specific adjustments. This ensures that unique lens effects like Vignetting or specific Color Grading remain attached to that specific “lens” and are not overridden when the camera moves into a different global volume.