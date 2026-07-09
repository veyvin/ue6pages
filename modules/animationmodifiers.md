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

s to automate the processing of Animation Sequences. It uses Animation Modifiers (classes derived from UAnimationModifier) to programmatically inject data—such as Animation Curves, Sync Markers, or Animation Notifies—directly into animation assets. This eliminates the need for manual frame-by-frame editing, ensuring consistency across large libraries of animations.

Practical Usage Tips & Best Practices
1. Automate Sync Markers for Footsteps

The most common use for this module is automatic footstep detection. Instead of manually placing “Footstep” notifies, create a modifier that samples the Z-velocity or height of the “foot” bones. When the bone hits the floor (velocity near zero or height at minimum), the modifier can automatically insert a Sync Marker or a Notify.

2. Use the Animation Data Model (UE 5.2+)

Starting with Unreal Engine 5.2, the internal data handling changed. When writing C++ or Blueprint modifiers, use the UAnimDataModel and IAnimationDataController interfaces to modify curves or tracks. This ensures your changes are properly serialized and compatible with the latest engine versions.

3. Implement “Apply All Modifiers” in Pipelines

Animation Modifiers can be applied to individual sequences or assigned to a Skeleton. If assigned to a Skeleton, you can use the Apply All Modifiers command to batch-process every animation associated with that character. This is a best practice for maintaining project-wide standards for curve naming and metadata.

4. Optimize with “Fast Path” and Multithreading

While modifiers run in the Editor, they can be heavy. When sampling bone transforms (using GetBonePose), perform your calculations efficiently. Use the OnApply event to do the heavy lifting once, so that the resulting curves can be used by the Animation Blueprint Editor’s “Fast Path” logic during runtime.

5. Tag Animations for Elimination Events

You can use modifiers to automatically tag the exact frame where a character should react to an elimination event. For example, a modifier can analyze the “Root” bone’s velocity in a falling animation and place a “DeathImpact” Notify at the precise moment the mesh hits its maximum downward velocity.

6. Toggle “Is Root Motion Lock Forced”

When sampling root motion data within a modifier (e.g., to generate a “Speed” curve), ensure you check the IsRootMotionLockForced flag on the sequence. If this is active, the root motion transform might return as identity, breaking your calculations. It is a best practice to cache the original value, disable the lock to sample data, and then re-apply the original setting at the end of the modifier logic.

7. Handle Re-entrant Logic with “Revert”

Always consider what happens when a modifier is applied twice. A good modifier should first call RemoveCurve or ClearNotifies for the specific data it manages before adding new data. This prevents the accumulation of duplicate curves or notifies every time the “Apply” button is clicked.

8. Utilize AnimPoseExtensions for Sampling

For modern UE5 development, avoid deprecated functions like GetBonePoseForTime. Instead, use UAnimPoseExtensions::GetAnimPoseAtTime. This provides a more robust and performance-aware way to retrieve the skeletal state at any given point in the animation timeline, which is essential for accurate data extraction.