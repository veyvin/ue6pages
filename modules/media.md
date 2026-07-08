---
layout: default
title: Media
---

<!-- ai-generation-failed -->

<h1>Media</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Media/Media.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Media Framework. While the MediaAssets module provides the high-level Blueprint-exposed objects like Media Players and Media Textures, the core Media module defines the low-level interfaces (IMediaPlayer, IMediaSource, IMediaOutput) that allow the engine to communicate with various playback plugins (such as Electra, WMF, or AvfMedia).

It is used to handle the lifecycle of media playback, including stream discovery, track selection (video, audio, subtitles), and transport control (Play, Pause, Seek). By acting as an agnostic abstraction layer, it helps you eliminate platform-specific code, allowing the same logic to drive a video on a 3D mesh or a UI element across Windows, Linux, Android, and iOS.

Practical Usage Tips and Best Practices
Store Media in the ‘Content/Movies’ Directory
To ensure your media files are correctly recognized and packaged by the engine, always place them in the /Content/Movies/ folder. This is a hard-coded convention; following it helps you eliminate “File Not Found” errors during deployment to consoles or mobile devices.
Prefer the HAP Codec for High Resolutions
For 4K or 8K video playback where performance is critical, use the HAP codec. It is designed to be decoded almost entirely on the GPU with minimal CPU overhead. This helps you eliminate frame drops and CPU spikes that often occur when using standard H.264/H.265 decoders for high-bitrate content.
Initialize Media Players via C++ or BeginPlay
Media Players do not automatically open their source on load to save memory. You must explicitly call OpenSource or OpenUrl. Handling this during an initialization event or a specific trigger helps you eliminate “Black Texture” bugs where the material is ready but the video stream hasn’t started.
Use Electra Player for Cross-Platform Streaming
If your project requires HLS or DASH web streaming, use the Electra Player plugin. It is Epic’s internal player designed to provide a consistent experience across all platforms, helping you eliminate the behavioral differences between the native Windows Media Foundation (WMF) and Apple AVFoundation.
Implement Proper Media Texture Sampling
In your Materials, ensure your Sampler Type is set to External when using a Media Texture. This allows the engine to handle the YUV to RGB conversion efficiently on the GPU, which helps you eliminate color inaccuracies and reduces the performance cost of rendering video.
Manage Audio via Media Sound Components
Do not rely on the OS to handle video audio. Attach a UMediaSoundComponent to an Actor and link it to your Media Player. This allows the audio to be processed through Unreal’s audio engine (MetaSounds/Sound Cues), helping you eliminate issues with spatialization and volume ducking.
Check ‘Precache File’ for Small Loops
For short, frequently looping videos (like UI backgrounds), enable the Precache File option in the File Media Source settings. This loads the entire video into RAM, which helps you eliminate disk-read latency and ensures a seamless, “glitch-free” loop.
Always Call ‘Close’ on Elimination
When an Actor or UI widget containing a Media Player is destroyed (an “elimination” of that object), ensure you call Close() on the Media Player. This releases the hardware decoder and memory resources immediately, which helps you eliminate memory leaks and potential crashes in video-heavy scenes.