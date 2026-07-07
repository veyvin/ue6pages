---
layout: default
title: TextureBuild
---

<!-- ai-generation-failed -->

<h1>TextureBuild</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/TextureBuild/TextureBuild.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DerivedDataCache, ImageCore, ImageWrapper, TextureBuildUtilities, TextureCompressor, TextureFormat</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

endering pipeline responsible for the background compilation, encoding, and compression of texture assets.

Description and Purpose

This module serves as the management layer for the Texture Build Worker, which handles the heavy lifting of converting raw source images into platform-specific formats (like BC7, ASTC, or DXT). Its primary purpose is to decouple the texture processing from the main editor thread, allowing for asynchronous builds that don’t freeze the user interface. By coordinating with the Derived Data Cache (DDC) and third-party encoders like Oodle Texture, this module ensures that textures are optimized for the target hardware’s memory and bandwidth requirements. This allows the engine to eliminate long wait times when importing large batches of high-resolution assets.

Practical Usage Tips and Best Practices
Ensure Power-of-Two Dimensions
The TextureBuild module requires textures to have dimensions that are a power of two (e.g., 1024x1024) to generate mipmaps and apply block compression. If you use non-power-of-two textures, the module may pad the memory or fail to compress, so stick to this standard to eliminate unnecessary GPU memory waste.
Configure Oodle RDO (Lambda)
Unreal Engine uses Oodle Texture for compression. You can adjust the Lambda value in the Texture Editor (under the Oodle tab) to trade visual quality for disk size. A higher Lambda value allows the module to eliminate more data during the build process, leading to smaller packaged builds.
Audit sRGB vs. Linear Settings
The encoding path used by the module depends entirely on the sRGB checkbox. For data maps (Normal, Roughness, Mask), ensure sRGB is unchecked. This allows the module to use the correct compression algorithm (like BC5 for Normals) and eliminate lighting artifacts caused by incorrect gamma math.
Optimize via Texture Groups (LOD Groups)
Instead of setting compression settings manually for every asset, assign textures to a Texture Group (e.g., World, Character, UI). The TextureBuild module uses these presets to eliminate inconsistency in compression quality across your project.
Leverage Virtual Texturing for 8K+ Assets
For extremely large textures, enable Virtual Texturing. The build module will then process these as tiles rather than a single massive blob, which helps you eliminate the high memory overhead and “out of memory” crashes during the build phase.
Monitor Build Progress in the Status Bar
When importing many assets, keep an eye on the “Building Textures” notification in the bottom right. Avoid closing the editor or launching a “Cook” while this is active to eliminate the risk of corrupting the Derived Data Cache (DDC).
Use Sharpening Filters for Mips
Within the Texture Editor, you can select different Mip Gen Settings. Using a “Sharpen” filter (Sharpen 0 through 10) allows the build module to preserve fine details in distant objects, helping you eliminate the blurry look often associated with standard mipmap downsampling.
Clean the DDC if Corruption Occurs
If textures appear incorrectly colored or display a “red/green” checkerboard after a build, it usually indicates a corrupted cache. Deleting the DerivedDataCache folder forces the TextureBuild module to re-encode all assets from source, which will eliminate persistent visual glitches.