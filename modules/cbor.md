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

ance, binary-based data serialization format. Based on the IETF RFC 7049 standard, it is designed to be a more compact and faster alternative to JSON while maintaining a similar tree-like data structure.

What it is and What it’s used for

The module provides the FCborWriter and FCborReader classes to convert structured data (maps, arrays, integers, strings) into a binary stream. Unlike JSON, which is human-readable text, CBOR is machine-optimized, making it ideal for scenarios where bandwidth and parsing speed are critical.

Primary uses include:

Networking: Sending compact data packets between a game client and a backend server (e.g., via WebSockets or HTTP).
Save Games: Storing complex player data in a small binary footprint that is harder for players to edit manually than a text file.
Asset Metadata: Packaging information that needs to be read quickly during loading screens.
Cloud Integration: Communicating with external web services that support CBOR for reduced latency.
Practical Usage Tips and Best Practices
1. Add the Module Dependency

To use CBOR in your C++ code, you must explicitly add it to your project’s build dependencies. In your YourProject.Build.cs file, include it in the PublicDependencyModuleNames array:

C#
	PublicDependencyModuleNames.AddRange(new string[] { "Core", "Cbor" });

	```

	 

	#### 2. Use FMemoryWriter for Buffer Management

	The `FCborWriter` requires an `FArchive` to function. For most use cases (like networking or temporary storage), use an `FMemoryWriter` to serialize data directly into a `TArray<uint8>`.

	```cpp

	#include "CborWriter.h"

	#include "Serialization/MemoryWriter.h"

	 

	TArray<uint8> BinaryBuffer;

	FMemoryWriter Ar(BinaryBuffer);

	FCborWriter Writer(&Ar);

	 

	Writer.WriteContainerStart(ECborCode::Map, -1); // Start an indefinite map

	Writer.WriteValue(TEXT("PlayerHealth"), 100.0f);

	Writer.WriteContainerEnd();

	```

	 

	#### 3. Match Writer and Reader Containers

	When reading data, your `FCborReader` calls must exactly mirror the structure of your `FCborWriter`. If you started a map with `WriteContainerStart(ECborCode::Map, ...)`, you must read it using a corresponding container check or loop until `IsContainerEnd()`. Failing to match the structure will result in the reader losing its place in the stream.

	 

	#### 4. Prefer Definite-Length Containers when Possible

	While CBOR supports indefinite-length containers (passing `-1` to `WriteContainerStart`), providing an exact count of items allows the reader to pre-allocate memory and reduces the overhead of end-of-container markers. This is significantly more performant for large arrays.

	 

	#### 5. Use Key-Value Pairs for Map Data

	When writing a Map (the CBOR equivalent of a JSON object), you must write entries in pairs: one `WriteValue` for the key (usually a string or integer) followed immediately by one `WriteValue` for the actual data. 

	```cpp

	Writer.WriteValue(TEXT("Level")); // Key

	Writer.WriteValue(42);           // Value

	```

	 

	#### 6. Validate Data Types During Reading

	The `FCborReader` provides a `PeekCode()` and `GetType()` method. Use these to validate that the data you are about to read matches the expected type (e.g., checking if the next item is an integer before calling `ReadValue(MyInt)`). This prevents crashes when handling potentially corrupted or version-mismatched data.

	 

	#### 7. Handle Byte Strings for Binary Payloads

	CBOR is excellent at "nesting" binary data. If you have a raw byte array (like a thumbnail image or a compressed struct), use `WriteValue(MyByteArray)` to store it as a CBOR Byte String. This is much more efficient than Base64-encoding binary data into a JSON string.

	 

	#### 8. Optimize String Serialization

	Unreal's CBOR implementation handles `FString` and `FName` naturally. However, if you are sending data to a non-Unreal backend, ensure your strings are UTF-8 compliant. The `FCborWriter` handles the conversion to the standard CBOR string format (Major Type 3) automatically, ensuring cross-platform compatibility.
Copy code
2. Use FMemoryWriter/Reader for Buffers

The CBOR classes require an FArchive to function. For most use cases (like preparing a network payload), use an FMemoryWriter to serialize data into a TArray<uint8> (byte array):

C++
	TArray<uint8> BinaryData;

	FMemoryWriter Ar(BinaryData);

	FCborWriter Writer(&Ar);

	Writer.WriteValue(TEXT("Health"), 100.0f);
Copy code
3. Match Writer and Reader Structures

CBOR is a stream-based format. Your FCborReader calls must exactly mirror the order and structure of your FCborWriter calls. If you write a Map followed by an Array, you must read the Map before the Array. Failing to do so will lead to deserialization errors and the potential elimination of the data stream’s integrity.

4. Prefer Definite-Length Containers

While CBOR supports “indefinite” containers (where the size is unknown at the start), providing an exact count to WriteContainerStart is more efficient. This allows the reader to pre-allocate memory for the incoming items, reducing the number of reallocations during the loading process.

5. Utilize Byte Strings for Binary Data

A major advantage of CBOR over JSON is its native support for “Byte Strings.” If you need to embed a raw binary blob (like a small thumbnail or a compressed struct) inside your data, use Writer.WriteValue(MyByteArray). This avoids the 33% size increase associated with Base64 encoding used in text formats.

6. Validate with PeekCode

When reading data from an untrusted source (like a network packet), use Reader.PeekCode() or Reader.GetType(). This allows you to verify the data type of the next item before attempting to read it, preventing crashes or logic errors if the incoming data format has changed.

7. Keep Key Names Short

In CBOR Maps, keys are stored as strings. If you are sending thousands of objects with the same keys (e.g., “PositionX”, “PositionY”), the strings will consume significant space. Consider using short integer IDs as keys (e.g., 0, 1, 2) instead of long strings to further minimize the binary footprint.

8. Use for Cross-Platform Serialization

CBOR is a platform-agnostic standard. Because the cbor module follows the official spec, you can serialize data in Unreal Engine and deserialize it in a backend written in Go, Python, or Node.js using any standard CBOR library, facilitating seamless full-stack development.