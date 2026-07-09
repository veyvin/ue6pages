---
layout: default
title: ImageCore
---

<!-- ai-generation-failed -->

<h1>ImageCore</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/ImageCore/ImageCore.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, stb_image_resize2</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Unreal Engine designed for raw image data manipulation and storage. Unlike the high-level UTexture2D system—which is tied to the GPU and the engine’s rendering pipeline—ImageCore operates on raw CPU-side pixel buffers. It provides essential structures like FImage and FImageCore for tasks such as format conversion, resizing, and linear-to-gamma space transformations. It is primarily used in asset import pipelines (like Fab), texture compression, and custom editor tools.

Practical Usage Tips & Best Practices
1. Perform Image Processing Off-Thread

Because ImageCore operates purely on CPU memory and does not interact with the GPU or the UObject system, it is inherently thread-safe for isolated operations.

Best Practice: Move heavy image operations—such as resizing or format conversion—to a background thread using the Task Graph or FRunnable. This ensures the elimination of UI freezes and frame-rate hitches that occur when processing large textures on the Game Thread.
2. Use FImage for Multi-Format Support

The FImage class acts as a flexible container that supports a wide array of pixel formats (RGBA8, RGBA16F, FloatRGBA, etc.).

Tip: When writing custom importers, load your raw data into an FImage first. Its internal utility functions allow for the elimination of manual bit-shifting and byte-math when converting exotic raw file data into an Unreal-compatible format.
3. Leverage ImageCore for Non-Power-of-Two (NPOT) Logic

While the rendering engine prefers power-of-two textures for mipmapping, UI elements and icons often require specific, non-standard dimensions.

Best Practice: Use ImageCore::Resize() to handle the scaling of these assets during the import or cooking phase. Utilizing these optimized algorithms leads to the elimination of aliasing artifacts and scaling distortions in your final UI assets.
4. Optimize via “Linear Space” Conversions

Color math performed in Gamma space is mathematically incorrect and leads to “muddy” results.

Tip: Use FImageCore::CopyTo() with the EImageColorSpace::Linear flag to convert textures before performing any blending or math operations. This ensures the elimination of color-shift bugs, particularly when processing HDR or high-precision mask data.
5. Efficiently Prepare Data for Texture Compression

Before a texture can be sent to the GPU, it usually needs to be compressed (e.g., to DXT/BC7). The ImageCore module is the standard way to feed data into the TextureCompressor module.

Best Practice: Ensure your source FImage is properly aligned and in a supported format before calling the compressor. Proper pre-processing with ImageCore results in the elimination of compression errors and artifacts during the asset cooking process.
6. Use Raw Bit-Block Transfers (Memcpy) Safely

FImage provides direct access to its underlying RawData buffer as a TArray64<uint8>.

Tip: When dealing with very large images (8K and above), use RawData.GetData() for direct memory operations. Direct buffer access, when handled carefully, facilitates the elimination of the overhead associated with frequent element-wise array copies.
7. Handle Alpha Premultiplication Correctly

Incorrectly handled alpha channels often cause “dark fringes” around the edges of transparent textures.

Best Practice: Use the ImageCore utility functions to premultiply or un-premultiply alpha channels based on your target Material’s requirements. This precise control ensures the elimination of halo artifacts in your sprites and transparent UI elements.
8. Implement “Elimination” of Temporary Buffers

Image processing often involves creating multiple intermediate buffers for different steps (e.g., Blur -> Resize -> Convert).

Tip: Explicitly call .Empty() on your FImage objects as soon as their data has been moved to a UTexture2D or written to disk. Proactive memory management leads to the elimination of temporary memory bloat, which is critical when batch-processing thousands of assets in a single editor session.