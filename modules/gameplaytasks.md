---
layout: default
title: GameplayTasks
---

<!-- ai-generation-failed -->

<h1>GameplayTasks</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/GameplayTasks/GameplayTasks.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, Engine, GameplayTags, GameplayTagsEditor, NetCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ting asynchronous, latent actions in Unreal Engine. It provides a robust alternative to standard Blueprint Latent Actions by offering a managed lifecycle and resource-based prioritization.

What it is and What it’s used for

Located in Runtime/GameplayTasks, this module is the foundational layer for the Gameplay Ability System (GAS)’s UAbilityTask, though it can be used independently. It consists of the UGameplayTask class and the UGameplayTasksComponent.

Primary uses include:

Managed Asynchronous Logic: Executing multi-frame operations like “Wait for Event,” “Move to Location,” or “Delay” that need to be tracked and potentially canceled.
Resource Conflict Resolution: Preventing two tasks from using the same “Resource” simultaneously (e.g., preventing an AI from “Walking” and “Sitting” at the same time if both require the “Legs” resource).
Stateful Operations: Handling logic that has a clear Beginning, Middle, and End, with the ability to trigger different execution paths (Success/Failure/Cancel) via delegates.
AI and Tooling: Implementing complex sequences in AI controllers or Editor tools that require persistent, managed state without the overhead of a full State Tree or Behavior Tree.
Practical Usage Tips and Best Practices
1. Implement the Static Factory Pattern

To expose a task as a latent node in Blueprints, you must implement a static factory function in your UGameplayTask subclass. Use NewInternalTask<T> or NewAbilityTask<T> (if using GAS) to instantiate the task. This ensures the system registers the task correctly with the owner’s component.

2. Always Explicitly Call EndTask()

A Gameplay Task will remain in memory and potentially continue its internal logic until EndTask() is called. Failing to do so results in “phantom logic” and memory leaks. Once EndTask() is invoked, the task is marked for the elimination of its references, allowing the Garbage Collector to clean it up.

3. Use Resources to Prevent Overlap

Define UGameplayTaskResource classes to represent shared systems (e.g., ULegsResource). If a task claims a resource, any new task attempting to claim that same resource can automatically cancel the existing one based on priority, ensuring the elimination of conflicting state bugs.

4. Avoid Tick for Better Performance

While UGameplayTask supports ticking, it is a best practice to avoid it. Instead, use Delegates, Timers, or Latent Wait functions. This ensures your task only consumes CPU cycles when a relevant event occurs, keeping the engine’s main tick loop efficient.

5. Use Dynamic Multicast Delegates for Outputs

To create multiple execution pins on a Blueprint node (like “OnSuccess” or “OnInterrupted”), define UPROPERTY(BlueprintAssignable) dynamic multicast delegates. Broadcast these delegates within your C++ logic to drive the flow of the Blueprint graph.

6. Bind to the UGameplayTasksComponent

Any Actor intended to run these tasks must possess a UGameplayTasksComponent and implement the IGameplayTaskOwnerInterface. This component acts as the central manager that handles the replication, ticking, and cleanup of all active tasks for that Actor.

7. Override OnDestroy for Safety

If your task manages external resources (like spawning temporary actors or attaching components), override the OnDestroy function. This function is called regardless of how the task ends (via EndTask, cancellation, or Actor destruction), making it the safest place for cleanup logic.

8. Strategic Elimination of Task Bloat

Tasks are UObjects and carry more overhead than a simple timer. Use UGameplayTasks for logic that requires state management, cancellation, or networking. For trivial logic like a one-off frame delay, a simple timer or a Blueprint Delay node is often more performant.