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

Its primary purpose is to provide Property Customizations and utility functions that allow JSON data to be represented clearly in the Details panel. It enables developers to create custom editor windows, data-import factories, and automation scripts that can parse, validate, and display JSON structures in a human-readable format. This module is essential for building pipelines where external data (like web API responses or config files) needs to be integrated directly into Unreal assets.

Practical Usage Tips and Best Practices
Restrict to Editor-Only Modules
Since this module is part of the Editor, you must only include it in your .Build.cs file within an Editor module or wrapped in an #if WITH_EDITOR block. Including it in a Runtime module will eliminate your ability to package the game for shipping.
Implement Custom Detail Customizations
If you have a FString property that stores JSON, use this module’s classes to create an IPropertyTypeCustomization. This allows you to display the JSON as a structured list of fields in the Details panel, which helps you eliminate the risk of manual syntax errors (like missing brackets) when designers edit the data.
Validate JSON During Asset Import
When writing a custom UFactory to import external JSON files, use this module to perform a “pre-flight” validation check. Catching malformed JSON before the import finishes helps you eliminate editor crashes or the creation of corrupted assets.
Use for Data-Driven UI in Tools
If you are building a custom Editor Utility Widget or Slate window, use this module to bridge the gap between JSON keys and Slate labels. It provides helper logic to iterate through JSON objects and generate UI elements dynamically, helping you eliminate hard-coded UI layouts for variable data.
Leverage FJsonStructCustomization
This module provides built-in logic for mapping JSON fields to UProperty handles. Utilizing these existing classes for your custom tools is a best practice that helps you eliminate redundant boilerplate code when syncing your C++ variables with JSON sources.
Sanitize JSON Strings for Display
The module includes utilities for “pretty-printing” and formatting raw JSON strings. Before showing a JSON blob in a tool’s text box, use these formatters to add indentation and line breaks, which helps you eliminate the frustration of reading unformatted, single-line “minified” JSON.
Verify Schema Compatibility
When using JSON to drive level generation or actor properties, use the editor utilities to compare the JSON structure against a UStruct template. Identifying missing or renamed fields early in the pipeline helps you eliminate “silent failures” where data is loaded incorrectly during a playtest.
Handle Multi-Object Editing with Property Handles
When several actors are selected in the editor, this module’s integration with the property system ensures that JSON-based properties are updated correctly across all instances. Using the standard IPropertyHandle interface via this module helps you eliminate data desynchronization between selected actors.