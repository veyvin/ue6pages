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

grates the FFmpeg (libavcodec, libavformat, etc.) libraries into the engine’s ecosystem. It serves as a foundational component for the Electra Media Player and other media-handling systems.

While Unreal typically relies on platform-specific decoders (like WMF for Windows or AVFoundation for macOS), the libav module provides a cross-platform fallback and extended codec support. It is used for demuxing (separating audio and video streams) and decoding compressed media data into raw frames that the engine can render as textures.

Practical Usage Tips and Best Practices
1. Add Module Dependencies Correctly

Since libav is a third-party library wrapper, it is often utilized as a dependency for other media plugins.

Action: If you are writing a custom C++ video decoder, add "LibAV" to your PrivateDependencyModuleNames in your *.Build.cs file. Ensure you also include "ElectraCodecFactory" if you are working within the Electra framework to eliminate linker errors.
2. Respect Licensing Constraints (LGPL/GPL)

The underlying FFmpeg libraries used by the libav module are subject to specific licenses (usually LGPL).

Best Practice: If you modify the source code within the ThirdParty/FFmpeg directory, you may be required to share those changes under LGPL. Stick to using the engine’s provided wrapper to eliminate legal risks associated with static linking or proprietary modifications.
3. Offload Decoding to Worker Threads

Decoding high-resolution video is one of the most CPU-intensive tasks a game can perform.

Tip: Never call libav decoding functions on the Game Thread. Use the FRunnable or Task Graph system to process packets in the background. This helps you eliminate frame-rate hitches and stuttering during video playback.
4. Manage Memory via FMemory

Libav frequently allocates large buffers for raw YUV or RGB pixel data.

Action: When transferring data from libav to an Unreal UTexture2D or FRenderTarget, use FMemory::Memcpy or Lock/Unlock patterns. Efficiently reusing buffers instead of reallocating them every frame helps you eliminate memory fragmentation and garbage collection pressure.
5. Verify Codec Compatibility

The libav module supports a wide range of formats (H.264, H.265, VP9), but not all platforms support hardware acceleration for every codec via FFmpeg.

Tip: Test your media on your target hardware early. If a software-only decoder is used for a 4K video, it may overwhelm the CPU. Using optimized, hardware-friendly profiles helps you eliminate playback lag on lower-end devices.
6. Coordinate with Electra Media Player

The libav module is most effective when used as a backend for the Electra Player.

Action: If a video fails to play, check the “Electra” category in the Output Log. It will often report specific libav demuxing errors. Troubleshooting through the high-level player first helps you eliminate the need to debug raw C-style pointers in the libav wrapper.
7. Handle Color Space Conversions

Libav often outputs data in YUV420p format, which cannot be directly sampled by a standard GPU shader without conversion.

Best Practice: Use a specialized Media Material or a Compute Shader to handle the YUV-to-RGB conversion. Doing this on the GPU rather than the CPU via libav’s swscale helps you eliminate massive CPU bottlenecks.
8. Use for Specialized Data (Non-Video)

Because the libav module includes libavformat, it can be used to parse metadata or non-standard data streams embedded in video files.

Tip: Use the demuxer to extract timed text or telemetry data synced with a video. Utilizing the existing libav infrastructure for this helps you eliminate the need to write custom binary file parsers for complex media containers.