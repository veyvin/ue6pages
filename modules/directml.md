---
layout: default
title: DirectML
---

<!-- ai-generation-failed -->

<h1>DirectML</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/DirectML/DirectML.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ed DirectX 12 library for machine learning (ML). It allows developers to run neural network inference directly on the GPU using the DirectX Raytracing (DXR) and Compute pipelines.

In Unreal Engine, DirectML is primarily accessed through the Neural Network Engine (NNE) plugin via the NNERuntimeORTDml backend. It is the preferred solution for running ML models (like upscalers, physics predictors, or character deformation models) on Windows-based hardware, as it provides a standardized way to leverage the power of any DX12-compatible GPU (including NVIDIA, AMD, and Intel).

1. Require DirectX 12 RHI

DirectML is built on top of the DirectX 12 API and cannot run on older versions.

Best Practice: Ensure your project is set to use the DirectX 12 RHI in the Project Settings. DirectML will fail to initialize if the engine falls back to DX11 or Vulkan. Always include a check in your C++ code to verify the current RHI before attempting to load a DirectML model.
2. Interface via Neural Network Engine (NNE)

While you can use raw DirectML, it is highly recommended to use the NNE abstraction.

Tip: Use UE::NNE::GetRuntime(TEXT("NNERuntimeORTDml")). This provides a consistent INNERuntimeRDG interface. By using NNE, you can easily swap the backend to a CPU or CUDA runtime later without having to rewrite your core inference logic.
3. Use the Render Dependency Graph (RDG)

Running ML inference on the GPU can stall the frame if it isn’t properly synchronized with the engine’s rendering tasks.

Best Practice: Use the INNERuntimeRDG interface to enqueue your model. This allows the DirectML work to be scheduled by Unreal’s Render Dependency Graph, enabling the engine to overlap the ML task with other GPU work (like shadow depth passes) and ensuring proper resource synchronization to eliminate pipeline bubbles.
4. Optimize Models for the DML Provider

DirectML in Unreal primarily consumes ONNX models, but they must be prepared correctly.

Tip: Open your UNNEModelData asset in the Editor and ensure NNERuntimeORTDml is checked in the “Supported Runtimes” list. This triggers the engine to pre-optimize the model for the DirectML execution provider during the cook process, significantly speeding up model loading at runtime.
5. Validate Tensor Shapes

DirectML is extremely sensitive to input dimensions and will cause a GPU crash if the input data doesn’t match the model’s expectations.

Best Practice: Use Model->GetInputTensorShapes() to validate your input buffers (textures or arrays) before calling EnqueueInference. This is critical when processing dynamic resolutions, such as when using a DirectML-based upscaler that must handle different screen aspect ratios.
6. Leverage Half-Precision (FP16)

For real-time games, memory bandwidth and VRAM usage are often more important than absolute numerical precision.

Tip: Use FP16 (Half-Float) models where possible. DirectML has excellent hardware support for FP16 on modern GPUs, which can effectively double your inference speed and eliminate 50% of the VRAM footprint compared to standard FP32 models.
7. Warm Up the DDC Cache

The first time a DirectML model is loaded, the system may need to compile specific “operator fusions” for the local GPU.

Best Practice: This compilation can cause a significant “hitch” during gameplay. To eliminate this, load and initialize your models during a loading screen or via a background task using the Derived Data Cache (DDC). This ensures that the compiled GPU kernels are ready before the player enters the action.
8. Profile with NVIDIA Nsight or PIX

Standard Unreal GPU profilers (like stat gpu) often group DirectML work into a generic “Compute” or “External” category.

Tip: If your ML model is impacting the frame rate, use Microsoft PIX or NVIDIA Nsight. These tools can “see” inside the DirectML dispatch calls, allowing you to identify which specific neural network layers (e.g., a heavy Convolution) are the bottleneck.