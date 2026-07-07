---
layout: default
title: TextureFormatUncompressed
---

<!-- ai-generation-failed -->

<h1>TextureFormatUncompressed</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/TextureFormatUncompressed/TextureFormatUncompressed.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, ImageCore, TextureBuild</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

des the logic for handling texture assets that require raw, pixel-perfect data without block compression.

Description and Purpose

While most textures in Unreal Engine are compressed to save memory (using formats like BC7 or ASTC), the TextureFormatUncompressed module handles the “Uncompressed” and “Vector Displacement” compression settings. It is used when an asset demands absolute fidelity where compression artifacts—even minor ones—would break the functionality of a shader or system. Its primary purpose is to pass raw data (such as B8G8R8A8 or FloatRGBA) directly to the Derived Data Cache (DDC) and eventually the GPU. By using this module for specific technical textures, you can eliminate the visual noise, banding, and data loss associated with standard lossy compression.

Practical Usage Tips and Best Practices
Use for UI and Icons with Sharp Gradients
Small UI elements and icons with transparency often suffer from “smearing” when compressed. Applying the “UserInterface2D” or “Uncompressed” setting triggers this module to keep the pixels crisp, helping you eliminate blurriness in your HUD elements.
Reserve for Vector Displacement Maps
Vector Displacement requires high precision to move vertices in three dimensions. Standard compression can shift these vectors incorrectly, leading to mesh “jitter.” Use the VectorDisplacementMap setting to eliminate geometry artifacts by ensuring the module treats the data as raw floating-point values.
Audit Memory Usage via “stat streaming”
Uncompressed textures take up significantly more memory (often 4x to 8x more) than compressed ones. Use the console command stat streaming to list loaded textures by size; this helps you eliminate oversized uncompressed assets that might be ballooning your VRAM usage.
Handle Non-Power-of-Two (NPOT) Assets
If you import a texture that is not a power of two (e.g., 305x305), the engine may default to an uncompressed format because standard block compression (DXT/BC) requires multiples of 4. Resizing these to power-of-two allows you to eliminate the high memory cost of uncompressed NPOT textures.
Utilize for Look-Up Tables (LUTs)
Color grading LUTs rely on precise color values to map shadows and highlights correctly. This module ensures that the RGB values in a LUT remain identical to the source, which helps you eliminate “flickering” or color-shifting in your post-process volume.
Prefer Grayscale (G8) for Masks
If you only need a single-channel mask and cannot afford compression artifacts, set the compression to Grayscale. This module will then store it as a single 8-bit channel, which helps you eliminate the memory overhead of a full 32-bit RGBA uncompressed texture while maintaining quality.
Be Mindful of HDR Formats
When using the RGBA16F (Half-Float) format for high-quality lightmaps or HDR textures, this module handles the high-precision data. While expensive, it is a best practice to use this for skyboxes to eliminate the banding visible in the sky during night scenes or high-contrast environments.
Disable Mipmaps if Unnecessary
For textures like UI icons or internal data buffers that are always rendered at a 1:1 scale, disable mipmap generation. This allows the module to eliminate the extra 33% memory overhead typically added by the mipmap chain.