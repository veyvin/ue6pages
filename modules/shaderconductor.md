---
layout: default
title: ShaderConductor
---

<!-- ai-generation-failed -->

<h1>ShaderConductor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/ShaderConductor/ShaderConductor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

er for the Microsoft DirectX Shader Compiler (DXC), enabling the cross-compilation of HLSL source code into various platform-specific formats.

Description and Purpose

While Unreal Engine authors shaders primarily in HLSL (High-Level Shading Language), those shaders must be translated into bytecode or intermediate languages that different GPUs understand (such as SPIR-V for Vulkan or MSL for Metal). ShaderConductor facilitates this by leveraging the modern DXC infrastructure. Its primary purpose is to provide a unified interface for converting HLSL into high-performance SPIR-V or GLSL while maintaining high fidelity with modern HLSL features (like Shader Model 6.x). By utilizing this module, Unreal Engine can eliminate the discrepancies between different platform compilers, ensuring that a shader written once behaves consistently across Windows, Linux, Android, and consoles.

Practical Usage Tips and Best Practices
Standardize on Modern HLSL
ShaderConductor allows the engine to use the latest DXC features. When writing custom shaders, leverage modern HLSL syntax (e.g., structured buffers, wave intrinsics). This helps you eliminate the need for legacy “workaround” code that was previously required for older cross-compilers like FXC.
Configure via r.ShaderCompiler.JobCache
Because ShaderConductor and DXC are computationally intensive, ensure your shader job cache is active in your BaseEngine.ini. This allows the engine to store the results of the compilation, helping you eliminate redundant recompiles during project startup or when switching between shading models.
Debug via r.DumpShaderDebugInfo
If a shader fails to compile on a specific platform (like Vulkan/Android), set r.DumpShaderDebugInfo=1. The engine will dump the intermediate SPIR-V and the commands sent to ShaderConductor into the Saved/ShaderDebugInfo folder. This is the best way to eliminate guesswork when diagnosing driver-level compiler crashes.
Monitor Vulkan Compatibility
ShaderConductor is the primary path for generating SPIR-V for Vulkan. If you encounter artifacts on mobile devices, check the LogShaderCompilers output for ShaderConductor warnings. These warnings often point to register-limit issues that you should eliminate by optimizing your shader’s local variable usage.
Use for Offline Tooling
If you are developing a standalone tool that needs to validate shaders outside of the Unreal Editor, you can link against the ShaderConductor module in C++. This allows your tool to verify that a .usf file is syntactically correct for all target platforms, helping you eliminate broken shaders before they are ever checked into source control.
Optimize Compile Times with Worker Threads
ShaderConductor calls are often delegated to the ShaderCompileWorker (SCW). To speed up the compilation of a large material library, increase the number of worker processes in your GlobalShaderCompiler.cpp or via the XGE (Incredibuild) settings. This helps eliminate long “Compiling Shaders” wait times.
Validate Half-Precision (FP16) Support
For mobile and console optimization, ShaderConductor handles the translation of float to half precision. Ensure your shader code uses the half type where full precision isn’t needed. This allows ShaderConductor to generate optimized instructions that eliminate unnecessary bandwidth and power consumption on mobile GPUs.
Stay Aligned with DirectX Shader Model Versions
ShaderConductor’s capabilities are tied to the version of DXC it wraps. If you are trying to use the latest Ray Tracing or Mesh Shader features, ensure your project’s Targeting Settings match a Shader Model (e.g., SM6) supported by the module. This is critical to eliminate “Unsupported Feature” errors during the cross-compilation phase.