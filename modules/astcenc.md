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

mpression) Encoder, a high-efficiency texture compression toolset. In Unreal Engine, this module is a critical component of the mobile cooking pipeline. It is responsible for converting raw textures into the ASTC format, which is the industry standard for modern Android and iOS devices due to its ability to balance high visual fidelity with extremely low memory footprints.

Practical Usage Tips & Best Practices
1. Select the Optimal Encoder (Intel vs. ARM)

In Project Settings > Cooker > Textures, you can choose between the Intel ISPC and ARM encoders.

Best Practice: Use the Intel ISPC encoder for faster build times on Windows/Linux development machines. It uses SIMD instructions to accelerate the ASTC compression process significantly without sacrificing quality.
2. Choose the Correct Block Size

ASTC allows you to choose block sizes ranging from 4x4 (high quality, 8 bits per pixel) to 12x12 (low memory, ~0.89 bits per pixel).

Tip: Use 4x4 or 5x5 for Normal Maps and UI elements to avoid compression artifacts. Use 8x8 or 10x10 for Albedo/Diffuse textures of background environment assets to maximize memory savings.
3. Configure ASTC Quality Levels

In the Texture Asset Editor, you can set the “ASTC Compression Quality.”

Best Practice: Keep this set to Fast or Medium during daily development to ensure quick iteration. Switch to Thorough or Exhaustive only for final “Shipping” builds, as higher quality levels exponentially increase the time required to cook the project.
4. Enable ASTC HDR Profile for High-End Mobile

Unreal Engine supports the ASTC HDR profile. If you are developing for high-end mobile devices (like those with Apple A13+ or Adreno 660+ GPUs), you can enable HDR compression for skyboxes and emissive textures to maintain high dynamic range lighting without the massive memory cost of uncompressed floats.

5. Prioritize ASTC in Multi-Format Builds

If you are packaging for “Android Multi” (which includes ETC2, DXT, and ASTC), ensure the ASTC Priority is set to the highest value (default is 0.9) in Project Settings. This ensures that if a device supports ASTC, the engine will prioritize the elimination of lower-quality formats in favor of the ASTC textures.

6. Utilize the Texture Encoding Project Settings

In UE 5.4+, you can use the Texture Encoding settings to define different encode speeds for “Shared Linear” vs “Final” builds. This allows you to force the astcenc module to use “Fast” settings for your team’s internal playtests while reserving “Final” quality for the build machine.

7. Monitor Build Times via Cooker Logs

ASTC compression is one of the most time-consuming parts of the cooking process. If your builds are slow, check the cooker logs for astcenc activity. If the elimination of long build times is a priority, consider reducing the “Maximum Texture Size” for non-essential assets, which reduces the total number of blocks the encoder must process.

8. Avoid Re-compressing Small Textures

For very small textures (e.g., 16x16 or 32x32), the overhead of ASTC block structures can sometimes result in less efficiency or visible “bleeding.” In these rare cases, consider using an uncompressed format or a simple 4x4 block size to ensure the visual integrity of critical small-scale icons or masks.