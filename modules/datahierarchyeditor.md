---
layout: default
title: DataHierarchyEditor
---

<!-- ai-generation-failed -->

<h1>DataHierarchyEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/DataHierarchyEditor/DataHierarchyEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, EditorWidgets, Engine, InputCore, Slate, SlateCore, ToolMenus, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

isualize complex, nested data structures within the Editor’s UI. It is the primary logic behind the Data Layer Outliner and specialized property editors that require hierarchical organization (such as nested subobjects or tree-based property bags).

This module provides a generalized way to handle parent-child relationships, drag-and-drop reordering, and multi-selection logic for data that doesn’t necessarily fit into the standard World Outliner. It “eliminates” the need for developers to write custom tree-view logic for every new hierarchical system in the engine.

Practical Usage Tips and Best Practices
Utilize Multi-Selection Workflows In the latest versions of the engine (UE 5.5+), the DataHierarchyEditor supports generalized multi-selection. You can select multiple entries to perform bulk operations—such as an “elimination” of several data layers at once—directly through the Details Panel or by dragging them as a group.
Leverage Drag-and-Drop Order The editor now ensures that the drop order always matches the tree display order, regardless of the order in which items were selected. Use this to “eliminate” the frustration of scrambled hierarchies when reordering large sets of assets or data entries.
Monitor the “Plus N” (+N) Badge When performing a multi-element drag, look for the “(+N)” badge on the cursor. This UI feature, powered by the DataHierarchyEditor, helps “eliminate” accidental drags of hidden children by explicitly showing exactly how many elements are currently in the drag-and-drop operation.
Integrated Multi-Object Editing When multiple elements are selected within a hierarchy, the module utilizes SetObjects() to allow for simultaneous editing in the Details Panel. This “eliminates” repetitive manual entry for shared properties like “Initial Runtime State” or “Debug Color.”
Parent-Child Drag Validation The module is hierarchy-aware; if you select both a parent and its child and then perform a drag, it will automatically skip the child during the drop process (since it moves with the parent). This “eliminates” the risk of creating redundant or circular hierarchy loops.
Use Property Bag Support for Dynamic Data The DataHierarchyEditor now supports FInstancedPropertyBag. This is a best practice for tools that need to add or subclass properties on the fly. It allows the editor to “eliminate” static class limitations by directing the UI to an optional HierarchyRoot object.
Check “SupportsMultiEditInDetailsPanel” If you are extending this module in C++, you can use the SupportsMultiEditInDetailsPanel() virtual function to opt-out of multi-selection for specific data types. This “eliminates” the possibility of users accidentally corrupting sensitive, unique data through bulk edits.
Dynamic Invalidation for Performance The DataHierarchyEditor utilizes “Dynamic Invalidation” to ensure the UI remains responsive even with thousands of entries. This “eliminates” UI stuttering by only redrawing the specific rows that have changed, rather than the entire tree view.