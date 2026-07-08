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

-performance JSON parser and generator for C++. While Unreal Engine provides the Json and JsonUtilities modules, RapidJSON is included for scenarios requiring extreme speed, a smaller memory footprint, or advanced JSON schema validation.

It is a header-only library located in the engine’s ThirdParty directory. It is primarily used by low-level engine subsystems, such as the Live Link plugin and various data-heavy importers, where the overhead of UObject-based JSON wrappers must be eliminated to maintain high performance.

Practical Usage Tips and Best Practices
Link via Build.cs
To use RapidJSON in your project, add it to your module’s Build.cs file:
PublicDependencyModuleNames.Add("RapidJSON");
Since it is a header-only library, this adds the necessary include paths to your project so you can use #include "rapidjson/document.h".
Prefer Over JsonUtilities for High-Frequency Data
If you are parsing JSON data every frame (e.g., streaming motion capture data via Live Link), use RapidJSON. Its In-place parsing and SAX (Simple API for XML) style parsing help you eliminate the CPU spikes often caused by Unreal’s standard FJsonObject creation and destruction.
Use ‘In-Situ’ Parsing to Save Memory
RapidJSON allows “in-situ” parsing, where the JSON string is modified directly in memory to store the DOM. If you have a mutable buffer, use Document.ParseInsitu(buffer). This helps you eliminate an extra copy of the data, which is critical when working with large datasets on memory-constrained platforms.
Convert FString to UTF-8 Correctly
RapidJSON typically expects UTF-8 encoding. When passing an Unreal FString to a RapidJSON document, use the TCHAR_TO_UTF8 macro:
Document.Parse(TCHAR_TO_UTF8(*MyFString));
This ensures that the conversion from Unreal’s internal 16-bit encoding to 8-bit JSON-standard encoding is handled properly, helping you eliminate encoding errors.
Leverage Schema Validation
Unlike the standard Unreal JSON modules, RapidJSON supports JSON Schema validation. You can use this to verify that incoming data (from a web API or local config) matches your expected structure before processing it, which helps you eliminate crashes caused by malformed or unexpected data.
Use RapidJSON for Serialization to Disk
When saving large game state data or complex tool configurations, RapidJSON’s Writer and StringBuffer classes are highly efficient. Using them can significantly reduce the time spent in “Save Game” operations, helping you eliminate noticeable hitches for the player.
Handle Namespaces Carefully
RapidJSON uses the rapidjson namespace. Avoid using using namespace rapidjson; in header files to eliminate potential naming collisions with Unreal’s own types. Instead, use specific types like rapidjson::Document or use a namespace alias within your .cpp files.
Clear Buffers on Elimination of the Data Task
When you are finished with a JSON document or a string buffer (the “elimination” of the current data task), ensure the Document object goes out of scope or call Clear(). Because RapidJSON uses its own memory allocators, properly managing the object’s lifetime helps you eliminate memory leaks in long-running processes.