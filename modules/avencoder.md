---
layout: default
title: AVEncoder
---

<!-- ai-generation-failed -->

<h1>AVEncoder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AVEncoder/AVEncoder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CUDA, Core, Engine, RHI, RenderCore, SignalProcessing</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

or hardware-accelerated video encoding. It provides a common C++ interface that allows the engine to communicate with various GPU-based encoding SDKs—such as NVIDIA NVENC, AMD AMF, and Apple VideoToolbox—without needing to write vendor-specific code for each platform.

This module is the backbone of Pixel Streaming and the Movie Render Queue (when exporting to MP4), enabling the engine to compress high-resolution frames into H.264 or H.265 (HEVC) video streams in real-time with minimal CPU impact.

Practical Usage Tips and Best Practices
1. Add Correct Build Dependencies

To interface with hardware encoders in C++, you must include both AVEncoder and the platform-agnostic HardwareEncoders module in your Build.cs.

C#
	// In YourModule.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "AVEncoder", 

	    "HardwareEncoders",

	    "RHI"

	});

	```

	 

	#### 2. Verify Encoder Availability at Runtime

	Hardware encoders may be unavailable due to old drivers, unsupported GPUs, or maximum session limits (common on consumer NVIDIA cards). Always query the `FHardwareEncoders` singleton before attempting to initialize an encoder.

	```cpp

	#include "HardwareEncoders.h"

	 

	if (FHardwareEncoders::Get().IsAvailable(AVEncoder::ECodec::H264))

	{

	    // Proceed with initialization

	}

	```

	 

	#### 3. Match RHI Textures for Zero-Copy Encoding

	For maximum performance, avoid copying pixel data back to the CPU (system memory). The **avencoder** module is designed to work directly with **RHI Textures** (typically `FRHITexture2D`). Pass the texture handle directly to the encoder to perform "zero-copy" encoding, which drastically reduces latency and CPU overhead.

	 

	#### 4. Select the Right Rate Control Mode

	For Pixel Streaming or interactive applications, always use **Constrained Bitrate (CBR)** or **Low Latency VBR**. Avoid "High Quality" presets intended for local recording, as they often introduce "B-frames" which add significant latency to the stream.

	*   **Best for Streaming:** `EAVPreset::UltraLowLatency`

	*   **Best for Recording:** `EAVPreset::HighQuality`

	 

	#### 5. Handle Video Frame Elimination Safely

	When passing textures to the encoder, the encoder may process the frame asynchronously. Ensure you are not modifying or deleting the underlying RHI resource until the encoder has signaled completion. Use the `FAVVideoFrame` wrapper to manage the lifetime of the frame being encoded.

	 

	#### 6. Minimize Resolution Changes

	Frequent resolution changes (resizing the viewport) force the hardware encoder to re-initialize or flush its internal buffers, causing a "hiccup" in the stream. If your application supports resizing, try to pad the encoder input to a fixed size or use a scaler before the encoding stage.

	 

	#### 7. Use h.265 (HEVC) for High Resolutions

	If you are streaming 4K content and the hardware supports it, prefer h.265 over h.264. The **avencoder** implementation for h.265 provides roughly 25-50% better quality at the same bitrate, which is critical for maintaining visual clarity in dense Unreal Engine scenes over limited network bandwidth.

	 

	#### 8. Monitor Encoder Thread Load

	The hardware encoder operates on its own dedicated chip, but the *submission* logic happens on the engine's rendering thread. Use **Unreal Insights** or the `stat GPU` command to ensure that the time spent "handing off" frames to the encoder isn't causing a bottleneck for your main render loop.
Copy code
2. Always Verify Hardware Availability

Not all GPUs support hardware encoding (and some have session limits, especially consumer-grade NVIDIA cards). Before initializing an encoder, always check if the specific codec is available on the current machine.

C++
	#include "HardwareEncoders.h"

	if (FHardwareEncoders::Get().IsAvailable(AVEncoder::ECodec::H264)) { /* ... */ }
Copy code
3. Prioritize Zero-Copy Encoding

For maximum performance, avoid moving pixel data from the GPU to the CPU (system memory). The avencoder module is optimized to take an RHI Texture (FRHITexture2D) directly. By keeping the frames on the GPU, you drastically reduce latency and prevent CPU bottlenecks.

4. Use Low-Latency Presets for Streaming

If you are using the encoder for interactive experiences like Pixel Streaming, ensure you set the EAVPreset to UltraLowLatency. This setting forces the elimination of B-frames (Bidirectional frames), which require future data and would otherwise introduce a multi-frame delay in the stream.

5. Handle Frame Lifetime Safely

Encoders process frames asynchronously. When you pass a frame to the avencoder, do not modify or allow the elimination of the source texture until the encoder confirms it has finished reading the data. Use the FAVVideoFrame wrapper to manage the reference counting of the video data correctly.

6. Opt for H.265 (HEVC) on High Resolutions

When streaming or recording in 4K, prefer H.265 if the hardware supports it. H.265 provides significantly better visual quality at the same bitrate compared to H.264. This is critical for maintaining the fine details of Nanite and Lumen at lower bandwidths.

7. Match Project Sample Rates

If you are also encoding audio via this module, ensure your project’s audio sample rate matches the encoder’s expectations (usually 48kHz). This prevents the module from having to perform costly real-time resampling before the final multiplexing.

8. Monitor Performance via Unreal Insights

Use the Unreal Insights tool to track the time spent in the avencoder submission thread. If the “EncodeFrame” task starts taking longer than your frame budget (e.g., 16.6ms for 60fps), it may indicate that the GPU’s dedicated encoding chip is saturated or that the bitrate is set too high for the hardware to handle.