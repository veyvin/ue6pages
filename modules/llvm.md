---
layout: default
title: llvm
---

<!-- ai-generation-failed -->

<h1>llvm</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/llvm/llvm.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

evel Virtual Machine) compiler infrastructure. Rather than relying solely on system-level compilers, Unreal Engine includes this module as a ThirdParty dependency to ensure a consistent, cross-platform compilation environment. It is the backbone for Clang, the compiler used for targeting Linux and Android, and is increasingly utilized for internal engine technologies like the Verse language compiler and advanced shader translation pipelines.

Practical Usage Tips & Best Practices
1. Use for Cross-Platform Toolchain Consistency

When targeting Linux from a Windows host, the engine uses the bundled LLVM/Clang toolchain to ensure the binary produced is compatible with the target environment.

Best Practice: Always use the version of the “Multi-arch” toolchain recommended for your specific Unreal Engine version. This ensures the elimination of “GLIBC version mismatch” errors that occur when using a system compiler that is newer or older than what the engine’s precompiled binaries expect.
2. Leverage Address Sanitizer (ASan) for Memory Debugging

LLVM provides powerful sanitizers that can detect memory corruption, buffer overflows, and use-after-free bugs.

Tip: You can rebuild your project with ASan enabled by passing the -EnableASAN flag to the Unreal Build Tool (UBT). This allows for the elimination of hard-to-trace crashes by providing a detailed call stack the moment a memory violation occurs.
3. Optimize Linux Server Performance

Since LLVM/Clang is the primary compiler for Linux, its optimization flags directly impact dedicated server performance.

Best Practice: When packaging for high-performance ARM64 or x86_64 servers, ensure your TargetRules are set to BuildSettingsVersion.Latest. This allows the LLVM backend to utilize modern CPU instructions (like AVX or NEON), resulting in the elimination of CPU bottlenecks in high-tick-rate multiplayer environments.
4. Interface with the Verse Compiler (UEFN)

In Unreal Editor for Fortnite (UEFN) and modern UE5 versions, LLVM serves as the backend for the Verse VM.

Tip: While you rarely interact with the LLVM module directly when writing Verse, understanding that it handles the low-level machine code generation helps in debugging performance. Efficiently structured code allows the LLVM optimizer to perform better dead-code elimination, resulting in faster script execution.
5. Debugging with LLVM-Specific Tools

The module includes utilities like llvm-symbolizer which are used by the engine to turn raw hex addresses into human-readable function names in logs.

Best Practice: If your Linux logs are showing “UnknownFunction” instead of names, verify that the llvm-symbolizer binary is present in the Engine/Extras/ThirdPartyNotUE/SDKs folder. Having the symbolizer active ensures the elimination of guesswork during post-mortem crash analysis.
6. Coordinate Build.cs Dependencies for Third-Party Code

If you are integrating a third-party C++ library that requires LLVM headers or libraries, you must reference it correctly in your build script.

Tip: Use AddEngineThirdPartyPrivateStaticDependencies(Target, "LLVM"); in your .Build.cs. This ensures that the engine’s specific version of LLVM is linked, facilitating the elimination of symbol conflicts that arise from linking against a different system-installed version of LLVM.
7. Monitor Shader Compilation via Clang

For platforms using the Vulkan RHI, LLVM is often involved in the translation of HLSL into SPIR-V or intermediate formats.

Best Practice: If you experience unusually long shader compile times on Linux, check the ShaderCompileWorker logs. Issues here can sometimes be resolved by clearing the DerivedDataCache (DDC), which leads to the elimination of stale, partially-compiled IR (Intermediate Representation) files.
8. Proactive “Elimination” of RTTI Mismatches

LLVM/Clang handles Run-Time Type Information (RTTI) differently than MSVC.

Tip: If you are mixing C++ modules, ensure they all agree on the bForceEnableRTTI setting in their respective Build.cs files. On Linux, mixing RTTI-enabled and disabled modules will fail to link; maintaining consistency ensures the elimination of these cryptic linker errors during the final build phase.