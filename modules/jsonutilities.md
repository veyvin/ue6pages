---
layout: default
title: JsonUtilities
---

<!-- ai-generation-failed -->

<h1>JsonUtilities</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/JsonUtilities/JsonUtilities.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

n raw JSON data and the engine’s reflection system (UStructs and UClasses). While the base Json module provides low-level tools to manually parse strings, JsonUtilities introduces the FJsonObjectConverter, which can automatically map JSON keys to C++ variables.

This module is the standard choice for handling REST API responses, configuration files, and web-based data, facilitating the elimination of tedious manual parsing by automating the serialization and deserialization of complex data structures.

Practical Usage Tips and Best Practices
1. Add Module Dependency in Build.cs

To use the automation features of this module, you must add "JsonUtilities" and "Json" to your project’s Build.cs file. Forgetting this step is the most common cause of linker errors. Proper dependency management is the first step toward the elimination of “unresolved external symbol” errors when calling JSON functions.

2. Match UPROPERTY Names with JSON Keys

The FJsonObjectConverter uses the names of your UPROPERTY variables to find matching keys in the JSON string. If your JSON uses a key like "player_score", your C++ struct should have a variable named player_score. Using consistent naming conventions across your web backend and game client leads to the elimination of mapping errors.

3. Use USTRUCTs for Automatic Serialization

Instead of manually building a JSON object, define a USTRUCT. You can then use FJsonObjectConverter::UStructToJsonObjectString to convert the entire struct into a JSON string in a single line. This practice assists in the elimination of “string-building” bugs where a missing comma or bracket would otherwise break the JSON format.

4. Handle Nested Objects with Nested Structs

JsonUtilities natively supports nested data. If your JSON contains an object within an object, simply create a USTRUCT that contains another USTRUCT as a member. The converter will recursively parse the data, facilitating the elimination of complex, multi-stage parsing logic for deep data hierarchies.

5. Be Mindful of Large World Coordinates (LWC)

Standard JSON numbers are double-precision. When serializing Unreal’s FVector (which uses doubles in UE5), ensure your JSON backend can handle the precision. If you are targeting platforms with strict memory limits, you may need to manually clamp values to ensure the elimination of precision-related “jitter” in your transmitted coordinates.

6. Use “SkipStandardCustomProperties” for Clean Data

When converting a UObject to JSON, the engine may try to include internal metadata that you don’t need for a web API. Use the export flags in FJsonObjectConverter to exclude these properties. This leads to the elimination of “payload bloat,” keeping your JSON strings small and efficient for network transmission.

7. Verify Parsing Success with Boolean Checks

Methods like JsonObjectStringToUStruct return a boolean. Always wrap these calls in an if statement. If the JSON is malformed, the function will return false, allowing you to handle the error gracefully. This is a best practice for the elimination of crashes caused by trying to access data from an uninitialized or null struct.

8. Leverage for Data-Driven Testing

You can use JsonUtilities to load mock game data from local .json files during development. This allows you to quickly tweak balance variables (like “elimination” damage or move speeds) without recompiling C++ code. Using JSON for local overrides assists in the elimination of slow iteration cycles in your gameplay tuning process.