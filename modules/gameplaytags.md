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

labels (tags) that can be used to identify, categorize, and query game objects and states.

Description

The GameplayTags module is a core architectural tool used to replace hard-coded strings and enums with a robust, hierarchical naming system (e.g., State.Debuff.Stun). Unlike standard strings, Gameplay Tags are registered in a central dictionary, providing autocomplete in the editor and high-performance comparisons in C++. They are heavily integrated into the Gameplay Ability System (GAS) and Enhanced Input, where they act as the “connective tissue” that determines if an ability can trigger, if an animation should play, or if an actor is currently “eliminated.”

Practical Usage Tips and Best Practices
1. Prefer Native Tags in C++

To ensure maximum performance and avoid spelling errors, define your core tags in C++ using the NativeGameplayTags.h macros. Use UE_DECLARE_GAMEPLAY_TAG_EXTERN in your header and UE_DEFINE_GAMEPLAY_TAG in your source file. This makes the tags globally accessible as static variables, which are faster than searching for tags by name at runtime.

2. Leverage Hierarchical Logic

Gameplay Tags are hierarchical, meaning a check for State.Buff will return true if an actor has the tag State.Buff.Speed. Use this to simplify your logic: instead of checking for ten different types of status effects, check for a single parent tag to determine if a character is currently affected by any “Debuff.”

3. Use Tag Queries for Complex Logic

The module includes FGameplayTagQuery, which allows you to perform complex boolean logic (AND, OR, NOT) within a single data asset. Instead of writing nested Blueprint branches to check if a player “Is Airborne AND NOT Stunned,” you can create a single Tag Query that evaluates the entire condition at once, leading to the elimination of “spaghetti” logic.

4. Manage Tags via Data Tables

For large projects, manage your tag list using a Data Table with the GameplayTagTableRow row type. This allows you to import and export tags from .csv or .json files, making it easier for designers to manage hundreds of tags without touching Project Settings or C++ files.

5. Optimize with FGameplayTagContainer

When an object needs to store multiple tags (e.g., a character’s current states), always use FGameplayTagContainer. This container is highly optimized for “HasTag” and “HasAny” operations. Internally, it uses bit-masking and sorted arrays to ensure that checking for a tag’s presence is nearly as fast as a simple boolean check.

6. Use for Enhanced Input Mapping

In Enhanced Input, use Gameplay Tags to identify your Input Actions. By associating an action with a tag like Input.Action.Jump, you can easily swap mapping contexts or disable specific inputs by simply removing or blocking the corresponding tag. This is a best practice for the elimination of hard-coded input handling.

7. Debug with “showdebug gameplaytags”

Use the console command showdebug gameplaytags during play-in-editor (PIE). This creates an on-screen overlay showing every tag currently active on the selected actor. This is the most efficient way to debug why an ability didn’t fire or why a character wasn’t properly eliminated during a combat event.

8. Prevent Tag Bloat

While tags are powerful, creating thousands of overly specific tags (e.g., Object.Tree.Oak.Branch.Left.01) can lead to a cluttered dictionary and slower search times. A best practice is to keep tags for “States” and “Types” and use Actor Components or Data Assets for specific instance data. The elimination of redundant or hyper-specific tags keeps your project’s data architecture clean and maintainable.