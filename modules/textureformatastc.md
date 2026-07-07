---
layout: default
title: TextureFormatASTC
---

<!-- ai-generation-failed -->

<h1>TextureFormatASTC</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/TextureFormatASTC/TextureFormatASTC.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DerivedDataCache, ImageCore, TextureBuild, astcenc</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ements support for the Adaptive Scalable Texture Compression (ASTC) format, primarily used for mobile and modern console platforms.

Description and Purpose

This module integrates the ASTC encoding logic into Unreal Engine’s texture building pipeline. ASTC is an industry-standard compression format that offers a superior balance between image quality and memory footprint by allowing variable bit rates through different block sizes. Its primary purpose is to provide high-fidelity texture compression for Android (OpenGL ES 3.1+ and Vulkan), iOS, and Nintendo Switch. By utilizing this module, the engine can eliminate the need for multiple legacy compression formats (like ETC2 or PVRTC) while maintaining high visual quality for both HDR and LDR textures.

Practical Usage Tips and Best Practices
Select the Optimal Block Size
ASTC allows you to choose block sizes ranging from 4x4 (high quality, 8 bits per pixel) to 12x12 (lower quality, ~0.89 bits per pixel). Use smaller block sizes for hero assets and larger block sizes for background objects to eliminate unnecessary memory usage without sacrificing perceived quality.
Standardize on ASTC for Android
Modern Android development should prioritize ASTC over ETC2. Since over 80% of Google Play devices support ASTC, using this module as your primary target allows you to eliminate the “Multi” (ASTC/DXT/ETC2) packaging option, significantly reducing your final build size and download time.
Utilize for High Dynamic Range (HDR) Textures
Unlike many older mobile compression formats, ASTC handles HDR data natively. Use this module to compress skyboxes and lightmaps, which helps you eliminate “banding” artifacts and color clamping in mobile environments.
Adjust Encoder Speed Settings
In your Project Settings under Texture Encoding, you can set the ASTC encoder speed to “Fast,” “Normal,” or “Exhaustive.” Use “Fast” during active development to eliminate long iteration times, but switch to “Exhaustive” for your final shipping build to ensure the highest possible quality.
Audit Alpha Channel Impact
ASTC handles alpha channels much more efficiently than legacy formats. You no longer need to pack alpha into a separate texture to avoid quality loss; the TextureFormatASTC module will manage the bit distribution across channels to eliminate the blocky artifacts typically seen in mobile transparency.
Check for Normal Map Quality
When compressing Normal Maps, ensure the Compression Settings are set to “Normalmap (BC5, ASTC/ETC2).” This tells the module to use a specialized encoding path that preserves vector directionality, helping you eliminate lighting glitches on smooth surfaces.
Profile Memory with “stat Texture”
Use the stat Texture console command on your target mobile device to verify that your ASTC textures are occupying the expected amount of memory. This allows you to identify “uncompressed” textures that may have slipped through, helping you eliminate unexpected VRAM pressure.
Leverage for Nintendo Switch Development
ASTC is the native and preferred texture format for the Nintendo Switch. Using this module for Switch titles is essential to eliminate the performance overhead of decompressing non-native formats at runtime and to ensure the best possible use of the console’s limited memory bandwidth.