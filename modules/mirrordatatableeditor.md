---
layout: default
title: MirrorDataTableEditor
---

<!-- ai-generation-failed -->

<h1>MirrorDataTableEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/MirrorDataTableEditor/MirrorDataTableEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetTools, Core, CoreUObject, DataTableEditor, EditorStyle, Engine, SkeletonEditor, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

user interface and management of Mirror Data Tables. While mirroring logic can exist at runtime, this module provides the specialized tools within the Unreal Editor to define how bone, curve, and sync marker data should be flipped across a specific axis (usually the X-Z plane).

This module is a critical part of the animation pipeline, as it allows developers to create a single animation (e.g., a “Run Right” cycle) and use data-driven rules to automatically generate the mirrored version (“Run Left”). By centralizing these name-mapping and axis-flipping rules, it helps you eliminate the need for animators to manually author symmetrical animations, significantly reducing memory footprint and production time.

Practical Usage Tips and Best Practices
Define Standardized Suffixes/Prefixes
Use the Find and Replace Expressions array within the Mirror Data Table. By setting up search patterns like _l to _r or left_ to right_, the module can automatically populate the table for you. This helps you eliminate the tedious task of manually mapping hundreds of bones in a complex skeleton.
Leverage Regular Expressions (Regex)
For complex bone hierarchies where simple prefixes aren’t enough (e.g., finger_left_01_pal'), use the **Regular Expression** search method. A pattern like(\S)left(\S)replaced with\(1_right_\)2` allows the module to find modifiers in the middle of a string, helping you eliminate mapping errors in non-standard naming conventions.
Configure the Mirror Axis Correctly
In the Data Table Details, verify the Mirror Axis. For most Unreal Engine characters, this is the X-axis (Right-to-Left). Ensuring this is set correctly before generating the table helps you eliminate “inverted” or “inside-out” animations where the character appears to fold into themselves.
Include Mirroring for Animation Curves
Don’t just mirror bones; add entries for Curves (like foot planting or morph targets). If a curve is named L_Foot_Lock, ensure it mirrors to R_Foot_Lock. This module ensures that synced gameplay logic remains consistent, helping you eliminate foot-sliding or broken logic on mirrored animations.
Set Up Project-Wide Defaults
Go to Project Settings > Engine > Animation > Mirroring. You can define a default Mirror Data Table or a set of find/replace expressions that apply to the whole project. This global setup helps you eliminate the need to re-configure mirroring rules every time a new character is imported.
Use ‘Mirroring’ in Animation Blueprints
Once the Data Table is created via this module, use the Mirror node in your AnimGraph. You can pass the Data Table into this node to flip animations dynamically at runtime. This allows you to eliminate redundant assets from your “Movies” or “Animations” folders by mirroring a single set of movement cycles.
Validate the Skeleton Mapping
After generating a table, use the “Mirror Data Table” editor window to check for “Unmapped” entries. If a bone doesn’t have a mirrored counterpart, it won’t move when mirrored. Fixing these unmapped bones helps you eliminate “dead” limbs or static appendages on your mirrored characters.
Cleanup on Skeleton Elimination
If you delete a skeleton or significantly change its hierarchy (an “elimination” of the old bone structure), you must re-sync your Mirror Data Table. Use the Reimport or Refresh actions within the editor to ensure the table doesn’t point to “ghost” bones, which helps you eliminate crashes or log warnings during animation playback.