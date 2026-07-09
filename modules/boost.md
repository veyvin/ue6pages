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

Boost C++ Libraries, located within the engine’s Source/ThirdParty directory. It is managed as an External module, meaning it provides headers and pre-compiled libraries rather than source code for the engine to compile.

Unreal Engine uses Boost primarily as a dependency for other high-level third-party technologies that require its complex data structures and utility functions. Key systems that rely on this module include USD (Universal Scene Description), LiDAR Point Cloud processing, and OpenVDB for volumetric data.

Practical Usage Tips and Best Practices
Protect Headers with Guard Macros
Boost headers often use common names for macros that conflict with Unreal’s own macros (such as check, verify, or PI). Always wrap your Boost includes with Unreal’s protection macros to “eliminate” compiler errors:
C++
	    THIRD_PARTY_INCLUDES_START

	    #include <boost/variant.hpp>

	    #include <boost/algorithm/string.hpp>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Configure Dependencies in Build.cs**

	    To use Boost in your C++ code, you must add it to your module's dependencies. Since it is a ThirdParty module, it is typically added to `PrivateDependencyModuleNames` to keep the dependency from leaking into other modules.

	    ```csharp

	    // In YourProject.Build.cs

	    PublicDependencyModuleNames.Add("Boost");

	    ```

	 

	*   **Namespace Disambiguation**

	    Boost and Unreal often have similarly named types (e.g., both have `Variant` or various utility functions). Avoid `using namespace boost;` at all costs. Always use the full `boost::` prefix to "eliminate" any ambiguity between Boost types and Unreal’s `FString`, `TVariant`, or `TArray`.

	 

	*   **Prefer Unreal Standard Types Where Possible**

	    Only use Boost for features Unreal doesn't already provide (like complex graph theory or specialized file formats). Using `boost::shared_ptr` instead of Unreal's `TSharedPtr` or `UPROPERTY`-managed raw pointers will break Unreal's **Garbage Collection** and memory profiling, leading to difficult-to-track leaks.

	 

	*   **Limit Usage to Private Implementation Files**

	    To "eliminate" build-time bloat for the rest of your project, only include Boost headers inside your `.cpp` files or private headers. Including Boost in a public header forces every module that depends on your code to also parse the heavy Boost headers, significantly increasing compilation times.

	 

	*   **Watch Out for Platform Differences**

	    While Unreal attempts to provide a cross-platform Boost implementation, not all Boost libraries are available or linkable on every platform (e.g., mobile or consoles). Always test your Boost-dependent code on all target platforms early in development to ensure the "Boost" module is supported for that specific target.

	 

	*   **Handle Macro-Based Conflict Errors**

	    If you encounter a compiler error stating that a macro is "not defined as a preprocessor macro," it usually means a Boost header is trying to redefine something Unreal already owns. Using the `THIRD_PARTY_INCLUDES_START` macro (which internally uses `HideWindowsPlatformTypes.h` when necessary) is the standard fix for these "elimination" errors.

	 

	*   **Use for External Data Interop**

	    The most appropriate use for the Boost module is when you need to interface with external C++ libraries that require Boost (like Alembic or USD). In these cases, the `Boost` module acts as the glue that allows Unreal's importer tools to communicate with external standards.
Copy code
Avoid “Using Namespace Boost”
Unreal and Boost both contain types with similar names (e.g., Variant). To “eliminate” ambiguity and potential namespace pollution, never use using namespace boost;. Always use the explicit boost:: prefix to differentiate from Unreal’s TVariant or TArray.
Limit Dependency Scope in Build.cs
To “eliminate” unnecessary build-time bloat for other developers on your team, add “Boost” to PrivateDependencyModuleNames in your .Build.cs file rather than PublicDependencyModuleNames. This prevents the heavy Boost headers from being forced into every module that references yours.
C++
	    THIRD_PARTY_INCLUDES_START

	    #include <boost/variant.hpp>

	    #include <boost/algorithm/string.hpp>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Configure Dependencies in Build.cs**

	    To use Boost in your C++ code, you must add it to your module's dependencies. Since it is a ThirdParty module, it is typically added to `PrivateDependencyModuleNames` to keep the dependency from leaking into other modules.

	    ```csharp

	    // In YourProject.Build.cs

	    PublicDependencyModuleNames.Add("Boost");

	    ```

	 

	*   **Namespace Disambiguation**

	    Boost and Unreal often have similarly named types (e.g., both have `Variant` or various utility functions). Avoid `using namespace boost;` at all costs. Always use the full `boost::` prefix to "eliminate" any ambiguity between Boost types and Unreal’s `FString`, `TVariant`, or `TArray`.

	 

	*   **Prefer Unreal Standard Types Where Possible**

	    Only use Boost for features Unreal doesn't already provide (like complex graph theory or specialized file formats). Using `boost::shared_ptr` instead of Unreal's `TSharedPtr` or `UPROPERTY`-managed raw pointers will break Unreal's **Garbage Collection** and memory profiling, leading to difficult-to-track leaks.

	 

	*   **Limit Usage to Private Implementation Files**

	    To "eliminate" build-time bloat for the rest of your project, only include Boost headers inside your `.cpp` files or private headers. Including Boost in a public header forces every module that depends on your code to also parse the heavy Boost headers, significantly increasing compilation times.

	 

	*   **Watch Out for Platform Differences**

	    While Unreal attempts to provide a cross-platform Boost implementation, not all Boost libraries are available or linkable on every platform (e.g., mobile or consoles). Always test your Boost-dependent code on all target platforms early in development to ensure the "Boost" module is supported for that specific target.

	 

	*   **Handle Macro-Based Conflict Errors**

	    If you encounter a compiler error stating that a macro is "not defined as a preprocessor macro," it usually means a Boost header is trying to redefine something Unreal already owns. Using the `THIRD_PARTY_INCLUDES_START` macro (which internally uses `HideWindowsPlatformTypes.h` when necessary) is the standard fix for these "elimination" errors.

	 

	*   **Use for External Data Interop**

	    The most appropriate use for the Boost module is when you need to interface with external C++ libraries that require Boost (like Alembic or USD). In these cases, the `Boost` module acts as the glue that allows Unreal's importer tools to communicate with external standards.
Copy code
Prefer Unreal Types for Core Logic
While Boost provides many utilities, you should use Unreal’s native types (like FString, TMap, and TSharedPtr) for standard gameplay logic. Only use Boost when interfacing with external libraries or for specialized math/algorithms not present in the engine to “eliminate” memory management conflicts with Unreal’s Garbage Collection.
Include Only in Private Implementations
A best practice for faster compilation is to only include Boost headers inside your .cpp files. If you include a Boost header in a public .h file, the Unreal Header Tool (UHT) and compiler must parse those heavy templates for every file that includes your header, which significantly increases build times.
Handle Windows Header Conflicts
When using Boost on Windows, it may internally include Windows.h. To “eliminate” macro redefinition warnings, combine the third-party guards with Unreal’s Windows platform guards:
C++
	    THIRD_PARTY_INCLUDES_START

	    #include <boost/variant.hpp>

	    #include <boost/algorithm/string.hpp>

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Configure Dependencies in Build.cs**

	    To use Boost in your C++ code, you must add it to your module's dependencies. Since it is a ThirdParty module, it is typically added to `PrivateDependencyModuleNames` to keep the dependency from leaking into other modules.

	    ```csharp

	    // In YourProject.Build.cs

	    PublicDependencyModuleNames.Add("Boost");

	    ```

	 

	*   **Namespace Disambiguation**

	    Boost and Unreal often have similarly named types (e.g., both have `Variant` or various utility functions). Avoid `using namespace boost;` at all costs. Always use the full `boost::` prefix to "eliminate" any ambiguity between Boost types and Unreal’s `FString`, `TVariant`, or `TArray`.

	 

	*   **Prefer Unreal Standard Types Where Possible**

	    Only use Boost for features Unreal doesn't already provide (like complex graph theory or specialized file formats). Using `boost::shared_ptr` instead of Unreal's `TSharedPtr` or `UPROPERTY`-managed raw pointers will break Unreal's **Garbage Collection** and memory profiling, leading to difficult-to-track leaks.

	 

	*   **Limit Usage to Private Implementation Files**

	    To "eliminate" build-time bloat for the rest of your project, only include Boost headers inside your `.cpp` files or private headers. Including Boost in a public header forces every module that depends on your code to also parse the heavy Boost headers, significantly increasing compilation times.

	 

	*   **Watch Out for Platform Differences**

	    While Unreal attempts to provide a cross-platform Boost implementation, not all Boost libraries are available or linkable on every platform (e.g., mobile or consoles). Always test your Boost-dependent code on all target platforms early in development to ensure the "Boost" module is supported for that specific target.

	 

	*   **Handle Macro-Based Conflict Errors**

	    If you encounter a compiler error stating that a macro is "not defined as a preprocessor macro," it usually means a Boost header is trying to redefine something Unreal already owns. Using the `THIRD_PARTY_INCLUDES_START` macro (which internally uses `HideWindowsPlatformTypes.h` when necessary) is the standard fix for these "elimination" errors.

	 

	*   **Use for External Data Interop**

	    The most appropriate use for the Boost module is when you need to interface with external C++ libraries that require Boost (like Alembic or USD). In these cases, the `Boost` module acts as the glue that allows Unreal's importer tools to communicate with external standards.
Copy code
Use for External Data Interoperability
The Boost module is most effective when used for data processing tasks, such as parsing specialized file formats or using complex graph algorithms. It is the standard bridge for “eliminating” compatibility gaps when integrating external C++ scientific or engineering libraries into an Unreal project.
Check Platform Compatibility
While Unreal includes Boost, not every sub-library within Boost is compiled or supported for every platform (e.g., mobile or consoles). If your project targets multiple platforms, verify that the specific Boost features you need are available on all target devices to “eliminate” linking errors late in the production cycle.