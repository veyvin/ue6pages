---
layout: default
title: CelSpec
---

<!-- ai-generation-failed -->

<h1>CelSpec</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/cel-spec/CelSpec.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Protobuf</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

gine 5.6 source code or C++ API. It is highly likely that you are referring to a specialized third-party plugin (such as a Cel Shader pack from Fab), a custom module within a specific studio’s project, or a specific property within the Cine Camera system.

However, if you are looking to implement Cel Shaded (Toon) Stylization or work with Cinematic Specifications in Unreal Engine, the following modules and workflows are the professional standards used to achieve those results.

Core Modules for Cel Shading and Cinematics
Renderer / PostProcess: Used to create the “Cel” look via Post Process Materials (Sobel filters, multi-banding).
CinematicCamera: Used to define the “Specs” (Focal length, aperture, sensor size) of your shot.
Practical Tips for Cel Shading and Cinematic “Specs”
1. Implement Custom Depth for Outlines

To create high-quality cel-shaded outlines without affecting the entire screen, you must use the Custom Depth buffer.

Tip: Enable “Render CustomDepth Pass” on the Actors you want to outline. In your Post Process Material, compare the Scene Depth to the Custom Depth to eliminate outlines on background elements or unwanted objects.
2. Use the Sobel Filter for Edge Detection

The “Cel” look relies heavily on edge detection logic within a Post Process Material.

Best Practice: Use a Sobel Edge detection algorithm in your material graph. By sampling neighboring pixels in the Scene Depth and World Normal textures, you can eliminate the “flat” look and generate clean, ink-like lines.
3. Quantize Lighting for “Toon Bands”

To achieve the classic banded lighting look:

Tip: In your material, take the Dot Product of the Light Vector and the Surface Normal. Pass this through a Ceil or a Step node (or a 1D Lookup Texture/Curve Atlas). This will eliminate smooth gradients and replace them with sharp, stylized color bands.
4. Configure Cine Camera Sensor Specs

If “celspec” refers to camera specifications, you should focus on the CineCameraComponent.

Best Practice: Use the “Filmback” settings to match real-world camera sensors (e.g., Super 35mm). Matching these “specs” correctly will eliminate the “CGI feel” by providing realistic Field of View and Depth of Field relationships.
5. Leverage Material Parameter Collections (MPC)

Managing stylized lighting across an entire level can be difficult.

Tip: Use an MPC to store global “specs” like “Outline Thickness” or “Shadow Sharpness.” By updating one value in the MPC, you can eliminate the need to manually update dozens of Material Instances when the art direction changes.
6. Utilize Vertex Normal Offsets for Outlines

A common alternative to Post Process outlines is the “Inverted Hull” method.

Action: Create a second material shorthand that pushes vertices along their normals and inverts the polygons. This technique is often more performant on mobile and can eliminate the artifacts often seen with post-process edge detection.
7. Combine with Niagara for Stylized VFX

Cel shading is often ruined by realistic particle effects.

Tip: Use Niagara with custom sprite materials that also use light quantization. This ensures your fire, smoke, and sparks match the “Cel” specs of your characters, eliminating visual inconsistency.
8. Adjust Scalability for Cel Shaders

Post-process cel shaders can be heavy on the GPU.

Best Practice: Wrap your cel-shading logic in a Feature Level Switch or a Scalability check. If the player is on low-end hardware, you can eliminate the most expensive passes (like thick multi-sample outlines) to maintain a stable frame rate.

Note: If “celspec” is part of a specific plugin you downloaded from Fab, please check the /Plugins folder in your project directory for a README or documentation specific to that vendor, as it is not an internal Epic Games module.