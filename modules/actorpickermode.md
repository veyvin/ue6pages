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

an editor-side event.

What it is and What it’s used for

Technically, it is a UI-driven interaction state managed by the FActorPickerModeModule. When activated, the editor enters a modal picking state where the cursor changes to an eyedropper and highlights valid targets under the mouse.

Primary uses include:

Property Customization: Filling AActor* or TSoftObjectPtr fields in the Details Panel.
Custom Editor Tools: Selecting target Actors for placement tools, alignment scripts, or logic linking (e.g., connecting a switch to a door).
Sequencer/Cinematics: Quickly assigning Actors to tracks or visibility groups.
Practical Usage Tips and Best Practices
1. Restrict Targets via Class Filters

Never allow a “blind” pick if you know the required type. When invoking the mode in C++, provide an FOnGetAllowedClasses delegate. This prevents users from accidentally selecting the Skybox, Floor, or Post-Process volumes when they should be selecting a specific gameplay Actor.

2. Implement the Selection Callback

The module relies on delegates to return data. Ensure your callback function (associated with FOnActorSelected) is robust enough to handle the selection. Remember that the mode ends the moment a valid Actor is clicked, so your callback should immediately handle the assignment or data storage.

3. Module Dependency Setup

Since this is an editor-only system, it must be localized within an Editor Module. Add “ActorPickerMode” to your editor module’s .Build.cs file under PrivateDependencyModuleNames. Never include this in a runtime module, or your project will fail to package for shipping.

4. Use SObjectPropertyEntryBox for Slate UI

If you are building a custom Slate-based editor window, you don’t need to manually initialize the module. Use the SObjectPropertyEntryBox widget and set the AllowPicker attribute to true. This handles the integration with the ActorPickerMode module automatically.

5. Handle the Cancellation State

Users can exit picking mode by pressing Esc or clicking into empty space. Ensure your tool logic doesn’t stall or hang if a selection is aborted. If you have “dimmed” other UI elements while picking, ensure they are restored regardless of whether a selection was successful.

6. Keep Filtering Logic Lightweight

The FOnShouldFilterActor delegate runs every frame for the Actor currently under the cursor to determine highlight eligibility. Avoid heavy logic like GetAllActorsOfClass or complex trace calls inside this delegate; stick to simple class checks or ActorHasTag to prevent viewport lag.

7. Provide Status Bar Instructions

When activating the mode for a custom tool, use the FNotificationInfo or the Status Bar message system to tell the user what they are picking (e.g., “Select the Actor to be Eliminated”). This provides essential UX feedback while the eyedropper is active.

8. Verify Actor Validity

Always check if the returned Actor is valid and not pending elimination (IsValid(SelectedActor)) before performing operations on it. In an editor context, it is also wise to check IsTemplate() to ensure you haven’t accidentally picked an actor from a preview world or a class default object.