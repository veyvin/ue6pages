---
layout: default
title: detex
---

<!-- ai-generation-failed -->

<h1>detex</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Android/detex/detex.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at provides high-performance decompression for various texture formats. It is a critical low-level utility used by the engine to read compressed texture data back into a raw pixel format.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/detex, this module is a C-based library wrapped for Unreal Engine. While Unreal uses specialized compressors (like Oodle or NVTT) to create textures, it uses Detex primarily for the reverse process: decompressing block-compressed data into RGBA buffers.

Primary uses include:

Editor Visualization: Decompressing textures so they can be displayed in the Texture Editor or UI widgets that require raw pixel access.
Platform Translation: Converting textures from one compressed format to another during the “Cooking” process.
Thumbnail Generation: Powering the creation of Content Browser thumbnails by decompressing the source asset.
Format Support: Providing a unified interface for handling BC1–BC7 (DirectX), ETC1–ETC2 (Android), and PVRTC (Legacy iOS) formats.
Practical Usage Tips and Best Practices
1. Use via FImageCore for Safety

While you can call the Detex API directly, it is a best practice to use the ImageCore module (e.g., FImage or FImageCore::Decompress). These wrappers handle the memory allocation and pixel format mapping automatically, reducing the risk of memory leaks or buffer overflows when interacting with the Detex C-code.

2. Verify Format Compatibility

Before calling a decompression routine, always verify that the texture format is supported by Detex. It is specifically designed for block-compressed formats. Attempting to pass uncompressed or “raw” formats ( like B8G8R8A8) to Detex functions is unnecessary and will lead to the elimination of execution efficiency.

3. Handle BC6H and BC7 with Care

Detex is one of the few libraries that robustly handles high-bit-depth BC6H (HDR) and BC7 (High Quality) textures. When writing custom C++ tools to analyze HDR textures, ensure you are utilizing the Detex pathways to maintain the floating-point precision of your color data.

4. Pre-allocate Buffers Correctly

If you must call detexDecompressBlock directly, you are responsible for calculating the output buffer size. A standard 4x4 block of compressed data always decompresses into 16 pixels. Ensure your destination buffer is pre-allocated to accommodate 16 * BytesPerPixel to avoid memory corruption.

5. Parallelize Batch Decompression

Decompressing large textures (like 4K or 8K maps) is CPU intensive. If you are writing a tool that processes many textures, use Unreal’s ParallelFor to run Detex decompression tasks across multiple CPU cores. Detex is stateless at the block level, making it “thread-safe” for concurrent block processing.

6. Use for Custom Asset Inspectors

If you are building an Editor Utility Widget or a C++ tool that needs to “Read Pixels” from a texture on disk (which is usually compressed), Detex is the engine’s preferred way to get that data. Access the SourceArt of the UTexture2D, identify the format, and pass it to Detex to get a raw array you can analyze.

7. Monitor Decompression Overhead

Be aware that decompression is much slower than simple memory copying. If your tool feels sluggish when opening many assets, ensure you are only decompressing the specific Mip level required (e.g., a low-res Mip for a thumbnail) rather than the full-resolution Mip 0.

8. Strategic Elimination of Alpha Errors

When decompressing formats like BC3 or BC7 that contain alpha, verify if the texture was imported with “Alpha as Coverage” or “Compress without Alpha.” Using Detex to decompress a texture that lacks an alpha channel into an RGBA8 buffer will result in the alpha channel being filled with 255 (opaque) by default.