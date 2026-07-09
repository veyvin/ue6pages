---
layout: default
title: CUDAHeader
---

<!-- ai-generation-failed -->

<h1>CUDAHeader</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/NVIDIA/CUDA/CUDAHeader.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the Engine/Source/ThirdParty directory of Unreal Engine. It acts as a standardized “bridge” that provides the necessary header files and include paths for NVIDIA’s CUDA (Compute Device Architecture).

Rather than requiring developers to manually manage local CUDA SDK paths on every workstation, this module allows Unreal’s build system (UBT) to detect and include CUDA functionality in a portable way. It is primarily used by high-performance systems such as Niagara GpuSimulation, ML Deformer, and TensorRT integrations to perform massive parallel computations directly on NVIDIA GPUs.

Practical Usage Tips and Best Practices
Enforce Build.cs Dependencies
To use CUDA in your custom plugin or module, you must add it to your Build.cs. This “eliminates” manual include-path configuration and ensures the Unreal Build Tool knows where to look for the toolkit:
C#
PublicDependencyModuleNames.Add("cudaheader");
Copy code
Wrap Includes to Prevent Naming Collisions
CUDA headers often use common names that conflict with Unreal Engine’s core macros. Always wrap your CUDA includes with the third-party guard macros to “eliminate” compiler errors and macro redefinitions:
C++
	THIRD_PARTY_INCLUDES_START

	#include <cuda_runtime.h>

	#include <cuda.h>

	THIRD_PARTY_INCLUDES_END
Copy code
Platform and Hardware Validation
CUDA is proprietary to NVIDIA hardware. Always wrap your CUDA-specific code in #if PLATFORM_WINDOWS || PLATFORM_LINUX and perform a runtime check for the NVIDIA driver. This “eliminates” crashes or “illegal instruction” errors on users with AMD or Intel GPUs.
Synchronize with the RHI (Rendering Hardware Interface)
If you are passing data between Unreal textures and CUDA kernels, you must use CUDA-Graphics Interop. Ensure you lock the RHI resource before CUDA access and unlock it immediately after to “eliminate” race conditions between the engine’s renderer and your compute kernels.
Leverage Existing Engine Patterns
Before writing a custom implementation, study the Niagara or MLDeformer source code. These modules use cudaheader and demonstrate the “best practice” for sharing GPU buffers between Unreal’s Render Dependency Graph (RDG) and CUDA, “eliminating” the need for expensive GPU-to-CPU memory copies.
Use the Correct CUDA Toolkit Version
Unreal Engine versions are often validated against specific CUDA Toolkit versions (e.g., 11.x or 12.x). To “eliminate” compatibility issues, check the CudaHeader.Build.cs file in the engine source to see which version your specific engine build expects to find on the system.
Handle Memory “Elimination” Carefully
CUDA memory is not managed by Unreal’s Garbage Collector. You must manually call cudaFree for every cudaMalloc. Failing to do so will “eliminate” your available VRAM over time, leading to “Out of Video Memory” crashes in the editor.
Debug with NVIDIA Nsight
Standard Unreal debugging tools cannot step into CUDA kernels. Use NVIDIA Nsight Systems or Nsight Graphics to profile your kernels. This helps “eliminate” performance bottlenecks in your parallel logic that stat GPU might miss.