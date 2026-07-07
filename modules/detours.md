---
layout: default
title: Detours
---

<!-- ai-generation-failed -->

<h1>Detours</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Detours/Detours.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

inally developed by Microsoft Research) used for binary function hooking. It allows developers to intercept and reroute function calls at runtime by modifying the prologue of target functions in memory.

In the context of Unreal Engine, this is a low-level systems module primarily used by the Editor, Live Coding, and Crash Reporting systems to patch code or instrument functions without requiring a full recompile or access to the original source of every linked library.

1. Primarily for Live Coding and Hot Reload

The most common use of the Detours module in Unreal is powering the Live Coding system.

Best Practice: When you compile code while the editor is running, the engine uses Detours to “patch” the old function addresses to point to the new, recompiled memory locations. To ensure this works reliably, avoid making massive structural changes (like adding new virtual functions) while Live Coding is active, as these can occasionally exceed the patching capabilities of the Detours system.
2. Use for Low-Level Engine Instrumentation

If you are building a custom profiling tool or a deep-level debugger, you can use the Detours module to intercept engine calls.

Tip: You can hook into third-party DLLs that Unreal uses (like graphics drivers or physics libraries) to log parameters or measure execution time. This is useful for identifying bottlenecks in closed-source components that are otherwise “black boxes.”
3. Handle Thread Safety During Hooking

Modifying function prologues is inherently dangerous in a multi-threaded environment.

Best Practice: Always use the DetourTransactionBegin() and DetourUpdateThread() APIs provided by the module. This ensures that other threads are suspended or safely managed while the function is being redirected, which helps to eliminate race conditions that could lead to an immediate crash.
4. Implement Custom Crash Handling Logic

The Detours module is often used to intercept OS-level signals or specific C++ exception handlers.

Tip: If you need to perform custom cleanup or log specific data when a third-party library triggers a fatal error, you can hook the library’s error-handling functions. This allows your game to shut down gracefully or save a “recovery file” before the process is eliminated by the OS.
5. Be Mindful of “Inline” Functions

The Detours module works by redirecting memory addresses of compiled functions.

Constraint: If a function has been inlined by the compiler (common with small, high-performance functions or those marked FORCEINLINE), there is no central address to hook. In these cases, Detours will not work. To ensure a function is “hookable” for debugging purposes, you may need to temporarily disable inlining using the FORCENOINLINE macro.
6. Avoid Use in Shipping Game Logic

While Detours is powerful for development tools and editor features, it should generally be avoided for core gameplay mechanics.

Best Practice: Using binary hooking in a shipping build can be flagged as suspicious behavior by Anti-Cheat software (like Easy Anti-Cheat or BattlEye), as it is the same technique used by many “trainers” and malicious hacks. Keep your Detours-related code wrapped in #if WITH_EDITOR or #if !UE_BUILD_SHIPPING blocks.
7. Correct Module Linking in C++

To utilize the Detours API in your custom engine tools or plugins, you must explicitly add it to your module dependencies.

Best Practice: Add the following to your project’s .Build.cs file:
C#
	if (Target.bBuildEditor || Target.Configuration != UnrealTargetConfiguration.Shipping)

	{

	    PublicDependencyModuleNames.Add("Detours");

	}
Copy code
This ensures the library is only linked when you actually need it for development or debugging.
8. Use for Testing “What-If” Scenarios

Detours is an excellent tool for “Mocking” system-level responses during automated testing.

Tip: If you want to test how your game handles a network failure without actually unplugging the cable, you can use Detours to hook the socket “send” or “receive” functions and force them to return an error code. This allows you to test edge-case error handling in a controlled, repeatable environment.