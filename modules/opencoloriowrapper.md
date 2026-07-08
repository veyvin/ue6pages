---
layout: default
title: OpenColorIOWrapper
---

<!-- ai-generation-failed -->

<h1>OpenColorIOWrapper</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/OpenColorIOWrapper/OpenColorIOWrapper.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, ImageCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the OpenColorIO (OCIO) v2 library into Unreal Engine. It serves as a bridge between the engine’s rendering pipeline and the industry-standard OCIO color management system used extensively in film, VFX, and virtual production.

This module is responsible for performing complex color space transformations, such as converting linear engine data into specific camera profiles (like ARRI LogC or Sony S-Log) or display standards (like Rec.709). By providing a unified way to handle these transforms, it helps you eliminate color inconsistencies across different monitors, LED walls, and post-production software, ensuring that “what you see” in the viewport matches the final output.

Practical Usage Tips and Best Practices
Standardize with ACES Configurations
For most professional workflows, use an ACES (Academy Color Encoding System) config file. You can point the OCIO Configuration Asset to ocio://default to use the built-in ACES CG config. This helps you eliminate the guesswork involved in matching CG elements with live-action plates.
Apply Transformations to the Viewport
In the Editor Viewport, go to View Mode > OCIO Display to apply a transform directly to your workspace. This allows you to view your scene through a specific LUT (Look-Up Table) in real-time, helping you eliminate lighting and material errors that only become visible after a final render.
Leverage Movie Render Queue (MRQ) Integration
When exporting cinematics, add the OpenColorIO setting to your MRQ job. You can specify a “Source” (usually Linear Working Space) and a “Destination” (like Rec.709). This helps you eliminate the need for an extra color-grading pass in external software for quick reviews.
Synchronize Colors in nDisplay
For Virtual Production, apply OCIO profiles to individual nDisplay viewports. This ensures that the color output of the LED wall matches the color response of the physical camera, which helps you eliminate the “blue-cast” or “wash-out” effects often seen on digital stages.
Include Module Dependencies in C++
If you are building custom editor tools that manipulate color data, you must add "OpenColorIOWrapper" and "OpenColorIO" to your Build.cs file. Proper dependency management helps you eliminate linker errors when calling OCIO transformation functions programmatically.
Manage Texture Color Spaces
Ensure your input textures (like UI elements or reference images) are tagged with the correct color space. The OCIO module can then transform them into the engine’s working space accurately, which helps you eliminate “crushed blacks” or over-saturated colors in your UI.
Use for Composure CG Layers
In Composure, use OCIO transforms to blend CG layers with live video feeds. By transforming both to a common working space, you can eliminate the visual “pop” where CG objects look like they are floating on top of the video rather than being part of the scene.
Update Configs on Project Elimination
When moving a project to a new pipeline or “eliminating” an old color workflow, always update your .ocio config files and re-link the OCIO Configuration Asset. This prevents the engine from falling back to default sRGB, helping you eliminate sudden shifts in visual fidelity across different versions of your project.