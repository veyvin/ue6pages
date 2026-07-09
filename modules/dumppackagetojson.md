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

and metadata of an asset without needing to open the Unreal Editor UI.

This tool is essential for technical artists and pipeline engineers who need to audit asset data, “eliminate” corruption by inspecting raw values, or perform large-scale data analysis across thousands of assets.

Practical Usage Tips and Best Practices
Run via the Command Line
Execute the commandlet using the UnrealEditor-Cmd.exe. Use the following syntax to “eliminate” the need for the full editor overhead:
UnrealEditor-Cmd.exe YourProject.uproject -run=DumpPackageToJson -Package=/Game/Path/To/Asset
Use for Version Control Diffing
Standard .uasset files are binary and cannot be easily diffed. Use this module to export JSON versions of problematic assets to “eliminate” the mystery of what changed between two versions in your source control history.
Specify the Output Directory
Use the -Output= flag to direct the resulting JSON to a specific workspace. This “eliminates” clutter in your project folders and allows external scripts (Python or Node.js) to easily pick up the data for automated reporting.
Filter for Specific Property Types
When auditing assets for optimization, use external JSON parsers to look for specific flags. This helps “eliminate” assets that are incorrectly configured—for example, finding all Static Meshes that accidentally have “Generate Overlap Events” enabled.
Audit Asset Dependencies
The JSON output includes the ImportMap and ExportMap. Reviewing these sections helps you “eliminate” hidden dependencies that might be ballooning your project size or causing long load times due to “asset circularity.”
Detect “Ghost” Data
Sometimes assets retain properties from deleted components or old classes. Dumping to JSON “eliminates” the invisibility of this “ghost data,” allowing you to see if an asset is carrying unnecessary serialized bytes that the Editor UI isn’t showing.
Batch Process via Python or PowerShell
For large-scale audits, wrap the commandlet in a script. This allows you to “eliminate” manual labor by dumping every asset in a specific folder to JSON, which can then be indexed into a database for project-wide data visualization.
Validate against Schema Changes
If you have refactored a C++ struct, use this module to see how the engine is currently serializing the data on disk. This helps “eliminate” data loss by ensuring the “cooked” or “saved” values match your new structural expectations.