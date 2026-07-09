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

developed by AMD and integrated into Unreal Engine. It allows the engine to interface directly with the dedicated multimedia processing chips on AMD Radeon and Instinct GPUs.

The module is primarily used for high-performance video encoding and decoding (H.264 and HEVC/H.265). By offloading these tasks to the GPU’s hardware encoder, developers can achieve low-latency streaming and high-resolution video capture without taxing the CPU or the primary GPU shaders used for rendering.

Practical Usage Tips and Best Practices
Configure Module Dependencies If you are developing custom video capture or streaming solutions in C++, add the AMF module to your Build.cs. It is often used alongside the AVEncoder module to provide hardware-specific implementations.
C#
	    // In YourProject.Build.cs

	    PublicDependencyModuleNames.AddRange(new string[] { "AVEncoder", "AMF" });

	    ```

	 

	*   **Force AMF via Command Line**

	    When running a packaged build (especially for Pixel Streaming), you can force the engine to use the AMD encoder if multiple GPUs are present. Use the following launch parameter:

	    `-AudioVideoEncoder=AMF`

	    *Note: This is useful for debugging to ensure the engine isn't falling back to software encoding (VP8/VP9).*

	 

	*   **Configure Presets with FVideoEncoderConfigAMF**

	    When initializing a custom encoder in C++, use the `FVideoEncoderConfigAMF` class to define the encoding quality. You can choose presets like `EAVPreset::UltraLowLatency` for streaming or `EAVPreset::HighQuality` for local recording to disk.

	 

	*   **Monitor Initialization via Logs**

	    Hardware encoders are notoriously sensitive to driver versions. Always check your logs for the `LogAMF` or `LogAVEncoder` categories to verify successful initialization.

	    ```bash

	    # Look for this in your project log:

	    LogAVEncoder: Display: Found AMF (AMD Advanced Media Framework) encoder

	    ```

	 

	*   **Optimize for Pixel Streaming**

	    If using Pixel Streaming on AMD hardware, you can fine-tune the AMF encoder bitrate and rate control using console variables. This helps prevent "stuttering" on high-motion scenes:

	    `PixelStreaming.Encoder.RateControl=CBR` (Constant Bitrate for more stable network streams).

	 

	*   **Handle VRAM Overhead**

	    AMF requires a small amount of dedicated VRAM to maintain encoding buffers. In memory-constrained environments (like large-scale ArchViz), ensure you aren't hitting the VRAM ceiling, as AMF may fail to initialize or cause a GPU crash if the primary render consumes 100% of available memory.

	 

	*   **Driver Compatibility**

	    AMF functionality is heavily tied to the **AMD Radeon Software** or **AMD Pro Drivers**. Ensure your target machines have the "Minimal" or "Full" driver install; "Driver Only" installs sometimes lack the necessary AMF DLLs required by Unreal Engine.

	 

	*   **Support for HEVC (H.265)**

	    While H.264 is the default for compatibility, the AMF module supports HEVC (H.265), which offers significantly better quality at the same bitrate. You can enable this in your `FVideoEncoderConfigAMF` setup to reduce the bandwidth required for high-resolution 4K streams.
Copy code
Prioritize for Pixel Streaming On machines equipped with AMD hardware, the AMF module is essential for Pixel Streaming. It enables the engine to encode the viewport at high frame rates with minimal latency. Ensure the plugin is enabled in the editor to allow the engine to “eliminate” the performance bottleneck of software encoding.
Force Hardware Selection via Command Line In multi-GPU setups or environments where you want to ensure AMD hardware is being utilized, you can force the use of the AMF encoder by adding the following parameter to your executable: -AudioVideoEncoder=AMF
Optimize Bitrate Control for Network Stability When using the AMF encoder for streaming, use the CBR (Constant Bitrate) rate control mode via console variables to prevent large spikes in data. This is crucial for maintaining a stable connection in cloud-gaming scenarios: PixelStreaming.Encoder.RateControl=CBR
Monitor Initialization via Logs Hardware encoders depend heavily on specific driver versions. Always verify the status of the AMF module in your logs. Search for LogAVEncoder or LogAMF to confirm the hardware was detected and initialized successfully.
Match Presets to Use-Cases Use the FVideoEncoderConfigAMF class in C++ to set appropriate presets. Choose UltraLowLatency for interactive experiences (like Pixel Streaming) and HighQuality for non-real-time tasks like recording “elimination” highlights for a replay system.
Manage VRAM Constraints The AMF hardware encoder requires a small portion of dedicated VRAM for its internal buffers. In high-fidelity projects utilizing Nanite and Lumen, monitor your VRAM usage; if the GPU memory is entirely saturated, the AMF encoder may fail to initialize or cause a driver crash.
Keep Drivers Updated AMD frequently updates the AMF SDK. To ensure compatibility with the latest Unreal Engine features (such as 10-bit encoding or HEVC support), ensure your deployment environment uses the latest AMD Radeon Software or Pro drivers.