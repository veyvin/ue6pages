---
layout: default
title: ActorPickerMode
---

<!-- ai-generation-failed -->

<h1>ActorPickerMode</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ActorPickerMode/ActorPickerMode.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, EditorInteractiveToolsFramework, Engine, InputCore, InteractiveToolsFramework, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

t enables interactive actor selection directly within the Level Viewport. It provides the logic behind the “eyedropper” tool often seen in the Details panel, allowing users to pick an actor by clicking on it in the 3D scene rather than searching through a long list or the Outliner.

Core C++ Interface

The module is accessed via FActorPickerModeModule (defined in ActorPickerModeModule.h). The primary workflow involves calling BeginActorPickingMode, which puts the editor into a specialized state where the cursor changes and the next click on a valid actor triggers a callback.

Practical Usage Tips & Best Practices
1. Add Module Dependencies

Since this is an editor-only feature, you must add the module to your Build.cs file. It is best practice to wrap this in an editor-only check or include it only in your project’s Editor module:

C#
	if (Target.Type == TargetRules.TargetType.Editor)

	{

	    PrivateDependencyModuleNames.AddRange(new string[] { "ActorPickerMode", "PropertyEditor" });

	}

	```

	 

	#### 2. Use PropertyCustomizationHelpers for UI

	If you are building a Detail Customization, do not call the module directly. Use `PropertyCustomizationHelpers::MakeInteractiveActorPicker`. This helper automatically creates the standard "Eyedropper" button and handles the module communication for you.

	 

	#### 3. Implement Robust Filtering

	Always provide an `FOnShouldFilterActor` delegate. This prevents users from picking invalid targets (e.g., the actor they are currently editing, hidden utility actors, or actors in different sub-levels).

	```cpp

	// Example filter logic

	bool FMyCustomization::ShouldFilterActor(const AActor* const CandidateActor) const

	{

	    return CandidateActor && !CandidateActor->IsA<ALight>(); // Only allow non-light actors

	}

	```

	 

	#### 4. Handle Selection via Delegates

	The `BeginActorPickingMode` function requires an `FOnActorSelected` delegate. Use this to perform your logic (like updating a property or assigning a pointer) immediately when the user clicks. The mode terminates automatically once a selection is made.

	 

	#### 5. Check "Is Picking" State

	To prevent UI flickering or multiple activations, use `FActorPickerModeModule::Get().IsInActorPickingMode()` to check if the user is already in selection mode before trying to start it again.

	 

	#### 6. Coordinate with Editor Modes

	Actor picking is an **Editor Mode**. Activating it will temporarily override other modes (like Placement or Foliage). If your tool relies on another custom mode, be aware that entering Actor Picking mode might suspend your mode's input handling.

	 

	#### 7. Provide Viewport Feedback

	When the module is active, the engine automatically displays instructional text in the viewport (e.g., "Click to select an actor"). Ensure your custom tool doesn't obscure the top-left area of the viewport so the user can see these instructions.

	 

	#### 8. Safe Cleanup

	If the user cancels picking (e.g., by pressing `ESC` or clicking empty space), ensure your code handles a `nullptr` or "canceled" state gracefully. The `FOnActorSelected` delegate is typically only called on a successful pick, so you may need to track the "active" state of your UI button manually to reset its appearance if the user aborts.

	 

	### Summary Header Example

	```cpp

	#include "ActorPickerModeModule.h"

	 

	void FMyEditorTool::StartPicking()

	{

	    FActorPickerModeModule& PickerModule = FModuleManager::LoadModuleChecked<FActorPickerModeModule>("ActorPickerMode");

	    

	    FOnActorSelected OnSelected = FOnActorSelected::CreateRaw(this, &FMyEditorTool::OnActorChosen);

	    FOnShouldFilterActor OnFilter = FOnShouldFilterActor::CreateRaw(this, &FMyEditorTool::FilterActor);

	 

	    PickerModule.BeginActorPickingMode(OnSelected, FOnGetAllowedClasses(), OnFilter);

	}
Copy code
2. Use PropertyCustomizationHelpers for UI

If you are building a Detail Customization, you rarely need to call the module directly. Use PropertyCustomizationHelpers::MakeInteractiveActorPicker. This helper creates the standard “Eyedropper” button and handles the module communication for you, ensuring a consistent UI/UX.

3. Implement Robust Filtering

Always provide an FOnShouldFilterActor delegate. This prevents users from picking invalid targets. For example, if you are creating a system to eliminate target dummies, you should filter out the floor, skybox, or the player character itself.

C++
	bool FMyTool::ShouldFilterActor(const AActor* const Candidate) const

	{

	    // Return true to REJECT/FILTER OUT the actor

	    return !Candidate || !Candidate->IsA<ATargetDummy>(); 

	}
Copy code
4. Handle Selection via Delegates

The BeginActorPickingMode function requires an FOnActorSelected delegate. Use this to perform your logic immediately when the user clicks. The mode terminates automatically once a selection is made or the action is canceled.

5. Check “Is Picking” State

To prevent UI flickering or redundant activations, use FActorPickerModeModule::Get().IsInActorPickingMode() to check if the user is already in selection mode before attempting to start it again.

6. Coordinate with Editor Modes

Actor picking is technically a specialized Editor Mode. Activating it will temporarily override other modes (like Placement or Foliage). If your tool relies on another custom mode, be aware that entering Actor Picking mode will suspend your mode’s input handling until the pick is complete or canceled.

7. Provide Viewport Feedback

When the module is active, the engine displays instructional text in the viewport (e.g., “Pick an actor”). Ensure your custom tool or overlay doesn’t obscure the top-left area of the viewport so the user remains aware that the editor is in a modal picking state.

8. Graceful Cancellation

Ensure your code handles a “canceled” state. If the user presses ESC or clicks into empty space, the FOnActorSelected delegate may not fire with a valid actor. If your UI changed state (e.g., a button stayed highlighted), you must ensure it resets even if no actor was successfully picked.