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

le for the background processing and compilation of texture data. It serves as the low-level worker implementation for the TextureBuild system, handling asynchronous tasks such as generating mipmaps, calculating texture streaming data, and preparing tiles for Virtual Textures. It is a critical component of the engine’s Derived Data Cache (DDC) pipeline, ensuring that raw source images are converted into engine-ready formats without freezing the Editor UI.

Practical Usage Tips & Best Practices
1. Understand the Role in DDC

This module does not “create” textures; it “builds” them. When you import a TGA or EXR file, this worker is triggered to compress the data and generate the necessary mips.

Best Practice: Ensure your Derived Data Cache is on a fast SSD. Because this worker frequently reads and writes large amounts of data during the build process, a slow drive will become a bottleneck for the entire texture pipeline.
2. Monitor Virtual Texture Tiling

The BaseTextureBuildWorker is heavily involved in the “cooking” of Virtual Textures (VT). It breaks large textures into small, manageable tiles. If you notice long hitches when saving a Material that uses VT, it is likely this worker processing the new tile data in the background.

3. Leverage Multi-Core Parallelism

The texture build system is designed to be highly parallel. The engine will spawn multiple instances of this worker based on your CPU core count.

Tip: If you are part of a large team, use Zen Dashboard or a Shared DDC. This allows one developer’s worker to build the texture data and upload it to a network drive, effectively resulting in the elimination of build times for every other developer on the project.
4. Configure Texture Streaming Data

Every time a Material is saved, this worker recomputes the texture streaming data (UV channel scales and indices).

Best Practice: If your streaming data is inaccurate (textures appearing blurry in-game), run the Build Texture Streaming command from the Build menu. This forces the worker to perform a comprehensive pass on all level actors to ensure the resolution requirements are correctly calculated.
5. Optimize Build Speeds in Project Settings

In Project Settings > Texture Encoding, you can adjust the “Encode Speed.”

Tip: Set this to Fast during active development. This tells the worker to use lower-complexity compression algorithms, which speeds up the import and save process. Switch to Final only when preparing a shipping build to ensure maximum visual fidelity.
6. Handle Elimination of Stale Data

Sometimes the DDC can become corrupted, leading to strange visual artifacts. You can trigger the elimination of stale texture builds by using the command line -ddc=None (to bypass) or by manually clearing the DerivedDataCache folder in your project directory. This forces the BaseTextureBuildWorker to re-generate all assets from their source files.

7. Dependency Management in Build.cs

Since this is an internal worker module, you should almost never need to list it in your PublicDependencyModuleNames. If you are writing custom editor tools that require manual texture building, include TextureBuild instead, as it provides the higher-level API that communicates with this worker.

8. Verify Worker Success in Logs

If textures are failing to appear or show the “Default Grid” pattern, check the Output Log for entries under LogTexture. If the BaseTextureBuildWorker encountered a memory limit or an unsupported file format, the specific error—such as an out-of-memory (OOM) error during a massive 8K texture build—will be detailed there.