---
layout: default
title: GameplayMediaEncoder
---

<!-- ai-generation-failed -->

<h1>GameplayMediaEncoder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/GameplayMediaEncoder/GameplayMediaEncoder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AVEncoder, ApplicationCore, Core, CoreUObject, Engine, HTTP, Json, RHI, RenderCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

traditionally associated with software-based video encoding.

Practical Usage Tips and Best Practices
1. Leverage for Low-Latency Streaming

The primary strength of this module is its integration with Pixel Streaming. By using hardware-accelerated paths, it minimizes the time between a frame being rendered and being sent over the network. This is critical for the elimination of input lag in interactive remote applications.

2. Configure Bitrate via Console Variables

You can fine-tune the encoder’s performance at runtime using console variables such as PixelStreaming.Encoder.TargetBitrate. Adjusting these values dynamically based on network conditions leads to the elimination of stuttering and visual artifacts during high-motion gameplay sequences.

3. Use Hardware-Specific Plugins

The GameplayMediaEncoder acts as a wrapper. For it to function, you must enable the corresponding hardware vendor plugins (e.g., NVIDIA Video Codec SDK or AMD Advanced Media Framework). Ensuring these are active in your project settings assists in the elimination of fallback “Software Encoding” which can drastically reduce frame rates.

4. Optimize Frame Capture with MediaCapture

When using this module for recording, combine it with the Media IO Framework. Using UMediaCapture to feed the encoder ensures that frames are pulled efficiently from the backbuffer, leading to the elimination of unnecessary memory copies between the GPU and CPU.

5. Handle Encoder Session Limits

Hardware encoders often have a physical limit on the number of simultaneous encoding sessions (e.g., consumer NVIDIA cards often limit users to 3-5 sessions). Use the PixelStreaming.Encoder.MaxSessions setting to manage these resources, aiding in the elimination of crashes caused by exceeding hardware capabilities.

6. Match Resolution to Codec Profiles

Ensure your gameplay resolution and aspect ratio are compatible with the selected codec (H.264, H.265, or AV1). Using standard resolutions (like 1080p or 4K) within the encoder’s supported profile levels facilitates the elimination of “Invalid Configuration” errors that can prevent the encoder from starting.

7. Monitor Performance with Unreal Insights

Encoding adds a specific cost to the GPU pipeline. Use Unreal Insights to track the “Encode” trace events. Analyzing these timings allows you to balance visual quality against the frame budget, which is a best practice for the elimination of performance bottlenecks in VR or high-fidelity projects.

8. Verify Build.cs Dependencies

To utilize the encoder interface in your C++ classes, you must add "GameplayMediaEncoder" to your PrivateDependencyModuleNames in your Build.cs file. Proper dependency management is the essential first step for the elimination of linker errors when building custom streaming or recording solutions.