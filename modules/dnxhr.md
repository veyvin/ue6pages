---
layout: default
title: DNxHR
---

<!-- ai-generation-failed -->

<h1>DNxHR</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/AvidDNxHD/DNxHR/DNxHR.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

gh-performance video integration for Unreal Engine. It enables the engine to handle Avid’s professional-grade, lossy-but-high-quality video codecs, specifically designed for high-resolution content up to 8K.

In UE5, this module is primarily utilized within the Movie Render Queue (MRQ) for high-end cinematic exports and the Media Framework for playing back high-bitrate video textures in-engine. It is the industry-standard choice for the elimination of the heavy compression artifacts often found in H.264/H.265 formats.

Practical Usage Tips and Best Practices
1. Enable the Plugin via the Editor

The DNxHR module is not active by default. Navigate to Edit > Plugins, search for Avid DNxHR/DNxMXF Media Plugin, and enable it. You must restart the editor to complete the process. This step is required for the elimination of “Unsupported Format” errors when attempting to use .mxf files.

2. Use for Post-Production Intermediate Renders

When rendering cinematics for further editing in Premiere Pro or DaVinci Resolve, select Avid DNx [8bit] in the Movie Render Queue. This provides a high-fidelity video file in an .mxf container, which allows for the elimination of the massive disk space requirements of uncompressed image sequences while maintaining professional quality.

3. Manage Encoding Threads for Performance

In the Movie Render Queue settings for DNx, you can adjust the Number of Encoding Threads. Increasing this number utilizes more of your CPU to speed up the export process. Tuning this setting correctly leads to the elimination of long render bottlenecks during large cinematic exports.

4. Export Audio Separately

Note that the DNxHR module currently focuses on video data and does not export embedded audio. To ensure a complete cinematic delivery, add a .wav Audio setting to your Movie Render Queue configuration. This practice assists in the elimination of silent video files and allows for precise audio syncing in post-production.

5. Toggle Compression for Lossless Needs

The module allows you to enable or disable compression. If you require a mathematically lossless file for archival purposes, disable the Use Compression checkbox. While this increases file size, it facilitates the elimination of any potential data loss during the export of high-dynamic-range content.

6. Optimize for Media Plate Playback

If using DNxHR files as textures within your level via a Media Plate, ensure your storage medium (SSD/NVMe) has enough bandwidth. Because DNxHR files have much higher bitrates than standard web video, high-speed storage is essential for the elimination of playback stuttering or frame dropping during cinematics.

7. Standardize on 8-bit Precision

Currently, the Avid DNx implementation in Unreal Engine supports 8-bit precision. When prepping source footage in external tools for use in Unreal, keep this limitation in mind to ensure the elimination of unexpected color shifting or bit-depth conversion errors during import.

8. Verify MXF Compatibility

The DNxHR module outputs files using the .mxf (Material Exchange Format) container. Ensure your target playback software or video editor is updated to support this container. Proper pipeline verification before a major render leads to the elimination of “File Not Found” or “Codec Missing” errors at the end of a production cycle.