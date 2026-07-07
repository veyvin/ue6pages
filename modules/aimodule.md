---
layout: default
title: AIModule
---

<!-- ai-generation-failed -->

<h1>AIModule</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/AIModule/AIModule.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AutoRTFM, Core, CoreUObject, EditorFramework, Engine, GameplayTags, GameplayTasks, InputCore, NavigationSystem, Navmesh, RHI, RenderCore, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

lligent agent behaviors and automated decision-making. It provides the essential infrastructure that separates an NPC’s “brain” (logic) from its “body” (the Pawn or Character).

This module is primarily used to handle high-level navigation, environmental perception, and complex logic flow through dedicated assets like Behavior Trees and the Environment Query System (EQS).

Practical Usage Tips and Best Practices
1. Add Module Dependencies

To use AI classes in C++, you must explicitly include the module in your project’s Build.cs file. Without this, the linker will fail to find standard classes like AAIController.

C#
	// In YourProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "AIModule" });

	```

	 

	#### 2. Prioritize AI Perception over PawnSensing

	Avoid the legacy `UPawnSensingComponent`. Use the **AIPerceptionComponent** for modern AI. It is event-driven, more optimized, and supports multiple senses (Sight, Hearing, Damage, Prediction) within a single unified system. 

	*   **Best Practice:** Use `OnTargetPerceptionUpdated` to react to changes rather than checking visibility in `Tick()`.

	 

	#### 3. Keep Logic in C++, Structure in Behavior Trees

	While you can write logic in Blueprint nodes, complex math or heavy loops should be implemented as C++ **BTTaskNodes** or **BTDecorators**.

	*   Use the **Behavior Tree Editor** to visualize the high-level decision flow (e.g., "Should I flee or fight?").

	*   Use **C++ Tasks** to execute the granular actions (e.g., "Calculate best flanking position").

	 

	#### 4. Leverage the Environment Query System (EQS)

	Avoid manually iterating through arrays of actors to find the "best" target or cover point. **EQS** allows you to "ask" the environment questions (e.g., "Find a point within 1000 units that has line-of-sight to the player but is hidden from the sniper").

	*   **Performance Tip:** EQS queries can be expensive; run them at lower frequencies or use the "Run EQS Query" task in a Behavior Tree with a cooldown.

	 

	#### 5. Use Blackboard Keys for State, Not Logic

	The **Blackboard** should act as the AI's "short-term memory." Store data like `TargetActor`, `DestinationVector`, or `IsPanicked`. 

	*   **Best Practice:** Avoid storing complex structures. Stick to basic types or `UObject*` pointers. Use **Blackboard Decorators** (Conditionals) to interrupt behavior branches immediately when a value changes.

	 

	#### 6. Optimize NavMesh with Modifiers

	Don't rely solely on static geometry for navigation. Use **Nav Modifier Volumes** to increase the "cost" of certain areas (like fire or mud) without blocking them entirely. 

	*   **C++ Tip:** Use `UNavigationPath` to manually inspect or manipulate paths if your AI needs custom steering logic beyond simple "MoveTo" commands.

	 

	#### 7. Override OnPossess for Initialization

	When an AI Controller takes control of a Pawn, use the `OnPossess` override in C++ to initialize your Behavior Tree and Blackboard. This ensures the "brain" is synced with the "body" as soon as it enters the world.

	```cpp

	void AMyAIController::OnPossess(APawn* InPawn)

	{

	    Super::OnPossess(InPawn);

	    if (AMyCharacter* MyChar = Cast<AMyCharacter>(InPawn))

	    {

	        RunBehaviorTree(MyChar->BehaviorTreeAsset);

	    }

	}

	```

	 

	#### 8. Utilize the AI Debugger

	Press the **' (apostrophe)** key during gameplay to activate the AI Debugger. It provides a real-time overlay showing:

	*   The active Behavior Tree branch.

	*   Perception ranges and detected stimuli.

	*   EQS query results (represented by colored spheres).

	*   Current Pathfinding routes.
Copy code
2. Prioritize AI Perception over PawnSensing

Use the UAIPerceptionComponent instead of the legacy UPawnSensing. The AI Perception system is more optimized, supports multiple senses (Sight, Hearing, Damage) in one place, and works seamlessly with the AI Debugger.

3. Keep Heavy Logic in C++ Tasks

While Behavior Trees are visual, you should implement complex math or expensive searches as C++ classes inheriting from UBTTaskNode. Use the tree to manage the high-level state, but let C++ handle the heavy lifting to ensure high performance.

4. Leverage the Environment Query System (EQS)

Use EQS to eliminate hard-coded “find target” logic. EQS allows the AI to “ask” questions about the world (e.g., “Which cover point is furthest from the player but still has a line of sight?”). It is much more flexible than manual raycasting and array sorting.

5. Utilize the AI Debugger

During gameplay, press the ’ (apostrophe) key to open the AI Debugger. It provides a real-time overlay showing current Behavior Tree nodes, Blackboard values, and perception stimuli. It is the fastest way to diagnose why an agent is stuck or behaving unexpectedly.

6. Optimize Navigation with Nav Modifiers

Instead of constantly rebuilding the NavMesh, use Nav Modifier Volumes. These allow you to change the “cost” of traversing certain areas (like making AI prefer sidewalks over mud) or dynamically block areas without the performance hit of a full mesh rebuild.

7. Implement Correct Elimination Logic

When an agent is defeated, ensure the AI Controller is properly unpossessed and its logic is paused. Use BrainComponent->StopLogic() to ensure the Behavior Tree stops running immediately upon the elimination of the pawn, preventing “ghost” logic from executing on a non-existent actor.

8. Use Blackboard Decorators for Interruption

Use Blackboard Decorators as observers to interrupt lower-priority tasks. For example, if a TargetActor value on the Blackboard is cleared (indicating the target was eliminated), the decorator can instantly abort a “MoveTo” task and return the AI to an idle state.