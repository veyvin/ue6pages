---
layout: default
title: AnimationModifiers
---

<!-- ai-generation-failed -->

<h1>AnimationModifiers</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AnimationModifiers/AnimationModifiers.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimationBlueprintLibrary, AssetRegistry, AssetTools, ClassViewer, ContentBrowser, Core, CoreUObject, DeveloperSettings, EditorFramework, Engine, InputCore, MainFrame, PropertyEditor, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at allows developers to automate the creation and manipulation of animation metadata. It provides a way to run scripts (via Blueprints or C++) that “bake” data directly into Animation Sequences.

Description and Purpose

The module defines the UAnimationModifier class, which is used to analyze animation data (like bone positions or velocity) and automatically generate Notify Tracks, Sync Markers, or Animation Curves. Instead of manually placing footstep sounds or synchronization tags on hundreds of animations, a modifier can calculate where the feet hit the ground and insert the necessary data automatically. This ensures consistency across large animation libraries and significantly reduces manual labor.

Practical Usage Tips and Best Practices
Implement OnApply and OnRevert
Every Animation Modifier must implement OnApply to add data and OnRevert to remove it. This allows you to “Undo” changes safely. Ensure OnRevert is thorough so that re-applying a modifier doesn’t result in duplicate tracks or overlapping curves.
Automate Footstep Notifies
Use the Animation Blueprint Library functions within your modifier to track the Z-height of foot bones. When the bone reaches its lowest point relative to the root, have the modifier automatically spawn a “PlaySound” or “Particle” Notify. This ensures footsteps are perfectly synced regardless of animation speed.
Apply to Skeletons for Batch Processing
You can apply an Animation Modifier to a Skeleton asset instead of individual sequences. When applied to the Skeleton, the modifier will run on every animation associated with that skeleton, making it easy to update an entire character’s library in one click.
Use for Sync Marker Generation
For high-quality locomotion blending, use modifiers to create Sync Markers (e.g., “LeftFootDown”, “RightFootDown”). By automating this, you ensure that Blend Spaces transition smoothly between walk and run cycles without foot sliding.
Cache Data with Anim Pose Extensions
In UE 5.2 and later, use AnimPoseExtensions::GetAnimPoseAtTime to sample bone transforms. This is the modern, performant way to query where a bone is located on a specific frame, allowing your modifier to make decisions based on precise spatial data.
Handle Elimination Effects Automatically
When processing “hit reaction” or “death” animations, use a modifier to detect the exact frame where a character’s collision should be disabled or where a “dissolve” effect should begin. The modifier can then insert a custom elimination Notify at that precise timestamp, ensuring visual effects always match the skeletal movement.
Avoid Expensive Logic in OnApply
Modifiers are intended to be “baked” tools, but they still run in the editor. Avoid extremely complex physics simulations or heavy loops within OnApply. If you must perform heavy calculations, consider caching results or using a specialized C++ implementation of the modifier for better performance.
Check “IsRootMotionLockForced”
If your modifier needs to sample root motion (e.g., to calculate travel distance), ensure you check and temporarily disable the IsRootMotionLockForced flag on the animation sequence. Otherwise, the root motion transform may return as identity (zeroed out), leading to incorrect calculations.