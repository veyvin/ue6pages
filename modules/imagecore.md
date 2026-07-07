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

Unreal Engine designed for the direct manipulation of raw pixel data.

Description and Purpose

ImageCore serves as the engine’s primary “pixel engine” for CPU-side image processing. Unlike high-level UTexture2D assets, which are managed by the renderer and GPU, this module operates on the FImage class—a lightweight container for raw memory buffers. It is used extensively in texture importing pipelines, material baking, and procedural generation. Its core functionality includes converting between different pixel formats (e.g., 32-bit Float to 8-bit BGRA), resizing images, cropping, and managing color space transformations before data is finalized for use in the engine.

Practical Usage Tips and Best Practices
Use FImage for CPU-Side Processing
When you need to modify pixels manually, avoid using raw TArray<uint8> buffers. Wrap your data in an FImage object to leverage built-in metadata (width, height, format). This allows you to use optimized utility functions and helps you eliminate manual stride and offset math errors.
Prefer Move Semantics for Large Buffers
FImage supports move constructors and assignment. When passing high-resolution images between functions, use MoveTemp(MyImage) to transfer ownership of the underlying buffer. This allows you to eliminate expensive deep copies of multi-megabyte image data.
Leverage Built-in Color Space Conversion
The module provides standardized functions to convert between Linear and Gamma (sRGB) spaces. Using FImageCore::CopyTo with the correct format flags ensures your color math remains consistent with the engine’s rendering standards and helps you eliminate “washed out” or overly dark texture artifacts.
Optimize with FImageCore::Resize
If you need to generate thumbnails or low-resolution previews on the fly, use the Resize utility. It supports high-quality filtering methods like Bilinear or Area. Pre-scaling images on the CPU before creating a UTexture2D helps you eliminate unnecessary GPU memory pressure and bandwidth usage.
Validate Pixel Formats via ERawImageFormat
Always check the Format member before processing. The module handles everything from BGRA8 to RGBA32F. Performing a check against ERawImageFormat before a loop helps you eliminate buffer overflows and crashes caused by treating a 32-bit float array as 8-bit integers.
Utilize Linear Image Processing for Accuracy
For operations like blending or blurring, always convert your images to a linear floating-point format first. Performing math in a non-linear gamma space leads to inaccurate results; using RGBA32F during processing helps you eliminate dark fringes and color shifting in your textures.
Avoid Frequent Allocations in Loops
If you are processing a sequence of images (such as for a video or sprite sheet), reuse the same FImage container. Calling FImage::Init with existing dimensions often allows the module to reuse the allocated memory, which helps you eliminate the performance hit of constant memory allocation and deallocation.
Check Image Validity Before Export
Always use MyImage.IsValid() before attempting to bake or save to disk. This ensures the dimensions are non-zero and the buffer is successfully allocated, helping you eliminate null-pointer exceptions in your procedural asset pipelines.