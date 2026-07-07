---
layout: default
title: OpenGLDrv
---

<!-- ai-generation-failed -->

<h1>OpenGLDrv</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/OpenGLDrv/OpenGLDrv.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, ArmlibGPUInfo, Core, CoreUObject, Engine, GoogleGameSDK, PreLoadScreen, RHI, RHICore, RenderCore, TraceLog, detex</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

t allows Unreal Engine to communicate with graphics hardware using the OpenGL and OpenGL ES (Embedded Systems) APIs.

Description and Purpose

This module translates the engine’s generic rendering commands into specific OpenGL function calls. While modern development has shifted toward DirectX 12 and Vulkan, OpenGLDrv remains a critical fallback for Linux desktop support and legacy Android devices. Its primary purpose is to ensure cross-platform compatibility on hardware that does not support modern low-overhead APIs. By maintaining this module, the engine can eliminate compatibility gaps, allowing games to run on a wider range of hardware, from older mobile handsets to specialized Linux distributions.

Practical Usage Tips and Best Practices
Use -gl for Testing and Debugging
You can force the editor or a packaged build to use the OpenGL RHI by launching with the -gl or -opengl command-line argument. This is a best practice to eliminate “driver-specific” bugs by verifying if a visual artifact is unique to DirectX/Vulkan or exists across all rendering APIs.
Prioritize Vulkan for Android
While OpenGL ES 3.2 is supported via this module, modern Android devices perform significantly better with Vulkan. Only use the OpenGL RHI as a secondary fallback in your Project Settings to eliminate performance bottlenecks on newer mobile hardware that can leverage more efficient APIs.
Manage the Binary Program Cache
OpenGL suffers from “shader compilation hitching” because it traditionally compiles shaders at runtime. Use the -ClearOpenGLBinaryProgramCache command-line flag during development to eliminate stale or corrupted shader data that could cause crashes or visual glitches after an engine update.
Monitor Mobile Feature Levels
The OpenGL RHI in UE5 typically supports OpenGL ES 3.1 and 3.2. Ensure your materials do not exceed the texture sampler limits of these specifications. Exceeding these limits is a common cause of “black textures” or material compilation failures; keeping your shaders simple helps eliminate these mobile-specific rendering errors.
Validate Linux Compatibility
For Linux development, the OpenGL RHI is often the most stable path for users with older NVIDIA or AMD drivers. If your game fails to launch on Linux via Vulkan, providing an OpenGL launch option is the best way to eliminate user frustration and ensure the game remains accessible to the broader community.
Avoid Using Desktop OpenGL for New Projects
Desktop OpenGL (4.x) is considered a legacy path in UE5. Most modern engine features, such as Lumen and Nanite, require the high-frequency hardware access provided by DX12 or Vulkan. To eliminate technical debt, avoid relying on OpenGL for high-end desktop visuals unless it is a strict requirement for your target platform.
Disable Texture Streaming if Necessary
On some legacy OpenGL drivers, texture streaming can cause significant stalls. If you experience massive hitches on older hardware, use the console variable r.OpenGL.DisableTextureStreamingSupport 1. This will eliminate the streaming logic for OpenGL specifically, though it will increase the initial memory footprint.
Use openglDebug for Driver Analysis
If you encounter a driver-level crash, launch the engine with -openglDebug. This enables the OpenGL Debug Output extension, which provides much more detailed error messages from the GPU driver. This is the fastest way to eliminate ambiguity when trying to determine if a crash is caused by an invalid API call or a hardware failure.