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

d in recent versions of Unreal Engine to provide a generalized UI for managing complex, nested data structures. It serves as the underlying logic for the Data Layers Outliner and the Property Bag hierarchy systems.

Its primary purpose is to allow developers to visualize and manipulate hierarchical relationships between data elements—such as parent-child actors in a World Partition layer or nested variables in a schema—while providing built-in support for multi-selection, drag-and-drop, and details panel integration. This framework helps “eliminate” the need for developers to build custom tree-view logic for every new hierarchical data tool.

Practical Usage Tips and Best Practices
Implement Multi-Edit for Productivity
The module supports a SupportsMultiEditInDetailsPanel() virtual function. When building custom hierarchy tools, ensure this returns true to allow users to “eliminate” repetitive tasks by editing properties for multiple selected hierarchy entries simultaneously.
Leverage Hierarchy-Aware Drag-and-Drop
When moving elements, the module automatically identifies if a child is being moved along with its parent. Use the bIsContainedInAnotherDraggedElement flag in your drag-drop operations to “eliminate” redundant processing of child nodes, ensuring only the top-level parent is processed for the move.
Utilize Property Bag Integration
The DataHierarchyEditor is highly integrated with FInstancedPropertyBag. If your tool uses dynamic properties (like those in Mass Entity or Niagara), use the PropertyBagSchema to direct your details panel to a HierarchyRoot object. This helps “eliminate” clutter by organizing dynamic variables into a clear, logical tree.
Customize Multi-Selection Logic
You can toggle multi-selection via the view model. For tools where selection order or exclusivity is critical (such as specific animation state overrides), disable multi-selection to “eliminate” the risk of users accidentally applying changes to unintended nodes.
Use the Data Hierarchy Drag Drop Context
Always wrap your drag-drop data in a FDataHierarchyDragDropContext. This provides utility functions like GetTopLevelEntries, which allow you to “eliminate” lower-level nodes from your logic during a drop, preventing “circular dependency” errors where a parent is dropped onto its own child.
Define Custom Drag Decorators
For a professional editor experience, use the module’s ability to render custom drag decorators. When multiple elements are dragged, the system can show a vertical stack with a “(+N)” badge. This “eliminates” confusion during complex level reorganization by clearly showing exactly how many assets are being moved.
Apply Streaming Priority for Data Layers
If using this module via the Data Layers Outliner, take advantage of the Streaming Priority property. Assigning a lower value gives the layer higher priority, which helps “eliminate” loading hitches by ensuring critical environmental data is streamed in before decorative foliage.
Validate Drop Operations Thoroughly
The module uses an “all-or-nothing” validation approach. If you are implementing a custom drop target, ensure your validation check returns false if any of the dragged elements are invalid for that target. This “eliminates” partial state errors where only some assets are successfully moved, leaving the hierarchy in a broken state.