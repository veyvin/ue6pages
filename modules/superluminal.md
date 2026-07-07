---
layout: default
title: SuperLuminal
---

<!-- ai-generation-failed -->

<h1>SuperLuminal</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/SuperLuminal/SuperLuminal.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

bridge that allows Unreal Engine to communicate directly with the Superluminal Performance Profiler, a high-frequency sampling profiler for Windows.

Description and Purpose

While Unreal Insights is the standard for high-level timing and task-based analysis, the Superluminal module provides a lower-level, stack-based view of the engine’s execution. It provides a C++ interface (ISuperluminalProfiler) and macros that wrap the Superluminal API. Its primary purpose is to provide instruction-level profiling; it allows developers to see exactly which C++ functions, loops, or lines of code are consuming CPU cycles on any given thread. By using this module, developers can eliminate the ambiguity of high-level “GameThread” tasks by drilling down into the actual native call stacks.

Practical Usage Tips and Best Practices
Instrument with SUPERLUMINAL_PROFILER_SCOPE
To mark specific blocks of code for the profiler, use the SUPERLUMINAL_PROFILER_SCOPE("Label", Color) macro. This creates a visible, colored block in the Superluminal timeline, helping you eliminate the difficulty of identifying custom logic within the massive engine call stack.
Wrap in Non-Shipping Build Guards
The Superluminal module is designed for development and is eliminated from Shipping builds. When adding the module to your Build.cs or including its headers, always wrap the logic in if (Target.Configuration != UnrealTargetConfiguration.Shipping) or #if !UE_BUILD_SHIPPING to prevent compilation errors.
Profile in “Test” Configuration
For the most accurate results, profile your game in the Test configuration rather than Development. The Test build keeps optimizations enabled while retaining symbols, allowing you to eliminate “observer effect” overhead where the debugger slows down the code you are trying to measure.
Use for “Wait” and “Lock” Analysis
Superluminal is exceptional at identifying thread contention. Use the module to see where the GameThread is stalled by a mutex or waiting on a TaskGraph worker. This helps you eliminate bottlenecks caused by improper multi-threading or resource locking.
Identify Instruction-Level Bottlenecks
Because Superluminal is a sampling profiler, it can show you which specific lines of C++ code (like a heavy math operation or an inefficient TArray search) are the hottest. Use this data to eliminate micro-stutters that high-level profilers might miss.
Check Symbol (.pdb) Settings
For the module to provide meaningful data, Superluminal must be able to find your project’s .pdb files. Ensure your build system is generating and preserving these symbols; otherwise, you will see raw memory addresses instead of function names, which you should eliminate to make the profile useful.
Keep Scopes Out of Tight Loops
Avoid placing manual instrumentation macros inside loops that run thousands of times per frame. The overhead of calling the profiler API repeatedly can skew your data. Instead, scope the entire function to eliminate “profiler noise” in your performance results.
Analyze Context Switches
Enable the “Context Switch” tracking in the Superluminal application alongside the module’s data. This allows you to see when the OS deschedules an Unreal thread, helping you eliminate performance issues caused by other background processes or CPU over-subscription.