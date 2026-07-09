---
layout: default
title: ProResLib
---

<!-- ai-generation-failed -->

<h1>ProResLib</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Apple/ProResLib/ProResLib.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ides the core implementation for the Apple ProRes video codec. It serves as the underlying backend for both the Apple ProRes Media player (for high-bitrate video playback) and the Movie Render Queue (for high-fidelity video exports).

ProRes is an industry-standard, “intermediate” codec used primarily in film and virtual production. It offers a balance between high visual quality (supporting up to 12-bit depth) and relatively low CPU overhead during decoding compared to highly compressed formats like H.264/H.265.

Practical Usage Tips & Best Practices
1. Enable the Apple ProRes Media Plugin

The ProResLib module is not active by default in all project templates.

Best Practice: Navigate to Edit > Plugins and search for Apple ProRes Media. You must enable this plugin and restart the editor to gain access to ProRes export options in the Movie Render Queue. This ensures the elimination of “Missing Plugin” errors when attempting to render master files.
2. Select the Correct Flavor (422 vs. 4444)

ProRes comes in several “flavors” that vary in bitrate and feature support.

Tip: Use ProRes 422 HQ for standard high-quality masters. Use ProRes 4444 or 4444 XQ only when you need to preserve an Alpha channel or perform heavy color grading. Choosing the appropriate flavor results in the elimination of unnecessarily massive file sizes for simple preview renders.
3. Enable Alpha Channel Support in Project Settings

Even if you select ProRes 4444, the engine will not export transparency by default.

Best Practice: Go to Project Settings and search for Enable Alpha Channel Support in Post Processing. Set this to Allow through Tonemapper. This configuration leads to the elimination of solid black backgrounds in your renders, allowing for clean compositing in external software.
4. Manage High Disk I/O Requirements

ProRes files have extremely high bitrates (hundreds of Mbps).

Tip: Always render ProRes files to a high-speed NVMe SSD rather than a mechanical hard drive or a network share. Using fast storage facilitates the elimination of “stuttering” during playback and prevents the Movie Render Queue from stalling while waiting for disk writes.
5. Use for Virtual Production “Plates”

Because ProRes is optimized for multi-stream playback, it is the ideal format for “plates” used on LED volumes.

Best Practice: Convert your background videos to ProRes before importing them into the Media Framework. Using a professional intermediate codec results in the elimination of “macroblocking” and compression artifacts that are often visible when using MP4s on large-scale displays.
6. Utilize for 10-bit and 12-bit HDR Workflows

Standard video formats often clip color data, leading to “banding” in gradients like skies.

Tip: Use ProRes 4444 to maintain the full dynamic range of your scene. This leads to the elimination of color banding and ensures that your HDR highlights remain intact when moving from Unreal Engine to a color grading suite like DaVinci Resolve.
7. Verify Frame Rate Consistency

ProRes is a “constant frame rate” format, which is essential for syncing with audio and external hardware.

Best Practice: In the Movie Render Queue, ensure your output frame rate matches your sequence settings exactly. Proper synchronization leads to the elimination of “drift” where the video and audio slowly fall out of sync over long durations.
8. Monitor CPU vs. GPU Balance

While ProRes is easier to decode than H.265, it still relies on the CPU for the final “unpacking” of the frames.

Tip: If you experience low frame rates when playing back 8K ProRes video in the editor, check your CPU usage. Identifying these bottlenecks facilitates the elimination of playback hitches by allowing you to proxy the footage or upgrade your processor.