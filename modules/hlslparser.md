---
layout: default
title: HlslParser
---

<!-- ai-generation-failed -->

<h1>HlslParser</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/HlslParser/HlslParser.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ST).

This module is primarily used during the shader compilation process to “eliminate” platform dependencies. By parsing HLSL into an intermediate representation, Unreal can perform device-independent optimizations and then cross-compile the code into other languages, such as GLSL for OpenGL/Vulkan or Metal Shading Language (MSL) for macOS and iOS.

Practical Usage Tips and Best Practices
Avoid Manual Parsing for Runtime Logic
The HLSLParser is designed for the shader compiler backend. Do not attempt to use it for runtime gameplay logic or UI. To “eliminate” performance bottlenecks, ensure any shader analysis or preprocessing happens in the Editor or during the “Cook” process.
Understand the Lexer and Parser Relationship
The module is built using Flex (lexer) and Bison (parser). If you are extending the engine to support custom HLSL syntax, you must modify the .ll and .yy files and regenerate the C++ code. This “eliminates” syntax errors when the compiler encounters your custom keywords.
Leverage for Shader Validation Tools
If you are building custom pipeline tools to enforce coding standards in shaders, you can use the HLSLParser to “eliminate” invalid patterns (like global variable abuse) by inspecting the AST before the shader even reaches the platform-specific compiler.
Monitor Cross-Compilation Errors
Errors originating from this module often appear as “Cross-compiler” errors in the output log. If a shader works on DX11 but fails on Vulkan/Mobile, it is often because the HLSLParser encountered a syntax it couldn’t map to the AST. Simplify your HLSL code to “eliminate” these mapping failures.
Be Mindful of Non-Standard Syntax
Unreal’s HLSLParser handles specific UE-style macros and includes. When writing shaders in external IDEs, “eliminate” the use of features not supported by Unreal’s specific parser version (like certain newer HLSL 2021 features) to ensure the cross-compiler can correctly build the AST.
Use for Reflection Data
The engine uses the results of this parsing to generate reflection information (mapping uniform names to registers). This “eliminates” the need for the CPU to guess where data should be bound, ensuring that SetShaderParameter calls correctly find their targets on the GPU.
Optimize AST Traversal
If you are writing an engine-level optimization pass, “eliminate” deep recursive traversals of the AST where possible. Use the visitor pattern provided by the module to efficiently analyze nodes without causing stack overflows on complex shaders.
Sync with ShaderDevelopmentMode
Enable r.ShaderDevelopmentMode=1 in ConsoleVariables.ini. This “eliminates” the frustration of silent failures; when the HLSLParser or Cross-Compiler fails, you will receive a prompt to retry or view the preprocessed source that caused the error.