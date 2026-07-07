---
layout: default
title: RapidJSON
---

<!-- ai-generation-failed -->

<h1>RapidJSON</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/RapidJSON/RapidJSON.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ly optimized, header-only C++ JSON parser and generator. It is widely recognized as one of the fastest JSON libraries available, focusing on memory efficiency and high-performance serialization.

In Unreal Engine, while the Json and JsonUtilities modules provide easy-to-use wrappers for UStruct conversion, the RapidJSON module is utilized for low-level, high-throughput tasks where the overhead of the engine’s standard TSharedPtr-based JSON objects is too high. It is particularly useful for massive data processing, real-time web socket communication, and large-scale configuration parsing.

Practical Usage Tips and Best Practices
1. Include with Third-Party Macros

Since RapidJSON is an external library located in the ThirdParty directory, its headers do not follow Unreal’s coding standards and may trigger compiler warnings.

Action: Always wrap your include statements in the third-party guard macros:
C++
	THIRD_PARTY_INCLUDES_START

	#include "rapidjson/document.h"

	#include "rapidjson/writer.h"

	THIRD_PARTY_INCLUDES_END
Copy code
This helps you eliminate “shadowed variable” or “missing macro” warnings during compilation.
2. Use for Large-Scale Data Sets

The standard FJsonObject creates a significant number of heap allocations because every field is a shared pointer.

Best Practice: Use RapidJSON when parsing files larger than a few megabytes or containing thousands of nodes. Its “In-Situ” parsing mode and contiguous memory buffers help you eliminate the performance penalty of excessive memory allocations.
3. Leverage “In-Situ” Parsing for Speed

RapidJSON can parse a JSON string by modifying the source buffer directly instead of copying strings into new memory locations.

Tip: If you have a mutable char* buffer, use document.ParseInsitu<0>(buffer). This is the fastest way to parse JSON as it points the DOM nodes directly to the source string, effectively eliminating the time spent on string allocations and copies.
4. Manage Encodings Correctly (FString to UTF-8)

Unreal Engine uses TCHAR (UTF-16 on Windows), while RapidJSON typically expects UTF-8.

Action: Convert your FString data using the FTCHARToUTF8 converter when passing data to a RapidJSON StringStream. Correct conversion helps you eliminate character corruption and ensures that localized text or symbols remain intact.
5. Avoid Deep DOM Nesting where Possible

While RapidJSON is fast, building a massive Document Object Model (DOM) still consumes memory.

Tip: For extremely large files where you only need to extract specific values, consider using the SAX (Simple API for XML/JSON) parser provided by RapidJSON. It processes the file as a stream, which helps you eliminate the memory overhead of loading the entire JSON structure into RAM.
6. Add Module Dependency in Build.cs

Even though it is header-only, you must tell the Unreal Build Tool where to find the headers.

Action: Add "RapidJSON" to your PrivateDependencyModuleNames in your *.Build.cs file. This ensures the include paths are correctly mapped to Engine/Source/ThirdParty/RapidJSON/include, eliminating “header not found” errors.
7. Reuse Document and Allocator Objects

RapidJSON uses an internal allocator to manage the memory for its DOM nodes.

Best Practice: If you are parsing or generating JSON frequently (e.g., every frame or for every network packet), reuse the rapidjson::Document or rapidjson::MemoryPoolAllocator. Reusing memory blocks helps you eliminate frequent calls to the system’s memory manager, keeping your Game Thread smooth.
8. Use for Custom Editor Tooling

RapidJSON is excellent for parsing metadata from external DCC tools that export complex JSON.

Tip: Use it in Editor Utility Widgets or C++ Commandlets to process bulk asset data. The speed of RapidJSON ensures that importing thousands of items doesn’t freeze the editor, eliminating long wait times for developers and technical artists.