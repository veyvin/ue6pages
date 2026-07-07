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

infrastructure upon which the entire engine is built. Unlike other modules that focus on specific features (like rendering or physics), Core provides the fundamental building blocks of C++ development in UE, including platform abstraction, memory management, math libraries, container classes, and the engine’s custom string types.

Without the Core module, the engine cannot function; it is a mandatory dependency for every other module, plugin, and project.

Practical Usage Tips & Best Practices
1. Always Use Unreal’s String Types

Avoid standard library strings (std::string). Instead, use the specialized types provided by Core:

FString: For mutable, searchable, and manipulatable strings.
FName: For high-performance, case-insensitive identifiers (stored in a global hash table for fast comparison).
FText: For all user-facing strings; it handles localization and culture-invariant formatting automatically.
2. Prefer TArray Over std::vector

Use TArray for dynamic arrays. It is deeply integrated with the engine’s memory management and reflection system.

Optimization Tip: Use TArray::Reserve() if you know the approximate number of elements you will add. This prevents multiple reallocations and the unnecessary “elimination” of performance during a loop.
3. Standardize Logging with UE_LOG

Use the UE_LOG macro for all diagnostic output. This allows you to categorize your logs and control their visibility via the Output Log or console.

C++
	// Define a category in your header/cpp

	DECLARE_LOG_CATEGORY_EXTERN(LogMyProject, Log, All);

	DEFINE_LOG_CATEGORY(LogMyProject);

	 

	// Usage

	UE_LOG(LogMyProject, Warning, TEXT("Character health is low: %f"), CurrentHealth);
Copy code
4. Leverage Math Utilities (FMath)

The FMath library provides a massive collection of platform-optimized functions for common game development tasks. Use FMath::Lerp for interpolation, FMath::Clamp for range limiting, and FMath::FInterpTo for smooth value transitions over time. These are often faster and more robust than writing the math from scratch.

5. Use Modern Smart Pointers

Core provides TSharedPtr, TSharedRef, and TWeakPtr for non-UObject memory management. For objects that are not part of the Garbage Collection system (standard C++ classes), these smart pointers ensure that memory is cleaned up automatically once the last reference is removed, preventing memory leaks.

6. Use the FPlatform API for Portability

If you need to perform platform-specific tasks (like finding a file path or checking the OS version), never use raw Win32 or Linux APIs. Use the FPlatformProcess, FPlatformFileManager, and FPaths classes. This ensures your code remains cross-platform and will compile for consoles, mobile, and PC without modification.

7. Assertions and Validation

Use check(), verify(), and ensure() macros for debugging.

check(Condition): Crashes the editor/game if the condition is false (use for critical logic).
ensure(Condition): Logs an error and provides a stack trace if false, but allows the game to continue. This is excellent for non-fatal logic errors where you want to avoid the total elimination of a playtest session.
8. Avoid Direct Memory Allocation

Avoid new and delete. Use NewObject<T>() for UObjects, SpawnActor<T>() for Actors, and MakeShared<T>() for standard C++ classes. These methods ensure that Unreal’s memory tracking and garbage collection systems are aware of the object’s existence.