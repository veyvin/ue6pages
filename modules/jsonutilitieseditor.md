---
layout: default
title: JsonUtilitiesEditor
---

<!-- ai-generation-failed -->

<h1>JsonUtilitiesEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/JsonUtilitiesEditor/JsonUtilitiesEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetTools, BlueprintGraph, Core, CoreUObject, Engine, Json, JsonUtilities, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

Engine JsonUtilities system. While the runtime version handles basic serialization for gameplay, this module provides specialized tools for Editor-specific workflows, such as automated testing, data-driven tool configuration, and asset-importing pipelines. It is a critical component for developers building custom editor utilities that need to bridge the gap between external JSON data and the engine’s internal UStruct and UObject reflection systems.

Practical Usage Tips & Best Practices
1. Scope to Editor-Only Build Targets

Since this module resides in the Editor category, it will cause linker errors if included in a shipping build.

Best Practice: In your .Build.cs file, wrap the module dependency in a check for Target.Type == TargetType.Editor. In your C++ code, always use #if WITH_EDITOR guards. This ensures the elimination of compilation failures when packaging the final game.
2. Utilize for Automated Test Configurations

The module includes classes like UJsonTestConfig, which are designed to drive automated testing parameters from external files.

Tip: Use this module to load complex test scenarios or “mock” data for your automation suite. This allows for the elimination of hard-coded test values, enabling QA teams to modify test logic by simply editing a JSON file without needing a recompile.
3. Streamline Asset Import Metadata

When creating custom asset importers, you often need to process sidecar JSON files that contain metadata for textures or meshes.

Best Practice: Use the utilities in this module to map JSON fields directly to UObject properties during the import phase. This facilitates the elimination of manual data entry in the Details panel, especially when batch-importing hundreds of assets.
4. Distinguish from Runtime JsonUtilities

Developers often confuse this module with the standard JsonUtilities used for web APIs or SaveGames.

Tip: Use JsonUtilitiesEditor exclusively for Editor-side automation and Tooling. For any data that must be accessed by the player at runtime, stick to the runtime module to ensure the elimination of “Module Not Found” crashes in the standalone build.
5. Integrate with Editor Utility Widgets

If you are building custom tool interfaces using Editor Utility Widgets (Blutilities), you can use this module to save and load the tool’s state.

Best Practice: Save the user’s last-used settings for your custom tool in a JSON file within the project’s Intermediate folder. This results in the elimination of repetitive setup tasks for artists when they restart the editor or reopen the tool.
6. Leverage UStruct Serialization for Complex Configs

The module excels at converting entire JSON objects into nested UStruct types with a single call.

Tip: Define your tool’s settings as a USTRUCT() and use FJsonObjectConverter to populate it. This type-safe approach ensures the elimination of fragile string-parsing logic and makes your editor tools more robust and easier to maintain.
7. Combine with Python for Rapid Tooling

The JsonUtilitiesEditor module provides the C++ backend that allows Python scripts to interact effectively with Unreal’s reflection system.

Best Practice: If you are using the Python API for editor automation, leverage this module’s ability to handle JSON-to-Object conversion. This ensures the elimination of complex “bridge” code, allowing for a seamless flow of data between Python dictionaries and Unreal C++ classes.
8. Proactive “Elimination” of Invalid Data

JSON is prone to syntax errors and schema mismatches which can crash editor tools if not handled.

Tip: Always wrap your serialization calls in validation checks to ensure the JSON matches the target UStruct. Implementing strict validation leads to the elimination of silent data corruption and editor hangs when a malformed configuration file is loaded.