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

set of static utility functions for programmatically interacting with Blueprint assets. It is part of the Scriptable Editor initiative, allowing developers to perform tasks that traditionally required manual mouse clicks—such as compiling Blueprints, adding variables, or modifying function graphs—via C++, Python, or Editor Utility Blueprints.

This library is primarily used for Automation and Pipeline Tooling. It is essential for developers building custom tools to “eliminate” repetitive asset management tasks and ensure consistency across large-scale projects.

Practical Usage Tips and Best Practices
Automate Bulk Compilation
In large projects, changes to a base class can often result in dozens of “dirty” child Blueprints. Use UBlueprintEditorLibrary::CompileBlueprint in an Editor Utility to batch-recompile assets. This helps you “eliminate” manual compilation errors before submitting code to version control.
Programmatic Variable Management
You can use the library to dynamically add or remove variables from a Blueprint. This is particularly useful when refactoring data structures. For example, if you are moving “Elimination” stats from a PlayerState to a new Component, you can script the addition of the new variables across hundreds of character Blueprints simultaneously.
Dynamic Function and Graph Injection
The library allows you to add new function graphs or macros to a Blueprint asset. If you have a standardized “Elimination Logic” block that needs to be present in every AI variant, you can use AddFunctionGraph to inject that logic programmatically rather than copy-pasting nodes manually.
Set Default Values for Data-Driven Design
Use SetBlueprintVariableDefaultValue to update the default values of variables within a Blueprint asset without opening the editor UI. This is a best practice for syncing Blueprint values with external data sources like JSON files or spreadsheets, “eliminating” data entry discrepancies.
Check for Compilation Errors in CI/CD
When running commandlets or automated build scripts, use the library to query the Status of a Blueprint. If a Blueprint is in a BS_Error state, you can trigger an “elimination” of the build process and alert the responsible developer immediately, preventing broken assets from reaching the team.
Manage Interface Implementations
The library provides functions to check if a Blueprint implements a specific Interface and to add new ones. This is helpful when updating gameplay frameworks (e.g., adding an IInteractable interface to all prop Blueprints) to ensure that the new “elimination” or interaction logic is properly exposed.
Module Dependency Setup
Because this library is part of the Unreal Editor’s internal tools, it is strictly Editor-Only. Ensure you wrap any C++ calls in #if WITH_EDITOR guards and add the module to the Editor section of your Build.cs to “eliminate” packaging errors.
C#
	// In YourProject.Build.cs

	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("BlueprintEditorLibrary");

	}
Copy code
Use with “Find and Replace” Workflows
Combine this library with the AssetRegistry to find all Blueprints of a certain type and perform mass updates. For example, you can find every Blueprint that uses a deprecated “Kill” event and replace it with a new “Elimination” function call programmatically.