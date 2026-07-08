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

Arm ASTC Encoder. It is a low-level library integrated into the engine’s texture cooking pipeline to handle Adaptive Scalable Texture Compression (ASTC), which is the industry standard for modern mobile and Vulkan-based platforms.

Description

The module is located in Engine/Source/ThirdParty/astcenc. It is not used during gameplay; rather, it is a critical “Cooker” component. When you package a project for Android or iOS, this module is invoked to compress high-resolution textures into a format that the mobile GPU can sample directly, significantly reducing memory bandwidth and storage footprint without a heavy loss in visual fidelity.

Practical Usage Tips and Best Practices
1. Prioritize ASTC for Vulkan Projects

If your project targets modern Android devices using the Vulkan API, ensure ASTC is your primary texture format. In Project Settings > Android, set the ASTC Priority higher than ETC2 or DXT (usually 0.9 by default). ASTC offers significantly better quality-to-size ratios, which helps eliminate visual artifacts like blockiness in gradients.

2. Fine-Tune Block Size for Quality vs. Size

ASTC compression works on variable block sizes (e.g., 4x4, 6x6, 8x8).

4x4: Highest quality, highest memory usage (8 bits per pixel). Use for Normal Maps and critical UI elements.
8x8: Lower quality, significantly smaller file size (2 bits per pixel). Use for distant environmental textures or low-detail masks. You can adjust these per-texture or via Texture Groups in your BaseDeviceProfiles.ini.
3. Control Compression Speed in Project Settings

In the Unreal Editor, navigate to Project Settings > Texture Encoding. You can choose between Fast, Medium, and Final (Thorough) encode speeds.

Use Fast for daily development to reduce iteration and cook times.
Use Final for your release builds to allow the astcenc module to spend more time finding the optimal bit distribution, which can eliminate subtle “noise” in your textures.
4. Manage Alpha Channel Efficiency

ASTC is highly efficient at handling alpha channels. Unlike older formats (like ETC1) that required a separate texture for alpha, ASTC handles RGBA in a single pass. If a texture does not need alpha, ensure the Compression Settings in the Texture Editor are set to TC_Default and Has Alpha is unchecked; this allows the encoder to reallocate those bits to the RGB channels for higher clarity.

5. Verify Texture Sizes are Power of Two

While ASTC technically supports non-power-of-two (NPOT) textures, the astcenc module and the mobile hardware operate most efficiently with Power of Two dimensions. Using NPOT textures can sometimes lead to padding or performance penalties during the cook process. Always aim for 512, 1024, or 2048 dimensions to ensure the best compression alignment.

6. Use Normal Map Specific Compression

For normal maps, always set the Compression Settings to TC_Normalmap. The astcenc module will use a specialized mode (usually encoding the X and Y axes into specific channels) to ensure that the lighting vectors remain accurate. Failing to do this will result in “swirly” or pixelated lighting on your mobile assets.

7. Profile Cook Times with Unreal Insights

Compressing large batches of textures with astcenc can be time-consuming. Use Unreal Insights or the -stats commandlet during a cook to identify which textures are taking the longest to encode. If specific assets are causing a bottleneck, consider reducing their resolution or lowering their individual ASTC quality setting.

8. Evaluate Memory Elimination

After packaging, use the listtextures console command on the mobile device to see the actual memory footprint of your ASTC assets. This helps you verify that your block size choices are effectively reducing memory usage. By optimizing these settings, you can eliminate memory-related crashes on lower-end mobile devices with limited RAM.