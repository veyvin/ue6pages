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

in Unreal Engine 5 that provides a programmatic interface for creating, modifying, and managing Blueprint assets. It is the primary tool for developers building custom editor tools, automated asset validators, or procedural content generation pipelines that need to interact with the Blueprint graph system.

In C++, this functionality is primarily accessed via the UBlueprintEditorLibrary class. It exposes high-level functions that allow you to “script the scriptable,” such as adding variables, renaming graphs, or triggering a recompile of a Blueprint asset from code.

Practical Usage Tips and Best Practices
Explicitly Add to Build.cs
Since this is an editor-only module, you must add it to your module’s Build.cs file within an editor-only block. This ensures your game doesn’t fail to package because of a dependency on editor code.
C#
	    if (Target.Type == TargetType.Editor)

	    {

	        PublicDependencyModuleNames.AddRange(new string[] { "BlueprintEditorLibrary", "UnrealEd" });

	    }

	    ```

	 

	*   **Always Compile After Modification**

	    Modifying a Blueprint via the library (e.g., adding a variable or node) often leaves the asset in a "Dirty" or "Needs Compile" state. Always call `UBlueprintEditorLibrary::CompileBlueprint` after your changes to ensure the generated class is updated and valid for use in the editor.

	 

	*   **Use Transaction Scopes for Undo Support**

	    When modifying Blueprints via code, wrap your operations in an `FScopedTransaction`. This allows users to undo your procedural changes using `Ctrl+Z`. If you "eliminate" this step, your changes will be permanent until the asset is manually reloaded, which can lead to data loss.

	    ```cpp

	    FScopedTransaction Transaction(FText::FromString("Procedural BP Update"));

	    BlueprintAsset->Modify();

	    // Perform modifications here...

	    ```

	 

	*   **Validate Asset Types**

	    Before calling library functions, verify that the `UObject` you are working with is actually a `UBlueprint`. Attempting to run Blueprint-specific logic on a `UStaticMesh` or `UTexture` will result in null pointer crashes or "eliminated" logic execution.

	 

	*   **Avoid Runtime Module Dependencies**

	    Never include `BlueprintEditorLibrary` in a runtime module. If you need to trigger logic based on a Blueprint change at runtime, use a Data Asset or a message bus to bridge the gap. The module's header files are only available in `UE_EDITOR` builds.

	 

	*   **Leverage for Automated Unit Testing**

	    Use this module in your **Automation Specs** to programmatically create a "Test Blueprint," add a specific node configuration, and then verify the output. This is the best way to "eliminate" manual regression testing for complex Blueprint-based game systems.

	 

	*   **Handle "Dirty" State and Saving**

	    Simply modifying a Blueprint does not save it to disk. Use the `UEditorAssetLibrary` in conjunction with `BlueprintEditorLibrary` to mark the package as dirty and save it after your procedural operations are complete to ensure the work isn't lost on restart.

	 

	*   **Use for Batch Variable Renaming**

	    If your project undergoes a major refactor, use this library to write a small C++ utility that iterates through all Blueprints in a folder and renames specific variables or functions, "eliminating" hours of tedious manual labor and potential human error.
Copy code
Always Compile After Modification
Modifying a Blueprint via the library (e.g., adding a variable or node) often leaves the asset in a “Dirty” or “Needs Compile” state. Always call UBlueprintEditorLibrary::CompileBlueprint after your changes to ensure the generated class is updated and valid for use in the editor.
Use Transaction Scopes for Undo Support
When modifying Blueprints via code, wrap your operations in an FScopedTransaction. This allows users to undo your procedural changes using Ctrl+Z. If you “eliminate” this step, your changes will be permanent until the asset is manually reloaded, which can lead to data loss.
C#
	    if (Target.Type == TargetType.Editor)

	    {

	        PublicDependencyModuleNames.AddRange(new string[] { "BlueprintEditorLibrary", "UnrealEd" });

	    }

	    ```

	 

	*   **Always Compile After Modification**

	    Modifying a Blueprint via the library (e.g., adding a variable or node) often leaves the asset in a "Dirty" or "Needs Compile" state. Always call `UBlueprintEditorLibrary::CompileBlueprint` after your changes to ensure the generated class is updated and valid for use in the editor.

	 

	*   **Use Transaction Scopes for Undo Support**

	    When modifying Blueprints via code, wrap your operations in an `FScopedTransaction`. This allows users to undo your procedural changes using `Ctrl+Z`. If you "eliminate" this step, your changes will be permanent until the asset is manually reloaded, which can lead to data loss.

	    ```cpp

	    FScopedTransaction Transaction(FText::FromString("Procedural BP Update"));

	    BlueprintAsset->Modify();

	    // Perform modifications here...

	    ```

	 

	*   **Validate Asset Types**

	    Before calling library functions, verify that the `UObject` you are working with is actually a `UBlueprint`. Attempting to run Blueprint-specific logic on a `UStaticMesh` or `UTexture` will result in null pointer crashes or "eliminated" logic execution.

	 

	*   **Avoid Runtime Module Dependencies**

	    Never include `BlueprintEditorLibrary` in a runtime module. If you need to trigger logic based on a Blueprint change at runtime, use a Data Asset or a message bus to bridge the gap. The module's header files are only available in `UE_EDITOR` builds.

	 

	*   **Leverage for Automated Unit Testing**

	    Use this module in your **Automation Specs** to programmatically create a "Test Blueprint," add a specific node configuration, and then verify the output. This is the best way to "eliminate" manual regression testing for complex Blueprint-based game systems.

	 

	*   **Handle "Dirty" State and Saving**

	    Simply modifying a Blueprint does not save it to disk. Use the `UEditorAssetLibrary` in conjunction with `BlueprintEditorLibrary` to mark the package as dirty and save it after your procedural operations are complete to ensure the work isn't lost on restart.

	 

	*   **Use for Batch Variable Renaming**

	    If your project undergoes a major refactor, use this library to write a small C++ utility that iterates through all Blueprints in a folder and renames specific variables or functions, "eliminating" hours of tedious manual labor and potential human error.
Copy code
Validate Asset Types
Before calling library functions, verify that the UObject you are working with is actually a UBlueprint. Attempting to run Blueprint-specific logic on a UStaticMesh or UTexture will result in null pointer crashes or “eliminated” logic execution.
Avoid Runtime Module Dependencies
Never include BlueprintEditorLibrary in a runtime module. If you need to trigger logic based on a Blueprint change at runtime, use a Data Asset or a message bus to bridge the gap. The module’s header files are only available in UE_EDITOR builds.
Leverage for Automated Unit Testing
Use this module in your Automation Specs to programmatically create a “Test Blueprint,” add a specific node configuration, and then verify the output. This is the best way to “eliminate” manual regression testing for complex Blueprint-based game systems.
Handle “Dirty” State and Saving
Simply modifying a Blueprint does not save it to disk. Use the UEditorAssetLibrary in conjunction with BlueprintEditorLibrary to mark the package as dirty and save it after your procedural operations are complete to ensure the work isn’t lost on restart.
Use for Batch Variable Renaming
If your project undergoes a major refactor, use this library to write a small C++ utility that iterates through all Blueprints in a folder and renames specific variables or functions, “eliminating” hours of tedious manual labor and potential human error.