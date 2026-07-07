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

infrastructure for visual graph editors used in AI systems. It serves as the bridge between the visual nodes a designer sees in the Graph Editor and the actual runtime logic used by the AI systems.

While the AIModule handles runtime execution (the “brains”), AIGraph handles the visual representation and compilation of Behavior Trees and the Environment Query System (EQS). It defines how nodes are connected, how they are colored, and how properties are synchronized from the editor to the runtime objects.

Practical Usage Tips and Best Practices
1. Separate Editor and Runtime Logic

The most critical rule for this module is architectural separation.

Best Practice: Place any code inheriting from UAIGraph or UAIGraphNode inside an Editor Module. These classes should never be compiled into a shipping build, as they depend on editor-only libraries that do not exist in the runtime environment.
2. Configure Module Dependencies

If you are extending the Behavior Tree editor or creating a custom AI tool, you must add the module to your editor-specific Build.cs file.

C#
	// In YourProjectEditor.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { 

	        "AIGraph", 

	        "AIModule",

	        "GraphEditor",

	        "BlueprintGraph" 

	    });

	}

	```

	 

	#### 3. Inherit from UAIGraphNode for Custom AI Nodes

	To create a custom node that appears in the Behavior Tree editor with specialized visual properties (like custom colors or icons), you should inherit from `UAIGraphNode`.

	 

	```cpp

	#include "AIGraphNode.h"

	#include "MyCustomAINode.generated.h"

	 

	UCLASS()

	class MYEDITOR_API UMyCustomAIGraphNode : public UAIGraphNode

	{

	    GENERATED_BODY()

	 

	public:

	    // Overriding this allows you to link the editor node to a specific runtime object

	    virtual FText GetNodeTitle(ENodeTitleType::Type TitleType) const override;

	    

	    // Define the color of the node in the editor graph

	    virtual FLinearColor GetNodeTitleColor() const override { return FLinearColor::Red; }

	};

	```

	 

	#### 4. Manage Node Instancing Policy

	Unreal AI nodes are often **shared objects** (singleton-like) to save memory.

	*   **Best Practice:** If your custom AI node needs to store per-agent state (like a timer or a target reference), you must set `bCreateNodeInstance = true` in the runtime class, or better yet, use the **Node Memory** system (`GetInstanceMemorySize`) to avoid the overhead of full UObject instancing.

	 

	#### 5. Leverage the "Class Filter" for Custom Graphs

	If you are building a custom AI graph type, use `FGraphActionFilter` within your AIGraph implementation. This ensures that the right-click context menu only shows nodes relevant to your specific AI logic, preventing users from accidentally adding Behavior Tree tasks to an EQS graph.

	 

	#### 6. Synchronize Editor and Runtime Data

	Override `PostEditChangeProperty` in your `UAIGraphNode` to ensure that changes made by a designer in the visual graph are immediately reflected in the underlying runtime data asset. This is critical for maintaining a "What You See Is What You Get" (WYSIWYG) workflow for AI designers.

	 

	#### 7. Use AIGraph for Debugging Visualization

	The AIGraph module provides the hooks for **Visual Debugging**. You can extend `UAIGraphNode` to display runtime execution states (like "Running," "Succeeded," or "Failed") directly on the graph while the game is active. Use `GetDescription()` to provide dynamic, per-node debug text that appears in the editor during simulation.

	 

	#### 8. Modularize with Sub-Graphs

	For complex AI, don't create one massive graph. AIGraph supports sub-graphing.

	*   **Best Practice:** Use the `UBTTask_RunBehavior` (Behavior Tree) or similar patterns to keep graphs readable. In C++, ensure your `UAIGraph` implementation correctly handles nested graph instances to maintain a clean hierarchy.
Copy code
3. Customize Node Visuals

You can override GetNodeTitle and GetNodeTitleColor in your UAIGraphNode subclass to make specific AI tasks easier to identify.

Best Practice: Use distinct colors for different categories of AI logic (e.g., Green for sensing, Red for combat) to help designers navigate large Behavior Trees quickly.
4. Synchronize Runtime Data via PostEditChangeProperty

When a designer changes a value on a node in the graph, the changes must be pushed to the underlying runtime object (the UBTNode).

Best Practice: Override PostEditChangeProperty in your graph node to trigger a “re-compile” or data sync of the AI asset. This ensures that the logic executed in Play-In-Editor (PIE) matches the visual state of the graph.
5. Leverage the Connection Constraints

The AIGraph system allows you to define what can be connected to what.

Best Practice: Use CanCreateConnection to prevent invalid logic. For example, if you are building a custom graph, ensure a “Decorator” node cannot be connected directly to the “Root” without a “Composite” node in between. This helps eliminate user errors during the design phase.
6. Support Visual Debugging

The AIGraph module provides the hooks needed for the “red glow” or “flashing” effects seen during execution in the editor.

Best Practice: If creating a custom AI system, implement the GetDescription and GetRuntimeStatus functions. This allows the graph to display real-time variables (like current health or target names) directly on the node while the game is running.
7. Use Node Instancing Policy

AI nodes are often shared across many agents to save memory. However, if your node needs to store per-agent data, ensure your runtime class is configured to allow instances.

Best Practice: In your runtime node class, set bCreateNodeInstance = true. The AIGraph editor will respect this and handle the property editing for that specific instance correctly.
8. Implement Context Menu Filters

When right-clicking in an AI graph, the module uses a filtering system to show relevant nodes.

Best Practice: When extending the module, ensure your nodes are properly categorized using the Category metadata in the UCLASS macro. This prevents your custom AI nodes from cluttering unrelated graph types.