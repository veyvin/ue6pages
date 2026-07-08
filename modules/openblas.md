---
layout: default
title: OpenBLAS
---

<!-- ai-generation-failed -->

<h1>OpenBLAS</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/OpenBLAS/OpenBLAS.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ebra Subprograms (BLAS) library. It is a highly optimized, open-source library specifically designed for performing complex numerical linear algebra operations on the CPU.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/OpenBLAS, this module provides the engine with accelerated routines for matrix-matrix and matrix-vector multiplications. Because OpenBLAS is tuned for specific CPU architectures (using SIMD instructions like AVX/AVX-512), it is significantly faster than standard C++ loops for mathematical operations.

Primary uses include:

Machine Learning Inference: Serving as a mathematical backend for the NNE (Neural Network Engine) and NeuralNetworkInference modules when running models on the CPU.
Massive Data Processing: Powering plugins that require heavy spatial math, such as the Lidar Point Cloud plugin or complex procedural mesh generation.
Optimization Solvers: Providing the “heavy lifting” for linear solvers used in physics simulations or inverse kinematics (IK) calculations.
Practical Usage Tips and Best Practices
1. Add via Build.cs for Custom Math

If you are writing a custom plugin that requires multiplying massive matrices (e.g., a custom AI or simulation system), add OpenBLAS to your dependencies to perform the elimination of slow, manual for loops.

C#
	// MyModule.Build.cs

	AddEngineThirdPartyPrivateStaticDependencies(Target, "OpenBLAS");
Copy code
2. Respect Threading Limitations

OpenBLAS is highly threaded by default. In a game environment, this can lead to “oversubscription” where OpenBLAS threads fight with the Unreal Task Graph for CPU time. Setting the environment variable OPENBLAS_NUM_THREADS=1 is a common best practice for the elimination of thread contention and micro-stuttering during gameplay.

3. Prefer NNE for High-Level AI

Unless you specifically need raw matrix multiplication (GEMM), use the NNE (Neural Network Engine) module instead of calling OpenBLAS directly. NNE manages the OpenBLAS backend for you, resulting in the elimination of complex data-marshaling code in your gameplay classes.

4. Align Memory for SIMD Performance

OpenBLAS reaches peak performance when data is memory-aligned. When preparing buffers for OpenBLAS routines, use FMemory::Malloc with appropriate alignment or TArray with custom allocators. Proper alignment leads to the elimination of “unaligned access” penalties that can cut math performance in half.

5. Monitor CPU Temperature and Throttling

Because OpenBLAS utilizes aggressive AVX instructions, it can cause the CPU to generate significant heat. If your tool runs OpenBLAS continuously (e.g., during a massive asset bake), monitor for thermal throttling. Efficient batching of calls results in the elimination of heat-induced performance drops.

6. Use for Pre-computation, Not Every-Frame Logic

While fast, calling into a third-party C-library has an interface overhead. Use OpenBLAS for pre-computing data (like generating navigation data or baking vertex animations). This leads to the elimination of frame-time spikes that occur when trying to solve large linear systems on the Game Thread.

7. Verify Platform Support

OpenBLAS is primarily used on Windows, Linux, and Android in the engine. Before relying on it for a cross-platform project, check the ThirdParty/OpenBLAS directory to confirm the .lib or .a files exist for your target. This proactive check ensures the elimination of “Linker Error” surprises late in development.

8. Strategic Elimination of Intermediate Buffers

OpenBLAS routines (like cblas_sgemm) often support “in-place” style operations or can output directly to a pre-allocated buffer. Designing your math pipeline to reuse buffers results in the elimination of constant memory allocations and deallocations, which is critical for maintaining a stable memory footprint.