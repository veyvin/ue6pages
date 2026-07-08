---
layout: default
title: DumpPackageToJson
---

<!-- ai-generation-failed -->

<h1>DumpPackageToJson</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Experimental/DumpPackageToJson/DumpPackageToJson.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, JsonObjectGraph, StorageServerClient</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

gned to serialize binary Unreal Engine package files (.uasset, .umap) into a human-readable JSON format. It is primarily used for deep asset inspection, auditing, and comparing the internal data structures of a package without opening the Unreal Editor.

By converting the binary data into structured text, this module helps developers eliminate the “black box” nature of binary assets, making it possible to see exactly how properties, object headers, and export tables are stored on disk.

Practical Usage Tips and Best Practices
Execute via Commandlet for Automation
Run the module using the UnrealEditor-Cmd.exe with the -run=DumpPackageToJSON flag. This allows you to integrate asset serialization into your CI/CD pipelines to eliminate manual checking of asset properties across large project updates.
Use for Version Control Diffing
If you suspect a binary conflict in Perforce or Git, dump both versions of the asset to JSON and use a text-based diffing tool. This practice helps eliminate the ambiguity of binary merges by showing exactly which float, string, or boolean property was modified.
Audit for Bloated Data
Analyze the resulting JSON to find unexpectedly large arrays or heavy metadata. This is an effective way to eliminate “asset bloat,” where a simple Blueprint or Data Asset might be carrying hidden, heavy references or legacy data that isn’t visible in the standard Details panel.
Validate Data-Driven Properties
For complex systems like Data Tables or Primary Data Assets, use the JSON output to verify that values are being serialized in the correct format (e.g., ensuring a “double” hasn’t been accidentally truncated to a “float”). This helps eliminate subtle data-driven bugs before they reach runtime.
Filter Output to Specific Objects
When dumping large levels (.umap), the JSON file can become massive. Use command-line arguments to limit the dump to specific object classes or names. This focus helps you eliminate noise and find specific actor data more efficiently.
Strip Sensitive Metadata
When sharing asset structures with external partners or for documentation, use the dump tool to extract the structure while eliminating sensitive or proprietary metadata. This ensures you only share the necessary technical schema of the package.
Identify Circular Dependencies
The JSON output includes an “Imports” section listing every external package the asset relies on. Reviewing this list can help you eliminate accidental circular dependencies or “hard” references that might be causing slow load times or packaging errors.
Verify Serialization Changes in C++
If you have modified a C++ struct’s Serialize function or changed a UPROPERTY macro, use this module to verify the disk format. Comparing a “before and after” JSON dump helps eliminate risks of data loss or corruption when updating your underlying C++ data structures.