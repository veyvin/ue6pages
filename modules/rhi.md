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

straction layer that sits between high-level rendering code (like the Renderer module) and low-level graphics APIs (DX12, Vulkan, Metal). Its primary purpose is to provide a unified C++ interface so that the engine can perform draw calls, manage GPU buffers, and set pipeline states without needing to know which specific platform or graphics card is being used.

It manages the communication between the Render Thread (which determines what to draw) and the RHI Thread (which translates those commands into API-specific calls).

Practical Usage Tips and Best Practices
1. Prefer RDG Over Raw RHI

In modern Unreal Engine development, you should rarely use the RHI module directly. Instead, use the Render Dependency Graph (RDG). RDG sits on top of RHI and automatically handles resource lifetimes, synchronization, and transient memory aliasing. Utilizing RDG leads to the elimination of manual “Barriers” and complex resource-state tracking.

2. Respect Thread Boundaries

RHI commands must only be executed on the Render Thread. Attempting to call RHI functions from the Game Thread will cause immediate crashes or race conditions. Use the ENQUEUE_RENDER_COMMAND macro to safely send logic from the Game Thread to the Render Thread, ensuring the elimination of threading-related memory corruption.

3. Minimize Pipeline State Changes

The RHI is a “thin” layer, but every state change (like switching a Blend State or Depth State) has a cost on the driver. Use TStaticState templates (e.g., TStaticBlendState) to define states at compile-time. This allows the RHI to cache and reuse state objects, facilitating the elimination of redundant API calls during the frame.

4. Use “stat RHI” for Profiling

To understand your GPU overhead, use the console command stat RHI. This display shows critical metrics such as the number of Draw Calls, Triangles, and Render Target switches occurring per frame. Monitoring these numbers is the first step toward the elimination of CPU bottlenecks caused by excessive draw call counts.

5. Avoid Mid-Frame Flushes

Avoid calling functions that force the CPU to wait for the GPU, such as FlushRenderingCommands() or locking a buffer with RLM_ReadOnly, unless absolutely necessary. These “flushes” stall the pipeline and result in the elimination of any performance gains from Unreal’s multi-threaded rendering architecture.

6. Utilize Feature Levels for Compatibility

When writing RHI-level code, always check the current ERHIFeatureLevel. Logic designed for SM6 (DX12) might fail on ES3_1 (Mobile). Wrapping your code in feature level checks ensures the elimination of crashes when your game runs on hardware that does not support specific modern graphics techniques.

7. Profile with the GPU Crash Debugger

If you are developing custom RHI-level shaders or passes and encounter a GPU hang, use r.GPUCrashDebugging=1. This tracks RHI command execution and helps pinpoint exactly which command caused the hardware to fail. This is essential for the elimination of “TDR” (Timeout Detection and Recovery) errors.

8. Use Uniform Buffers for Constant Data

When passing data to shaders, prefer Uniform Buffers over individual shader parameters. Grouping variables into a single buffer that is updated once per pass is significantly more efficient for the RHI to handle, leading to the elimination of overhead associated with frequent “SetShaderParameter” calls.