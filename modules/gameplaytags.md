---
layout: default
title: GameplayTags
---

<!-- ai-generation-failed -->

<h1>GameplayTags</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/GameplayTags/GameplayTags.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AutoRTFM, Core, CoreUObject, DeveloperSettings, Engine, Json, JsonUtilities, NetCore, Projects, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

escribe objects through hierarchical, user-defined labels (e.g., Character.State.Exhausted or Damage.Fire). Unlike Enums, which are rigid and limited to a single selection, Gameplay Tags are lightweight strings handled as 64-bit integers, allowing for fast comparisons and multiple simultaneous labels. This module is the backbone of the Gameplay Ability System (GAS) but is increasingly used in standalone projects to handle state management, actor filtering, and conditional logic.

Practical Usage Tips & Best Practices
1. Prefer Gameplay Tags over String/Name Comparisons

Direct string or FName comparisons are slow and prone to human error (typos).

Best Practice: Always use the FGameplayTag type for variables. This provides a dropdown selector in the editor, ensuring the elimination of “magic string” bugs and significantly improving performance by using integer-based comparisons.
2. Leverage the Hierarchy for Broad Queries

Gameplay Tags support a parent-child relationship that is extremely efficient for filtering.

Tip: If you have tags like Weapon.Ranged.Sniper and Weapon.Ranged.Pistol, you can check if an actor HasTag(Weapon.Ranged). This “parent match” logic allows for the elimination of complex “if/else” chains when checking for broad categories of objects.
3. Use Gameplay Tag Containers for Multiple States

Actors often exist in multiple states at once (e.g., a character can be Status.Poisoned and Status.Slowed).

Best Practice: Store tags in an FGameplayTagContainer. This container allows you to perform operations like HasAny, HasAll, or HasNone. Using containers leads to the elimination of excessive boolean variables like bIsPoisoned or bIsSlowed on your character classes.
4. Register Tags in C++ for Native Performance

While you can add tags in the Project Settings UI, registering core “permanent” tags in C++ is safer for large teams.

Tip: Use the FNativeGameplayTags helper macro in your C++ header files. This makes the tags available globally and ensures the elimination of accidental tag deletions by designers in the editor.
5. Replace Casting with Tag Checks

Casting to specific classes (e.g., Casting to BP_Zombie) creates hard references that increase memory usage and load times.

Best Practice: Give your actors a GameplayTag variable (like Identity.Enemy.Zombie). Instead of casting, simply check if the actor has the specific tag. This architectural shift facilitates the elimination of “spaghetti” dependencies and heavy memory footprints.
6. Use Tags for Event Signaling

Gameplay Tags can be used as unique identifiers for global events or UI triggers.

Tip: Use the UGameplayMessageSubsystem in conjunction with tags to broadcast events like Event.Combat.Elimination. This decoupling of the “killer” and the “victim” results in the elimination of hard-wired event dispatchers between unrelated actors.
7. Optimize Multiplayer via Tag Replication

Tags are highly optimized for networking; they are sent as compressed indices rather than full strings.

Best Practice: Replicate a FGameplayTagContainer to represent a character’s state. Because the engine knows the tag dictionary on both client and server, it results in the elimination of massive bandwidth waste compared to sending raw strings or custom structs over the wire.
8. Utilize Tag Redirectors during Refactoring

Renaming a tag that is used in hundreds of Blueprints can be disastrous.

Tip: Use the Gameplay Tag Redirector in your DefaultGameplayTags.ini. When you rename Old.Tag to New.Tag, the redirector ensures the elimination of broken references in your assets, allowing for safe project-wide refactoring.