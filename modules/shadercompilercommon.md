---
layout: default
title: ShaderCompilerCommon
---

<!-- ai-generation-failed -->

<h1>ShaderCompilerCommon</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/ShaderCompilerCommon/ShaderCompilerCommon.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, FileUtilities, HlslParser, RenderCore, ShaderPreprocessor</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

structures used by the various platform-specific shader compilers (like HLSLCC, DXC, or the Metal compiler). It acts as a middle-tier library that facilitates the preprocessing, minification, and translation of Unreal Shader Format (USF) and Unreal Shader Header (USH) files into a format the hardware-specific backends can ingest.

This module is critical for the “elimination” of code duplication across different shader backends. It handles low-level tasks like macro expansion, virtual file path resolution, and shader reflection, ensuring that custom shaders behave consistently whether they are compiled for DirectX, Vulkan, or Metal.

Practical Usage Tips and Best Practices
Utilize the Shader Minifier
This module contains the FShaderMinifier utility. During the build process, it is used to strip comments and unnecessary whitespace from shader source code. Using this tool helps you eliminate bloated shader binaries, which reduces the final memory footprint of your packaged game assets.
Resolve Virtual Shader Paths
Unreal uses a virtual file system for shaders (e.g., /Engine/Private/...). If you are writing a custom shader compiler extension, use the path resolution functions in this module to map these virtual paths to actual disk locations. This helps you eliminate “File Not Found” errors during the preprocessing stage.
Include Module in Shader Tooling
If you are creating a standalone commandlet or an Editor utility that needs to inspect or validate shader source code, add "ShaderCompilerCommon" to your Build.cs. This gives you access to the engine’s standard preprocessor logic, ensuring you eliminate discrepancies between your tool and the actual engine compiler.
Manage Cross-Platform Macro Definitions
The module defines common macros used across all platforms. When writing custom .usf files, rely on the definitions provided here (like COMPILER_HLSLCC or FEATURE_LEVEL) rather than platform-specific ones. This abstraction helps you eliminate the need for multiple versions of the same shader code.
Inspect Reflection Data for Parameters
ShaderCompilerCommon handles the extraction of reflection data, which identifies which buffers and textures a shader requires. Use this data in your C++ code to verify that your FShaderParameterBindings match the actual shader source, helping you eliminate runtime crashes caused by binding mismatches.
Debug via ‘r.DumpShaderDebugInfo’
This module is responsible for the logic that writes intermediate shader files to the Saved/ShaderDebugInfo folder. Enabling r.DumpShaderDebugInfo=1 allows you to see the “Preprocessed” version of your shader, which is the best way to eliminate bugs hidden behind complex #ifdef blocks.
Handle Header Dependencies Correctly
The module tracks which .ush files are included by a .usf file. When you modify a common header, this dependency tracking ensures the engine re-compiles only the necessary shaders. Understanding this helps you eliminate long, unnecessary full-engine shader recompiles when only a small local change was made.
Cleanup Temporary Preprocessor Files
During high-volume shader compilation (like during a full project cook), the compiler generates many temporary preprocessed files. Upon the “elimination” of the compile task, ensure your custom build scripts or tools allow the engine to clean up these buffers to eliminate excessive disk space consumption in the Intermediate folder.