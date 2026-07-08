---
layout: default
title: Interpose
---

<!-- ai-generation-failed -->

<h1>Interpose</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/IOS/Interpose/Interpose.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

in Unreal Engine, primarily utilized on macOS and Linux environments. Its core function is to facilitate “symbol interposition”—a technique where the engine “interposes” or intercepts calls to system dynamic libraries (like libc or memory allocators).

In Unreal Engine, this is most commonly used to redirect standard memory allocation calls (such as malloc and free) to the engine’s own high-performance memory allocators (like Binned2 or Stomp). This ensures that all memory used by the process—even by third-party libraries—is tracked and managed by the engine, facilitating the elimination of “untracked memory” and providing a unified view for memory profiling.

Practical Usage Tips and Best Practices
1. Use for Comprehensive Memory Profiling

When debugging memory issues on macOS or Linux, the Interpose module ensures that allocations made by the OS on behalf of the engine are captured. This practice leads to the elimination of discrepancies between what the “Activity Monitor” reports and what “Unreal Insights” shows, providing a “single source of truth” for memory usage.

2. Debugging with the Malloc Stomp

If you are encountering rare memory corruption or “use-after-free” bugs on Unix-based platforms, the Interpose module allows the engine to force a Malloc Stomp across the entire process. This assists in the elimination of hard-to-track crashes by immediately crashing the engine the moment a memory violation occurs in any library.

3. Verify Module Loading in Logs

The Interpose module usually operates very early in the engine’s boot cycle (pre-main). Check your terminal output or logs for messages regarding “Interpose” or “Dynamic Linker” overrides. Confirming that interposition is active is a best practice for the elimination of false-positive results during low-level performance audits.

4. Understand System Library Interactions

Be aware that interposing system calls can occasionally conflict with specific OS security features (like System Integrity Protection on macOS). If the engine fails to launch on a development machine, temporarily disabling custom allocators can lead to the elimination of launch-time errors caused by the Interpose module being blocked by the kernel.

5. Leverage for Third-Party Library Tracking

If your project uses many external .so or .dylib libraries, the Interpose module ensures their allocations are funneled through the Unreal Global Allocator. This is vital for the elimination of “hidden” memory leaks that originate inside closed-source third-party binaries that you cannot modify.

6. Optimize for Shipping Builds

While interposition is powerful for debugging, it can add a micro-overhead to every system call. Ensure that for your final Shipping configuration, the interposition logic is tuned for performance rather than tracking. This alignment aids in the elimination of CPU overhead in the memory management layer.

7. Use with Unreal Insights (LLM)

Combine the Interpose module with the Low Level Memory (LLM) tracker. By interposing at the system level, the LLM_TAG system becomes much more accurate. This leads to the elimination of the “Untagged” memory category, allowing you to see exactly which system sub-system is consuming resources.

8. Audit for Platform-Specific Behavior

The Interpose module behaves differently on Linux (using LD_PRELOAD concepts) than on macOS (using DYLD_INTERPOSE). If you are writing cross-platform C++ tools, do not assume identical behavior. Testing on both platforms facilitates the elimination of platform-specific memory fragmentation that only appears on one OS.