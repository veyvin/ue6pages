---
layout: default
title: StructViewer
---

<!-- ai-generation-failed -->

<h1>StructViewer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/StructViewer/StructViewer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, ContentBrowserData, Core, CoreUObject, EditorFramework, Engine, InputCore, Settings, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

face components necessary to browse, filter, and select UStruct types within the Unreal Editor.

Description and Purpose

Similar to the ClassViewer, the StructViewer module provides a specialized Slate widget (SStructViewer) that displays a hierarchical list of all available structures (including Native C++ structs and User-Defined Structs). Its primary purpose is to serve as the underlying framework for “Struct Pickers” used in the Details Panel, Data Tables, and various editor tools. By using this module, developers can eliminate the need to manually build search and filtering logic when they need to allow a user to pick a specific data structure from a list of thousands.

Practical Usage Tips and Best Practices
Initialize with FStructViewerInitializationOptions
When spawning a Struct Viewer, always use the FStructViewerInitializationOptions struct to define the initial state. You can set it to show only “User Defined Structs” or specific “Native Structs,” which helps you eliminate visual clutter for the user by hiding irrelevant data types.
Implement Custom Filtering via IStructViewerFilter
If your tool only supports a specific subset of structures, create a class that inherits from IStructViewerFilter. You can override IsStructAllowed to check for specific metadata or parent types. This is a best practice to eliminate user error by preventing the selection of incompatible structures.
Use for Data-Driven Tool Windows
If you are building a custom Editor Utility or a C++ editor window that manages data, use the FStructViewerModule::CreateStructViewer method to embed a picker directly. This provides a “native” feel and ensures you eliminate the friction of typing in struct names manually.
Leverage Metadata for Hidden Structs
You can use the InternalUseOnly or Hidden metadata specifiers in your C++ USTRUCT definitions. The Struct Viewer respects these flags by default, allowing you to eliminate internal-only helper structs from appearing in the picker list for designers.
Handle Selection via OnStructSelected Delegate
The SStructViewer widget provides an OnStructSelected delegate. Always bind to this to immediately update your tool’s state when a user clicks a struct. This ensures you eliminate the need for a “Confirm” or “Apply” button, making the workflow more fluid.
Enable Search Bar Functionality
Ensure you enable the search box in your initialization options (bShowNoneOption, bShowSearchBox). For projects with thousands of assets, this is essential to eliminate the time spent scrolling through long lists to find a specific data type.
Filter by Module or Path
You can restrict the viewer to show only structs from a specific module or folder path. This is highly effective in large-scale projects to eliminate name collisions where two different modules might have structs with similar names.
Check for Validity during Shutdown
Since this is an editor module, ensure that any custom widgets or filters you create are properly cleaned up when your editor module shuts down. This helps you eliminate memory leaks or “Access Violation” crashes when closing the Unreal Editor.