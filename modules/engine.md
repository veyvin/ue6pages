---
layout: default
title: Engine
---

<!-- ai-generation-failed -->

<h1>Engine</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Engine/Engine.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, ClothingSystemEditorInterface, ClothingSystemRuntimeInterface, DesktopPlatform, DeveloperToolSettings, EditorToolEvents, IoStoreOnDemand, PerfCounters</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ay framework. It defines the core building blocks of any experience, including the base classes for Actors, Components, Levels, and Worlds. It acts as the “glue” between low-level systems (like Rendering and Physics) and high-level gameplay logic.

If a feature is essential to the existence of an object in the 3D world—such as its transform, its ability to tick, or its networking capabilities—it likely resides within this module.

1. Master the Actor Lifecycle

The Engine module governs how Actors are spawned, initialized, and eliminated.

Best Practice: Understand the specific order of events: PostInitializeComponents -> BeginPlay -> Tick. Never put complex logic in the Constructor that depends on other Actors being present; use BeginPlay for logic that requires a fully initialized world state.
2. Minimize “Tick” Usage

While the AActor::Tick function is a core part of the Engine module, it is often the primary cause of performance degradation.

Tip: By default, set PrimaryActorTick.bCanEverTick = false in your constructors. Instead of ticking, use Timers, Delegate Callbacks, or the Enhanced Input System to trigger logic only when necessary. This is the most effective way to eliminate wasted CPU cycles on the Game Thread.
3. Use Actor Components for Modularity

The Engine module promotes a “Composition over Inheritance” design pattern through UActorComponent.

Best Practice: Instead of creating a massive “God Class” for your player, break functionality into modular components (e.g., UHealthComponent, UInventoryComponent). This makes your code more reusable and allows you to add or remove features dynamically at runtime.
4. Optimize Networking via Replication

Networking logic is deeply integrated into the Engine module via the AActor::GetLifetimeReplicatedProps system.

Tip: Only replicate variables that are absolutely necessary for gameplay (like Health or Team ID). For purely visual effects, use Multicast RPCs or RepNotify functions to trigger local logic on clients, which helps to eliminate unnecessary bandwidth consumption.
5. Efficient Memory Management with UPROPERTY

The Engine module relies on Unreal’s Garbage Collection (GC) system to manage memory.

Constraint: Any UObject or AActor pointer stored as a member variable MUST be marked with the UPROPERTY() macro. If you fail to do this, the GC will not know the object is still in use and may eliminate it from memory while you are still trying to access it, causing a crash.
6. Leverage the Subsystem Framework

Modern UE development uses Subsystems (e.g., UGameInstanceSubsystem, UWorldSubsystem) to manage global logic.

Tip: Instead of putting global “Manager” logic in the GameMode or LevelBlueprint, use a Subsystem. They have managed lifecycles that the Engine module handles automatically, providing a cleaner and more modular way to access global data without complex casting.
7. Correct Dependency Management

Because the Engine module is so large, almost every other module in your project will depend on it.

Best Practice: In your Build.cs file, Engine should usually be in the PublicDependencyModuleNames list.
C#
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore" });
Copy code

However, to keep compile times low, avoid adding unnecessary modules to the Public list if they are only used in your .cpp files; use PrivateDependencyModuleNames instead.

8. Use Data Assets for Static Data

The Engine module provides UDataAsset to help separate logic from data.

Tip: Instead of hardcoding values (like MoveSpeed or Damage) inside your C++ classes or Blueprints, move them into a Data Asset. This allows designers to tune gameplay values in the Editor without needing a programmer to recompile code, and it helps to eliminate data bloat in your Actor classes.