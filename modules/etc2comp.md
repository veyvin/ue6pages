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

2comp” library, a tool specifically designed for compressing textures into the ETC2 (Ericsson Texture Compression 2) format. In Unreal Engine, this module is a critical component of the Android and mobile cook pipeline.

It is used to convert standard texture assets into compressed formats that are natively supported by OpenGL ES 3.0+ and Vulkan-capable mobile devices. This module is essential for the elimination of excessive memory usage and storage bloat on mobile platforms while maintaining high visual fidelity.

Practical Usage Tips and Best Practices
1. Prioritize ASTC Over ETC2 for Modern Devices

While the etc2comp module is robust, over 80% of modern Android devices now support ASTC. If your target hardware allows it, use ASTC for better quality-to-size ratios. Use ETC2 only as a fallback to ensure the elimination of compatibility issues on older OpenGL ES 3.0 devices.

2. Optimize Cook Times with Multithreading

Texture compression is a CPU-intensive process. The etc2comp library is designed to be multithreaded. Ensure your build machine has a high core count to speed up the cooking process. This facilitates the elimination of long “bottlenecks” during the packaging of large mobile projects.

3. Manage Alpha Channels Carefully

ETC2 supports alpha channels, but they require more data than RGB-only textures. If a texture does not require transparency, ensure the Compression Settings in the Texture Editor are set to “TC Default” or “TC Displacementmap” (RGB) to assist in the elimination of wasted memory in the alpha block.

4. Use “Android Multi” Packaging with Caution

Selecting “Android Multi” in the packaging settings will cook textures for every format (ETC2, ASTC, DXT). This significantly increases your build size. For a smaller download, package for a specific format or use the Google Play Asset Delivery system to facilitate the elimination of redundant texture data in the final APK.

5. Monitor Texture Group Max Sizes

Mobile GPUs have stricter limits on texture dimensions. Use Texture Groups in your Project Settings to clamp maximum resolutions for mobile. This works alongside the etc2comp module to ensure the elimination of “Out of Video Memory” crashes on lower-end mobile handsets.

6. Audit Textures for “Power of Two” Dimensions

For the most efficient compression via etc2comp, textures should be in power-of-two dimensions (e.g., 512x512, 1024x1024). Non-power-of-two textures may be padded or uncompressed, which leads to the elimination of the performance benefits provided by hardware-accelerated texture formats.

7. Leverage Device Profiles for Quality Control

Use Device Profiles to override texture compression quality based on the specific Android device tier. You can set lower quality compression for “low-end” profiles to speed up loading times, aiding in the elimination of long initial load screens for players on older hardware.

8. Verify Compression via the “Mobile Previewer”

Always test your textures using the Mobile Previewer (ES3.1/Vulkan) in the editor. This simulates how the etc2comp module will represent your colors on the device. Checking for compression artifacts early leads to the elimination of visual “banding” or “blockiness” before you send the build to QA.