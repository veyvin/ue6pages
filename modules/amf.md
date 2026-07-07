---
layout: default
title: Amf
---

<!-- ai-generation-failed -->

<h1>Amf</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/AMD/Amf/Amf.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

’s proprietary multimedia SDK. It provides Unreal Engine with low-level, hardware-accelerated access to AMD GPUs for video encoding, decoding, and color space conversion.

This module is the backbone for high-performance video features on AMD hardware, most notably powering Pixel Streaming, AVEncoder (used for background recording), and the Media Framework when running on Radeon or Radeon Pro graphics cards. It allows the engine to offload heavy video processing from the CPU directly to the GPU’s dedicated multimedia engines.

Practical Usage Tips and Best Practices
1. Coordinate Module Dependencies

To utilize AMF features in C++, you generally need to link against both the core AV interfaces and the AMF-specific implementation. Add these to your Build.cs file:

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { 

	    "AVCodecsCore", 

	    "AVCodecsCoreAMF", // Core AMF logic

	    "AMFCodecs"        // Implementation of H.264/H.265 encoders

	});

	```

	 

	#### 2. Prioritize for Pixel Streaming on AMD Hardware

	AMF is the AMD equivalent to NVIDIA's NVENC. If your server-side deployment uses AMD Radeon or Radeon Pro GPUs, the AMF module is essential for delivering the low-latency video required for Pixel Streaming.

	*   **Best Practice:** Ensure your target machine has the latest **AMD Software: Adrenalin Edition** drivers installed, as the AMF module relies on the system-level DLLs provided by the driver.

	 

	#### 3. Manage Rate Control for Network Stability

	When using AMF via the AVEncoder or Pixel Streaming, you can tune the bitrate via C++ or Console Variables to prevent stuttering on poor connections.

	*   **Tip:** Use the console command `PixelStreaming.Encoder.RateControl VBR` to allow the AMF encoder to use **Variable Bitrate**, which is more efficient for complex visual scenes than CBR (Constant Bitrate).

	 

	#### 4. Check Encoder Availability

	Before attempting to initialize a hardware stream, always verify that the AMF encoder is available on the current hardware to avoid crashes or null pointer exceptions.

	 

	```cpp

	#include "AMF/Video/Encoder/VideoEncoderAMF.h"

	 

	// Basic check for AMF encoder presence

	bool IsAMDEncoderAvailable()

	{

	    // The AVEncoder registry manages hardware-specific implementations

	    // AMF is registered here if the hardware supports it

	    return FVideoEncoderAMF::IsAvailable();

	}

	```

	 

	#### 5. Leverage H.265 (HEVC) for High Resolution

	AMF supports both H.264 and H.265. For 4K streaming or high-fidelity recordings, H.265 offers significantly better quality at the same bitrate compared to H.264.

	*   **Best Practice:** In your encoder configuration, set the codec to HEVC if the client-side decoder supports it to maximize visual clarity while minimizing bandwidth.

	 

	#### 6. Handle Vulkan and D3D12 Contexts

	The AMF module interacts directly with the RHI (Rendering Hardware Interface). In UE5, it is specifically optimized for **D3D12** and **Vulkan**.

	*   **Tip:** If you are developing custom video capture logic, use `FVideoEncoderAMF::SetupContext` to correctly bind the encoder to the current Vulkan or DX12 device, ensuring that frame data never leaves the GPU memory (zero-copy).

	 

	#### 7. Debug with Audio/Video Stats

	To verify that the AMF module is actually doing the work (and the engine hasn't fallen back to software encoding), use the built-in stats:

	*   `stat pixelstreaming`: Displays which encoder is active (should show "AMF").

	*   `stat gpu`: Useful for checking if the hardware encoding process is adding significant latency to your frame time.

	 

	#### 8. Graceful Fallback Implementation

	Hardware encoders have a limit on the number of simultaneous sessions (streams) they can handle. 

	*   **Best Practice:** If `SetupContext` fails for an AMF encoder, implement a fallback to a software encoder (like `VP8` or `VP9` via the `Electra` or `WebM` modules) to ensure the application remains functional even when hardware resources are exhausted.
Copy code
2. Validate Hardware Support at Runtime

Before attempting to initialize a hardware-accelerated stream, verify that the AMF encoder is available on the user’s machine. This prevents crashes or “encoder not found” errors on non-AMD systems.

C++
	#include "AMFCodecs/Public/Video/Encoder/VideoEncoderAMF.h"

	 

	// Check if AMF is usable on the current hardware

	if (FVideoEncoderAMF::IsAvailable())

	{

	    // Proceed with hardware-accelerated initialization

	}
Copy code
3. Optimize Pixel Streaming Latency

For Pixel Streaming, the AMF module is essential for AMD-based servers.

Best Practice: Use the console command PixelStreaming.Encoder.LowLatency 1. This instructs the AMF module to prioritize frame delivery speed over maximum compression efficiency, which is vital for interactive experiences.
4. Leverage Zero-Copy Rendering

The AMF module is designed to work directly with RHI textures (D3D12 or Vulkan).

Best Practice: Avoid reading back texture data to the CPU before encoding. Use the FVideoResourceVulkan or FVideoResourceD3D12 structures to pass GPU pointers directly to the AMF encoder. This helps eliminate the performance cost of memory transfers between the GPU and RAM.
5. Monitor Session Limits

Consumer AMD GPUs often have a hardware limit on the number of simultaneous encoding sessions.

Tip: If your application supports multi-user Pixel Streaming on a single GPU, implement a fallback logic. If SetupContext fails for an AMF session, fall back to a software-based encoder (like VP8/VP9) to ensure the user is not completely eliminated from the session.
6. Tune Bitrate via Console Variables

You can adjust AMF’s behavior in real-time using console variables. This is useful for balancing visual quality against network stability.

AMF.Encoder.MaxBitrate: Sets the upper bound for the hardware encoder.
AMF.Encoder.RateControl: Switch between CBR (Constant Bitrate) and VBR (Variable Bitrate). Use VBR for local recordings and CBR for streaming over unstable networks.
7. Ensure Driver Compatibility

The AMF module relies on the system’s amfrt64.dll.

Best Practice: Advise users to keep their AMD Software: Adrenalin Edition drivers updated. If the module fails to initialize, it is frequently due to a missing or outdated driver library rather than a bug in the engine code.
8. Use H.265 (HEVC) for High-Fidelity

While H.264 is the standard for compatibility, AMF’s HEVC implementation offers significantly better quality-per-bit.

Tip: If your target audience uses modern browsers or players that support HEVC, configure the AMF encoder to use H.265 to provide a sharper image at lower bandwidths.