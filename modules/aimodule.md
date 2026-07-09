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

intelligence logic, decision-making, and sensory perception. It provides the infrastructure for non-player characters (NPCs) to observe their environment, process information, and execute complex behaviors.

It is primarily used to implement Behavior Trees, AI Controllers, the Environment Query System (EQS), and AI Perception. While the Engine module handles basic movement, the AIModule provides the “brain” that tells the Agent where to move and why.

1. Module Configuration

To use AI classes in C++, you must add the module to your Build.cs file. Many developers forget this step and encounter linker errors when referencing AAIController or UBehaviorTree.

C#
	// MyProject.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "AIModule" });
Copy code
2. Practical Usage Tips & Best Practices
Prefer AI Perception over Pawn Sensing

The UAIPerceptionComponent is the modern, optimized replacement for the legacy UPawnSensingComponent. It is event-driven and supports multiple senses (Sight, Hearing, Damage, etc.) within a single component. It also handles “forgetting” stimuli over time, which is essential for realistic AI behavior.

Decouple Logic via the Blackboard

Always use a Blackboard to share data between C++ and Behavior Trees. Avoid hard-coding logic that checks variables directly on the Pawn. By updating Blackboard keys (like TargetActor or IsAlerted), you allow the Behavior Tree to react via Decorators without constant polling, which is significantly more performant.

Use Decorators instead of Service Polling

New developers often use BT Services to check conditions every tick. This is expensive. Instead, use Decorators with “Observer Aborts” set to Both or Self. This ensures the AI only changes its behavior when a Blackboard value actually changes, effectively “eliminating” unnecessary tick costs.

Handle Pawn Elimination Gracefully

When an AI-controlled Pawn is destroyed, the AAIController can remain in the world, leading to memory leaks or logic errors.

Best Practice: Always call UnPossess() on the controller during the “elimination” sequence and ensure the controller is either destroyed or returned to a pool.
Offload Heavy Logic to EQS

If your AI needs to find the “best” cover point or a valid flanking position, do not run these calculations in a standard Blueprint loop. Use the Environment Query System (EQS). EQS runs asynchronously across frames, preventing the game from hitching when multiple AI agents are searching for paths simultaneously.

Utilize Pathfollowing Components

If you need custom movement logic (like climbing or jumping), don’t rewrite the movement system. Instead, create a custom UPathFollowingComponent. This allows you to intercept navigation points and inject custom logic while still benefiting from the engine’s built-in pathfinding and avoidance (RVO/Detour Crowd).

Limit “Tick” in AI Controllers

AI Controllers are Actors and can tick, but they rarely should. Most AI logic should be triggered by Perception updates or Behavior Tree timers. If you must use a tick, set a high TickInterval (e.g., 0.1s or 0.2s) to reduce the CPU overhead when scaling to large numbers of NPCs.

Use “Claimed” Resources with Smart Objects

For world interactions (like sitting on a chair or using a console), combine the AIModule with the Smart Objects plugin. This prevents multiple AI agents from trying to use the same object simultaneously, “eliminating” the visual bug of NPCs overlapping at the same interaction point.