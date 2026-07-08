---
layout: default
title: libav
---

<!-- ai-generation-failed -->

<h1>libav</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/libav/libav.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

. It serves as a cross-platform, low-level media framework used for high-performance audio and video encoding, decoding, and muxing.

While Unreal provides high-level tools like the Electra Media Player and the Movie Render Queue (MRQ), the Libav module acts as the “engine under the hood” that handles the actual processing of various codecs (like H.264, H.265, and AAC) and file containers (like .mp4 or .mkv). It is essential for developers who need to eliminate external dependencies when handling complex video tasks or building custom recording tools.

Practical Usage Tips and Best Practices
Link via Third-Party Dependencies
In your C++ Build.cs file, do not link to Libav as a standard module. Instead, use AddEngineThirdPartyPrivateStaticDependencies(Target, "libav");. This ensures the compiler finds the correct headers and libraries for your specific platform and helps you eliminate “unresolved external symbol” errors during compilation.
Configure the CLI Encoder Path
The Movie Render Queue uses this module to output final video files. Go to Project Settings > Movie Pipeline CLI Encoder and set the path to your ffmpeg executable. Placing the executable in your engine’s Binaries/Win64 folder helps you eliminate the need to set up environment variables on every developer’s machine.
Use ‘DumpCLIEncoderCodecs’ to Verify Support
If you are unsure which video formats your current engine build supports, run the console command MovieRenderPipeline.DumpCLIEncoderCodecs. This output will list every available codec recognized by the module, helping you eliminate guesswork when choosing a video format for your cinematics.
Prefer Electra for Runtime Playback
For in-game video playback, always use the Electra Player plugin. It is heavily optimized to use the Libav backend and provides better memory management than the legacy WMF player. Using Electra helps you eliminate frame drops and audio-sync issues during high-resolution video playback.
Handle Licensing with Care
FFmpeg/Libav libraries are often governed by LGPL or GPL licenses. To eliminate potential legal risks in commercial products, avoid statically linking custom versions of these libraries into your game executable. Instead, use the engine’s built-in hooks or call external binaries via the CLI encoder.
Use -crf for Quality Control
When exporting videos from MRQ, you can pass custom command-line arguments to the encoder. Use the -crf (Constant Rate Factor) flag (values between 18 and 23 are standard) to balance file size and visual fidelity. This helps you eliminate blocky compression artifacts in high-motion scenes.
Validate Audio/Video Stream Compatibility
A common point of failure is trying to mux an audio stream into a container that doesn’t support it (e.g., certain audio codecs in an .mp4 container). Always pair libx264 with aac for maximum compatibility, which helps you eliminate “Invalid Data” errors during the final muxing phase.
Utilize the Project Settings for Global Defaults
Instead of hardcoding encoding settings in every Render Config, use the Movie Pipeline CLI Encoder project settings to define your standard output format and quality. Centralizing these settings helps you eliminate inconsistencies across different levels or cinematics in a large-scale project.