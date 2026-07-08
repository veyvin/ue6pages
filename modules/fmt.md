---
layout: default
title: fmt
---

<!-- ai-generation-failed -->

<h1>fmt</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/fmt/fmt.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

open-source {fmt} library. It provides a modern, type-safe, and high-performance alternative to traditional printf-style formatting (like FString::Printf and the legacy UE_LOG).

Introduced as the backbone of Structured Logging (via the UE_LOGFMT macro), this module allows developers to format strings using a Python-like or C++20 std::format syntax. It is primarily used to create more readable, maintainable, and crash-resistant logs by using named or positional parameters, facilitating the elimination of errors caused by mismatched format specifiers.

Practical Usage Tips and Best Practices
1. Transition to UE_LOGFMT for Readability

Replace legacy UE_LOG calls with UE_LOGFMT when dealing with multiple variables. Using named parameters makes the intent of the log clear and assists in the elimination of confusion when reading long output logs.

C++
	// Legacy UE_LOG

	UE_LOG(LogTemp, Log, TEXT("Player %s has %d health"), *PlayerName, Health);

	 

	// Modern UE_LOGFMT

	UE_LOGFMT(LogTemp, Log, "Player {Name} has {Health} health", ("Name", PlayerName), ("Health", Health));

	```

	This practice facilitates the **elimination** of "mystery variables" in long log strings.

	 

	#### 2. Avoid Mixing Named and Positional Parameters

	While the system is flexible, you cannot mix named and positional arguments in a single `UE_LOGFMT` call. Pick one style for your project or module to ensure the **elimination** of compilation errors and to keep the codebase consistent.

	 

	#### 3. Exploit Compile-Time Type Safety

	The `fmt` module performs type checking at compile time. Unlike `printf`, which will crash or output garbage if you pass the wrong type, the `fmt` module will often fail to compile if a type is unsupported or incorrectly matched. This assists in the **elimination** of "silent" formatting bugs.

	 

	#### 4. Formatting Custom Types

	You can extend the `fmt` system to support your own `USTRUCT` or `UCLASS` by providing a `SerializeForLog` function or an `operator<<`. This allows you to pass a custom object directly to the log macro, leading to the **elimination** of repetitive `.ToString()` calls throughout your code.

	 

	#### 5. Leverage Performance Gains

	The `fmt` library is significantly faster than `sprintf` and `FString::Printf` because it minimizes memory allocations and performs more work during compilation. Using it for high-frequency logs (though still used sparingly) aids in the **elimination** of CPU spikes during heavy debugging sessions.

	 

	#### 6. Use for Structured Data (Insights)

	Data logged via `UE_LOGFMT` is preserved as "Structured Data" in **Unreal Insights**. This means you can filter traces by specific parameter names (like `Name` or `Health`) rather than searching through raw text strings, facilitating the **elimination** of tedious log parsing.

	 

	#### 7. Handle FText with Care

	Since `UE_LOGFMT` is designed for developer logging (which should usually be English-only), it expects `FString`, `FName`, or primitive types. If you need to log `FText`, convert it using `.ToString()` first. This practice ensures the **elimination** of "culture-invariant" confusion in your dev logs.

	 

	#### 8. Include the Correct Header

	To use the new structured logging system, you must include `Logging/StructuredLog.h`. In your `Build.cs`, ensure your module depends on `Core` (where the base implementation lives). Correct header management leads to the **elimination** of "Identifier not found" errors when implementing `UE_LOGFMT`.
Copy code
2. Leverage Compile-Time Type Checking

Unlike printf, which can crash if you pass a string to a %d specifier, the fmt module validates types during compilation. This behavior is essential for the elimination of “silent” runtime crashes and memory corruption issues in your debugging code.

3. Use for High-Performance String Construction

The fmt library is significantly faster than sprintf and FString::Printf because it minimizes memory allocations and avoids the overhead of parsing format strings at runtime. Using it for frequent log entries leads to the elimination of CPU spikes during heavy gameplay testing.

4. Avoid Mixing Parameter Styles

The fmt system allows for either Positional ({0}, {1}) or Named ({Name}) parameters, but you cannot use both in a single call. Sticking to one style within a module is a best practice for the elimination of compilation errors and maintaining a consistent codebase.

5. Handle Unreal Types Correctly

The module is “Unreal-aware” and can handle types like FString, FName, and FText without needing the * dereference operator (which is required for %s in legacy UE_LOG). This simplifies your code and aids in the elimination of boilerplate dereferencing throughout your C++ files.

6. Utilize Structured Data for Unreal Insights

Data passed through the fmt module is stored as structured metadata. When viewing logs in Unreal Insights, you can filter and search by the parameter names themselves rather than raw text. This facilitates the elimination of tedious log parsing when searching for specific gameplay events.

7. Provide SerializeForLog for Custom Structs

You can extend the fmt system by defining a SerializeForLog function for your custom USTRUCT. This allows you to pass a custom object directly into a log macro, leading to the elimination of repetitive manual formatting logic inside your functions.

8. Ensure Proper Header Inclusion

To use the structured logging features provided by the fmt module, you must include Logging/StructuredLog.h. Correct header management is the primary step for the elimination of “Identifier not found” errors when implementing modern Unreal logging.