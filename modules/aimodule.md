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

n-player character (NPC) intelligence and decision-making. It serves as the bridge between raw Actors and complex behaviors by providing the logic for sensing the world, navigating environments, and executing tactical decisions.

It is primarily used to implement AIControllers, Behavior Trees, Blackboards, AI Perception, and the Environment Query System (EQS).

Practical Usage Tips and Best Practices
1. Configure Module Dependencies

To use AI classes in C++, you must add the module to your [Project].Build.cs file. Many developers forget this, leading to linker errors when referencing AAIController or UBehaviorTreeComponent.

C#
PublicDependencyModuleNames.AddRange(new string[] { "AIModule", "NavigationSystem", "GameplayTasks" });
Copy code
2. Prefer AI Perception over Pawn Sensing

The UAIPerceptionComponent is the modern, optimized standard for NPC senses. Unlike the legacy Pawn Sensing, AI Perception is data-driven, supports multiple senses (Sight, Hearing, Damage, etc.) in one component, and is more performance-efficient when handling large numbers of agents.

3. Keep Logic Out of the AIController

The AAIController should act as a manager that runs the Behavior Tree and handles high-level possession logic. Avoid putting complex “if/else” logic or movement math directly in the controller’s Tick. Instead, use BTTasks for actions and BTDecorators for conditionals to keep your AI modular and debuggable.

4. Use the Gameplay Debugger

Press the ’ (apostrophe) key during Play-In-Editor (PIE) to activate the Gameplay Debugger. This tool provides a real-time overlay showing the AI’s current Behavior Tree state, Blackboard values, Perception stimuli, and NavMesh paths. It is essential for diagnosing why an AI failed to find a target.

5. Optimize via Behavior Tree Services

Instead of using Tick in your C++ classes, use UBTService nodes. Services execute at defined intervals (e.g., every 0.5 seconds) to update Blackboard data. This significantly reduces CPU overhead compared to every-frame logic.

6. Leverage the Environment Query System (EQS)

For complex positioning—such as finding the best cover spot or a flank position—use EQS. It allows the AI to “test” the world by spawning items (points/grids) and scoring them based on distance, visibility, or custom criteria, preventing hard-coded movement logic.

7. Handle Actor Elimination Correctly

When an AI-controlled Pawn undergoes elimination, ensure the AAIController is properly handled. Use UnPossess() and consider calling BrainComponent->StopLogic() to ensure the Behavior Tree stops executing. Failing to do this can lead to “ghost” AI logic attempting to move or attack from a destroyed Pawn.

8. Use Pathfollowing Components for Custom Movement

If your AI needs custom movement (like jumping or climbing), inherit from UPathFollowingComponent. This allows you to intercept movement segments and inject custom logic when the AI reaches a specific NavLink, ensuring they don’t get stuck on complex geometry.