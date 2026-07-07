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

managing hierarchical, user-defined labels (tags) that identify and categorize objects and states.

Description and Purpose

Gameplay Tags act as standardized, “smart” names (represented by the FGameplayTag struct) that are stored in a central dictionary. Unlike raw strings or Enums, which are prone to typos and rigid structures, Gameplay Tags are hierarchical (e.g., State.Debuff.Stun) and searchable. They are primarily used to drive gameplay logic, such as determining if a character is currently immune to an elimination effect or if a specific weapon can be equipped. The module is a core dependency for the Gameplay Ability System (GAS) but is frequently used as a standalone system for its powerful querying and performance benefits.

Practical Usage Tips and Best Practices
Prefer Tags Over Enums for Flexibility
Use Gameplay Tags for categories that might grow over time, such as damage types or status effects. This allows you to add a new Damage.Fire.Lava tag without modifying code or breaking existing logic, helping you eliminate the need for constant recompilation when expanding gameplay features.
Define Native Tags in C++
For core engine tags used in C++ logic, use the UE_DECLARE_GAMEPLAY_TAG_EXTERN and UE_DEFINE_GAMEPLAY_TAG macros. This provides static, type-safe access to tags in code and ensures they are registered early in the engine’s boot process, which helps you eliminate runtime lookup overhead.
Leverage Hierarchical Queries
Use the hierarchical nature of tags to simplify your logic. Checking if a container HasTag for State.Debuff will return true if the object has State.Debuff.Poison. This allows you to write broad logic for “any debuff” while still having specific sub-tags, helping you eliminate complex “switch” statements.
Enable Fast Replication for Multiplayer
In your DefaultEngine.ini, ensure FastReplication is enabled for Gameplay Tags. This causes the engine to replicate tags as small integer indices rather than full strings, which can significantly eliminate bandwidth consumption in high-traffic multiplayer matches.
Use Tag Containers for Multiple States
Always use FGameplayTagContainer when an object needs to hold more than one tag. This container is optimized for batch operations like HasAll, HasAny, or HasNone, allowing you to check for complex requirements (e.g., “Must have Red Key AND NOT be InCombat”) in a single, efficient call.
Utilize Gameplay Tag Queries for Complex Logic
For advanced conditions, use FGameplayTagQuery. This allows designers to build complex “AND/OR/NOT” logic within a dedicated editor UI. Using queries helps you eliminate hard-coded conditional logic in your Blueprints or C++ classes.
Import Tags via Data Tables or Fab
For large projects, manage your tag list using a Data Table or CSV. You can also find standardized tag sets on Fab. Centralizing your tag definitions in a table helps you eliminate “rogue” tags created by different team members in isolation.
Debug with the Gameplay Tag Searcher
Use the “Gameplay Tag Insights” or the “Gameplay Tag Searcher” in the editor (Tools -> Gameplay Tag Searcher) to find every reference to a specific tag in your project. This is essential when you want to eliminate a deprecated tag and need to see where it is still being used in assets or code.