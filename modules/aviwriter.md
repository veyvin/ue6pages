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

for capturing and encoding video data into the AVI (Audio Video Interleave) file format.

Description and Purpose

The module provides the FAVIWriter class, which serves as a wrapper for the Windows-specific AVI codecs. Its primary purpose was to allow the engine to output video frames directly from a viewport or render target into a playable movie file. In modern development (Unreal Engine 5.6 and 5.7), this module is considered legacy and has been largely superseded by the Movie Render Queue (MRQ) and the Media IO frameworks. However, it still exists within the codebase to support older internal tools and specialized pipelines that require rapid, uncompressed, or simply-encoded AVI output without the overhead of modern cinematic pipelines.

Practical Usage Tips and Best Practices
Recognize Legacy Status
For 99% of video export needs (cinematics, trailers, or gameplay capture), you should use the Movie Render Queue instead of this module. The AVIWriter is restricted to older AVI containers which often result in massive file sizes or compatibility issues with modern players.
Windows-Only Dependency
The AVIWriter relies on the Windows VFW (Video for Windows) API. If you are developing a cross-platform tool for macOS or Linux, this module will not function. For cross-platform video writing, utilize the ImageWriteQueue or the RemoteControl web-based capture systems.
Prefer Native MP4 in UE 5.6+
With the updates in Unreal Engine 5.6 and 5.7, the engine now supports native H.264 MP4 export within the Movie Render Queue. This effectively eliminates the need for the AVIWriter for most developer workflows, as it provides better compression and universal compatibility.
Use for Rapid Debug Captures
The one remaining advantage of the AVIWriter is its simplicity. If you are building a low-level C++ engine tool that needs to dump raw frames to a video file without setting up a LevelSequence or MRQ Config, FAVIWriter provides a more direct (albeit primitive) path.
Monitor Disk I/O Performance
Because the AVI format often defaults to uncompressed or high-bitrate MJPEG, writing to disk can be extremely taxing. When using this module, ensure you are writing to a fast NVMe drive to eliminate frame drops caused by disk write bottlenecks.
Handling Elimination Event Recordings
If you are using this module to record high-speed debug footage of a gameplay elimination, ensure you are capturing at a fixed frame rate. AVI containers handle variable frame rates poorly; forcing a fixed 60fps capture ensures that the elimination animation remains smooth and frame-accurate during playback.
Verify Codec Availability
The AVIWriter can only use codecs installed on the host Windows OS. If your code specifies a four-character code (FOURCC) for a codec that isn’t present, the writer will fail silently or fallback to uncompressed video. Always include a check to verify the writer initialized successfully before beginning a capture.
Explicit Module Cleanup
When using FAVIWriter in C++, you must explicitly call CompleteWriting() to finalize the file header. If the engine crashes or the object is destroyed before this call, the resulting .avi file will be corrupted and unplayable, as the index table at the end of the file will never be written.