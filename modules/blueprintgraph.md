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

e visual representation, node logic, and compilation preparation of Blueprint graphs. While the Engine module handles the runtime execution of Blueprints (via bytecode), BlueprintGraph manages the “Visual Scripting” interface—handling nodes (UEdGraphNode), pins (UEdGraphPin), and the translation of these visual elements into executable logic via the Kismet Compiler.

It is primarily used by tools and engine developers to create Custom K2Nodes, which allow for complex behavior (like async actions, wildcards, or dynamic pin generation) that standard BlueprintCallable functions cannot achieve.

1. Module Configuration

Because this is an editor-only module, it must be placed within an Editor module in your project and wrapped in #if WITH_EDITOR blocks. Include it in your Build.cs:

C#
	if (Target.bBuildEditor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "BlueprintGraph", "KismetCompiler", "UnrealEd" });

	}

	```

	 

	### 2. Practical Usage Tips & Best Practices

	 

	#### Prefer UK2Node Over UEdGraphNode

	While `UEdGraphNode` is the base for all visual nodes, always derive from **`UK2Node`** when extending Blueprints. `UK2Node` provides the specific hooks needed for the Kismet compiler, such as `ExpandNode`, which allows you to replace a single visual node with a complex network of internal function calls during compilation.

	 

	#### Master the `ExpandNode` Workflow

	The most powerful feature of this module is `UK2Node::ExpandNode`. Use this to "explode" a user-friendly node into a set of hidden, low-level nodes. This "eliminates" the need to write complex runtime C++ for every minor variation of a node; instead, you can re-use existing `BlueprintCallable` functions as the "backend" for your custom visual node.

	 

	#### Use `GetMenuActions` for Node Discovery

	To make your custom node appear in the Blueprint right-click menu, override `GetMenuActions`. Avoid the older `GetMenuEntries` style. The `FBlueprintActionDatabaseRegistrar` allows you to register your node under specific categories and even dynamically generate multiple versions of a node based on loaded assets or classes.

	 

	#### Implement `NotifyPinConnectionListChanged`

	If your node needs to change its behavior based on what is connected (e.g., a "Format String" node that adds pins as you connect variables), override `NotifyPinConnectionListChanged`. This allows you to dynamically call `CreatePin` or `RemovePin` to update the node’s UI in real-time, "eliminating" the need for users to manually refresh the node.

	 

	#### Validate with `GetCompilerMessages`

	To provide a good user experience, use `GetCompilerMessages` to surface errors or warnings directly on the node (e.g., "This node requires a valid Target"). This allows the Blueprint compiler to catch logical errors before the game even runs, "eliminating" difficult-to-trace runtime crashes.

	 

	#### Leverage `UEdGraphSchema_K2` Constants

	When creating pins manually in C++, never hard-code string types like `"float"` or `"exec"`. Instead, use the constants defined in `UEdGraphSchema_K2`, such as `UEdGraphSchema_K2::PC_Boolean` or `UEdGraphSchema_K2::PC_Exec`. This ensures your node remains compatible with future engine updates and avoids "pin type mismatch" errors.

	 

	#### Handle "Wildcard" Pins Correctly

	If creating a node that accepts any type (like a "Print" node for any variable), use the `PC_Wildcard` type. You must then implement `NotifyPinConnectionListChanged` to "resolve" the wildcard type to the type of the connected pin, ensuring that the Kismet compiler can correctly generate the bytecode for the specific data type.

	 

	#### Keep Nodes "Pure" Where Possible

	If your node only performs calculations and has no side effects, override `IsNodePure` to return `true`. This "eliminates" the need for execution (white) pins, making the Blueprint graph much cleaner and allowing the compiler to optimize the node's execution timing.
Copy code
2. Practical Usage Tips & Best Practices
Inherit from UK2Node, Not UEdGraphNode

For gameplay logic, always derive your custom nodes from UK2Node. While UEdGraphNode defines the visual box on the screen, UK2Node provides the specific hooks needed for the Kismet compiler. Most importantly, it gives you access to ExpandNode, which is where the “magic” of custom Blueprints happens.

Master the ExpandNode Workflow

The ExpandNode function is the core of custom node development. It allows you to “explode” a single user-friendly node into a hidden network of standard function calls during compilation. Use this to “eliminate” the need for users to wire up complex boilerplate code; the user sees one node, but the compiler sees a robust sequence of events.

Use GetMenuActions for Node Discovery

To make your custom node appear in the Blueprint right-click menu, override GetMenuActions. Avoid the older legacy methods. The FBlueprintActionDatabaseRegistrar allows you to register your node under specific categories and even dynamically generate different versions of the node based on loaded assets.

Implement Dynamic Pin Logic

If your node needs to change based on user input (e.g., a “Format String” node that adds pins as the user types {0}, {1}), override AllocateDefaultPins and ReallocatePinsDuringReconstruction. This allows the node to “eliminate” unused pins and keep the graph clean and readable.

Provide Compiler Feedback

Use GetCompilerMessages to surface errors or warnings directly on the node during the compile phase (e.g., “Missing Target input” or “Class type mismatch”). This allows the developer to fix issues before the game even runs, “eliminating” the need for difficult runtime debugging.

Use Schema Constants for Pin Types

When creating pins in C++, never hard-code strings like "bool" or "exec". Instead, use the constants defined in UEdGraphSchema_K2, such as UEdGraphSchema_K2::PC_Boolean or UEdGraphSchema_K2::PC_Exec. This ensures your custom nodes remain compatible with future engine updates.

Resolve Wildcard Pins Correctly

If you use PC_Wildcard to create a node that accepts any data type (like a “Print” node for any variable), you must implement NotifyPinConnectionListChanged. This logic should “resolve” the wildcard by changing the pin’s type to match whatever the user just plugged into it.

Flag “Pure” Nodes to Clean Graphs

If your node only performs calculations and has no side effects, override IsNodePure to return true. This “eliminates” the white execution pins on the node, making the Blueprint graph significantly easier to read and allowing the compiler to optimize when the node is actually called.