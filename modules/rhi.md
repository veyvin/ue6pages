---
layout: default
title: RHI
---

<!-- ai-generation-failed -->

<h1>RHI</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/RHI/RHI.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, BuildSettings, Cbor, Core, TraceLog, WindowsD3D</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

on layer that sits between the high-level Renderer and the platform-specific graphics APIs (such as DirectX 12, Vulkan, or Metal). Its primary purpose is to provide a unified C++ interface for creating and managing GPU resources, such as buffers, textures, and shaders, regardless of the underlying hardware.

By providing a common set of commands and states, the RHI facilitates the elimination of platform-specific code in the general rendering pipeline. This allows developers to write complex graphics logic once and have it function across consoles, PC, and mobile devices by translating engine commands into the appropriate API calls at runtime.

Practical Usage Tips and Best Practices
1. Execute Only on the Render Thread

RHI commands are not thread-safe for the Game Thread. Always wrap your RHI logic in an ENQUEUE_RENDER_COMMAND macro or execute it within a dedicated render pass. Adhering to this threading model leads to the elimination of race conditions and memory corruption that occur when the CPU and GPU attempt to access resources simultaneously.

2. Utilize the RHI Command List

Avoid calling static RHI functions directly; instead, use FRHICommandList. This list buffers commands to be executed efficiently by the RHI thread. Using the command list facilitates the elimination of “stalls” in the rendering pipeline, as it allows the engine to parallelize the translation of commands for modern APIs like DX12 and Vulkan.

3. Prefer TStaticState for Pipeline States

When setting render states (like Blend, Rasterizer, or Depth-Stencil states), use the TStaticState templates. These are pre-hashed and cached by the RHI. This practice leads to the elimination of redundant state changes on the GPU, which is a major driver of CPU overhead in complex rendering scenes.

4. Manage Resource Lifetimes with RefCount

RHI resources (like FTextureRHIRef) use reference counting for memory management. Always store these in TRefCountPtr or their specific RHIRef types. Proper reference management leads to the elimination of GPU memory leaks and “use-after-free” crashes that happen when a resource is destroyed while the GPU is still processing it.

5. Use Uniform Buffers for Shader Constants

Instead of setting individual shader parameters one by one, group related data into Uniform Buffers (TUniformBuffer). This allows the RHI to upload a single block of data to the GPU. This optimization assists in the elimination of excessive driver overhead and improves the efficiency of constant data access in your shaders.

6. Minimize RHI Flushes

Calling functions that force the RHI to finish all pending work (like FlushRenderingCommands) causes a massive performance hit. Structure your code to avoid these synchronization points. Minimizing flushes leads to the elimination of “hiccups” and micro-stuttering in the frame rate, keeping the GPU constantly fed with work.

7. Audit with RHI Validation

In development builds, you can enable the RHI Validation layer using the -rhivalidation command line argument. This provides detailed logs if you attempt to use resources incorrectly (e.g., reading from a texture while it is bound as a render target). This tool facilitates the elimination of subtle, hard-to-trace graphical glitches.

8. Transition to RDG (Render Graph)

For modern UE5 development, avoid manual RHI resource management in favor of the Render Graph System (RDG). RDG automatically handles resource lifetimes, transitions, and barriers based on a high-level graph. Using RDG leads to the elimination of manual barrier errors and optimizes the GPU memory footprint via automated transient resource aliasing.