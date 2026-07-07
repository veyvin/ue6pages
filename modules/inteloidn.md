---
layout: default
title: IntelOIDN
---

<!-- ai-generation-failed -->

<h1>IntelOIDN</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Intel/OIDN/IntelOIDN.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li><li><span class="label">依赖</span><span class="value">IntelTBB</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rary into Unreal Engine, providing a high-performance, AI-driven solution for cleaning up noisy images.

Description and Purpose

This module is a CPU-based denoiser designed primarily for the Path Tracer and GPU Lightmass. Because path-tracing techniques naturally produce “grain” or “noise” (especially in shadowed or complex-lighting areas), the IntelOIDN module uses deep-learning algorithms to differentiate between actual scene detail and ray-tracing artifacts. Its primary goal is to eliminate visual noise, allowing developers to achieve high-quality, cinematic results with significantly fewer samples per pixel, which dramatically reduces rendering and baking times.

Practical Usage Tips and Best Practices
Switching Denoisers via Console Variables
If you have multiple denoiser plugins enabled (like OptiX), you must specify OIDN to use it. Use the command r.PathTracing.Denoiser.Name OIDN to ensure the Intel library is active. This helps you eliminate confusion when comparing different AI denoising results.
Enable for GPU Lightmass Baking
In the GPU Lightmass settings, set the Denoise When property to “On Completion” or “During Interactive Preview.” This utilizes the IntelOIDN module to smooth out your lightmaps after the GPU finishes tracing, helping you eliminate blotchy shadows in your static lighting.
Improve Temporal Stability in Sequencer
When rendering cinematics with the Movie Render Queue (MRQ), OIDN may produce slight flickering between frames. To eliminate this, increase your Temporal Sample Count in the MRQ Anti-Aliasing settings. This provides the denoiser with more consistent data across the timeline.
Balance Samples vs. Denoising Quality
While OIDN is powerful, it cannot reconstruct details from extremely low sample counts without creating “smearing” artifacts. Aim for a moderate base sample count (e.g., 64–128 samples) before applying the denoiser to eliminate the “painted” look that occurs when the AI has too little information.
Use for High-Quality CPU Denoising
Because OIDN runs on the CPU, it does not compete for VRAM with the Path Tracer. This makes it an excellent choice for complex scenes where you are already hitting the limits of your GPU memory, helping you eliminate out-of-video-memory crashes during the final render.
Configure NNE Denoiser Presets
In newer versions of UE (5.3+), OIDN is often accessed via the NNE (Neural Network Engine) plugin. Ensure “Show Plugin Content” is enabled in your asset picker to find the OIDN runtime assets. This allows you to select “Balanced” or “High Quality” presets to eliminate specific types of rendering artifacts.
Optimize for “Interactive Preview” Mode
If using OIDN for interactive previews, be aware that it involves a memory round-trip (GPU to CPU and back). For large resolutions, this can cause a slight stutter. Lowering your viewport resolution percentage during setup can help you eliminate this latency while still getting a clear idea of the final lighting.
Pre-Divide Albedo for Detail Preservation
To keep textures sharp under the denoiser, ensure your albedo data is clean. OIDN uses “Auxiliary Features” (like Albedo and Normal maps) to guide the denoising process. Correctly setting these up in the Path Tracer settings helps the AI eliminate noise without blurring your high-frequency surface details.