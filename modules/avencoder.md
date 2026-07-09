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

high-level, platform-agnostic C++ interface for hardware-accelerated video encoding. It abstracts away the complexities of dealing directly with vendor-specific APIs like NVIDIA’s NVENC, AMD’s AMF, and Apple’s VideoToolbox.

It is primarily used to drive Pixel Streaming, record high-quality gameplay via the Movie Render Queue, and power custom real-time video streaming solutions.

1. Module Configuration

To use the AVEncoder in your C++ project, you must include it in your Build.cs file. Note that it is typically used alongside the RHI and Renderer modules to access GPU textures.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "AVEncoder", "RHI", "RenderCore" });

	```

	 

	### 2. Practical Usage Tips & Best Practices

	 

	#### Always Check Hardware Compatibility

	AVEncoder relies on specific hardware (NVIDIA, AMD, or Apple Silicon). Before initializing a session, use the module's factory to query available encoders. This "eliminates" runtime crashes on machines with older GPUs or integrated graphics that lack hardware-accelerated H.264/H.265 logic.

	 

	#### Utilize the IVideoEncoder Interface

	Instead of writing logic for specific codecs, program against the `AVEncoder::IVideoEncoder` interface. This allows your system to automatically switch between **H.264**, **H.265 (HEVC)**, or **AV1** (on supported hardware) based on the user's hardware or network bandwidth without changing your core logic.

	 

	#### Prefer RHI Texture Inputs

	For maximum performance, feed the encoder directly with `FRHITexture` pointers rather than CPU-side pixel arrays. This "eliminates" the massive performance cost of copying frames from GPU memory to RAM, keeping the entire encoding pipeline on the graphics card.

	 

	#### Manage Asynchronous Encoding

	Encoding is a non-blocking, asynchronous operation. When you send a frame to the encoder via `EncodeFrame`, it will return immediately. You must implement a **callback delegate** to receive the encoded packets. Ensure your callback logic is thread-safe, as it often fires on a dedicated encoding thread rather than the Game Thread.

	 

	#### Dynamic Bitrate Adjustment

	In streaming scenarios (like Pixel Streaming), use the encoder's bitrate control settings to respond to network congestion. You can update the bitrate mid-session. Lowering the bitrate when packet loss is detected "eliminates" visual stuttering at the cost of slight image quality degradation.

	 

	#### Set Up Zero-Latency Configurations

	For interactive applications like remote gaming or VR streaming, configure the encoder for **"Zero Latency"** (Disable B-frames). B-frames require future frames to be processed before they can be displayed, adding significant delay. Disabling them ensures the smallest possible gap between a user's input and the video response.

	 

	#### Handle D3D/Vulkan Interop

	On Windows, AVEncoder interacts heavily with the Direct3D or Vulkan device. If your project uses custom RHI commands, ensure you flush the GPU command buffer before passing a texture to the encoder. If the encoder tries to read a texture that the renderer is still writing to, you will see "ghosting" or "tearing" in the output video.

	 

	#### Leverage the Command Line Encoder for Debugging

	While AVEncoder is a C++ API, you can test its underlying codec performance using the **Movie Render Queue's Command Line Encoder**. By passing flags to the command line, you can quickly find the optimal GOP (Group of Pictures) size and bitrate for your specific art style before hard-coding those parameters into your C++ `FVideoEncoderConfig`.
Copy code
2. Practical Usage Tips & Best Practices
Always Check Hardware Compatibility

AVEncoder relies on specific hardware (NVIDIA, AMD, or Apple Silicon). Before initializing a session, use the module’s factory (FVideoEncoderFactory) to query available encoders. This “eliminates” runtime crashes on machines with older GPUs or integrated graphics that lack hardware-accelerated H.264/H.265 logic.

Utilize the IVideoEncoder Interface

Instead of writing logic for specific codecs, program against the AVEncoder::IVideoEncoder interface. This allows your system to automatically switch between H.264, H.265 (HEVC), or AV1 (on supported hardware) based on the user’s hardware or network bandwidth without changing your core logic.

Prefer RHI Texture Inputs

For maximum performance, feed the encoder directly with FRHITexture pointers rather than CPU-side pixel arrays. This “eliminates” the massive performance cost of copying frames from GPU memory to RAM, keeping the entire encoding pipeline on the graphics card.

Manage Asynchronous Encoding

Encoding is a non-blocking, asynchronous operation. When you send a frame to the encoder via EncodeFrame, it will return immediately. You must implement a callback delegate to receive the encoded packets. Ensure your callback logic is thread-safe, as it often fires on a dedicated encoding thread rather than the Game Thread.

Dynamic Bitrate Adjustment

In streaming scenarios (like Pixel Streaming), use the encoder’s bitrate control settings to respond to network congestion. You can update the bitrate mid-session. Lowering the bitrate when packet loss is detected “eliminates” visual stuttering at the cost of slight image quality degradation.

Set Up Zero-Latency Configurations

For interactive applications like remote gaming or VR streaming, configure the encoder for “Zero Latency” (Disable B-frames). B-frames require future frames to be processed before they can be displayed, adding significant delay. Disabling them ensures the smallest possible gap between a user’s input and the video response.

Handle D3D/Vulkan Interop

On Windows, AVEncoder interacts heavily with the Direct3D or Vulkan device. If your project uses custom RHI commands, ensure you flush the GPU command buffer before passing a texture to the encoder. If the encoder tries to read a texture that the renderer is still writing to, you will see “ghosting” or “tearing” in the output video.

Leverage the Command Line Encoder for Debugging

While AVEncoder is a C++ API, you can test its underlying codec performance using the Movie Render Queue’s Command Line Encoder. By passing flags to the command line, you can quickly find the optimal GOP (Group of Pictures) size and bitrate for your specific art style before hard-coding those parameters into your C++ FVideoEncoderConfig.