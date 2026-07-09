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

tive, it changes the editor’s interaction state, turning the mouse cursor into a picker that allows users to click directly on an actor in the 3D viewport or the Scene Outliner to assign a reference to a property or tool.

Practical Usage Tips and Best Practices
1. Restrict Selection via Class Filters

Never allow a generic “pick anything” unless necessary. When calling BeginActorPickingMode, provide a list of allowed classes or use a predicate. This improves user experience by ignoring irrelevant background geometry and ensures your tool receives valid data types.

2. Implement the Selection Delegate Correcty

The module operates asynchronously via a delegate. You must provide a callback (usually a lambda or a member function) that handles the AActor* returned. If you are modifying a UObject property, ensure your callback calls PreEditChange and PostEditChangeProperty to maintain Undo/Redo compatibility.

3. Handle Unexpected Termination

Users frequently cancel picking by pressing ESC or clicking into empty space. Your tool should be prepared for the picking mode to end without a valid selection. Ensure your UI reflects that picking has ended even if no actor was chosen to avoid “stuck” states.

4. Check Activity State Before Starting

Before triggering a picking session, always check IActorPickerModeModule::Get().IsInActorPickingMode(). Attempting to start a new picking session while one is already active can lead to state conflicts or redundant UI overlays.

5. Integration with Property Customizations

If you are building a custom IPropertyTypeCustomization, use the ActorPickerMode module to add an eyedropper button. This maintains visual consistency with the rest of the Unreal Editor and provides a familiar UX for level designers.

6. Use for Sequential Workflows

Actor picking is excellent for “Connect A to B” workflows. You can trigger one picker for a “Source” and, upon successful selection, immediately trigger a second picker for a “Target.” This creates a fluid interaction for complex scene setups that would be tedious in a text-based list.

7. Define Module Dependencies

Because this is an Editor-only module, you must wrap its inclusion in your Build.cs file. Failure to do so will cause “Module not found” errors when attempting to package the game for a client (Non-Editor build).

C#
	if (Target.bBuildEditor)

	{

	    PrivateDependencyModuleNames.Add("ActorPickerMode");

	}

	```

	 

	---

	 

	### Implementation Example (C++)

	 

	To use this in your own editor tool, you interact with the `IActorPickerModeModule` interface.

	 

	```cpp

	#include "ActorPickerModeModule.h"

	#include "Modules/ModuleManager.h"

	 

	void FMyCustomTool::StartPickingActor()

	{

	    // Load the module

	    FActorPickerModeModule& ActorPickerMode = FModuleManager::LoadModuleChecked<FActorPickerModeModule>("ActorPickerMode");

	 

	    // Configure the picking session

	    FBeginActorPickingModeParams Params;

	    Params.OnActorSelected = FOnActorSelected::CreateRaw(this, &FMyCustomTool::OnActorPicked);

	    

	    // Optional: Filter for only Point Lights

	    Params.CanPickActorPredicate = [](const AActor* Actor) -> bool

	    {

	        return Actor && Actor->IsA<APointLight>();

	    };

	 

	    // Enter the mode

	    ActorPickerMode.BeginActorPickingMode(Params);

	}

	 

	void FMyCustomTool::OnActorPicked(AActor* PickedActor)

	{

	    if (PickedActor)

	    {

	        UE_LOG(LogTemp, Log, TEXT("User picked: %s"), *PickedActor->GetName());

	        // Apply logic here...

	    }

	}

	```

	 

	### Debugging & Tools

	- **Visual Feedback**: The module automatically handles the "Eyedropper" cursor. If the cursor isn't changing, verify the module is correctly loaded.

	- **Console**: Use `LogActorPickerMode` (if available in your engine version) to track selection events in the Output Log.
Copy code
C++ Implementation Snippet

To utilize this in a custom Editor Utility or Tool, use the following pattern:

C++
	#include "ActorPickerModeModule.h"

	#include "Modules/ModuleManager.h"

	 

	void FMyEditorTool::StartPickingProcess()

	{

	    FActorPickerModeModule& PickerModule = FModuleManager::LoadModuleChecked<FActorPickerModeModule>("ActorPickerMode");

	 

	    FBeginActorPickingModeParams Params;

	    

	    // Bind the callback for when an actor is clicked

	    Params.OnActorSelected = FOnActorSelected::CreateRaw(this, &FMyEditorTool::OnActorPicked);

	    

	    // Optional: Filter to only pick StaticMeshActors

	    Params.CanPickActorPredicate = [](const AActor* Actor) -> bool

	    {

	        return Actor && Actor->IsA<AStaticMeshActor>();

	    };

	 

	    PickerModule.BeginActorPickingMode(Params);

	}

	 

	void FMyEditorTool::OnActorPicked(AActor* SelectedActor)

	{

	    if (SelectedActor)

	    {

	        // Logic to handle the picked actor

	        UE_LOG(LogTemp, Log, TEXT("Actor picked: %s"), *SelectedActor->GetName());

	    }

	}
Copy code
Performance & Best Practices
Avoid Tick: Do not check for picking status inside a Tick function. Use the delegate system provided by the module.
Eliminate Selection Confusion: If your tool requires picking specific sub-components, remember that ActorPickerMode returns the Actor. You may need to perform a subsequent LineTrace if you need the specific component or hit location.