---
layout: default
title: MetalRHI
---

<!-- ai-generation-failed -->

<h1>MetalRHI</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Apple/MetalRHI/MetalRHI.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, Engine, Projects, RHI, RHICore, RenderCore, Slate, SlateCore, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Apple’s Metal graphics API. It serves as the low-level translation layer that allows the Unreal Engine rendering pipeline to communicate with GPUs on macOS, iOS, and tvOS.

What it is and What it’s used for

Located in Engine/Source/Runtime/Apple/MetalRHI, this module translates generic engine rendering commands into Apple-specific Metal commands. It is responsible for managing GPU resources, shader execution, and memory allocation on Apple hardware.

Primary uses include:

Platform Rendering: Driving the graphics output for all Apple devices, including those with Apple Silicon (M-series) and older Intel-based Macs.
Shader Translation: Compiling cross-platform HLSL shaders into Metal Shading Language (MSL) via the ShaderConductor or DXC.
Feature Support: Enabling modern UE5 features like Lumen, Nanite, and Virtual Shadow Maps on supported Mac hardware (Metal 3.0+).
Resource Management: Handling the unique “Unified Memory” architecture of Apple Silicon to optimize data transfer between the CPU and GPU.
Practical Usage Tips and Best Practices
1. Enable Windows Metal Shader Compilation

To speed up development if your primary workstation is a PC, install the Metal Developer Tools for Windows. This allows the MetalRHI to compile shaders during the Windows “Cook” process. This setup results in the elimination of the requirement to use a Mac for the initial shader compilation phase of your iOS or macOS project.

2. Leverage Metal 3.0 for UE5 Features

In your Project Settings under Platforms > macOS, ensure the Metal Language Version is set to Metal 3.0 (or higher). This is a requirement for the elimination of compatibility issues when using Nanite and hardware-accelerated Ray Tracing on modern Apple Silicon Macs.

3. Monitor Unified Memory Usage

Apple Silicon uses a unified memory pool shared between the CPU and GPU. Use Xcode’s GPU Report or the stat GPU command in-engine to monitor memory pressure. Efficient asset management leads to the elimination of system-wide slowdowns caused by the GPU “swapping” memory to the SSD.

4. Implement PSO Precaching

Metal is highly sensitive to Pipeline State Object (PSO) creation hitches. In UE 5.6+, ensure PSO Precaching is enabled in your project settings. This pre-compiles shaders before they are needed on screen, leading to the elimination of “stutter” or “hitching” when a new effect or object first appears.

5. Use the Metal Frame Capture Tool

When debugging visual artifacts, use the Metal Frame Capture button in the Xcode debugger (or via the captureframe console command if enabled). Analyzing the command buffer directly is the best practice for the elimination of “black screen” bugs or incorrect draw calls specific to Apple’s driver implementation.

6. Optimize for Tile-Based Deferred Rendering (TBDR)

Mobile Apple GPUs use TBDR architecture. Keep your render passes efficient and minimize “Render Target” switches. This helps the MetalRHI keep data within the high-speed on-chip tile memory, resulting in the elimination of excessive bandwidth consumption and battery drain on mobile devices.

7. Profile with “Metal Performance Shaders” (MPS)

The MetalRHI can leverage Apple’s highly optimized MPS for tasks like image processing and ray tracing intersections. Using these built-in kernels through the RHI ensures the elimination of suboptimal custom compute shader performance on iOS and macOS.

8. Strategic Elimination of Legacy Metal Versions

If your project is targeting modern hardware, perform the elimination of support for older Metal versions (like 1.2 or 2.0) in your Target Platform settings. Limiting your project to modern Metal versions allows the RHI to use more efficient bindless resource patterns and reduces the number of shader permutations that need to be compiled.