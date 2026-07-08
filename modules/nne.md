---
layout: default
title: NNE
---

<!-- ai-generation-failed -->

<h1>NNE</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/NNE/NNE.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DerivedDataCache</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

r running neural network inference in real-time. It acts as an abstraction layer—similar to how RHI abstracts graphics APIs—allowing developers to run AI models across different backends (like ONNX Runtime, DirectML, or CoreML) using a single, consistent C++ API.

What it is and What it’s used for

Located in Engine/Source/Runtime/NNE, this module provides the interfaces required to load pre-trained models and execute them efficiently. It is designed to handle the complexities of data marshaling between the CPU/GPU and the inference engine.

Primary uses include:

Real-Time Game Logic: Powering AI behaviors, such as complex pathfinding or decision-making, using trained models.
Character Animation: Driving systems like ML Deformer for high-fidelity skinning and muscle simulation.
Asset Processing: Running in-editor tools for style transfer, automated tagging, or upscaling.
Cross-Platform AI: Ensuring that a model trained in PyTorch or TensorFlow (exported as ONNX) can run on Windows, Mac, Linux, and mobile devices without platform-specific code.
Practical Usage Tips and Best Practices
1. Choose the Correct Interface for Your Use Case

NNE provides three primary interfaces. Selecting the wrong one can lead to massive performance overhead:

INNERuntimeCPU: Best for logic-heavy AI where results are needed for gameplay decisions.
INNERuntimeGPU: Best for editor-side processing or independent tasks.
INNERuntimeRDG: Best for frame-aligned effects (like denoisers) that need to interact directly with the Render Dependency Graph. Selecting the right interface ensures the elimination of unnecessary synchronization stalls between the CPU and GPU.
2. Utilize Model Data Filtering

When you import an .onnx file, it creates a UNNEModelData asset. In the asset editor, you can filter which runtimes the model is optimized for. Unchecking runtimes you don’t intend to use results in the elimination of bloated package sizes and reduces cook times significantly.

3. Use Asynchronous Inference for Gameplay

Never run heavy inference directly on the Game Thread. For INNERuntimeCPU, wrap your RunSync calls in an AsyncTask or use the built-in async capabilities of the runtime. Offloading this work leads to the elimination of frame-rate hitches, keeping the player experience smooth while the “brain” calculates in the background.

4. Bind Memory to Avoid Data Copies

When passing data to IModelInstanceCPU, use SetInputTensorShapesAndData to point the engine directly to your existing memory buffers (e.g., a TArray<float>). This zero-copy approach is the best practice for the elimination of redundant memory allocations and CPU cycles spent moving data.

5. Verify Model Compatibility at Runtime

Not all models are supported by all runtimes (e.g., a specific operator might be missing in a mobile backend). Always check Runtime.IsValid() and Model->CreateModelInstance().IsValid() before attempting inference. This defensive coding ensures the elimination of crashes when your game runs on hardware with limited AI instruction sets.

6. Leverage the Derived Data Cache (DDC)

NNE caches optimized versions of your models in the DDC. During development, if a model feels slow to load the first time, it is likely being optimized. Understanding this allows for the elimination of “performance anxiety” during the first run, as subsequent loads will be significantly faster due to the cached binary.

7. Profile with Unreal Insights

Use Unreal Insights to track the time spent in RunSync or RunAsync. If the inference time is exceeding your frame budget, consider “Quantizing” your model (converting it from FP32 to INT8). Model quantization is a primary strategy for the elimination of CPU bottlenecks in complex AI systems.

8. Strategic Elimination of Unused Model Instances

Model Instances (IModelInstanceCPU/GPU) hold the state and intermediate buffers for an execution. If an Actor is eliminated or a logic state ends, ensure you reset the TUniquePtr holding the instance. Proper lifecycle management results in the elimination of memory leaks, especially when dealing with large models that allocate significant internal scratch space.