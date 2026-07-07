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

r-Only” third-party wrapper in Unreal Engine. It provides the necessary C++ headers (cuda.h, cuda_runtime.h, etc.) and function pointer definitions required to interface with the NVIDIA CUDA Driver and Runtime APIs.

Its primary purpose is to allow Unreal Engine modules—such as those for machine learning, complex physics, or specialized compute tasks—to leverage NVIDIA GPU hardware for GPGPU (General-Purpose GPU) calculations without requiring every developer to manually install the full CUDA Toolkit in their system’s global include paths.

Practical Usage Tips and Best Practices
1. Add as an External Module Dependency

To use CUDA in your custom C++ module, you must tell the Unreal Build Tool (UBT) to include these headers.

Action: Add the module to your Build.cs file. Use AddEngineThirdPartyPrivateStaticDependencies to ensure the paths are correctly mapped by the engine.
C#
	    // In YourProject.Build.cs

	    if (Target.Platform == UnrealTargetPlatform.Win64)

	    {

	        AddEngineThirdPartyPrivateStaticDependencies(Target, "CUDA");

	    }

	    ```

	 

	#### 2. Wrap Includes to Prevent Naming Conflicts

	NVIDIA’s headers often use common names or macros that conflict with Unreal’s `check`, `verify`, or `TYPE_ANY` definitions.

	*   **Action:** Always wrap CUDA includes with Unreal’s protection macros to **eliminate** "macro redefinition" compiler errors.

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include <cuda.h>

	    #include <cuda_runtime.h>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	#### 3. Share Resources via RHI Interoperability

	The most common mistake is trying to copy data back to the CPU to show it in Unreal. This is extremely slow.

	*   **Tip:** Use **CUDA-RHI Interop** (DirectX 12 or Vulkan). You can register a `FRHITexture` or `FRHIVertexBuffer` directly with CUDA as a "Graphics Resource." This allows CUDA to write directly into Unreal's GPU memory, **eliminating** expensive PCIe bus transfers.

	 

	#### 4. Guard with Platform and Hardware Checks

	CUDA only runs on NVIDIA hardware. If a user with an AMD or Intel GPU runs your code, it will crash or fail to initialize.

	*   **Best Practice:** Always check `FAndroidMisc::GetGPUFamily()` or use the CUDA Driver API `cuInit(0)` to verify an NVIDIA driver is present before calling any CUDA functions. This helps **eliminate** startup crashes on non-compatible hardware.

	 

	#### 5. Use TAsync or Task Graph for GPU Launching

	Launching a CUDA kernel is asynchronous on the GPU, but the API calls to set it up can still cause a minor hitch on the Game Thread.

	*   **Tip:** Wrap your CUDA launch logic in a `UE::Tasks::Launch` or `AsyncTask`. This keeps the Game Thread free for gameplay logic while the CPU waits for the GPU to finish its heavy math, **eliminating** frame-rate drops.

	 

	#### 6. Manage CUDA Contexts Carefully

	Unreal manages its own GPU contexts for rendering (DirectX/Vulkan). Creating a "Global" CUDA context can sometimes interfere with the engine's ability to reset the device.

	*   **Action:** Use "Scoped Contexts." Ensure you push and pop the CUDA context within your function scope using `cuCtxPushCurrent` and `cuCtxPopCurrent`. This ensures you don't "steal" the GPU focus from Unreal's renderer, **eliminating** device-loss errors.

	 

	#### 7. Synchronize with the Render Thread

	If CUDA is writing to a texture that Unreal is currently drawing, you will see "tearing" or "flickering."

	*   **Best Practice:** Use **GPU Semaphores** or Windows Fence objects to synchronize. Ensure the Render Thread (FRHICommandList) has finished with the resource before CUDA begins its work. This helps **eliminate** visual artifacts and race conditions.

	 

	#### 8. Leverage the "External" Module Type

	If you are adding a newer version of CUDA than what Unreal provides, you can create your own `CUDAHeader.Build.cs` as an `External` module.

	*   **Tip:** Set `Type = ModuleType.External;` in your `Build.cs`. This tells UBT that this module doesn't contain C++ code to be compiled, but merely provides include paths and pre-compiled `.lib` files, **eliminating** unnecessary build time.
Copy code
2. Wrap Includes to Eliminate Macro Conflicts

NVIDIA’s headers often define macros (like check or TYPE_ANY) that conflict with Unreal’s own definitions, which will cause compilation failure.

Best Practice: Always wrap the CUDA includes with Unreal’s protection macros to eliminate “macro redefinition” errors.
C#
	    // In YourProject.Build.cs

	    if (Target.Platform == UnrealTargetPlatform.Win64)

	    {

	        AddEngineThirdPartyPrivateStaticDependencies(Target, "CUDA");

	    }

	    ```

	 

	#### 2. Wrap Includes to Prevent Naming Conflicts

	NVIDIA’s headers often use common names or macros that conflict with Unreal’s `check`, `verify`, or `TYPE_ANY` definitions.

	*   **Action:** Always wrap CUDA includes with Unreal’s protection macros to **eliminate** "macro redefinition" compiler errors.

	    ```cpp

	    THIRD_PARTY_INCLUDES_START

	    #include <cuda.h>

	    #include <cuda_runtime.h>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	#### 3. Share Resources via RHI Interoperability

	The most common mistake is trying to copy data back to the CPU to show it in Unreal. This is extremely slow.

	*   **Tip:** Use **CUDA-RHI Interop** (DirectX 12 or Vulkan). You can register a `FRHITexture` or `FRHIVertexBuffer` directly with CUDA as a "Graphics Resource." This allows CUDA to write directly into Unreal's GPU memory, **eliminating** expensive PCIe bus transfers.

	 

	#### 4. Guard with Platform and Hardware Checks

	CUDA only runs on NVIDIA hardware. If a user with an AMD or Intel GPU runs your code, it will crash or fail to initialize.

	*   **Best Practice:** Always check `FAndroidMisc::GetGPUFamily()` or use the CUDA Driver API `cuInit(0)` to verify an NVIDIA driver is present before calling any CUDA functions. This helps **eliminate** startup crashes on non-compatible hardware.

	 

	#### 5. Use TAsync or Task Graph for GPU Launching

	Launching a CUDA kernel is asynchronous on the GPU, but the API calls to set it up can still cause a minor hitch on the Game Thread.

	*   **Tip:** Wrap your CUDA launch logic in a `UE::Tasks::Launch` or `AsyncTask`. This keeps the Game Thread free for gameplay logic while the CPU waits for the GPU to finish its heavy math, **eliminating** frame-rate drops.

	 

	#### 6. Manage CUDA Contexts Carefully

	Unreal manages its own GPU contexts for rendering (DirectX/Vulkan). Creating a "Global" CUDA context can sometimes interfere with the engine's ability to reset the device.

	*   **Action:** Use "Scoped Contexts." Ensure you push and pop the CUDA context within your function scope using `cuCtxPushCurrent` and `cuCtxPopCurrent`. This ensures you don't "steal" the GPU focus from Unreal's renderer, **eliminating** device-loss errors.

	 

	#### 7. Synchronize with the Render Thread

	If CUDA is writing to a texture that Unreal is currently drawing, you will see "tearing" or "flickering."

	*   **Best Practice:** Use **GPU Semaphores** or Windows Fence objects to synchronize. Ensure the Render Thread (FRHICommandList) has finished with the resource before CUDA begins its work. This helps **eliminate** visual artifacts and race conditions.

	 

	#### 8. Leverage the "External" Module Type

	If you are adding a newer version of CUDA than what Unreal provides, you can create your own `CUDAHeader.Build.cs` as an `External` module.

	*   **Tip:** Set `Type = ModuleType.External;` in your `Build.cs`. This tells UBT that this module doesn't contain C++ code to be compiled, but merely provides include paths and pre-compiled `.lib` files, **eliminating** unnecessary build time.
Copy code
3. Use RHI Interoperability for Performance

Transferring data from CUDA (GPU) back to the CPU and then back to Unreal (GPU) is extremely slow.

Tip: Use the CUDA-RHI Interop features. Register your Unreal FRHITexture or FRHIVertexBuffer directly with CUDA as a “Graphics Resource.” This allows CUDA to write directly into the engine’s GPU memory, eliminating the need for expensive PCIe bus transfers.
4. Guard Hardware-Specific Code

CUDA code only executes on NVIDIA hardware. Running this code on a machine with an AMD or Intel GPU will result in a crash or driver error.

Action: Always perform a runtime check using cuInit(0) or check the GPU vendor ID before calling CUDA functions. This helps eliminate startup crashes on non-compatible hardware.
5. Offload Kernel Launches from the Game Thread

While launching a CUDA kernel is asynchronous on the GPU, the API calls to set up the launch can still cause a minor hitch on the Game Thread.

Tip: Use the Unreal Task Graph or AsyncTask to handle the setup and launch of your CUDA kernels. This ensures the main gameplay logic remains smooth and helps eliminate frame-rate drops during heavy compute tasks.
6. Implement Scoped Context Management

Unreal manages its own GPU contexts for rendering. If your CUDA code “steals” the current context and doesn’t return it, the engine’s renderer may crash.

Best Practice: Use scoped context pushes and pops (cuCtxPushCurrent and cuCtxPopCurrent). This ensures that your CUDA operations are isolated from the engine’s rendering state, eliminating potential “Device Lost” errors.
7. Synchronize with GPU Fences

If you are writing to a texture that Unreal is currently using for rendering, you will see flickering or “tearing” artifacts.

Action: Use GPU Semaphores or Windows Fence objects to synchronize. Ensure the Render Thread has finished its work before the CUDA kernel starts. Proper synchronization will eliminate visual glitches and data race conditions.
8. Leverage the External Module Pattern for Upgrades

If your project requires a specific version of CUDA not provided by the engine’s default module:

Tip: Create your own MyCUDA.Build.cs and set Type = ModuleType.External;. This allows you to point to a specific version of the CUDA Toolkit on your local machine or server, eliminating version mismatch issues in specialized production pipelines.