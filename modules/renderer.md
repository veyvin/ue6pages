---
layout: default
title: Renderer
---

<!-- ai-generation-failed -->

<h1>Renderer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Renderer/Renderer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, Engine, GeometryCore, ImageWriteQueue, MaterialShaderQualitySettings, NaniteUtilities, RHI, RenderCore, StateStream, TargetPlatform, TraceLog</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

executing the 3D scene rendering pipeline. It acts as the “brain” that determines how objects are drawn, handling visibility (culling), lighting (Lumen), shadows (Virtual Shadow Maps), post-processing, and the coordination of the RHI (Render Hardware Interface) commands.

This module defines all drawing policies and shaders. By managing the flow of the rendering thread, it facilitates the elimination of unnecessary work through advanced occlusion and frustum culling. It is the primary area where technical artists and graphics engineers perform performance tuning to balance visual fidelity with frame rate.

Practical Usage Tips and Best Practices
1. Choose Between Deferred and Forward Shading

In Project Settings > Rendering, you can toggle the Forward Renderer. While the default Deferred renderer supports more complex lighting, the Forward Renderer provides better performance for VR and mobile. Switching to Forward leads to the elimination of the high memory bandwidth cost of G-Buffers, though it limits some screen-space effects.

2. Profile with the GPU Visualizer

Use the shortcut Ctrl+Shift+, (comma) or the console command ProfileGPU to open the GPU Visualizer. This provides a detailed breakdown of which passes (e.g., Base Pass, Shadow Depths, Bloom) are the most expensive. Monitoring these snapshots leads to the elimination of guesswork when identifying which assets or lights are causing frame drops.

3. Optimize Lumen via Scalability

Lumen is highly performance-intensive. Use the console variable r.Lumen.HardwareRayTracing to toggle between software and hardware-accelerated GI. Tuning these settings for lower-end hardware assists in the elimination of noise and light-leaking while maintaining a stable frame rate for different user configurations.

4. Manage Overdraw with the View Mode

Use the Optimization Viewmodes > Shader Complexity & Quads in the viewport. This visualizes areas where many transparent or complex materials overlap. Reducing overlapping translucent planes leads to the elimination of massive overdraw, which is one of the most common causes of GPU performance degradation.

5. Leverage Virtual Shadow Maps (VSM)

For projects using Nanite and Lumen, ensure Virtual Shadow Maps are enabled in Project Settings. VSM provides consistent, high-resolution shadowing for complex geometry. This technology facilitates the elimination of “shadow acne” and low-resolution cascades, providing a much sharper visual result for distant objects.

6. Control Post-Processing via Volumes

Always use a Post Process Volume with “Infinite Extent” to define the baseline look of your scene. Adjusting settings like Exposure, Bloom, and Color Grading within the volume leads to the elimination of inconsistent lighting across different parts of your world, ensuring the Renderer applies a unified look to the final frame.

7. Utilize Unreal Insights for Bottleneck Analysis

For deep analysis, use Unreal Insights with the GPU trace enabled. This tool provides a timeline view of how the Renderer is interacting with the CPU and GPU threads. Identifying long-running tasks here assists in the elimination of sync issues between the Game Thread and the Render Thread.

8. Use Distance Fields for Optimized Effects

Enable Generate Mesh Distance Fields in Project Settings. This allows the Renderer to use simplified representations of geometry for effects like Distance Field Ambient Occlusion (DFAO) and particle collisions. Using distance fields leads to the elimination of expensive ray-trace or collision checks for ambient lighting and VFX.