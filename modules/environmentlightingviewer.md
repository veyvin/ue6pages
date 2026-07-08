---
layout: default
title: EnvironmentLightingViewer
---

<!-- ai-generation-failed -->

<h1>EnvironmentLightingViewer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/EnvironmentLightingViewer/EnvironmentLightingViewer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, Settings, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

or the Environment Light Mixer window. It is designed to centralize the creation and management of all atmospheric and global lighting components into a single, streamlined interface.

What it is and What it’s used for

Located in Engine/Source/Editor/EnvironmentLightingViewer, this module is a specialized editor utility. Instead of requiring artists to search the “Place Actors” panel for individual components, it provides a one-click dashboard to instantiate and configure the entire environment stack.

Primary uses include:

Unified Lighting Hub: Providing a single panel to manage the Sky Light, Directional Lights (Sun/Moon), Sky Atmosphere, Volumetric Clouds, and Exponential Height Fog.
Simplified Scene Setup: Allowing for the rapid creation of a physically-based sky system in empty levels.
Global Property Access: Exposing the most critical properties of different actor types (e.g., Sun Intensity, Cloud Density, Sky Tint) in one list, categorized by “Minimal,” “Normal,” or “Advanced” detail levels.
Real-time Feedback: Facilitating the immediate visual reconciliation of how different atmospheric components interact with one another.
Practical Usage Tips and Best Practices
1. Quick Launch via the Window Menu

Access the tool by navigating to Window > Env. Light Mixer. It is a best practice to dock this tab alongside your Details panel. This allows you to jump between specific actor settings and the global environment overview without searching through the Outliner.

2. Use the “Create” Buttons for Dependency Management

If your level is missing a required component (like a Sky Atmosphere), the Environment Light Mixer will display a “Create” button for it. Using these buttons ensures that the actors are spawned with default settings that are pre-configured to work together, leading to the elimination of common setup errors.

3. Toggle Visibility to Isolate Light Sources

Each component in the mixer has a visibility (eye) icon. Use this to quickly toggle the Sky Light or Directional Light off and on. This is an essential technique for “lighting audits,” allowing you to see exactly how much ambient light vs. direct light is contributing to the shadows in your scene.

4. Leverage the “Normal + Advanced” Detail Mode

By default, the mixer shows “Minimal” properties. If you need fine-grained control over things like Volumetric Scattering Intensity or Cloud Ambient Occlusion, change the detail dropdown in the top-right of the window to Normal + Advanced. This exposes deep settings without cluttering the UI when they aren’t needed.

5. Synchronize Dual Sun Setups

The Environment Light Mixer natively supports two Directional Lights (Atmosphere Sun 0 and Atmosphere Sun 1). If you are creating a “binary star” system or a planet with a distinct sun and moon, use the mixer to manage both simultaneously, ensuring their intensities and colors remain balanced.

6. Real-Time Capture Check

When adjusting settings in the mixer, ensure your Sky Light is set to Real Time Capture. The mixer makes it easy to change sky colors, but if Real Time Capture is disabled, your shadows and reflections won’t update until you manually recapture the scene, potentially leading to inaccurate visual feedback.

7. Combine with “Ctrl + L” for Fast Iteration

While the mixer allows you to change light properties, you should use it in tandem with the viewport shortcut Ctrl + L (and Ctrl + Shift + L for the second sun). Moving the sun’s position visually while having the mixer open to tweak intensity provides the fastest workflow for establishing the “Time of Day.”

8. Strategic Elimination of Redundant Actors

If you accidentally spawn multiple Sky Atmospheres or Sky Lights, the Environment Light Mixer will often highlight the conflict or show multiple entries. Use the mixer as an audit tool to identify and remove duplicate atmospheric actors that can cause rendering artifacts and performance degradation.