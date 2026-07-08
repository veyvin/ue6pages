---
layout: default
title: Boost
---

<!-- ai-generation-failed -->

<h1>Boost</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/Boost/Boost.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at provides a wrapper for the Boost C++ Libraries. Boost is a collection of high-quality, peer-reviewed C++ source libraries that extend the functionality of the C++ Standard Library.

In Unreal Engine, this module is located in Engine/Source/ThirdParty/Boost. It is primarily used as a dependency for other third-party integrations—most notably USD (Universal Scene Description) and Datasmith—which require Boost’s advanced algorithms, data structures, and cross-platform utilities to handle complex data interchange and scene processing.

Practical Usage Tips and Best Practices
Restrict to Editor and Tooling
Boost is a heavy dependency. You should “eliminate” its use in runtime gameplay code. It is best suited for Editor-only plugins, importers, or commandlets where memory footprint and binary size are less critical than in a shipping game client.
Correct Build.cs Dependency
Since Boost is a third-party library, include it using the engine’s helper function in your .Build.cs file. This ensures the correct include paths and precompiled binaries are mapped for your target platform:
C#
	    if (Target.Type == TargetType.Editor)

	    {

	        AddEngineThirdPartyPrivateStaticDependencies(Target, "Boost");

	    }

	    ```

	 

	*   **Avoid Global Namespaces**

	    Never use `using namespace boost;` in your header or source files. Boost contains thousands of symbols that can conflict with Unreal’s core types. Always use the full `boost::` prefix to "eliminate" name collisions with Unreal’s `TArray`, `TMap`, or `FString`.

	 

	*   **Enable Exceptions with Caution**

	    Unreal Engine disables C++ exceptions by default for performance and binary size (`bEnableExceptions = false`). Many Boost libraries rely on exceptions. If you must use a Boost feature that throws, you must enable exceptions in your `.Build.cs`, which can lead to larger binaries and "elimination" of certain engine-wide optimizations.

	 

	*   **Stick to Header-Only Libraries**

	    The version of Boost included in Unreal is primarily set up to support header-only libraries (like `boost::optional` or `boost::algorithm`). If you need a Boost library that requires a compiled binary (like `boost::asio` or `boost::filesystem`), verify that the `.lib` or `.a` files for your target platform exist in the `ThirdParty/Boost` folder first.

	 

	*   **Never Mix with UObjects**

	    Do not use `boost::shared_ptr` or `boost::unique_ptr` to manage `UObject`-derived classes. Unreal’s Garbage Collector cannot track Boost’s smart pointers, which will lead to the "elimination" of your object by the GC even while the Boost pointer still thinks it is valid, causing a crash. Use `TObjectPtr` or `TWeakObjectPtr` instead.

	 

	*   **Prefer Unreal Threading Primitives**

	    While `boost::thread` or `boost::asio` are powerful, they do not integrate with Unreal’s **Task Graph** or **FRunnable** system. Using Boost’s threading logic can lead to deadlocks or "elimination" of thread safety guarantees provided by the engine. Always use `FPlatformProcess` or `UE::Tasks` for multi-threading.

	 

	*   **Memory Tracking Compatibility**

	    Boost uses standard `malloc`/`free` or its own internal pool allocators. These are invisible to Unreal’s **MallocLeakDetection** and memory profilers. If you use Boost heavily, your memory usage will appear as "untagged" or "system" memory, making it harder to "eliminate" memory leaks using standard Unreal profiling tools.
Copy code
Always Use Explicit Namespaces
Never use using namespace boost;. Boost contains thousands of symbols that overlap with Unreal’s core types (e.g., boost::array vs. TArray). To “eliminate” compiler ambiguity and naming collisions, always use the full boost:: prefix.
Prefer Unreal Native Types
For standard logic, “eliminate” the use of boost::vector, boost::shared_ptr, or boost::function. Always prefer Unreal’s native TArray, TSharedPtr, and TFunction. These are optimized for Unreal’s memory management and are fully compatible with the Garbage Collector.
Handle Exception Constraints
Unreal Engine typically compiles with exceptions disabled (bEnableExceptions = false). Many Boost libraries rely on exceptions. If you use a Boost feature that requires them, you must enable exceptions in your module, which can “eliminate” certain engine optimizations and increase binary size.
Avoid Mixing Smart Pointers
Do not store a UObject inside a boost::shared_ptr. Unreal’s Garbage Collector cannot “see” into Boost containers, meaning the GC will “eliminate” the UObject from memory even while the Boost pointer is still active, leading to a fatal crash.
Header-Only vs. Compiled Libraries
Unreal’s Boost module is best used for header-only libraries (like boost::algorithm or boost::numeric). If your logic requires a compiled Boost component (like boost::asio), verify that the precompiled .lib files for your specific target platform exist in the engine’s ThirdParty directory.
Use for External API Compatibility
The primary reason to use this module is to “eliminate” compatibility issues when integrating external SDKs (like Pixar’s USD) that already have Boost as a hard requirement. If you are not interfacing with such a library, you should generally avoid adding Boost to your project.