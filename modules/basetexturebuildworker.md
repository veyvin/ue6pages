---
layout: default
title: BaseTextureBuildWorker
---

<!-- ai-generation-failed -->

<h1>BaseTextureBuildWorker</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Programs/BaseTextureBuildWorker/BaseTextureBuildWorker.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>TextureBuildWorker</code></span></li><li><span class="label">依赖</span><span class="value">Core, TextureBuild, TextureBuildUtilities, TextureFormat, TextureFormatASTC, TextureFormatETC2, TextureFormatOodle, TextureFormatUncompressed</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

eal Engine’s Texture Build system. It provides the core logic for the distributed and background processing of texture assets during the cooking and encoding phases.

Description

This module is part of the modern Texture Build pipeline introduced to improve iteration times by moving heavy texture compression tasks to external worker processes. Instead of the main Unreal Editor process freezing while it compresses hundreds of textures, the BaseTextureBuildWorker handles the heavy lifting—such as DXT/BC, ASTC, or Oodle encoding—across multiple CPU cores or even remote machines. It is the “worker” half of the Director-Worker architecture used in multi-process cooking and the Derived Data Cache (DDC) generation.

Practical Usage Tips and Best Practices
1. Leverage Multi-Process Cooking

In Unreal Engine 5.x, you can enable Multi-Process Cook in your Project Settings or via command line. This module is what allows the engine to spawn multiple “cooker” instances. By utilizing these workers, you can significantly reduce the time it takes to package a project, as the workers can compress textures in parallel while the Director process handles asset serialization.

2. Configure Texture Encoding Speed

The behavior of the workers is dictated by your Texture Encoding project settings. You can choose between Fast, Medium, and Final.

Fast: Workers prioritize speed, which is great for daily development.
Final: Workers spend more CPU time to eliminate compression artifacts and find the smallest possible file size, which is essential for shipping builds.
3. Monitor Worker Health in the Output Log

If texture compression seems stuck or is failing, search your logs for “TextureBuildWorker.” If a worker process is eliminated (crashes) due to an Out-of-Memory (OOM) error, the main process will usually report it. Ensuring your machine has enough RAM for each worker (typically 2-4GB per worker) is critical to prevent these crashes.

4. Understand DDC Integration

The results produced by this module are stored in the Derived Data Cache (DDC). Once a worker has successfully built a texture, it is cached so that other developers on your team (or your build machine) don’t have to re-encode it. This eliminates redundant work across your studio.

5. Prioritize Oodle Texture Compression

Starting in UE 5.x, Oodle Texture is the default encoder for many formats. The BaseTextureBuildWorker is highly optimized for Oodle. Ensure the Oodle plugins are enabled in your project to allow the workers to produce high-quality, highly-compressible textures that reduce your final game’s download size.

6. Profile CPU Bottlenecks

Since this module is CPU-bound, having a high core-count processor is the best way to improve texture build times. Use Unreal Insights to see how many workers are active simultaneously. If you see high “idle” time, you may need to increase the number of worker processes allowed in your BaseEngine.ini or command-line arguments.

7. Handle Large Texture Sets

For massive textures (like 8K virtual textures), the BaseTextureBuildWorker may take a significant amount of time. If you have a build machine, consider using a Shared DDC (like a network drive or Zen Store). This allows the workers on the build machine to “prime” the cache, which eliminates the need for local developers to ever run these heavy encoding tasks on their own workstations.

8. Clean Up Stale Build Data

If you encounter visual corruption in your textures, it may be due to a corrupted build result in the cache. You can force the workers to restart their work by right-clicking a texture and selecting “Reimport” or by clearing your local DerivedDataCache folder. This forces the BaseTextureBuildWorker to re-generate the data from the source file, ensuring any previous errors are eliminated.