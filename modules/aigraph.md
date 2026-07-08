---
layout: default
title: AIGraph
---

<!-- ai-generation-failed -->

<h1>AIGraph</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AIGraph/AIGraph.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIModule, ApplicationCore, BlueprintGraph, Core, CoreUObject, EditorFramework, EditorStyle, Engine, GraphEditor, InputCore, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

specialized framework for creating and managing node-based AI graphs. It serves as the bridge between the generic UnrealEd Graph Editor and AI-specific runtime assets, such as Behavior Trees and Environment Query System (EQS) assets.

While the runtime logic is handled by the AIModule, the AIGraph module is responsible for the visual representation, connection logic, node categorization, and the synchronization of graph pins with the underlying data objects.

Practical Usage Tips and Best Practices
Strict Editor Module Scoping Since AIGraph depends on UnrealEd and GraphEditor, it must only be included in an Editor module. Including it in a runtime module will lead to “elimination” of your build process during packaging for consoles or mobile.
C++
	// YourProjectEditor.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AIGraph", "GraphEditor", "UnrealEd" });

	}

	```

	 

	#### 2. Synchronize Visual Nodes with Runtime Data

	A common pattern in `AIGraph` is that a `UAIGraphNode` acts as a "visual wrapper" for a runtime `UObject` (like a `UBTNode`). Always use `PostEditChangeProperty` or custom delegates to ensure changes made in the graph's Details panel are immediately reflected in the runtime instance stored within the Asset.

	 

	#### 3. Override `GetNodeTitle` and `GetDescription`

	To provide a professional UX, always override these functions in your `UAIGraphNode` subclass.

	*   **`GetNodeTitle`**: Should show the node's name and potentially key state (e.g., "MoveTo: [TargetLocation]").

	*   **`GetDescription`**: Use this to provide a multi-line summary of the node's logic, which appears inside the node body in the editor.

	 

	#### 4. Use Built-in Error Reporting

	`UAIGraphNode` includes an `ErrorMessage` string and `ErrorType` integer. If a node configuration is invalid (e.g., a required property is null), set these variables during the graph's compilation or `ReconstructNode` phase. This automatically renders an error icon and tooltip on the node for the designer.

	 

	#### 5. Handle Sub-nodes (Decorators and Services)

	If you are extending the Behavior Tree editor, remember that `AIGraph` supports "Sub-nodes." These are nodes that are visually attached to a parent node (like Decorators). Use the `SubNodes` array within `UAIGraphNode` to manage these relationships rather than standard pins if the logic is hierarchical rather than flow-based.

	 

	#### 6. Optimize Pin Management

	AI graphs often have specialized pin types (e.g., Boolean decorators vs. Execution flow). Use a custom `UAIGraphSchema` to define which pins can connect to each other. This prevents designers from creating invalid logic flows that would otherwise crash the runtime AI controller.

	 

	#### 7. Leverage `PostPlaced` for Initialization

	When a user drags a new AI node into the graph, use the `PostPlaced()` override to set up default values or auto-generate required sub-objects. This ensures the runtime object is correctly instantiated and linked to the visual node from the moment of creation.

	 

	#### 8. Use Metadata for Categorization

	When registering custom AI nodes, use the `Category` and `Tooltip` metadata in the `UCLASS` macro. The `AIGraph` node-picker uses these to group nodes, making it easier for designers to find your custom tools within the context menu.
Copy code
Override Visual Descriptions Always override UAIGraphNode::GetNodeTitle() and UAIGraphNode::GetDescription(). For custom AI nodes, displaying dynamic information (like a “Target Location” variable name) directly on the node body significantly improves the workflow for designers.
Leverage Sub-Node Systems The AIGraph module supports “Sub-nodes” (used for Decorators and Services in Behavior Trees). If you are building a custom graph tool, use the SubNodes array within UAIGraphNode to attach conditional logic directly to a node rather than creating messy pin-based spaghetti.
Synchronize via PostEditChangeProperty When a user modifies a value in the Details panel of an AI Graph Node, use PostEditChangeProperty to ensure the underlying runtime UObject is updated immediately. This ensures the visual graph and the actual AI logic remain in parity.
Implement Custom Error Reporting Use the built-in ErrorMessage and ErrorType variables in UAIGraphNode. If a designer connects nodes in an invalid way (e.g., an “Elimination” task with no target), you can set these variables to display a red error icon and tooltip directly on the node.
Utilize Context Menu Filtering When creating custom nodes, use the Category metadata in the UCLASS macro. The AIGraph schema uses this to organize the right-click context menu, which is essential for maintaining a clean workspace in complex AI projects.
Manage Pin Connections via Schema Instead of allowing any connection, create a custom UAIGraphSchema. This allows you to define strict rules on which pins can connect, preventing designers from accidentally plugging an EQS query into a Behavior Tree flow.
Use PostPlaced for Initialization Override the PostPlaced() function to automatically instantiate required sub-objects or default settings when a node is dragged into the graph. This reduces manual setup time and ensures that the runtime object is always correctly initialized.