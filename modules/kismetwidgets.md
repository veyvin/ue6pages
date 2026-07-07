---
layout: default
title: KismetWidgets
---

<!-- ai-generation-failed -->

<h1>KismetWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/KismetWidgets/KismetWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">BlueprintGraph, ClassViewer, ContentBrowserData, Core, CoreUObject, EditorFramework, EditorWidgets, Engine, InputCore, Slate, SlateCore, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

designed to support the Blueprint Editor (Kismet) and other graph-based tools. It contains a collection of low-level Slate widgets that handle the visual representation of graph nodes, pins, and complex expressions.

While the GraphEditor module handles the logic of connections and nodes, KismetWidgets provides the actual “atoms” of the UI—such as the input fields for pins, badges for node status, and widgets that change their appearance based on the camera’s zoom level.

Practical Usage Tips and Best Practices
1. Add to Editor-Only Dependencies

The KismetWidgets module contains editor-specific Slate code and is not available in “Shipping” builds.

Best Practice: Only add "KismetWidgets" to the PrivateDependencyModuleNames of an Editor or Developer module in your *.Build.cs. This helps you eliminate compilation errors when packaging your game for end-users.
2. Implement Semantic Zooming with SLevelOfDetailWidget

One of the most powerful tools in this module is SLevelOfDetailWidget. It allows you to swap or simplify a widget’s content based on the current zoom level of the graph.

Tip: Use this to hide complex text or intricate buttons when the user zooms out of a graph. This improves editor performance and helps eliminate visual noise, showing only high-level node icons at a distance.
3. Create Compact Math Nodes with SKismetLinearExpression

If you are building a custom graph (like a dialogue system or a math-heavy tool), standard nodes can become bulky.

Action: Use SKismetLinearExpression to render a compact, horizontal representation of logic (e.g., (A + B) * C). This widget is used internally by the “Math Expression” node to eliminate the need for dozens of individual connected nodes.
4. Customize Pin Input with SPinSimpleValue

When creating custom SGraphPin classes, you often need a standard input field for numbers or strings.

Tip: Use SPinSimpleValue. It provides a standardized, look-and-feel-consistent input box that handles the engine’s “Reset to Default” and “Keyframe” logic automatically. Using this widget helps you eliminate the need to manually style raw SEditableText widgets.
5. Visualize Execution with SGraphNodeStatusBadge

If your custom node has multiple states (e.g., “Active,” “Error,” or “Running”), you can use status badges.

Action: Use SGraphNodeStatusBadge to overlay small, informative icons on the corners of your nodes. This provides immediate visual feedback to the user, eliminating the need for them to open a separate log or details panel to see the node’s status.
6. Use SScrubWidget for Timeline Logic

KismetWidgets includes SScrubWidget, which is useful for any tool requiring a timeline or “slider” style scrubbing.

Tip: If your editor tool handles animation sequences or time-based data, use this widget to get a professional-looking “Playhead” interface. This helps you eliminate the effort of building a custom slider from scratch.
7. Standardize with SSearchBox (Kismet Style)

The module offers specialized variants of common widgets designed for the “My Blueprint” panel or “Context Menu.”

Best Practice: When building a custom search interface for an editor tab, look for the Kismet-specific wrappers. They often include built-in support for the engine’s “Filter” system, helping you eliminate manual string-filtering logic in your tool’s backend.
8. Reference Existing GraphNode Visuals

Most widgets in this module are intended to be used within an SGraphNode subclass.

Action: When overriding CreateNodeWidgetContent or AddPin, check how SKismetInspector or SGraphNodeKismetName are used in the engine source. Modeling your custom node’s layout after these helps you eliminate UI inconsistencies and makes your tool feel like a native part of Unreal Engine.