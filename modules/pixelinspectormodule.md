---
layout: default
title: PixelInspectorModule
---

<!-- ai-generation-failed -->

<h1>PixelInspectorModule</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/PixelInspector/PixelInspectorModule.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, Engine, InputCore, PropertyEditor, RHI, RenderCore, Renderer, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

kend logic for the Pixel Inspector tool in the Unreal Editor. It allows developers to sample a specific pixel on the screen and retrieve a comprehensive breakdown of the data contributing to its final color, including GBuffer values, Material inputs, and lighting calculations.

This module is essential for debugging rendering issues, such as incorrect shading, “broken” textures, or unexpected lighting behavior. By inspecting the raw data at the pixel level, you can eliminate the guesswork involved in visual troubleshooting and pinpoint exactly which part of the rendering pipeline is failing.

Practical Usage Tips and Best Practices
Access via the Tools Menu
Open the tool by navigating to Tools > Debug > Pixel Inspector. Use the magnifying glass icon to start a “live” inspection by hovering over any viewport. This helps you eliminate the need to repeatedly take screenshots and analyze them in external software.
Analyze GBuffer Channels for Material Errors
The inspector provides a detailed view of GBuffer A, B, and C. Use this to check if your Base Color, Metallic, or Roughness values are being passed correctly to the renderer. This is the fastest way to eliminate “flat” or “plastic” looking materials caused by incorrect texture sampling.
Debug Pre-Exposure Settings
If your scene looks washed out or too dark despite correct lighting, check the Pre-Exposure value in the inspector. This helps you eliminate exposure-related visual artifacts by ensuring the range of SceneColor is properly remapped for your camera settings.
Verify Shading Models
The inspector displays the Material Shading Model for the selected pixel. Use this to ensure that specialized shading—like Subsurface Scattering or Clear Coat—is actually being applied to the pixel. This helps you eliminate confusion when an effect appears missing despite being enabled in the Material.
Inspect HDR Luminance and Color
Check the HDR section to see the raw luminance values before tone mapping. If a pixel is “clipping” to white, seeing the underlying HDR values can help you eliminate blown-out highlights by adjusting your light intensity or post-processing volume settings.
Use ‘Escape’ to Freeze Data
When hovering over a specific point of interest, press Escape. This freezes the data fields in the inspector, allowing you to examine the numbers without the cursor moving. This practice helps you eliminate accidental data changes while you are trying to read complex coordinate values.
Identify Indirect Irradiance Issues
If an area is unexpectedly dark in the shadows, look at the Indirect Irradiance field. If this value is near zero, it indicates that your Global Illumination (Lumen or Lightmass) isn’t reaching that pixel. This helps you eliminate “black shadow” bugs in your level lighting.
Clean Up Debug Overlays on Elimination
When you are finished with your debugging session (the “elimination” of the investigation task), close the Pixel Inspector window. Keeping it open can incur a slight performance cost because the engine continues to track buffer data under the cursor; closing it helps you eliminate unnecessary editor overhead during high-performance playtests.