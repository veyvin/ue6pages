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

ompiler infrastructure, which enables Unreal Engine to author shaders once in HLSL and then transpile them into other languages like GLSL or Metal Shading Language (MSL) for cross-platform support.

It utilizes a lexer (generated via Flex) and a parser (generated via Bison) to interpret the syntax of HLSL, perform initial optimizations like constant folding, and prepare the code for the engine’s intermediate representation (IR).

Practical Usage Tips and Best Practices
1. Understand the Preprocessing Chain

The hlslparser does not see your raw .usf or .ush files directly. The engine first runs a preprocessing pass to resolve #define and #include directives.

Best Practice: When debugging parsing errors, always inspect the .usf file located in your project’s Saved/ShaderDebugInfo folder. This file represents the “final” source that the parser actually processes, helping you eliminate confusion caused by complex macro expansions.
2. Manage Lexer and Parser Regeneration

If you are modifying the engine source to add new HLSL keywords or syntax support, you must update the .ll (lexer) and .yy (parser) files.

Action: Use the GenerateParsers.bat script located in the module directory to regenerate the C++ code after making changes. Ensure you have Flex and Bison installed on your system path to eliminate “command not found” errors during the build process.
3. Respect Cross-Platform Constraints

Because this module is the gateway for cross-compilation, syntax that is “legal” in pure DirectX HLSL might fail if it cannot be parsed or mapped to other languages.

Tip: Avoid using platform-specific intrinsics that aren’t wrapped in the engine’s standard Common.ush. The parser acts as a validator; sticking to standard Unreal HLSL patterns helps eliminate transpilation failures when moving from Windows to Vulkan or Metal platforms.
4. Leverage Constant Folding

The parser performs “Constant Folding” during the AST generation phase, which simplifies mathematical expressions (e.g., (1.0 + 2.0) becomes 3.0).

Tip: Don’t be afraid to use readable math in your shader code. The hlslparser will evaluate these at compile time, eliminating the runtime GPU cost of simple arithmetic that involves constants.
5. Monitor Shader Compile Worker (SCW)

The hlslparser logic typically runs within the ShaderCompileWorker process rather than the main Editor process.

Action: If you encounter a crash during shader compilation, attach your debugger to the ShaderCompileWorker executable. This allows you to step through the parsing logic to eliminate the source of the crash in the lexer or AST generation.
6. Debug via HLSLCrossCompile Entry Point

The primary entry point for this module’s logic is the HLSLCrossCompile function.

Tip: When writing custom shader tools or engine extensions, look at how HLSLCrossCompile initializes the parser. Following this initialization pattern helps eliminate errors related to incorrect state tracking or global “yy” variables used by the underlying Bison parser.
7. Use Virtual File Paths for Includes

Unreal uses a virtual file system (e.g., /Engine/Private/...) to locate shaders across plugins and engine folders.

Best Practice: Always use the full virtual path in your #include statements. The parser relies on the engine’s preprocessor to resolve these; using relative disk paths will fail, while virtual paths eliminate broken link errors across different development environments.
8. Optimize for Fast Iteration

Extensive changes to the parser can trigger large-scale shader recompilations across the entire engine.

Action: When testing parser changes, use RecompileShaders Changed or Ctrl+Shift+. in the editor. This focuses the compiler on a smaller subset of shaders, eliminating the long wait times associated with a full global shader refresh.