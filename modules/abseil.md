---
layout: default
title: abseil
---

<!-- ai-generation-failed -->

<h1>abseil</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/abseil/abseil.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

or build errors.

Practical Usage Tips & Best Practices
1. Add via Build.cs as a Private Dependency

To use Abseil in your C++ project, you must explicitly add it to your module’s dependencies. Since Abseil is a third-party library, include it as a Private dependency to prevent it from leaking into other modules that might not require it.

C#
	// MyProject.Build.cs

	using UnrealBuildTool;

	 

	public class MyProject : ModuleRules

	{

	    public MyProject(ReadOnlyTargetRules Target) : base(Target)

	    {

	        PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

	 

	        // Add Abseil to private dependencies

	        PrivateDependencyModuleNames.AddRange(new string[] { "Core", "Abseil" });

	    }

	}

	```

	 

	#### 2. Wrap Includes with Third-Party Macros

	Abseil is written to standard C++ conventions which may trigger warnings (like shadowing or signed/unsigned mismatches) that Unreal’s build system treats as errors. Always wrap Abseil headers with Unreal's third-party include macros.

	 

	```cpp

	// MyClass.cpp

	#include "CoreMinimal.h"

	 

	// Protect against external warnings

	THIRD_PARTY_INCLUDES_START

	#include "absl/container/flat_hash_map.h"

	#include "absl/status/status.h"

	THIRD_PARTY_INCLUDES_END

	```

	 

	#### 3. Prefer `absl::flat_hash_map` for Performance-Critical Non-UObject Data

	While `TMap` is the standard for Unreal, `absl::flat_hash_map` is often more memory-efficient and faster for very large, flat data sets that **do not contain UObjects**. 

	*   **Warning:** Never store `UObject*` in an Abseil container. The Unreal Garbage Collector (GC) cannot "see" into Abseil containers, and your objects will be deleted mid-execution.

	 

	#### 4. Avoid Namespace "Using" Directives

	Never use `using namespace absl;` in a header file, and avoid it in source files. Abseil contains many types that look like standard library types (e.g., `absl::optional` vs `std::optional`). In the Unreal environment, where you also have `TOptional`, explicit namespaces prevent developer confusion and linker errors.

	 

	#### 5. Handle `absl::Status` for Plugin Interop

	If you are extending the **WebRTC** or **Pixel Streaming** modules, you will frequently encounter `absl::Status`. Do not try to convert these to `FString` immediately. Instead, use them to propagate errors up to your interface layer before converting them for Unreal's logging system.

	 

	```cpp

	absl::Status MyNetworkFunction() {

	    if (Failed) return absl::InternalError("Network pipe broken");

	    return absl::OkStatus();

	}

	 

	// In the Unreal-facing function:

	void UMyObject::DoWork() {

	    auto Status = MyNetworkFunction();

	    if (!Status.ok()) {

	        UE_LOG(LogTemp, Error, TEXT("Error: %hs"), Status.ToString().c_str());

	    }

	}

	```

	 

	#### 6. Mind the RTTI and Exception Settings

	Abseil often expects Run-Time Type Information (RTTI) or Exceptions to be enabled in some of its advanced features. Unreal disables both by default for performance. If you encounter link errors regarding `dynamic_cast` or `throw`, you may need to enable these in your `Build.cs` (e.g., `bEnableExceptions = true;`), though this is generally discouraged for gameplay code.

	 

	#### 7. Use `absl::string_view` for Third-Party Interop Only

	Unreal uses `FStringView` (introduced in UE4.25+) for lightweight string references. While Abseil uses `absl::string_view`, you should prefer `FStringView` for all internal Unreal logic. Only use `absl::string_view` when passing data directly into an Abseil-based API or WebRTC function.

	 

	#### 8. Check Version Compatibility

	Unreal Engine ships with a specific, frozen version of Abseil (located in `Engine/Source/ThirdParty/Abseil`). If you are trying to use a feature from the latest Abseil documentation (like newer `absl::Cord` features), verify that the version bundled with your UE version actually supports it. Upgrading the engine's Abseil manually is highly risky and can break the WebRTC/Pixel Streaming stack.
Copy code
2. Wrap Includes with Third-Party Macros

Abseil is written to standard C++ conventions which may trigger warnings (like shadowing or signed/unsigned mismatches) that Unreal’s build system treats as errors. Always wrap Abseil headers with Unreal’s third-party include macros.

C++
	// MyClass.cpp

	#include "CoreMinimal.h"

	 

	THIRD_PARTY_INCLUDES_START

	#include "absl/container/flat_hash_map.h"

	#include "absl/status/status.h"

	THIRD_PARTY_INCLUDES_END
Copy code
3. Prohibit UObjects in Abseil Containers

Never store UObject* or any pointers to garbage-collected objects in an Abseil container (like absl::flat_hash_map). The Unreal Garbage Collector (GC) cannot “see” into Abseil containers; therefore, it will not track these references, leading to the elimination of the object from memory while your container still holds a dangling pointer.

4. Avoid Namespace Directives

Never use using namespace absl; in a header file, and avoid it in source files. Abseil contains many types that look like standard library types (e.g., absl::optional vs std::optional). In the Unreal environment, where TOptional is the standard, explicit namespaces prevent developer confusion and linker errors.

5. Handle absl::Status for Plugin Interop

If you are extending the WebRTC or Pixel Streaming modules, you will frequently encounter absl::Status. Instead of immediate conversion to FString, use them to propagate errors up to your interface layer before converting them for Unreal’s logging system.

C++
	// Conversion for Unreal Logging

	absl::Status Status = CallWebRTCFunction();

	if (!Status.ok()) {

	    UE_LOG(LogTemp, Error, TEXT("Operation Failed: %hs"), Status.ToString().c_str());

	}
Copy code
6. Utilize for Non-UObject Performance Bottlenecks

For heavy mathematical or data-processing tasks that do not involve the Unreal reflection system, Abseil’s containers (like absl::InlinedVector) can be faster than TArray or std::vector because they optimize for small-element storage on the stack.

7. Use absl::string_view Only for External Interop

Unreal uses FStringView for lightweight string references. While Abseil uses absl::string_view, you should prefer FStringView for all internal Unreal logic. Only use absl::string_view when passing data directly into an Abseil-based API or WebRTC function.

8. Adhere to the Bundled Version

Unreal Engine ships with a specific version of Abseil located in Engine/Source/ThirdParty/Abseil. Do not attempt to link a different version of Abseil in the same project, as this will lead to symbol collisions with the engine’s built-in networking modules.