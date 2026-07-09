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

sential low-level building blocks that the rest of the engine (and your game code) relies upon. It is independent of the Gameplay Framework and the Editor, focusing on hardware abstraction, memory management, math libraries, and fundamental data structures.

It is used for everything from basic string manipulation and container management (TArray, TMap) to thread management, time handling, and the math primitives (FVector, FQuat, FRotator) that drive 3D simulation.

Practical Usage Tips and Best Practices
1. Always Use the TEXT() Macro

In Unreal Engine, strings are represented by TCHAR. To ensure your string literals are cross-platform compatible and correctly encoded (especially for non-ASCII characters), always wrap them in the TEXT("") macro. This prevents the “elimination” of character data when compiling for different operating systems.

2. Choose the Right String Type

The Core module provides three main string types. Choosing the wrong one can “eliminate” your performance:

FString: Use for string manipulation (concatenation, searching). It is the most expensive.
FName: Use for identifiers, keys, and tags. It is a hashed, case-insensitive index into a global table, making comparisons extremely fast.
FText: Use for all user-facing text. It handles localization, pluralization, and culture-invariant formatting.
3. Optimize Containers with Reserve()

When using TArray or TMap, if you know how many elements you are about to add, always call MyArray.Reserve(ExpectedCount). This prevents the container from reallocating memory multiple times during the loop, which can significantly “eliminate” CPU overhead in performance-critical code.

4. Leverage FMath Over Standard C Libraries

Unreal provides a comprehensive math library in the Core module via FMath. Always prefer FMath::Lerp, FMath::Clamp, and FMath::Sin over the standard std:: or math.h versions. FMath is specifically optimized for game development and handles edge cases (like divide-by-zero) more gracefully in a game context.

5. Use UE_LOG for Debugging

The Core module defines the logging system. Use UE_LOG(LogTemp, Warning, TEXT("Message")) to output data to the Output Log. For more advanced needs, define your own log categories in your header/source files to “eliminate” clutter and allow for easier filtering during intense debugging sessions.

6. Prefer TWeakObjectPtr for Non-Owned Objects

To avoid memory leaks or “dangling pointers” that cause crashes, use TWeakObjectPtr<T> for references to UObjects that your class does not “own.” This allows the Garbage Collector to “eliminate” the object if needed, while your pointer will safely null itself out rather than pointing to invalid memory.

7. Use FScopedSlowTask for Long Editor Operations

If you are writing a tool that will take several seconds to process (like a bulk asset rename), use FScopedSlowTask. This provides a progress bar in the Editor UI, preventing the application from appearing “frozen” and allowing the user to cancel the operation, which “eliminates” frustration during long tasks.

8. Utilize Static and Const for Optimization

In the Core module, memory efficiency is key. Use static const FName MyKey = TEXT("MyKeyName"); inside functions for keys you use frequently. This ensures the string is only hashed once during the entire lifecycle of the application, rather than re-hashing it every time the function is called.

Core Module Requirements

Every Unreal C++ project requires the Core module. It is included by default in the Build.cs of every module:

C#
PublicDependencyModuleNames.AddRange(new string[] { "Core" });
Copy code
Key Headers to Include
#include "CoreMinimal.h": Includes the most common headers (Strings, Containers, Math) without bloating compile times.
#include "Math/UnrealMathUtility.h": For advanced FMath functions.
#include "Logging/LogMacros.h": For custom logging categories.