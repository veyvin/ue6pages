---
layout: default
title: AnimationSettings
---

<!-- ai-generation-failed -->

<h1>AnimationSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AnimationSettings/AnimationSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tem for the Unreal Engine animation pipeline. It primarily revolves around the UAnimationSettings class, which is exposed in the Editor via Project Settings > Engine > Animation.

This module defines project-wide defaults for animation compression, import behaviors, performance optimizations, and custom attribute handling. It ensures consistency across large teams by dictating how animation data is processed and stored.

Practical Usage Tips and Best Practices
1. Configure Custom Attribute Import

If your project uses custom data from DCC tools (like Maya or Houdini) to drive gameplay logic, use the Bone Custom Attributes list in the Animation Settings. Defining attribute names here (e.g., “FootPlant_L”) allows the engine to recognize and import these values as curves or metadata, preventing them from being “eliminated” during the FBX import process.

2. Manage Global Compression Defaults

Set the Default Bone Compression Settings and Default Curve Compression Settings here to ensure all newly imported animations share the same optimization baseline. Using a high-quality codec like ACL (Animation Compression Library) as the default can significantly reduce your project’s memory footprint without manual per-asset configuration.

3. Utilize “Zero-Ticking” for Performance

The Performance section allows you to enable/disable “Zero-Ticking.” When enabled, animations will tick once upon initialization of a Skeletal Mesh. This is useful for ensuring that characters start in the correct pose immediately upon spawning, avoiding a “one-frame pop” that can occur with deferred animation updates.

4. Define Key End Effectors for Accuracy

The Key End Effectors Match Name Array is a powerful tool for animation compression. By adding bone name substrings (like “hand”, “foot”, or “weapon”) to this list, you tell the compression algorithm to treat these bones with higher precision. This prevents foot-sliding or weapon misalignment caused by aggressive data stripping.

5. Control Mirroring Profiles

The module manages Mirroring Data Assets. Instead of manually flipping logic in Blueprints, define your mirroring tables (e.g., mapping “LeftHand” to “RightHand”) within the Animation Settings. This provides a unified source of truth for the “Mirror” node in Animation Blueprints, ensuring symmetrical movement works out-of-the-box.

6. Optimize Attribute Blending

Use the Custom Attribute Blend Modes to define how specific attributes (like Strings or Integers) behave when two animations blend. You can set attributes to “Override” (highest weight wins) or “Blend” (weighted average), ensuring that gameplay-critical data remains accurate during transitions.

7. Protect Critical Bone Curves

If your pipeline relies on specific curve names for IK or Foot-locking, add them to the Alternative Compression Thresholds. This ensures that even if a global compression setting is aggressive, these specific curves are spared from heavy “elimination,” maintaining the mechanical integrity of your character’s movement.

C++ Access Example

To programmatically access or modify these settings (e.g., in an Editor Utility or Build Script), use the UAnimationSettings singleton:

C++
	#include "AnimationSettings.h"

	 

	void UMyEditorLib::LogAnimationDefaults()

	{

	    // Access the global animation settings object

	    const UAnimationSettings* AnimSettings = GetDefault<UAnimationSettings>();

	 

	    if (AnimSettings)

	    {

	        // Example: Check which bones are marked as high-priority effectors

	        for (const FString& EffectorName : AnimSettings->KeyEndEffectorsMatchNameArray)

	        {

	            UE_LOG(LogTemp, Log, TEXT("High Precision Bone: %s"), *EffectorName);

	        }

	    }

	}
Copy code
Performance & Best Practices
Avoid Runtime Modification: While these settings are technically accessible at runtime, they are designed as “Editor-Time” configurations. Modifying them mid-game can lead to unpredictable behavior in compressed animation data.
Version Control: These settings are stored in DefaultEngine.ini. Always ensure your team is synced on this file to avoid “flip-flopping” animation compression results between different developer machines.
Compression Re-evaluation: If you change the default compression asset in these settings, use the “Compress” button in the asset to apply the new logic to all existing sequences in your project.