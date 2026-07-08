---
layout: default
title: GuidelinesSupportLibrary
---

<!-- ai-generation-failed -->

<h1>GuidelinesSupportLibrary</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/GuidelinesSupportLibrary/GuidelinesSupportLibrary.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ore Guidelines Support Library. It provides a set of small, header-only helper types and functions designed to make C++ code safer, more expressive, and less prone to common memory or logic errors.

What it is and What it’s used for

Located in Engine/Source/ThirdParty/GSL, this module implements concepts originally proposed by Bjarne Stroustrup and Herb Sutter. While Unreal Engine has its own robust types (like TArray and TSharedPtr), the GSL module is used primarily at the low-level engine layer and in third-party integrations to enforce “correct-by-construction” code.

Primary uses include:

Pointer Safety: Using gsl::not_null<T*> to ensure a pointer is never null without constant manual checks.
Bounds Checking: Providing gsl::span<T>, which represents a contiguous sequence of objects (similar to TArrayView) but with strict adherence to Core Guidelines.
Logic Enforcement: Using finally or expect patterns to ensure resource cleanup or state validation.
Type Narrowing: Safe casting and narrowing of numeric types to prevent silent data loss.
Practical Usage Tips and Best Practices
1. Use gsl::not_null for Critical API Contracts

If a function requires a valid object to operate, declare the parameter as gsl::not_null<T*>. This acts as a self-documenting contract that the caller is responsible for providing a valid pointer, leading to the elimination of redundant if (Pointer != nullptr) checks inside the function body.

2. Replace Raw Pointer/Length Pairs with gsl::span

When passing raw C-style arrays or segments of memory to functions, use gsl::span<T>. This encapsulates both the pointer and the size, providing bounds-checked access. While TArrayView is the standard for most UE gameplay code, gsl::span is the best practice when writing low-level, engine-agnostic C++ or third-party wrappers.

3. Implement Cleanup with gsl::finally

For resources that don’t follow standard RAII (like a legacy C-API handle), use gsl::finally. This ensures that a cleanup lambda is executed when the current scope ends, regardless of how it is exited (via return, break, or error), ensuring the elimination of resource leaks.

C++
	auto FileHandle = OpenLegacyFile("data.bin");

	auto Cleanup = gsl::finally([&] { CloseLegacyFile(FileHandle); });

	// Perform operations...
Copy code
4. Prefer gsl::narrow for Safe Conversions

When you must cast a larger integer type (like int64) to a smaller one (int32), use gsl::narrow<T>. Unlike a static cast, this will throw an exception or trigger an assertion if the value cannot fit in the target type, preventing silent overflows that are difficult to debug.

5. Strategic Elimination of Pointer Arithmetic

The C++ Core Guidelines discourage raw pointer arithmetic. Use gsl::span iterators or indexing instead. This shift in practice significantly reduces the chance of “off-by-one” errors and buffer overflows, as the GSL types provide built-in validation for these operations.

6. Combine with Unreal’s Check Macros

While GSL has its own error-handling logic, ensure it integrates with Unreal’s crash reporting by wrapping GSL-intensive code within check() or ensure() macros where appropriate. This ensures that a GSL contract violation is captured by the Unreal Crash Reporter during development and QA.

7. Use gsl::owner<T*> for Legacy Documentation

If you are dealing with legacy code where you must return a raw pointer that the caller is responsible for deleting, mark the return type as gsl::owner<T*>. This doesn’t change the runtime behavior, but it signals to static analysis tools and other developers that a delete or Free call is mandatory.

8. Restrict Usage to C++ Core Logic

The GSL module is not reflected to Blueprints. A best practice is to keep GSL usage restricted to your private C++ implementation files (.cpp) or internal header files. Expose simplified, Blueprint-friendly types (like TArray or UObject*) in your public headers to maintain compatibility with the rest of the engine ecosystem.