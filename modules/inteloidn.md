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

ction of the time required for raw convergence.

Practical Usage Tips & Best Practices
1. Enable the Module for High-Quality Path Tracing

The Intel OIDN denoiser is superior to standard temporal denoisers for high-end cinematic stills and long-running frames.

Best Practice: In your Post Process Volume, set the Denoiser to Open Image Denoise. This ensures the elimination of grainy artifacts in your final renders, particularly in scenes with complex global illumination or soft shadows.
2. Configure Neural Network Engine (NNE) Settings

In modern versions of Unreal Engine (5.3+), OIDN is often handled via the NNE Denoiser plugin.

Tip: Use the console command r.PathTracing.Denoiser.Name NNEDenoiser to ensure you are using the latest optimized neural network models. Proper configuration results in the elimination of “smearing” artifacts often seen in older AI denoising versions.
3. Optimize GPU Lightmass Bakes

GPU Lightmass relies heavily on OIDN to smooth out lightmap results during the final stage of a bake.

Best Practice: In the GPU Lightmass settings, set Denoise: On Completion. This allows the engine to bake at a lower sample count and then apply OIDN as a post-process, leading to the elimination of hours of unnecessary rendering time while maintaining smooth light gradients.
4. Use “Reference Motion Blur” in Movie Render Queue

When rendering animations, denoising every individual sub-sample can cause flickering or “wobbling.”

Tip: Enable Reference Motion Blur in the Path Tracer settings within the Movie Render Queue. This causes the engine to combine samples before applying the Intel OIDN pass, which facilitates the elimination of temporal instability in moving shots.
5. Balance Samples vs. Denoising Quality

Applying OIDN to an extremely low-sample image (e.g., 1–4 samples per pixel) will result in a “watery” or “painterly” look.

Best Practice: Aim for at least 128 to 256 samples before allowing the denoiser to take over. Providing a cleaner base image to the IntelOIDN module results in the elimination of AI-generated “ghosting” or loss of fine geometric detail.
6. Toggle Interactive Denoising for Faster Iteration

For real-time look development, you can see denoised results as you move the camera.

Tip: Enable Interactive Denoising in the GPU Lightmass or Path Tracer settings. While it adds a small CPU overhead per frame, it ensures the elimination of visual noise during the setup phase, allowing you to judge lighting and materials much faster.
7. Monitor CPU/GPU Overhead

Because OIDN can run on the CPU, it can sometimes compete with the engine’s main threads during heavy bakes.

Best Practice: If your system becomes unresponsive during denoising, check the NNE Denoiser settings in the Project Settings to see if the runtime is set to CPU or GPU. Switching to a GPU-accelerated runtime (if supported) leads to the elimination of system-wide stalls during the final render phase.
8. Ensure Proper Albedo and Normal Passes

OIDN uses “Auxiliary Buffers” (Albedo and Normal data) to distinguish between lighting noise and actual texture detail.

Tip: If your textures look blurry after denoising, verify that your materials are outputting clean Albedo and Normal information to the Path Tracer. Ensuring high-quality auxiliary data assists in the elimination of detail loss, keeping your high-frequency textures sharp even after noise removal.