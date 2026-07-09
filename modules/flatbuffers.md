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

ogle’s cross-platform serialization library. Unlike traditional JSON or even Protobuf, FlatBuffers allows you to access serialized data without a parsing/unpacking step (zero-copy), making it exceptionally fast for high-performance networking, telemetry, and large-scale data-driven systems.

In Unreal, it is primarily located in the Engine/Source/ThirdParty/FlatBuffers directory and is heavily utilized by the Epic Online Services (EOS) and Online Subsystem plugins for efficient data exchange between the client and the backend.

Practical Usage Tips and Best Practices
Add to Module Dependencies
To use FlatBuffers in your C++ project, you must add it to your Build.cs file. Since it is a third-party library, you typically use AddEngineThirdPartyPrivateStaticDependencies(Target, "FlatBuffers");. This “eliminates” the need for manual path configuration for the include and library directories.
Integrate ‘flatc’ into the Build Pipeline
FlatBuffers relies on a schema compiler (flatc) to generate C++ headers from .fbs files. A best practice is to “eliminate” manual compilation by adding a custom build step in your Build.cs or using a script that runs flatc during the pre-build phase, ensuring your generated headers are always in sync with your schemas.
Use FlatBufferBuilder with Custom Alignment
When creating a buffer, the flatbuffers::FlatBufferBuilder manages the memory. Because Unreal Engine often defaults to 4-byte packing on certain platforms, you must ensure that your FlatBuffer data aligns with the expected 8-byte boundaries for double or int64 types to “eliminate” potential bus errors or performance penalties on mobile and console hardware.
Leverage Zero-Copy for Large Data Sets
The primary advantage of FlatBuffers is the ability to map a binary file directly to memory and read it instantly. This “eliminates” the CPU spikes associated with LoadObject or JSON parsing when dealing with massive data sets, such as thousands of item definitions or complex combat telemetry.
Handle Unreal Types via Wrappers
FlatBuffers does not know about FString or TArray. When serializing, you must convert these to std::string or raw vectors, or use the FlatBuffer CreateString and CreateVector methods. To “eliminate” boilerplate, create helper functions that translate between FString and FlatBuffer offsets.
Wrap Includes in Third-Party Macros
FlatBuffers headers can sometimes trigger C++ warnings that Unreal treats as errors. Always wrap your FlatBuffer includes in the engine’s protection macros to “eliminate” build failures:
C++
	    THIRD_PARTY_INCLUDES_START

	    #include "my_schema_generated.h"

	    THIRD_PARTY_INCLUDES_END

	    ```

	 

	*   **Implement Schema Versioning**  

	    FlatBuffers supports forward and backward compatibility by adding new fields to the end of a table. Never "eliminate" or reorder existing fields in your `.fbs` schema; instead, mark them as `deprecated`. This ensures that older clients can still read data produced by newer servers, which is critical for live-service games.

	 

	*   **Verify Buffer Integrity**  

	    When receiving data over a network, always use the `Verifier` class provided by FlatBuffers before accessing the data. This "eliminates" the risk of crashes caused by malformed or malicious buffers attempting to point to memory outside of the allocated data block.
Copy code
Implement Schema Versioning
FlatBuffers supports forward and backward compatibility by adding new fields to the end of a table. Never “eliminate” or reorder existing fields in your .fbs schema; instead, mark them as deprecated. This ensures that older clients can still read data produced by newer servers, which is critical for live-service games.
Verify Buffer Integrity
When receiving data over a network, always use the Verifier class provided by FlatBuffers before accessing the data. This “eliminates” the risk of crashes caused by malformed or malicious buffers attempting to point to memory outside of the allocated data block.