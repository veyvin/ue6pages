---
layout: default
title: Core
---

<!-- ai-generation-failed -->

<h1>Core</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Core/Core.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AtomicQueue, AutoRTFM, BuildSettings, ConcurrencyVisualizer, Detours, GoogleGameSDK, GuidelinesSupportLibrary, SuperLuminal, TraceLog, VKQuality, VSPerfExternalProfiler, WinPixEventRuntime, heapprofd, libGPUCounters, libpas, mimalloc, mimalloc212</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Providing the Unreal-specific collection types (TArray, TMap, TSet) which are optimized for the engine’s memory patterns.
Memory Management: Handling low-level memory allocation, smart pointers (TSharedPtr, TUniquePtr), and the foundational logic for Garbage Collection.
Platform Abstraction: Providing a unified API for interacting with the OS (File I/O, Threading, Time) across Windows, Linux, Consoles, and Mobile.
Practical Usage Tips and Best Practices
1. Choose the Right String Type

Understanding the three string types is critical for performance:

FString: Mutable, expensive; use for manipulation and data processing.
FName: Immutable, hashed; use for keys, tags, and lookups where fast comparison is needed.
FText: Use for all user-facing strings; it handles localization and culture-sensitive formatting.
2. Prefer TArray over std::vector

Always use TArray for collections. It is fully integrated with Unreal’s reflection system (when marked with UPROPERTY), allowing for automatic memory management, serialization, and visibility in the Editor. It also uses the engine’s FMemory allocators for better performance in the Unreal ecosystem.

3. Use UPROPERTY() for Object Safety

Any pointer to a UObject-derived class must be marked with the UPROPERTY() macro. This registers the pointer with the Garbage Collector. Failing to do so can result in the collector reclaiming the memory while you are still using it, leading to the elimination of application stability.

4. Master Smart Pointers for Non-UObjects

For classes that do not derive from UObject, use Unreal’s custom smart pointers:

TSharedPtr: Reference-counted thread-safe pointer.
TUniquePtr: Sole ownership; automatically deletes the object when it goes out of scope.
TWeakPtr: Accesses a shared object without preventing its destruction.
5. Leverage Math Utilities

Avoid writing custom math logic for common tasks. The FMath library in Core contains highly optimized functions for interpolation (FMath::Lerp, FMath::InterpTo), clamping, and geometry math. These are often hardware-accelerated and handle edge cases (like divide-by-zero) more safely than raw C++ math.

6. Utilize Logging and Assertions

Use the UE_LOG macro for debugging instead of printf or std::cout. Additionally, use assertions like check(), ensure(), and verify() to catch logical errors during development. ensure() is particularly useful as it reports an error to the log and allows the program to continue without a hard crash.

7. Minimize Heavy Operations in Tick

Because the Core module provides the threading and timing logic, remember that Tick functions run every frame. Use Core’s FTimerManager to execute logic at intervals (e.g., every 0.5 seconds) rather than every frame to improve performance and reduce CPU overhead.

8. Follow the Public/Private Folder Standard

When organizing your own modules based on the Core structure, place headers intended for other modules in the Public folder and internal logic in Private. This reduces physical dependencies and speeds up compile times by ensuring only necessary information is exposed to the rest of the project.