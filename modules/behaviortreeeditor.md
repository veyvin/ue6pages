---
layout: default
title: BehaviorTreeEditor
---

<!-- ai-generation-failed -->

<h1>BehaviorTreeEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/BehaviorTreeEditor/BehaviorTreeEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIGraph, AIModule, ApplicationCore, AssetDefinition, Core, CoreUObject, EditorStyle, EditorWidgets, Engine, GameplayTags, GraphEditor, InputCore, KismetWidgets, PropertyEditor, RewindDebuggerInterface, Slate, SlateCore, ToolMenus, TraceServices, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

.

It is used primarily by designers and technical artists to script complex agent behaviors—such as patrolling, combat positioning, and decision-making—through a hierarchical structure of Composites, Decorators, and Tasks.

Practical Usage Tips and Best Practices
1. Leverage the “Blackboard View” for Debugging

While a Behavior Tree is running in Play-In-Editor (PIE), the Behavior Tree Editor displays real-time execution flow. Use the Blackboard tab inside the editor to watch values change dynamically. This is the most effective way to see if a branch is failing because a specific key (like TargetActor) was “eliminated” or never set.

2. Utilize Composite Decorators

Instead of nesting multiple branches with simple “Is Set” checks, use the Composite Decorator. This node allows you to combine multiple Blackboard conditions using AND/OR logic within a single blue node. This keeps your graph clean and prevents “spaghetti” logic that is difficult to read.

3. Custom Node Icons and Colors

If you are creating custom C++ Tasks or Decorators, override the GetNodeIconName or GetNodeCategory functions. Giving your custom nodes distinct icons and colors helps team members quickly identify specialized logic (e.g., combat nodes in red, movement in green), reducing the time spent parsing the graph.

4. Node Instancing Policy (Performance)

By default, Behavior Tree nodes are shared across all agents to save memory. However, if your Task needs to store agent-specific data (like a timer or a local target), set bCreateNodeInstance = true in your C++ constructor. Be careful: overusing instanced nodes on hundreds of agents can lead to performance “elimination” due to high memory overhead.

5. Preferred Path: Struct-Based Memory

For high-performance tasks, avoid bCreateNodeInstance and instead use Node Memory. Override GetInstanceMemorySize() to allocate a small struct. This allows you to store per-agent variables in a single contiguous block of memory, which is much faster than creating unique UObject instances for every AI.

6. Use Service Nodes for Optimization

Instead of using a Task to constantly check a condition (which can be expensive), use a Service node attached to a Composite. Services run at a defined interval (e.g., every 0.5 seconds). This is the best practice for updating the Blackboard with “Search” or “Sense” data without ticking the entire AI logic every frame.

7. Clean Up with Subtrees

For complex AI, the main graph can become unmanageable. Use the Run Behavior task to reference other Behavior Tree assets as subtrees. This promotes modularity and allows you to reuse common logic—like “Find Cover” or “Patrol Path”—across different enemy types without duplicating nodes.

C++ Node Implementation Checklist

When extending the Behavior Tree Editor with custom C++ nodes, ensure you follow these standards:

BTTask_Custom.h

C++
	UCLASS()

	class MYGAME_API UBTTask_Custom : public UBTTaskNode

	{

	    GENERATED_BODY()

	 

	    virtual EBTNodeResult::Type ExecuteTask(UBehaviorTreeComponent& OwnerComp, uint8* NodeMemory) override;

	    

	    // Use this for per-agent variables without instancing the whole node

	    virtual uint16 GetInstanceMemorySize() const override { return sizeof(FMyCustomMemory); }

	 

	    UPROPERTY(EditAnywhere, Category = "Config")

	    struct FBlackboardKeySelector TargetKey;

	};
Copy code
Performance & Best Practices
Avoid Tick: Never use ReceiveTick in Blueprint Tasks if an event-driven approach (like a Decorator observer) can work instead.
Blackboard Observers: Use Decorators with the “Observer Aborts” setting set to “Both” or “Self” to immediately “eliminate” a running task when a condition changes (e.g., the player is no longer visible).
Search Tags: When creating custom nodes, use the Meta = (ToolTip = "...") specifier in the UCLASS macro. The Behavior Tree Editor’s context menu uses these for the search filter, making your tools easier for designers to find.