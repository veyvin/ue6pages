---
layout: default
title: Flatbuffers
---

<!-- ai-generation-failed -->

<h1>Flatbuffers</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/ThirdParty/flatbuffers/Flatbuffers.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">模块类型</span><span class="value"><code>External</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

cross-platform serialization library. It is stored as an External Third-Party module and is designed for maximum performance in data-heavy applications. Unlike standard JSON or even Unreal’s UObject serialization, FlatBuffers allows you to access serialized data without a separate parsing or unpacking step.

By mapping data directly to memory, this module helps eliminate the CPU and memory overhead associated with traditional data decoding, making it ideal for high-performance networking, save games, and large-scale data-driven systems.

Practical Usage Tips and Best Practices
Utilize Zero-Copy Access
The primary strength of FlatBuffers is its “zero-copy” nature. Use the generated C++ headers to access data directly from the binary buffer. This approach helps you eliminate the time-consuming step of converting binary data into intermediate C++ structs or UObjects before use.
Integrate via Build.cs
To use this module in your project, you must add "FlatBuffers" to your PublicDependencyModuleNames in your *.Build.cs file. This ensures the Unreal Build Tool (UBT) correctly configures the include paths and library links, helping to eliminate “file not found” errors during compilation.
Manage Schema Evolution
FlatBuffers supports forward and backward compatibility. When updating your data structures, always add new fields to the end of the table and avoid renaming existing ones. This practice helps you eliminate versioning conflicts when your game needs to load older save files or communicate with different server versions.
Automate with ‘flatc’
Do not manually write FlatBuffer headers. Use the flatc compiler (provided in the engine’s ThirdParty/FlatBuffers directory) to generate C++ code from your .fbs schema files. You can add a custom build step in the Unreal Editor to eliminate the manual effort of re-generating code every time the schema changes.
Verify Data Alignment
FlatBuffers relies on specific memory alignment for its “zero-copy” speed. When loading a buffer from disk or a network packet, ensure the pointer is aligned to the requirement of the FlatBuffer (usually 4 or 8 bytes). Proper alignment helps you eliminate bus errors or performance penalties on platforms like ARM or consoles.
Prefer Tables over Structs for Flexibility
In your .fbs schema, use table for most data types instead of struct. Tables are more flexible and allow for optional fields, which helps you eliminate wasted space in the binary buffer if many of your data fields are frequently null or default.
Use for Large Data Tables
If your project has massive Data Tables that cause slow load times or high memory usage, consider moving that data to FlatBuffers. Because it doesn’t require the overhead of the UObject system, it can eliminate the “hitch” that occurs when the engine loads and registers thousands of individual row objects.
Wrap in Preprocessor Guards
While FlatBuffers is a runtime-compatible library, keep your schema-processing logic clean. Use #include "ThirdParty/FlatBuffers/flatbuffers.h" and ensure your logic is structured to handle binary data safely. This helps eliminate potential crashes if a corrupted or malicious buffer is received over the network.