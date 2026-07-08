---
layout: default
title: DNxMXF
---

<!-- ai-generation-failed -->

<h1>DNxMXF</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/AvidDNxHD/DNxMXF/DNxMXF.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ngine to support Avid’s DNxHR and DNxHD high-definition video codecs within an MXF (Material Exchange Format) container.

Description

This module is a critical component for high-end Virtual Production, broadcast, and post-production pipelines. It allows Unreal Engine to both import and export video using Avid’s professional-grade lossy and lossless codecs. These codecs are industry standards because they provide a balance between high visual fidelity (supporting up to 8K resolution) and manageable bitrates. By using the dnxmxf module, developers can bring high-quality live-action plates into the engine with minimal compression artifacts or export cinematic renders from the Movie Render Queue (MRQ) directly into a format ready for professional editing software like Avid Media Composer or DaVinci Resolve.

Practical Usage Tips and Best Practices
1. Enable the Plugin for MRQ Support

The dnxmxf module is not enabled by default. To use it for rendering, navigate to Edit > Plugins, locate the Avid DNxHR/DNxMXF Media Plugin, and enable it. Once active, “Avid DNx [8bit]” will appear as an available export setting in the Movie Render Queue, allowing you to output .mxf files instead of standard image sequences.

2. Manage Audio via Separate Export

The Avid DNx export format in Unreal Engine does not currently support embedded audio. To ensure your video has sound in post-production, you must add a .wav Audio export setting to your Movie Render Queue job. This will output a separate high-quality audio file alongside your video, which can be synced later in your editing suite.

3. Optimize Encoding with Multi-Threading

When exporting through the dnxmxf module, you can adjust the Number of Encoding Threads. For faster renders on high-core-count workstations, increase this value. However, be aware that higher thread counts will consume more CPU resources, which might impact other background tasks or engine stability during the render process.

4. Balance Quality with “Use Compression”

The module offers a “Use Compression” toggle. Disabling this results in a lossless uncompressed file, which is ideal for “hero” assets or VFX plates where maximum quality is required. Enabling it uses Avid’s lossy compression, which is a best practice for dailies or preview renders to save significant disk space while maintaining high visual clarity.

5. Prioritize Image Sequences for Internal Playback

While the module allows you to play .mxf files via the Media Framework, for performance-critical real-time scenes, it is often better to use Image Sequences (like EXR). Video files can sometimes struggle with frame-perfect seeking; however, if you must use video, the DNx codec is significantly more performant than H.264 for intra-frame seeking within the engine.

6. Use for Alpha Channel Rendering

If your pipeline requires transparency (e.g., rendering a character with no background), ensure you use a DNx flavor that supports alpha (typically 444 variants). You must also enable “Allow Throughput of Alpha Channel” in your Project Settings under Post Processing to ensure the dnxmxf module correctly captures the transparency data.

7. Handle Media Source Elimination

When working with external .mxf files in the Content Browser, always place your source files in the Content/Movies directory before importing. This ensures the File Media Source uses a relative path. If the source file is moved or “eliminated” from the disk, the module will fail to resolve the link, leading to black textures in your materials or UI.

8. Verify 8-bit vs. 10-bit Precision

At this time, the engine’s implementation of Avid DNx primarily supports 8-bit precision for exports. If your project requires a full 10-bit or 12-bit HDR pipeline for color grading, you should verify if the current version of the module meets your bit-depth requirements or consider exporting as OpenEXR sequences for the final master.