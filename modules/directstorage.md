---
layout: default
title: DirectStorage
---

<!-- ai-generation-failed -->

<h1>DirectStorage</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Windows/DirectStorage/DirectStorage.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

mance I/O technology into Unreal Engine. It is designed to bypass CPU bottlenecks by allowing the GPU to request and decompress asset data directly from NVMe storage.

What it is and What it’s used for

Historically, loading a texture involved moving data from the disk to the CPU, decompressing it using CPU cycles, and then sending it to the GPU. On modern hardware, this creates a massive bottleneck. The DirectStorage module enables a more efficient pipeline where data is streamed in parallel batches, utilizing the high bandwidth of NVMe SSDs.

Primary uses include:

Virtual Texture Streaming: Drastically reducing the time it takes for high-resolution textures to “pop in” when using Runtime Virtual Texturing.
Nanite Data Management: Speeding up the streaming of Nanite geometry clusters as the camera moves through a highly detailed world.
Hitch Reduction: Moving decompression tasks (like GDeflate) to the GPU, which allows the CPU to focus on game logic and physics, resulting in the elimination of frame stutters during heavy loading.
Open World Performance: Supporting the massive data throughput required for World Partition transitions in large-scale environments.
Practical Usage Tips and Best Practices
1. Enable via the Project Settings

DirectStorage is often provided as a plugin. To use it, you must enable the DirectStorage Plugin in the editor and ensure your project is targeting DirectX 12 (SM6). It will not function on older RHI versions like DX11.

2. Use GDeflate Compression

DirectStorage is most effective when combined with GDeflate, a GPU-friendly compression format. Ensure your project’s compression settings are configured to use GDeflate for bulk data; this allows the GPU to decompress the assets directly, freeing up the CPU for other tasks.

3. Targeted Platforms (PC and Xbox)

DirectStorage is a Windows and Xbox-specific technology. For PC builds, the end-user must have an NVMe SSD and a DirectX 12 GPU with Shader Model 6.0 support to see the full benefits. The engine will automatically fall back to standard I/O if these hardware requirements are not met.

4. Monitor with “Stat DirectStorage”

Use the console command stat DirectStorage to view real-time I/O performance. This overlay displays current bandwidth, the number of active requests, and decompression latency. It is essential for identifying whether your storage throughput is meeting the needs of your level’s density.

5. Batch Your I/O Requests

DirectStorage performs best when handling many small requests in a single batch rather than a few massive, serialized requests. The engine’s Streaming Manager handles much of this automatically, but as a developer, you should avoid triggering massive synchronous loads during gameplay which can bypass the DirectStorage benefits.

6. Combine with Nanite and Lumen

DirectStorage is a force multiplier for Nanite. Because Nanite constantly streams geometry patches based on the camera view, the high-speed throughput provided by this module ensures that even the most complex scenes load with minimal latency and high fidelity.

7. Verify NVMe Driver Compatibility

For development machines, ensure you are using the latest NVMe drivers from the hardware manufacturer. Standard Windows “Standard NVM Express Controller” drivers may not fully support the bypass IO features required for the module to achieve its maximum rated speed.

8. Strategic Elimination of Loading Screens

With the high throughput of DirectStorage, you can design levels that transition seamlessly without traditional loading screens. By utilizing World Partition and fine-tuning your streaming distances, you can leverage the module to load assets fast enough that the player never perceives the data transfer.