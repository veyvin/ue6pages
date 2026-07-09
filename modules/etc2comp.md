---
layout: default
title: etc2comp
---

<!-- ai-generation-failed -->

<h1>etc2comp</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/etc2comp/etc2comp.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

th RGB and RGBA textures.

In Unreal Engine, this module is primarily utilized by the Texture Compressor during the “Cooking” process to “eliminate” the large memory footprint of uncompressed textures on mobile platforms.

1. Module Configuration

This module is part of the engine’s developer tools. If you are writing custom texture processing tools or commandlets in C++, you may need to reference it in your Build.cs:

C#
	// MyProject.Build.cs

	if (Target.bBuildEditor)

	{

	    PrivateDependencyModuleNames.Add("etc2comp");

	}
Copy code
2. Practical Usage Tips & Best Practices
Target Modern Mobile Hardware

ETC2 is supported by nearly all Android devices released in the last decade (OpenGL ES 3.0 or higher). Use this format as your baseline for Android deployments to “eliminate” the need for multiple texture formats like ATC or PVRTC, which are largely deprecated.

Balance Quality and Cook Times

The etc2comp library offers different compression effort levels. In your Project Settings > Android, you can often find settings for texture quality. High-quality settings provide better visuals (reducing “blockiness” in gradients) but significantly increase cook times. Use “Fast” for daily iteration to “eliminate” long waiting periods and “Best” for final shipping builds.

Optimize Alpha Channel Usage

Unlike ETC1, ETC2 handles alpha channels efficiently. However, if a texture does not actually need transparency, ensure the Compression Settings in the Texture Editor are set to Default (which usually results in ETC2 RGB8) rather than an RGBA variant. This “eliminates” unnecessary memory usage by half.

Leverage for UI and Sprites

Because ETC2 supports high-quality alpha, it is ideal for UI elements and 2D sprites on mobile. If you notice artifacts in your UI, verify that the texture is being compressed with the UserInterface2D setting, which directs the encoder to prioritize edge clarity, “eliminating” blurred outlines in your HUD.

Avoid “Multi” Packaging When Possible

Unreal allows you to package for “Android Multi” (which includes ETC2, ASTC, and DXTC). This creates a massive file size. Instead, identify your target hardware; since ETC2 is supported by >95% of devices, you can often “eliminate” the other formats to keep your app’s download size small.

Monitor the Derived Data Cache (DDC)

Texture compression is CPU-intensive. Once etc2comp has processed a texture, the result is stored in the DDC. If you find yourself recooking textures constantly, ensure your DDC is correctly configured (especially on build machines). This “eliminates” redundant compression tasks and speeds up the packaging process.

Use ASTC for Premium Devices

While ETC2 is the versatile standard, ASTC offers even better quality-to-size ratios. If your game targets high-end mobile devices, consider using ASTC instead. However, keep ETC2 as a fallback to “eliminate” the risk of your game failing to run on mid-range or older hardware.

Debugging Artifacts in Gradients

ETC2 can sometimes struggle with smooth gradients, leading to “banding.” If you encounter this, try to “eliminate” the banding by adding a small amount of dither to the source texture in Photoshop before importing it into Unreal. This helps the etc2comp encoder distribute the error more naturally across the blocks.