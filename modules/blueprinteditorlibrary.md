---
layout: default
title: BlueprintEditorLibrary
---

<!-- ai-generation-failed -->

<h1>BlueprintEditorLibrary</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/BlueprintEditorLibrary/BlueprintEditorLibrary.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AnimGraph, BlueprintGraph, Core, CoreUObject, Engine, Json, JsonUtilities, KismetCompiler, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ips and Best Practices
1. Enable the Required Plugin

The BlueprintEditorLibrary functions are part of the Editor Scripting Utilities plugin.

Action: Go to Edit > Plugins and search for “Editor Scripting Utilities.” You must enable this for these nodes to appear in your Editor Utility Blueprints or for the Python API to recognize the unreal.BlueprintEditorLibrary class.
2. Automate Mass Compilation

When refactoring a base C++ class or a parent Blueprint, many child Blueprints may become “dirty” and need a recompile.

Best Practice: Create an Editor Utility Widget that finds all Blueprints in a folder and uses CompileBlueprint in a loop. This helps eliminate the tedious process of opening and compiling hundreds of assets manually after a major code change.
3. Manage Blueprint Variables Programmatically

You can add, remove, or rename variables across multiple Blueprints using this library.

Tip: If you are implementing a new gameplay system that requires a specific variable (like “Health” or “TeamID”) on all character Blueprints, use AddVariable to batch-inject these properties. This helps eliminate human error and ensures consistency across large projects.
4. Change Parent Classes Safely

If you need to move a group of Blueprints from an Actor parent to a custom AMyBaseActor C++ class:

Action: Use the ReparentBlueprint function. This node handles the logic of re-linking existing variables and functions to the new hierarchy. Always run a “Compile” and “Save” immediately after reparenting to eliminate potential corruption or broken references.
5. Clean Up Unused Variables

Over time, large Blueprints often accumulate “orphaned” variables that are no longer used in any graphs.

Best Practice: Write a script that iterates through a Blueprint’s variables and checks their reference count. You can then use RemoveVariable to eliminate unused data, keeping your assets clean and reducing memory overhead.
6. Coordinate with Version Control

Because this library modifies the actual .uasset file, it is vital to handle file checkout logic.

Tip: Use the EditorAssetLibrary alongside the BlueprintEditorLibrary to check if a file is read-only. Attempting to modify a Blueprint that is not checked out in Perforce or Git will cause the library functions to fail silently or crash the editor.
7. Use for Automated Validation

You can use this library to build “Sanity Check” tools for your team.

Action: Create a tool that opens Blueprints and checks if they have a specific interface or if certain variables have default values. If a Blueprint fails validation, you can automatically flag it for the art or design team, eliminating bugs before they reach the main build.
8. Avoid Modifying Open Blueprints

While you can technically modify a Blueprint that is currently open in an editor tab, it can sometimes lead to UI desynchronization.

Best Practice: For large-scale batch operations, ensure the Blueprint Editor tabs are closed. After the script finishes, use unreal.EditorAssetLibrary.save_asset() to commit the changes to disk and eliminate the risk of losing work if the editor crashes.