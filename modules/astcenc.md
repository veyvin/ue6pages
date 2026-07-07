---
layout: default
title: astcenc
---

<!-- ai-generation-failed -->

<h1>astcenc</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/astcenc/astcenc.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ighly optimized library for compressing textures into the Adaptive Scalable Texture Compression (ASTC) format. In Unreal Engine 5.6, it is primarily used by the texture compression sub-system to prepare assets for mobile and modern console platforms.

Description and Purpose

ASTC is the industry-standard texture format for modern mobile devices (iOS and Android) and the Nintendo Switch. The ASTCenc module allows the Unreal Engine cooker to convert standard source textures (like .tga or .png) into hardware-accelerated ASTC blocks. Its purpose is to provide a balance between visual quality and memory footprint, supporting a wide range of bitrates through varying block sizes (from 4x4 up to 12x12 pixels).

Practical Usage Tips and Best Practices
Select the Correct Encoder in Project Settings
In Project Settings > Platforms > Android, you can choose between the Intel ISPC and ARM encoders. While both use the ASTCenc logic, the Intel ISPC version is significantly faster for Windows-based development machines when cooking textures, though you should verify the visual parity for sensitive assets.
Balance Quality vs. Cook Time
You can choose between “Fast,” “Medium,” “Thorough,” and “Exhaustive” compression settings. For most projects, Medium or Thorough is the best balance. Only use Exhaustive for high-priority UI or normal maps, as it can drastically increase the time it takes to package your project.
Optimize Memory with Block Sizes
ASTC uses fixed-size blocks of bits; larger pixel block sizes (e.g., 8x8 or 10x10) result in smaller file sizes but lower quality. Use 4x4 for critical normal maps and characters, but move to 8x8 for environment world textures and 12x12 for simple UI backgrounds to eliminate unnecessary memory bloat.
Configure for Mobile Build Size
When packaging for Android, select only the ASTC format in the “Multi” texture format setting if your target devices support it (which is over 80% of active devices). This prevents the engine from cooking textures multiple times (ETC2, DXT, etc.), significantly reducing the final build size.
Utilize HDR Profile Support
ASTC is one of the few compressed formats that natively supports High Dynamic Range (HDR) textures. Use the ASTC encoder for your skyboxes and emissive maps to maintain lighting range while keeping memory usage significantly lower than uncompressed float formats.
Debug via the Texture Editor
Open any Texture asset and look at the “View” menu. You can inspect the “Compressed” size and the “Format” (e.g., COMPRESSED_ASTC_6x6). If a texture looks “blocky,” lower the block size in the Texture Group or the individual asset settings to force the encoder into a higher bitrate.
Automate Texture Group Settings
Instead of adjusting every texture, configure your DefaultDeviceProfiles.ini. Define specific block sizes for different TEXTUREGROUP entries (e.g., TEXTUREGROUP_World at 8x8 and TEXTUREGROUP_Character at 4x4) to ensure the ASTCenc module compresses your entire library consistently.
Visualizing Elimination Feedback in Low-Memory Scenarios
For mobile games where memory is tight, use high-compression (10x10 or 12x12) ASTC for “VFX sprites” like smoke or sparks. When an elimination occurs, you can trigger many of these low-memory particles without risking an “Out of Video Memory” crash, ensuring the elimination remains visually satisfying on lower-end hardware.