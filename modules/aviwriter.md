---
layout: default
title: AVIWriter
---

<!-- ai-generation-failed -->

<h1>AVIWriter</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AVIWriter/AVIWriter.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

d for encoding and writing video data into the AVI (Audio Video Interleave) file format. It serves as a low-level bridge between the engine’s frame capture buffers and the Windows-specific AVI multimedia framework.

Description

The AVIWriter module is part of the older Movie Scene Capture system. It is primarily used to take a sequence of rendered frames and compress them into a single .avi video file. While it has largely been superseded by the more advanced Movie Render Queue (MRQ) and modern formats like ProRes or EXR sequences, it remains in the engine to support legacy tools, simple editor recordings, and specific internal pipelines that require a quick, uncompressed, or basic compressed video output without the overhead of professional cinema formats.

Practical Usage Tips and Best Practices
1. Understand the 2GB Limitation (AVI 1.0)

The AVIWriter module often operates under the constraints of the AVI 1.0 standard, which typically has a file size limit of approximately 2GB. If your recording exceeds this limit, the file may become corrupted. For long-form cinematic renders, it is highly recommended to use Movie Render Queue with image sequences instead.

2. Include Only for Windows Editor Builds

Because this module relies heavily on Windows-specific libraries (like VFW - Video for Windows), it is generally not available or functional on Linux or Mac. When referencing it in a *.Build.cs file, ensure it is wrapped in a platform check to avoid compilation errors on non-Windows targets:

C#
	if (Target.Platform == UnrealTargetPlatform.Win64)

	{

	    PublicDependencyModuleNames.Add("AVIWriter");

	}
Copy code
3. Use for Fast Draft Previews

The main advantage of AVIWriter is speed and immediate playability. Use it for “Daily” reviews or quick motion tests where you need a video file that can be opened instantly in a standard media player without needing a post-production pass or a complex transcoding step.

4. Configure Codecs via Project Settings

The module uses the codecs installed on your Windows system. You can often configure the compression settings in the Project Settings > Plugins > Movie Render Queue (if using the legacy compatibility) or the Capture Settings dialog. Selecting “Uncompressed” will produce the highest quality but will hit the file size limit almost immediately.

5. Match Resolution to Aspect Ratio

To avoid stretching or artifacts, ensure your capture resolution matches the viewport’s aspect ratio. The AVIWriter is sensitive to non-standard resolutions; sticking to common formats like 1920x1080 or 1280x720 ensures the broadest compatibility with external video players.

6. Transition to Movie Render Queue (MRQ)

For any production-quality work, treat AVIWriter as a legacy path. The Movie Render Queue provides significantly better spatial and temporal anti-aliasing, motion blur, and high-bitrate codecs (like Apple ProRes via the AppleProRes plugin) that eliminate the compression artifacts common in basic AVI files.

7. Handle Application Shutdown

If the engine crashes or is forcefully closed during the write process, the AVI file header will not be finalized. This results in a corrupted, unplayable file. Ensure you have a stable environment before starting a capture, as an unexpected elimination of the engine process will result in the loss of all recorded data.

8. Monitor Disk Space

Because AVI files (especially uncompressed ones) can be massive, always check your destination drive’s space. Filling a hard drive during a render can cause the engine to hang. By managing your output directory properly, you eliminate the risk of system instability during long capture sessions.