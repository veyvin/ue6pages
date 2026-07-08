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

tography: Creating high-end cinematics for film and broadcast using Sequencer.
Real-World Emulation: Matching virtual shots to real-world camera rigs (e.g., Arri Alexa, Panavision) for VFX compositing.
Physical Depth of Field: Achieving cinematic “bokeh” and focus pulls based on physical lens mathematics.
Virtual Production: Driving in-camera VFX (ICVFX) where the virtual camera must match the physical lens used on a live stage.
Practical Usage Tips and Best Practices
1. Choose the Correct Filmback Preset

The Filmback setting is the most critical starting point. It defines the sensor size (e.g., 16:9 Digital Film, 35mm Full Aperture). Changing the Filmback after composing a shot will alter the field of view and depth of field, so select your sensor size before you begin fine-tuning your lens settings.

2. Master Manual Focus and Debugging

For precise focus pulls, set the Focus Method to Manual. Enable the Draw Focus Plane debug option in the Details panel; this renders a translucent purple plane in the viewport. Move this plane until it intersects with your subject to ensure perfect sharpness, especially when working with narrow depths of field.

3. Match Real-World Lens Lingo

Use the Lens Settings to define a “Lens Kit.” Instead of arbitrarily sliding the Field of View, set a fixed Focal Length (e.g., 35mm, 50mm, 85mm) and Aperture (F-stop). This ensures your shots look physically grounded and consistent with professional filmmaking standards.

4. Utilize the Cinematic Viewport

When working with the Cinematic Camera, switch your viewport to Cinematic Viewport (under the Viewport options). This provides professional overlays like Safe Areas, Aspect Ratio Masks (Letterboxing), and Grid Lines (Rule of Thirds) which are essential for balanced shot composition.

5. Pilot the Camera for Composition

To intuitively move the camera, right-click the Cine Camera Actor in the Outliner and select Pilot. This allows you to fly the camera using standard WASD controls. This is the fastest way to find “the shot” and is much more efficient than using the transform gizmos.

6. Coordinate with Sequencer

Cine Cameras are designed to be “Spawnable” within Sequencer. When creating a cinematic, drag your Cine Camera directly into the Sequencer track. This automatically creates a Camera Cut Track, allowing you to keyframe focus, focal length, and aperture over time for dynamic storytelling.

7. Adjust Bokeh via Diaphragm Blade Count

To change the aesthetic of your out-of-focus highlights (bokeh), adjust the Diaphragm Blade Count in the Lens Settings. A lower count (e.g., 5) creates pentagonal bokeh, while a higher count (e.g., 20) results in perfectly circular, soft highlights.

8. Implement Tracking Focus

For scenes with moving characters, use Tracking Focus Settings. Assign an Actor to the Focus Target and add a relative offset if needed (e.g., to focus on the eyes rather than the root). This automates the focus pull, ensuring the elimination of blurry subjects during complex camera movements.