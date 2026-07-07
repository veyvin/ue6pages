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

gin in Unreal Engine, enabling support for high-end professional video codecs.

Description and Purpose

This module provides the integration between Unreal Engine’s Media Framework and the Avid DNx standard. It allows the engine to decode and encode video in the .mxf container using Avid’s high-bitrate, post-production-friendly codecs (DNxHD and DNxHR). It is primarily used in Virtual Production, broadcast, and high-end cinematic pipelines where maintaining visual fidelity across the editing process is critical. By using this module, developers can import high-quality video plates for in-camera VFX or export high-resolution renders from the Movie Render Queue that are ready for immediate use in professional editing suites like Avid Media Composer.

Practical Usage Tips and Best Practices
Enable the Plugin for MRQ Support
To use this module for rendering, you must navigate to the Plugins menu and enable the Avid DNxHR/DNxMXF Media Plugin. Once enabled, “Avid DNx” will appear as an export format in the Movie Render Queue, helping you eliminate the need for external video conversion tools.
Export Separate Audio Files
The Avid DNx export format does not support embedded audio. When rendering a sequence, you must add a .wav Audio setting in the Movie Render Queue alongside the DNx setting. This will eliminate the risk of losing your soundscape, allowing you to re-combine the video and audio in post-production.
Adjust Encoding Threads for Speed
The module allows you to specify the Number of Encoding Threads. If you are on a high-core-count workstation, increase this value to speed up your renders. This is the most effective way to eliminate long wait times during the export of complex cinematic elimination sequences.
Use for High-Fidelity Video Backplates
When working with Media Plates in a level, use DNxHR for your source video files. Its intra-frame compression is much easier for the engine to decode in real-time than inter-frame codecs like H.264, which helps eliminate dropped frames and stuttering during playback.
Select the Correct Bitrate for the Task
Choose between DNxHR LB (Low Bandwidth) for proxies and DNxHR HQX (High Quality) for final delivery. Using the appropriate compression level helps you eliminate unnecessary disk space usage while ensuring your master files maintain 12-bit color depth (where supported by the codec).
Verify MXF Container Compatibility
While .mxf is a standard, different software versions have varying levels of support. If your video is not appearing correctly, check the “Legacy” or “OP1a” settings in the export dialog. Testing these settings helps you eliminate “File Not Supported” errors in your downstream editing software.
Optimize for Virtual Production Elimination Tests
If you are capturing live performance for a character elimination scene on an LED stage, use the DNxMXF format for your “witness cameras.” The high quality and timecode support of this module eliminate synchronization issues when aligning live-action footage with engine-rendered sequences.
Monitor CPU Usage during Playback
High-resolution DNxHR files can be CPU-intensive to decode. If you experience performance hitches in the editor, check the Media Stats tool. If the CPU is pegged, consider lowering the resolution of your source video to eliminate playback lag during your development sessions.