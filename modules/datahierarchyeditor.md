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

ed in recent versions of Unreal Engine (UE 5.5+) to power the new, generalized Hierarchy Editor UI. It provides the framework for displaying and managing complex, multi-layered data structures in a tree-view format, specifically designed for systems that require hierarchical organization like Data Layers, Instanced Property Bags, and TEDS (Typed Element Data Storage).

While previous systems had bespoke, hard-coded outliners, this module provides a unified logic layer for multi-selection, drag-and-drop operations, and multi-object editing across different hierarchical data types in the editor.

Practical Usage Tips and Best Practices
1. Multi-Selection Generalization

The module enables a consistent “Shift+Click” and “Ctrl+Click” behavior across new hierarchy-based windows.

Best Practice: When managing Data Layers, leverage the multi-selection support to move large groups of actors or layers simultaneously. The module handles the validation logic to ensure that if one element in the selection cannot be moved, the entire operation is safely blocked to eliminate partial or corrupted data states.
2. Hierarchical Drag-and-Drop

The FHierarchyDragDropOp within this module is “hierarchy-aware,” meaning it understands parent-child relationships during a move.

Tip: If you select both a parent and its child and drag them to a new location, the module will skip the redundant child operation. This helps eliminate logic errors where children are accidentally detached or double-processed during organizational tasks.
3. Use the Selection “Badge” System

A new feature of this editor module is the “(+N)” badge that appears next to the cursor during a drag operation.

Action: Pay attention to this badge and the associated tooltips. It lists exactly which elements are being moved. Use this visual feedback to eliminate accidental “ghost” selections of hidden or collapsed nodes before committing a drop.
4. Leverage Multi-Edit in the Details Panel

The DataHierarchyEditor allows for “SetObjects()” style multi-editing when multiple elements are selected in the tree.

Best Practice: Select multiple Data Layers to edit their shared properties (like Debug Color) in the Details Panel at once. If a specific data type doesn’t support this, developers can opt-out using the SupportsMultiEditInDetailsPanel() virtual function to eliminate the risk of unintended bulk property changes.
5. Integration with Instanced Property Bags

This module is the engine behind the updated UI for FInstancedPropertyBag, allowing developers to subclass and add properties to a hierarchy dynamically.

Tip: Use this for complex NPC stats or procedural world generation parameters where variables need to be grouped in a tree structure. It provides a cleaner interface than a flat list, helping you eliminate UI clutter in complex data assets.
6. Smart Drop Validation

The module performs a “look-ahead” validation check before a drop is finalized.

Action: If a drop target turns red, it means one or more of your selected items is incompatible with that location. This automated validation is designed to eliminate invalid hierarchy loops (e.g., trying to parent a folder to its own child).
7. Property Bag Schema Customization

Developers can use UPropertyBagSchema to direct the hierarchy details to a specific root object.

Best Practice: When building custom editor tools, use a specialized Schema class to control how your data is displayed in the hierarchy. This allows you to enforce specific naming conventions and type constraints, which helps eliminate data entry errors by end-users.
8. Visual Consistency with TEDS

The module is increasingly used to find Slate nodes for elements that don’t have a standard UObject pointer but exist as rows in the Typed Element Data Storage.

Tip: If you are working with the experimental TEDS system, use the DataHierarchyEditor’s utility functions to locate nodes in the UI. This provides a unified way to interact with data regardless of its underlying storage format, eliminating the need for custom Slate-hunting code.