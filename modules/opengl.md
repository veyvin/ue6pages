---
layout: default
title: OpenGL
---

<!-- ai-generation-failed -->

<h1>OpenGL</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/OpenGL/OpenGL.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

er Hardware Interface (RHI) implementation for the OpenGL graphics API. While modern Unreal Engine development on Windows, Linux, and Android has shifted toward Vulkan and DirectX 12, this module remains in the engine to provide compatibility for older hardware and specific mobile devices that do not support modern explicit APIs.

In current versions of Unreal Engine, this module is primarily used for Android OpenGL ES 3.2 support. It acts as a translation layer between the engine’s high-level rendering commands and the OpenGL driver, facilitating the elimination of compatibility barriers for players using older mobile chipsets or legacy Linux environments.

Practical Usage Tips and Best Practices
1. Prioritize Vulkan Over OpenGL

Whenever possible, you should use the Vulkan RHI instead of OpenGL for Android and Linux projects. Vulkan offers significantly better CPU performance and multi-threading capabilities. Moving to Vulkan leads to the elimination of driver-side bottlenecks that are inherent to the aging OpenGL state machine.

2. Enable via Project Settings

To support older Android devices, navigate to Project Settings > Platforms > Android > Build and ensure Support OpenGL ES3.2 is checked. This ensures the OpenGLDrv module is included in your packaged build. Failure to include this leads to the elimination of your app’s ability to run on devices that lack Vulkan drivers.

3. Monitor Shader Complexity for Mobile

OpenGL ES 3.2 has stricter limits on texture samplers and uniform buffers compared to desktop APIs. Using the Mobile Stats visualization in the viewport facilitates the elimination of “Shader Compile Failed” errors by identifying materials that exceed the capabilities of the OpenGL ES hardware.

4. Use Console Variables for Debugging

If you encounter visual artifacts specific to this RHI, use console commands starting with r.OpenGL.. For example, r.OpenGL.AllowSyncCheck 1 can help identify CPU/GPU synchronization issues. Proper use of these variables assists in the elimination of “flickering” or “black screen” bugs during device testing.

5. Verify Feature Support (SM5 vs. ES3.1)

The OpenGL module in Unreal Engine is primarily tuned for the Mobile Forward renderer. Attempting to use high-end desktop features like Lumen or Nanite on an OpenGL RHI will lead to the elimination of those features at runtime, as they require the modern bindless architectures found in DX12 and Vulkan.

6. Handle Device Compatibility via Profiles

Use Device Profiles to automatically disable intensive post-processing when the engine detects it is running via the OpenGL RHI. This practice leads to the elimination of thermal throttling and poor frame rates on the older, lower-powered devices that typically rely on this module.

7. Audit Texture Compression

The OpenGL module for mobile primarily relies on ETC2 or ASTC texture compression. Ensure your textures are properly compressed for these formats in the cook settings. Using incompatible compression leads to the elimination of texture detail, as the engine will be forced to uncompress textures into memory, potentially causing a crash.

8. Transition to Modern APIs for Linux

For Linux desktop development, the engine now defaults to Vulkan. Avoid forcing the -opengl command-line argument unless specifically debugging legacy hardware. Embracing the modern RHI facilitates the elimination of the stuttering and high CPU overhead associated with the older OpenGL implementation on Linux.