---
layout: default
title: stb_image_resize2
---

<!-- ai-generation-failed -->

<h1>stb_image_resize2</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/stb_image_resize/stb_image_resize2.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

into Unreal Engine that provides high-quality, high-performance image resampling and scaling algorithms.

Description and Purpose

Found within the engine’s ThirdParty directory, this module is a modern update to the original stb_image_resize. It is used by the engine to perform software-based image scaling (upsampling and downsampling) outside of the GPU. Its primary purpose is to handle pixel data manipulation during asset import, thumbnail generation, and runtime texture processing where hardware filtering is unavailable or inappropriate. By leveraging this library, Unreal Engine can eliminate common scaling artifacts like aliasing or “ringing” by using advanced filters (such as Mitchell-Netravali or Catmull-Rom) during the resizing process.

Practical Usage Tips and Best Practices
Prefer Over Legacy stb_image_resize
The “v2” version included in modern Unreal Engine (5.x) is significantly faster and more memory-efficient. When writing custom C++ image processing code, always use the stb_image_resize2.h implementation to eliminate the performance bottlenecks of the older version.
Match Colorspace Requirements
The module provides specific functions for sRGB and linear color spaces. Always use the _srgb variants when resizing diffuse textures or UI icons to eliminate “washed out” or overly dark colors caused by incorrect gamma handling during resampling.
Utilize for Editor-Side Thumbnail Generation
If you are building a custom asset type that requires a unique thumbnail, use this module to downscale high-resolution renders into the standard 256x256 thumbnail size. This ensures you eliminate jagged edges in the Content Browser, providing a professional look for your assets.
Select the Correct Filter for Downsampling
When shrinking textures (downsampling), use the Box or Lanczos filters provided by the module. These filters are designed to average pixel data intelligently, helping you eliminate moiré patterns and shimmering that occur when details are smaller than the target pixel grid.
Implement for Dynamic Texture Baking
If your game uses a system that bakes multiple textures into a single “atlas” or “sheet” at runtime, use this module to normalize the sizes of incoming images. This practice helps you eliminate resolution mismatches before the final texture is uploaded to the GPU.
Handle Alpha Channels with Care
Resizing images with transparency can often lead to “dark edges” if not handled correctly. Ensure you use the module’s alpha-aware functions to eliminate halo artifacts by correctly weighting the RGB channels by the alpha values during interpolation.
Check Memory Allocation for Buffers
The module requires a destination buffer to be pre-allocated. Always calculate the required size correctly (Width * Height * Channels) to eliminate memory corruption or out-of-bounds writes when the resizing function executes.
Use in Asynchronous Tasks
Software image resizing is CPU-intensive. Wrap your stb_image_resize2 calls in an AsyncTask or a FNonAbandonableTask to eliminate main-thread hitches, especially when processing large 4K or 8K textures in the background.