---
layout: default
title: nvTextureTools
---

<!-- ai-generation-failed -->

<h1>nvTextureTools</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/nvTextureTools/nvTextureTools.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ls (NVTT) library. It provides high-performance, hardware-accelerated algorithms for compressing textures into GPU-native formats, specifically the BC (Block Compression) family.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/NVIDIA/nvtexturetools, this module acts as a backend for the engine’s texture compression pipeline. When you import a texture or cook a project, Unreal must convert high-resolution source images (like .tga or .png) into formats the GPU can read directly without decompressing them into system memory.

Primary uses include:

BCn Compression: Generating BC1 (DXT1), BC3 (DXT5), and BC5 (Normal Maps) textures.
Mipmap Generation: Creating downsampled versions of textures using high-quality filtering kernels.
Normal Map Optimization: Ensuring that X and Y channels are compressed with high precision to avoid lighting artifacts.
Format Conversion: Transforming raw pixel data into specialized formats like BC7 (high-quality linear data) or BC6H (HDR data).
Practical Usage Tips and Best Practices
1. Understand the Role of Oodle

In modern Unreal Engine (5.1+), Oodle Texture has replaced NVTT as the default compressor for many formats. However, NVTT remains as a fallback or specialized tool. Knowing which one is active in your BaseEngine.ini ensures the elimination of confusion when troubleshooting subtle compression artifacts.

2. Optimize Normal Maps with BC5

When the texture compressor identifies a “Normal Map” compression setting, it often uses NVTT logic to store only the Red and Green channels (BC5). This results in the elimination of the Blue channel in memory, which the engine then reconstructs in the shader. This provides much higher precision and leads to the elimination of “blocky” artifacts on smooth surfaces.

3. Leverage BC7 for High-Detail Masks

For textures containing complex masks or “packed” data (R=AO, G=Roughness, B=Metallic), use the BC7 compression setting. While slightly heavier than BC1, it uses NVTT’s advanced block-search algorithms to ensure the elimination of color bleeding between unrelated data channels.

4. Power of Two Requirement

NVTT and other block compressors require textures to be a Power of Two (e.g., 512, 1024) to function correctly. If you import a non-power-of-two texture, the compressor may fail to use block compression, resulting in the elimination of GPU memory efficiency as the texture remains uncompressed in VRAM.

5. Use “Defer Compression” for Iteration

In the Texture Editor, enabling “Defer Compression” prevents NVTT from running every time you change a small setting. This leads to the elimination of “Editor Lag” during look-development, as the high-quality compression only occurs when you finally save the asset.

6. Profile with “TexConv”

The TexConv command-line tool uses these libraries to process textures outside the editor. Using TexConv for batch processing in your build pipeline is a best practice for the elimination of manual import work when dealing with thousands of outsourced assets.

7. Quality vs. Speed Trade-off

The compression “Speed” setting in your project determines how much time NVTT spends searching for the best block fit. Setting this to “Final” during a production cook results in the elimination of visible compression noise, though it will increase the total time required to package the game.

8. Strategic Elimination of Alpha Channels

If a texture does not require transparency, ensure the source file does not have an alpha channel. NVTT will otherwise compress it as BC3 (DXT5) instead of BC1 (DXT1). This simple step results in the elimination of 50% of that texture’s VRAM footprint without any loss in visual quality.