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

provides a framework for the automated, programmatic modification of animation sequences. It centers around the UAnimationModifier class, which allows developers to analyze animation data and inject new information—such as sync markers, curves, or notifies—without manual asset editing.

Description

This module is used to eliminate repetitive manual tasks in the animation pipeline. Instead of a technical animator manually placing footstep notifies or calculating velocity curves for hundreds of clips, a modifier can be written in C++ or Blueprints to perform these actions automatically. Modifiers are non-destructive; they can be applied, reverted, or re-calculated at any time within the Animation or Skeleton editors, ensuring that data stays synchronized even if the base animation is updated.

Practical Usage Tips and Best Practices
1. Implement Both OnApply and OnRevert

A well-behaved modifier must be reversible to maintain a non-destructive workflow. Always implement OnRevert to explicitly remove only the data your modifier created. A common pattern is to call your OnRevert logic at the very beginning of OnApply to “clean the slate” and prevent duplicated data if the modifier is run multiple times.

2. Use the Data Model API (UE 5.2+)

In modern Unreal Engine versions, you should use the IAnimationDataController to perform changes to animation sequences. This ensures that your modifications are correctly broadcast to the editor UI and integrated into the Undo/Redo system.

C#
	// In YourProjectEditor.Build.cs

	PublicDependencyModuleNames.AddRange(new string[] { "AnimationModifiers", "AnimationBlueprintLibrary" });

	```

	 

	#### 2. Implement Both `OnApply` and `OnRevert`

	A well-behaved modifier must be reversible. `OnApply` should contain your logic for generating data, while `OnRevert` must explicitly remove only the data that the modifier created. This ensures that if a designer removes the modifier from an asset, the animation returns to its original "clean" state without leaving behind orphaned curves or notifies.

	 

	#### 3. Use the `IAnimationDataModel` (UE 5.2+)

	Starting with Unreal Engine 5.2, animation data management shifted to a **Data Model** architecture. When writing modifiers in C++, use the `IAnimationDataController` to perform changes. This ensures your modifications are undo-safe and correctly broadcasted to the editor UI.

	```cpp

	// Example: Accessing the controller in C++

	IAnimationDataController& Controller = AnimationSequence->GetController();

	Controller.OpenBracket(LOCTEXT("ApplyModifier", "Applying My Modifier"));

	// ... perform changes ...

	Controller.CloseBracket();

	```

	 

	#### 4. Optimize with the Animation Blueprint Library

	In your C++ implementation, leverage the static functions in `UAnimationBlueprintLibrary`. These functions are highly optimized for common tasks like retrieving bone positions at specific frames, calculating velocities, and finding the "lowest point" of a bone (useful for footstep detection).

	```cpp

	#include "AnimationBlueprintLibrary.h"

	 

	// Example: Getting bone location at a specific time

	FTransform BonePose = UAnimationBlueprintLibrary::GetSequenceLastKeyRotation(AnimationSequence, BoneName);

	```

	 

	#### 5. Handle "Elimination" of Old Data

	When `OnApply` is called, a common mistake is to append data to existing tracks. Best practice is to have your `OnApply` call your `OnRevert` logic first. This "cleans the slate" before re-calculating, preventing duplicated notifies or overlapping curve keys if the modifier is run multiple times.

	 

	#### 6. Utilize Native Modifiers for Complex Math

	While Blueprints are great for simple logic, use C++ for modifiers that require heavy bone-transform math or multi-frame analysis (e.g., extracting root motion to a curve). C++ modifiers compile faster and can access lower-level skeletal data that might not be exposed to the `AnimationBlueprintLibrary` nodes.

	 

	#### 7. Apply to Skeletons for Batch Processing

	If a modifier is meant to be universal (e.g., "Add Footstep Notifies to all Walk/Run cycles"), apply it to the **Skeleton Asset** rather than individual sequences. The `AnimationModifiers` module will automatically track all animations associated with that skeleton and offer to apply the modifier to the entire library in one click.

	 

	#### 8. Validate Data Before Calculation

	Always check if the required bones exist before running your logic. If a modifier depends on a "Foot_R" bone that isn't present in the skeletal mesh, the modifier should log a warning and exit gracefully. Use `UE_LOG` to provide feedback in the Output Log so animators know why a modifier failed to generate data.
Copy code
3. Leverage the Animation Blueprint Library

In your C++ or Blueprint implementation, use the static functions in UAnimationBlueprintLibrary. These are highly optimized for common tasks like retrieving bone transforms at specific frames, calculating bone velocity, and finding the “lowest point” of a bone (essential for automated footstep detection).

4. Optimize Module Dependencies

Since this is an editor-only utility, add it to your *.Build.cs only for the Editor target. This prevents your runtime game from attempting to load editor-specific animation classes:

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "AnimationModifiers", "AnimationBlueprintLibrary" });

	}
Copy code
5. Batch Process via the Skeleton Asset

If a modifier is universal (e.g., a “Footstep Marker” modifier for all bipeds), apply it to the Skeleton Asset rather than individual sequences. The module will track every animation associated with that skeleton and allow you to apply or update the modifier across the entire library in one click.

6. Validate Bone References

Always verify that required bones exist before running your logic. If a modifier depends on a “Foot_R” bone that is missing in a specific skeletal mesh, the modifier should log a warning and exit. This helps eliminate crashes or silent failures when dealing with diverse animation sets.

7. Profile Heavy Math in C++

While Blueprints are excellent for simple logic, use C++ for modifiers that require complex per-frame calculations or multi-pass analysis. C++ modifiers have faster access to the raw data buffers and can perform the heavy lifting needed to extract root motion or complex bone-space metadata.

8. Verify Data on Elimination

When creating modifiers that handle “state” data (like flags for when a character is in an elimination animation), use the modifier to automatically tag the exact frame where the elimination event should trigger gameplay logic. This ensures that visual cues and gameplay triggers are perfectly frame-aligned across all variants of an animation.