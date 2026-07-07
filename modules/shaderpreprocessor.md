---
layout: default
title: ShaderPreprocessor
---

<!-- ai-generation-failed -->

<h1>ShaderPreprocessor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/ShaderPreprocessor/ShaderPreprocessor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, RenderCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e shader compilation pipeline responsible for the initial transformation of raw shader source code into a format ready for platform-specific compilers.

Description and Purpose

Before a shader is sent to a backend compiler (like DXC or glslang), it must be “preprocessed” to resolve all #include directives, evaluate #if/#endif macros, and expand #define statements. The ShaderPreprocessor module performs this cross-platform pass, creating a single “flattened” version of the .usf or .ush file. Its primary purpose is to handle Unreal’s virtual file system (mapping paths like /Engine/ or /Plugin/ to physical disk locations) and to inject global defines required by the renderer. By standardizing the code at this stage, the engine can eliminate platform-specific syntax issues and ensure that the same shader logic is applied consistently across all target RHIs.

Practical Usage Tips and Best Practices
Utilize #pragma once in Headers
Unreal’s preprocessor supports #pragma once in .ush files. Always include this at the top of your shader headers to eliminate redundant file parsing and “multiple definition” errors during the preprocessing phase.
Leverage Virtual Shader Paths
The preprocessor resolves paths based on module registrations (e.g., #include "/Plugin/MyPlugin/Private/MyCommon.ush"). Always use these virtual paths instead of relative disk paths to eliminate broken includes when moving assets or sharing code across different project structures.
Inspect Output via r.DumpShaderDebugInfo
If you have complex nested macros, set r.DumpShaderDebugInfo=1. The preprocessor will save the final, flattened .usf file to the Saved/ShaderDebugInfo folder. Reviewing this file is the best way to eliminate logic errors caused by incorrectly evaluated #if blocks.
Enable Shader Development Mode
Set r.ShaderDevelopmentMode=1 in your ConsoleVariables.ini. This causes the preprocessor to provide detailed error logs with exact line numbers when an include is missing or a macro is malformed, helping you eliminate time spent hunting for syntax errors.
Minimize Large Include Chains
Including massive headers like Common.ush in every small shader increases the preprocessor’s workload. Where possible, split your utility functions into smaller, specialized .ush files to eliminate unnecessary overhead and speed up the “Compiling Shaders” phase.
Use r.ShaderCompiler.JobCache for Efficiency
The results of the preprocessor are often cached to prevent redundant work. Ensure your Job Cache is functional to eliminate the need to re-preprocess thousands of shaders after a minor change to a distant, unrelated file.
Validate Macro Definitions in C++
If your C++ code injects defines via FShaderCompilerInput::Environment.SetDefine, ensure the values are valid strings. The preprocessor will fail if a macro is defined without a value or with illegal characters, so verifying these in C++ helps you eliminate mysterious compilation failures.
Check for Platform-Specific Blocks
The preprocessor defines flags like VULKAN_PROFILE or METAL_PROFILE. Use these within your shaders to wrap platform-specific optimizations. This allows the preprocessor to eliminate code branches that are irrelevant to the current target, resulting in cleaner bytecode for the final GPU driver.