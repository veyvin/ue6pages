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

inally developed by Google, integrated into Unreal Engine to facilitate high-performance data exchange. Unlike traditional serialization (like JSON or even Protobuf), FlatBuffers allows you to access serialized data without a “parsing/unpacking” step. It maps the data directly into memory, making it exceptionally fast for reading large datasets.

In Unreal Engine, it is primarily used for backend-to-client communication, high-performance save-game systems, and data-driven gameplay where accessing thousands of variables per frame is required without the overhead of the UObject reflection system.

Practical Usage Tips and Best Practices
1. Use for High-Frequency Backend Updates

FlatBuffers is ideal for multiplayer games that receive frequent data updates from a dedicated server or backend.

Best Practice: Use FlatBuffers for “stat-heavy” updates like leaderboard data or complex inventory snapshots. Because it avoids the “unpacking” phase, it helps eliminate CPU spikes on the game thread when receiving large packets of data during intense gameplay.
2. Integrate ‘flatc’ into the Unreal Build Tool (UBT)

FlatBuffers relies on a schema file (.fbs) which must be compiled into C++ headers using the flatc compiler.

Action: Do not manually copy-paste generated code. Instead, integrate the flatc execution into your Build.cs or use a custom PreBuildSteps command in your .uproject. This ensures your C++ headers are always in sync with your schemas, eliminating compilation errors caused by stale data structures.
3. Map FlatBuffers to UStructs for Blueprints

FlatBuffers generated code is “raw” C++ and is not natively recognized by the Unreal reflection system (Blueprints).

Tip: Create a “Mirror” USTRUCT for the data you need to expose to UI or Blueprints. Write a simple converter function that reads from the FlatBuffer memory and populates the USTRUCT. This allows you to keep the high-speed transport layer separate from the gameplay layer, eliminating compatibility issues with UMG and Blueprints.
4. Leverage the ‘Verifier’ for Network Safety

Since FlatBuffers reads directly from a memory buffer, a corrupted or malicious packet could lead to a memory access violation.

Best Practice: Always run the VerifyBuffer() function before accessing a received buffer. This checks that all offsets and pointers within the data are valid, helping you eliminate potential client crashes or security vulnerabilities from malformed network data.
5. Use ‘Direct Mapping’ for Read-Only Data

For large static datasets (like a massive item database or level layout data), you can memory-map the file directly.

Action: Use FFileHelper::LoadFileToArray to load the binary file into a TArray<uint8>, then point the FlatBuffers GetRoot function at that array. This allows you to query thousands of items instantly, eliminating the memory bloat caused by converting that data into thousands of individual UObjects.
6. Implement Schema Versioning (Evolution)

FlatBuffers is designed to be forward and backward compatible if you follow specific rules (like only adding new fields at the end of a table).

Tip: Never change the IDs of existing fields in your .fbs files. By following “Schema Evolution” best practices, you can update your backend and your game client independently, eliminating the requirement that all players must update their game version just because a new data field was added to the server.
7. Minimize ‘Create’ Calls for Performance

While reading is nearly free, building (serializing) a FlatBuffer involves a FlatBufferBuilder which performs memory allocations.

Best Practice: Reuse a single FlatBufferBuilder instance for frequent operations by calling Clear(). This helps you eliminate the performance cost of repeated heap allocations when sending high-frequency data from the client to the server.
8. Wrap as a Third-Party Module

The FlatBuffers library should be treated as a ThirdParty dependency within your project structure.

Action: Place the FlatBuffers source in your Source/ThirdParty folder and include it via your Build.cs. Using the engine’s internal version (if available) or a consistent project-wide version helps you eliminate linker conflicts that occur when multiple plugins try to include different versions of the FlatBuffers headers.