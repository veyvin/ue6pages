---
layout: default
title: AssetDefinition
---

<!-- ai-generation-failed -->

<h1>AssetDefinition</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AssetDefinition/AssetDefinition.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

w custom C++ classes appear and behave within the Content Browser. It replaces the legacy IAssetTypeActions system. By creating a class that inherits from UAssetDefinition, developers can specify an asset’s display name, icon, color-coding, and the logic that triggers when a user double-clicks or right-clicks the asset.

This module is essential for anyone creating custom data types, specialized tools, or plugins that require a professional, integrated look within the Unreal Editor.

Practical Usage Tips & Best Practices
1. Transition from AssetTypeActions

If you are upgrading a project from UE4, you should migrate your IAssetTypeActions logic to UAssetDefinition. The new system is more modular and uses a data-driven approach that is easier for the engine to load. Instead of registering actions in the module’s startup, the editor automatically discovers UAssetDefinition classes via the reflection system.

2. Inherit from UAssetDefinitionDefault

For most custom assets, do not inherit from the base UAssetDefinition. Instead, use UAssetDefinitionDefault. This base class provides sensible defaults for common operations, allowing you to only override the specific properties you need to change, such as the color or the associated class.

3. Organize with Asset Categories

Use the GetAssetCategories() function to place your asset in the correct right-click “Create” menu. You can use existing engine categories (like EAssetTypeCategories::Gameplay) or create a custom category for your project. This prevents your custom tools from being lost in the general “Misc” folder and helps eliminate UI clutter.

4. Define Asset Colors for Visual Filtering

Always override GetAssetColor(). Providing a unique color for your asset type (e.g., a specific shade of teal for a “Quest” asset) allows developers to quickly identify their files in a crowded folder. This visual shorthand is one of the most effective ways to improve team productivity in the Content Browser.

5. Implement Custom Double-Click Behavior

If your asset requires a specialized editor (rather than just the default Details panel), override GetAssetOpenConfig(). You can direct the editor to open a custom Toolkit or even trigger a specific function—such as launching a web URL or a specific level—when the asset is double-clicked.

6. Add Right-Click Context Actions

Use GetAssetActions() to add custom functionality to the right-click menu. This is ideal for utility functions like “Export to JSON,” “Validate Data,” or “Eliminate Unused References.” These actions can be gated by logic, ensuring they only appear when the asset is in a specific state.

7. Module Dependency Setup

Since this is an editor-only system, ensure the AssetDefinition module is added to your Editor module’s Build.cs. It should never be included in a runtime/game module.

C#
	if (Target.Type == TargetRules.TargetType.Editor)

	{

	    PublicDependencyModuleNames.AddRange(new string[] { "AssetDefinition", "UnrealEd" });

	}
Copy code
8. Specify Supported Classes

In your implementation, ensure GetAssetClass() returns the correct UClass. If your asset definition is meant to cover a base class and all its children, verify that your logic handles casting correctly. This ensures that a single definition can provide a consistent look for an entire hierarchy of custom data objects.