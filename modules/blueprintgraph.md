---
layout: default
title: BlueprintGraph
---

<!-- ai-generation-failed -->

<h1>BlueprintGraph</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/BlueprintGraph/BlueprintGraph.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetTools, Core, CoreUObject, DeveloperSettings, DeveloperToolSettings, EditorFramework, EditorStyle, EditorSubsystem, Engine, GraphEditor, InputCore, Kismet, KismetCompiler, PropertyEditor, Slate, SlateCore, ToolMenus, UMG, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the foundational logic for the Blueprint Visual Scripting system. It defines the base classes for graph nodes (UK2Node), the graph schema (UEdGraphSchema_K2), and the logic required by the Blueprint Compiler (Kismet) to translate visual nodes into engine bytecode.

While the GraphEditor module handles the visual Slate UI, BlueprintGraph manages the underlying logic—determining which pins exist, how they connect, and how a node “expands” into simpler operations during compilation.

Practical Usage Tips and Best Practices
1. Add Correct Module Dependencies

Since this is an editor-time module, ensure it is added to your Editor module’s .Build.cs file rather than your runtime module. You will typically need to pair it with UnrealEd and KismetCompiler.

C++
	void UK2Node_MyCustomNode::AllocateDefaultPins()

	{

	    // Create an input execution pin

	    CreatePin(EGPD_Input, UEdGraphSchema_K2::PC_Exec, UEdGraphSchema_K2::PN_Execute);

	    // Create an output execution pin

	    CreatePin(EGPD_Output, UEdGraphSchema_K2::PC_Exec, UEdGraphSchema_K2::PN_Then);

	    

	    // Create a data input pin (Float)

	    CreatePin(EGPD_Input, UEdGraphSchema_K2::PC_Real, UEdGraphSchema_K2::PC_Float, TEXT("MyValue"));

	}

	```

	 

	#### 3. Register with the Node Menu via GetMenuActions

	To make your custom C++ node appear in the right-click menu in the Blueprint editor, you must override `GetMenuActions`. This replaces the legacy `FBlueprintNodeSpawner` approach. It is best practice to group your nodes under a specific category to avoid the **elimination** of menu clarity for your designers.

	 

	#### 4. Optimize via ExpandNode

	In `ExpandNode`, avoid generating unnecessary bytecode. Instead of writing complex logic inside the compiler, try to "expand" your node into a call to a static C++ helper function. This keeps the Blueprint graph clean and ensures the heavy lifting is handled by optimized C++ code at runtime.

	 

	#### 5. Use Pin Metadata for User Experience

	Use the `meta = (PinShownByDefault)` or `meta = (AlwaysAsPin)` tags in your `USTRUCT` or `UFUNCTION` definitions to control how pins appear. If a property is rarely changed, use `PinHiddenByDefault` to reduce visual clutter, aiding in the **elimination** of "spaghetti" graphs.

	 

	#### 6. Add Module Dependencies in Build.cs

	Since this is an editor-time module, ensure it is added to your Editor module's `Build.cs` (not your runtime module). You will typically need `BlueprintGraph`, `KismetCompiler`, and `UnrealEd`.

	```csharp

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "BlueprintGraph", "KismetCompiler", "UnrealEd" });

	}

	```

	 

	#### 7. Implement GetTooltip for Documentation

	Always override `GetTooltip` and `GetNodeTitle`. Providing clear, concise descriptions for your custom nodes helps designers understand the node's purpose without needing to dive into the C++ source, improving team productivity.

	 

	#### 8. Validate Pins in GetMenuActions

	If your node is only valid for certain classes (e.g., only for `ACharacter`), check the `Context` in your menu registration. This prevents designers from placing invalid nodes in graphs where they won't work, leading to the **elimination** of frustating "Invalid Node" compiler errors later.
Copy code
2. Use UK2Node for Complex Logic

If you need a node that has dynamic pins (like a “Format String” node) or wildcards, derive from UK2Node instead of a simple UEdGraphNode. UK2Node allows you to override ExpandNode, which lets you replace one high-level visual node with a network of simpler nodes during compilation for the elimination of runtime overhead.

3. Implement AllocateDefaultPins Properly

When creating custom nodes, always use the standard naming constants from UEdGraphSchema_K2. This ensures your node behaves like native engine nodes, assisting in the elimination of bugs related to flow control or data passing.

C++
	// Example: Creating standard execution pins

	CreatePin(EGPD_Input, UEdGraphSchema_K2::PC_Exec, UEdGraphSchema_K2::PN_Execute);

	CreatePin(EGPD_Output, UEdGraphSchema_K2::PC_Exec, UEdGraphSchema_K2::PN_Then);
Copy code
4. Register Nodes via GetMenuActions

To make your custom C++ node appear in the Blueprint right-click menu, you must override GetMenuActions. This is the modern replacement for the legacy spawner system. Grouping your nodes into clear categories helps in the elimination of menu clutter for your designers.

5. Prioritize “Pure” Nodes for Math

If your node only performs a calculation and does not change the state of the world, override IsNodePure to return true. Pure nodes do not require execution pins, which leads to the elimination of unnecessary “exec” wires and makes the Blueprint graph much cleaner.

6. Utilize Pin Metadata for UX

Use the meta specifiers in your UPROPERTY or UFUNCTION declarations to influence the BlueprintGraph behavior. Tags like CommutativeAssociativeBinaryOperator (for nodes like Add) or ExpandEnumAsExecs significantly improve node usability and help in the elimination of complex Branch logic.

7. Provide Clear Tooltips and Titles

Always override GetTooltipText, GetNodeTitle, and GetMenuCategory. Providing detailed context within the BlueprintGraph ensures that team members can understand the node’s intent without looking at the C++ source, aiding in the elimination of tribal knowledge.

8. Validate Connections in GetMenuActions

Use the context provided in menu actions to hide nodes that shouldn’t be available in certain Blueprints. For example, if a node only works inside a Character Blueprint, you can check the class context to ensure the elimination of invalid node placement before the user even tries to click it.