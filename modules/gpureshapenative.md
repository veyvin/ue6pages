---
layout: default
title: GPUReshapeNative
---

<!-- ai-generation-failed -->

<h1>GPUReshapeNative</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/GPUReshape/Source/GPUReshapeNative/GPUReshapeNative.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

it is and What it’s used for

Located within the RHI and RenderCore layers, this module handles the dynamic reconfiguration of GPU memory. In modern graphics APIs (DX12, Vulkan, and Console APIs), memory is often managed in large heaps. “Reshaping” allows the engine to change how a specific region of GPU memory is interpreted at the hardware level.

Primary uses include:

Transient Resource Aliasing: Underpinning the Render Dependency Graph (RDG) by “reshaping” a single block of memory to serve as different resources across various passes in a frame.
Buffer Layout Adaptation: Dynamically adjusting the stride, count, or type of structured buffers (e.g., for Niagara or Nanite) to match varying workloads.
Memory Footprint Optimization: Ensuring that resources occupy the minimum required space on the GPU, leading to the elimination of wasted VRAM.
RHI Thread Efficiency: Translating high-level resource changes into platform-specific commands (like DiscardResource or PlaceResource) during the RHI submission phase.
Practical Usage Tips and Best Practices
1. Leverage RDG for Automatic Reshaping

As a developer, you rarely interface with GPUReshapeNative directly. Instead, use the Render Dependency Graph (RDG). RDG utilizes this module to manage the elimination of redundant memory allocations. By using FRDGBuilder::CreateTexture or CreateBuffer, you allow the RHI to automatically “reshape” and reuse existing GPU memory blocks.

2. Monitor via the GPU Profiler

Use the UE 5.6+ GPU Profiler (ProfileGPU or Ctrl+Shift+,) to look for “Reshape” or “Alias” events. These markers indicate where the hardware is reinterpreting memory. Excessive reshaping within a single frame can sometimes suggest a fragmented RDG pass structure that could be optimized.

3. Optimize Transient Memory with CVars

You can influence how the engine reshapes and reuses GPU memory via console variables. For example, r.RDG.TransientAllocator controls how aggressively the engine aliases memory. Fine-tuning these settings is a best practice for reaching the elimination of out-of-memory (OOM) crashes on consoles.

4. Understand “Native” Platform Variations

The “Native” suffix signifies that behavior depends on the target hardware. On DX12, this involves ID3D12Resource aliasing, while on Vulkan, it involves memory binding tweaks. When debugging GPU hangs, check if the error occurs during a resource transition; this often points to a layout mismatch handled by this module.

5. Strategic Elimination of Resource Barriers

GPU Reshaping is often computationally tied to Resource Barriers. To minimize performance overhead, try to group passes that use the same “reshaped” memory footprint together. This reduces the number of times the RHI has to signal the GPU to change its memory interpretation.

6. Use for Large-Scale Compute Buffers

If writing custom Compute Shaders, use Structured Buffers with the BUF_AnyShaderResource flag. This allows the RHI to “reshape” the buffer view depending on whether it’s accessed as a ByteAddressBuffer or a StructuredBuffer in different pipeline stages.

7. Profile Memory Aliasing with Unreal Insights

Run your project with the -trace=gpu,memory flag and view the results in Unreal Insights. Look for the “Transient Resource” track. If you see many “gaps” between resources, the GPU Reshaper is struggling to fit resources into contiguous memory. Consider adjusting your Texture Pool size to provide more overhead.

8. Verify Layouts with “DumpGPU”

Use the r.DumpGPU.Viewer.Visualize 1 command to inspect how buffers are being interpreted. If a buffer is being “reshaped” into a layout that doesn’t match your shader’s expectation (e.g., incorrect stride), you will see corrupted data in the viewer, allowing for rapid debugging of low-level memory issues.