---
layout: default
title: CUDA
---

<!-- ai-generation-failed -->

<h1>CUDA</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/CUDA/Source/CUDA.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">CUDAHeader</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

VIDIA CUDA SDK. It is primarily used to facilitate high-performance GPGPU (General-Purpose computing on Graphics Processing Units) tasks that go beyond standard graphics rendering.

While Unreal Engine generally uses HLSL and Compute Shaders for GPU work, the CUDA module is essential for integrating specialized NVIDIA libraries (like those used for AI, physical simulations, or fluid dynamics) and for performing direct memory interop between CUDA kernels and the Unreal RHI (Rendering Hardware Interface).

1. Module Dependency and Platform Logic

The CUDA module is platform-specific and requires NVIDIA hardware.

Best Practice: Always wrap your CUDA module dependencies in your Build.cs with a check for the Windows platform and NVIDIA support to ensure your project still compiles for other platforms (where CUDA logic should be bypassed).
C#
	if (Target.Platform == UnrealTargetPlatform.Win64)

	{

	    PublicDependencyModuleNames.Add("CUDA");

	}
Copy code
2. Leverage for Niagara Fluids

One of the most common uses of the CUDA module in modern UE5 is powering Niagara Fluids.

Tip: If you are developing custom fluid solvers or specialized Niagara Data Interfaces, use the CUDA module to handle the heavy math. It allows for much more complex simulation logic than standard GPU emitters, though it requires users to have an NVIDIA GPU.
3. Direct RHI Interop

The CUDA module provides the necessary structures to share data between CUDA and DirectX/Vulkan without round-tripping to the CPU.

Best Practice: Use Shared Semaphores and External Memory handles. This allows you to run a CUDA kernel to process a buffer and then immediately use that buffer as a texture or vertex array in Unreal’s renderer, which is critical to eliminate the performance bottleneck of PCI-E bus transfers.
4. Manage Resource Lifecycles

CUDA resources are not managed by Unreal’s Garbage Collector.

Constraint: You must manually track and release any CUdeviceptr or cudaGraphicsResource you create. Failing to eliminate these handles in the BeginDestroy or EndPlay phase of your Actor/Component will lead to GPU memory leaks that can eventually crash the display driver.
5. Use for AI and Machine Learning

If you are integrating custom TensorRT or ONNX Runtime models that require direct GPU access, the CUDA module is your primary entry point.

Tip: Use the module to prepare input tensors from engine textures. This is significantly faster for real-time inference (like custom style transfer or pose estimation) compared to processing data on the CPU.
6. Monitor GPU Context Switching

Mixing CUDA work with Unreal’s rendering commands can cause “Context Switching” overhead.

Best Practice: Batch your CUDA calls and use CUDA Streams. This allows the GPU to overlap execution of your custom compute work with Unreal’s own rendering tasks, preventing the custom simulation from stalling the Render Thread.
7. Deployment and Driver Requirements

Using the CUDA module introduces a dependency on the user’s local NVIDIA drivers.

Tip: Always implement a fallback path. If the CUDA module fails to initialize (e.g., on an AMD card or outdated drivers), your game logic should either switch to a standard Compute Shader implementation or gracefully eliminate the specific visual feature to prevent a fatal crash at startup.
8. Debugging with NVIDIA Nsight

Standard Unreal debugging tools (like stat gpu) have limited visibility into raw CUDA kernels.

Best Practice: Use NVIDIA Nsight Systems or Nsight Graphics to profile your CUDA kernels within the context of the Unreal frame. This is the only way to see if your CUDA work is causing bubbles in the GPU pipeline or if it is being properly interleaved with the engine’s Draw Calls.