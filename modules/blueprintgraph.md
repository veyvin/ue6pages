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

foundational classes for creating and managing Blueprint node graphs. It defines the logic for how nodes are represented visually, how pins are connected, and—most importantly—how high-level visual nodes are translated into executable code via the K2Node system.

This module is used by developers to create custom Blueprint nodes, manage graph schemas (rules for what can connect to what), and extend the Blueprint editor’s functionality. It serves as the bridge between the visual representation in the editor and the underlying K2VM (Kismet 2 Virtual Machine) or C++ backend.

Practical Usage Tips and Best Practices
1. Implement Custom Logic via K2Nodes

If you need a Blueprint node that does more than a simple function call (such as a node with dynamic pins, multiple output execution paths, or specialized context menus), you must derive from UK2Node. This class, found within the BlueprintGraph module, allows you to define complex behavior during the Blueprint compilation process.

2. Manage Module Dependencies

Because BlueprintGraph is an editor module, it should only be included in an Editor type module within your .uplugin or .uproject file. In your Build.cs, wrap it in an editor check to ensure your runtime builds remain optimized and free of editor-only code:

C#
	if (Target.bBuildEditor)

	{

	    PrivateDependencyModuleNames.Add("BlueprintGraph");

	}
Copy code
3. Use ExpandNode for Code Generation

When creating a UK2Node, the most critical function is ExpandNode. Instead of writing complex runtime logic, use this function to perform the elimination of the custom node by replacing it with a network of simpler, standard nodes (like function calls or variable accesses) during compilation. This ensures your custom node is “compiled away” into efficient bytecode.

4. Override GetMenuActions for Discoverability

To ensure your custom nodes appear correctly in the Blueprint context menu, override the GetMenuActions function. This allows you to specify the category, tooltip, and keywords for your node, making it easier for designers to find and use your custom tools.

5. Enforce Safety with Pin Connection Rules

Use the UK2Node::GetMenuEntries and CanCreateConnection methods to enforce strict rules on what can be wired together. This prevents users from creating invalid graph logic, leading to the elimination of common runtime crashes caused by passing incorrect data types through the graph.

6. Utilize Pin Metadata for UI

You can use metadata specifiers within your node’s pin definitions to change how they look. For example, using PC_Object or PC_Struct ensures the pins are color-coded correctly (blue for objects, light blue for structs), which helps maintain visual consistency with the rest of Unreal Engine’s built-in nodes.

7. Optimize Compilation via Early Validation

Override ValidateNodeDuringCompilation to catch errors early. By providing clear compiler warnings or errors within the Blueprint editor, you help developers fix issues before they ever hit “Play,” effectively resulting in the elimination of bugs that would otherwise only appear at runtime.

8. Prefer BlueprintPure for Data Nodes

If your custom node only performs a calculation and does not change the state of the world, mark it as “Pure” by overriding IsNodePure. This tells the BlueprintGraph system that the node does not need execution pins, allowing for a cleaner and more flexible graph layout for mathematical or data-retrieval operations.