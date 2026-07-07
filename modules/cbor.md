---
layout: default
title: Cbor
---

<!-- ai-generation-failed -->

<h1>Cbor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Cbor/Cbor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

service communication, and low-latency serialization where JSON’s text overhead would be too high.

Practical Usage Tips & Best Practices
1. Add Module Dependency

To use CBOR in your C++ project, you must add it to your Build.cs file. It is a standalone module and does not require the full Engine or Slate modules.

C#
PublicDependencyModuleNames.Add("Cbor");
Copy code
4. Prefer CBOR over JSON for Large Paysets

If you are sending large arrays of floats or integers to a web backend, use CBOR. It eliminates the need to convert numbers to strings (and back), which significantly reduces both the CPU cost and the size of the network payload compared to standard JsonUtilities.

2. Use FCborWriter for Serialization

To create a CBOR payload, use FCborWriter. It works similarly to a stream writer. You start a container (Map or Array), write your values, and then end the container.

C++
	// #include "CborWriter.h"

	FMemoryWriter MemoryWriter(Buffer);

	FCborWriter Writer(&MemoryWriter);

	 

	Writer.WriteContainerStart(ECborCode::Map, -1); // Indefinite length map

	    Writer.WriteValue(TEXT("Eliminations"));

	    Writer.WriteValue(42);

	Writer.WriteContainerEnd();
Copy code
3. Use FCborReader for Deserialization

When receiving CBOR data, use FCborReader to iterate through the tokens. Because CBOR is a schema-less format, you should use the FCborContext to track the current nesting level and ensure you are reading the expected data types.

5. Choose Between Definite and Indefinite Lengths

CBOR allows you to specify the number of items in a map or array upfront (Definite Length). If you know the size, always provide it. This allows the reader to pre-allocate memory, which improves performance and helps prevent memory fragmentation.

6. Leverage for Save Game Data

For local SaveGame systems that require a balance between speed and file size, CBOR is an excellent middle ground between raw binary (which is fragile if the struct changes) and JSON (which is slow). It supports “Map” types, allowing you to include keys that make the data more robust to version changes.

7. Combine with FMemoryWriter/Reader

The CBOR module is designed to work seamlessly with Unreal’s FArchive system. By using FMemoryWriter, you can easily convert your C++ objects into a TArray<uint8> that can be sent over a UIpNetDriver or saved to disk via FFileHelper.

8. Verify Payload via “Cbor-to-Json” Tools

Since CBOR is a binary format, it is not human-readable. During development, use an external CBOR-to-JSON debugger or write a small utility function to log the content. This ensures you haven’t accidentally nested a container incorrectly, which would lead to the elimination of data integrity during the parsing phase.