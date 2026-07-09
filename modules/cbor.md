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

unication (IPC). While JSON is human-readable, CBOR is machine-optimized, significantly reducing the CPU overhead of serialization and the resulting payload size.

Practical Usage Tips and Best Practices
1. Add the Module Dependency

To use CBOR in your C++ code, you must include the module in your project’s Build.cs file. It is a standalone module and does not require the full Engine or UnrealEd dependencies.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Core", "Cbor" });

	```

	 

	#### 2. Use for Performance-Critical Serialization

	Prefer CBOR over JSON for high-frequency data (e.g., telemetry or real-time state synchronization). Because CBOR is a binary format, the engine does not need to perform expensive string parsing or float-to-ASCII conversions. This can "eliminate" frame-time spikes when saving large amounts of data.

	 

	#### 3. Standard Serialization Pattern

	The module provides `FCborWriter` for output and `FCborReader` for input. Both interface with Unreal's `FArchive` system, allowing you to stream data directly to memory (`TArray<uint8>`) or to disk.

	 

	```cpp

	#include "CborWriter.h"

	#include "CborReader.h"

	#include "Serialization/MemoryWriter.h"

	 

	// Example: Serializing a simple map to a binary buffer

	TArray<uint8> BinaryBuffer;

	FMemoryWriter MemWriter(BinaryBuffer);

	FCborWriter CborWriter(&MemWriter);

	 

	CborWriter.WriteContainerStart(ECborCode::Map, 1);

	CborWriter.WriteValue(TEXT("Health"));

	CborWriter.WriteValue(100.0f);

	```

	 

	#### 4. Leverage Indefinite Length Containers

	Unlike many binary formats, CBOR supports "indefinite length" containers. This is useful when you are streaming data and don't know the final count of items in a list or map beforehand. You can start a container with `ECborCode::Indefinite`, write your data, and then call `WriteContainerEnd()`.

	 

	#### 5. Handle Type Safety with `FCborContext`

	When reading CBOR data, use the `FCborReader` to inspect the type of the next token before reading it. This prevents crashes or memory corruption if the incoming data format changes. Always check `Reader.PeekNextCode()` to ensure the data matches your expected `USTRUCT` or variable type.

	 

	#### 6. Compactness vs. Human Readability

	While CBOR is not human-readable by default, it is highly structured. For debugging, you can write a utility that converts CBOR to JSON using the `IStructSerializerBackend` interfaces. During development, you might keep data as JSON for easy tweaking, then switch the "Backend" to CBOR in your `Shipping` build for maximum performance.

	 

	#### 7. Avoid Raw Pointer Serialization

	Just like with standard Unreal serialization, never serialize raw pointers to `UObjects`. Instead, serialize the path name or a GUID, and resolve the reference upon deserialization using `StaticLoadObject` or a lookup table. CBOR handles strings and byte arrays efficiently, making it ideal for storing these identifiers.

	 

	#### 8. Use with `FStructuredArchive`

	In modern Unreal (5.0+), the best way to use CBOR is through `FStructuredArchive`. You can create a CBOR formatter and pass it into a structured archive. This allows you to write your serialization logic once and switch between Binary, JSON, and CBOR simply by changing the formatter at the top level.

	 

	---

	 

	### Comparison at a Glance

	 

	| Feature | JSON | CBOR |

	| :--- | :--- | :--- |

	| **Format** | Plain Text (ASCII/UTF8) | Binary |

	| **Parsing Speed** | Slow (String manipulation) | Fast (Direct memory read) |

	| **Payload Size** | Large | Small / Compact |

	| **Readability** | High | Low (Requires Viewer) |

	| **UE5 Support** | `Json` / `JsonUtilities` | `Cbor` Module |

	 

	### Recommended Header Includes

	```cpp

	#include "CborWriter.h"

	#include "CborReader.h"

	#include "Serialization/CborStructSerializerBackend.h" // For USTRUCT integration

	 
Copy code
2. Use for Performance-Critical Serialization

Prefer CBOR over JSON for high-frequency data (e.g., telemetry or real-time state synchronization). Because CBOR is a binary format, the engine does not need to perform expensive string parsing or float-to-ASCII conversions. This can eliminate frame-time spikes when saving large amounts of data.

3. Standard Serialization Pattern

The module provides FCborWriter for output and FCborReader for input. Both interface with Unreal’s FArchive system, allowing you to stream data directly to memory (TArray<uint8>) or to disk.

C++
	#include "CborWriter.h"

	#include "CborReader.h"

	#include "Serialization/MemoryWriter.h"

	 

	// Example: Serializing a simple map to a binary buffer

	TArray<uint8> BinaryBuffer;

	FMemoryWriter MemWriter(BinaryBuffer);

	FCborWriter CborWriter(&MemWriter);

	 

	CborWriter.WriteContainerStart(ECborCode::Map, 1);

	CborWriter.WriteValue(TEXT("Health"));

	CborWriter.WriteValue(100.0f);
Copy code
4. Leverage Indefinite Length Containers

Unlike many binary formats, CBOR supports “indefinite length” containers. This is useful when you are streaming data and don’t know the final count of items in a list or map beforehand. You can start a container with ECborCode::Indefinite, write your data, and then call WriteContainerEnd().

5. Handle Type Safety with PeekNextCode

When reading CBOR data, use the FCborReader to inspect the type of the next token before reading it. This prevents crashes or memory corruption if the incoming data format changes. Always check Reader.PeekNextCode() to ensure the data matches your expected variable type.

6. Compactness vs. Human Readability

While CBOR is not human-readable by default, it is highly structured. For debugging, you can write a utility that converts CBOR to JSON using the IStructSerializerBackend interfaces. During development, you might keep data as JSON for easy tweaking, then switch the backend to CBOR in your shipping build for maximum performance.

7. Avoid Raw Pointer Serialization

Just like with standard Unreal serialization, never serialize raw pointers to UObjects. Instead, serialize the path name or a GUID, and resolve the reference upon deserialization using StaticLoadObject. CBOR handles strings and byte arrays efficiently, making it ideal for storing these identifiers.

8. Use with FStructuredArchive

In modern Unreal (5.0+), the best way to use CBOR is through FStructuredArchive. You can create a CBOR formatter and pass it into a structured archive. This allows you to write your serialization logic once and switch between Binary, JSON, and CBOR simply by changing the formatter at the top level.

Comparison at a Glance
Feature	JSON	CBOR
Format	Plain Text (ASCII/UTF8)	Binary
Parsing Speed	Slow (String manipulation)	Fast (Direct memory read)
Payload Size	Large	Small / Compact
Readability	High	Low (Requires Viewer)
UE5 Support	Json / JsonUtilities	Cbor Module
Recommended Header Includes
C++
	#include "CborWriter.h"

	#include "CborReader.h"

	#include "Serialization/CborStructSerializerBackend.h" // For USTRUCT integration
Copy code