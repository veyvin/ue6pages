---
layout: default
title: AssetTagsEditor
---

<!-- ai-generation-failed -->

<h1>AssetTagsEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/AssetTagsEditor/AssetTagsEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

vides the framework for managing and visualizing User Asset Tags. While the Asset Registry handles the low-level metadata of files, this module focuses on the high-level management of custom, user-defined tags that can be applied to any asset in the project.

As of Unreal Engine 5.7, this module is integral to the Asset Tag Management system, allowing developers to categorize, filter, and organize content without changing the asset’s folder structure or modifying its core properties.

Practical Usage Tips and Best Practices
Scoping for Editor Tools Since this module relies on editor-specific UI and logic, it must only be included in your Editor.Build.cs. Including it in a runtime module will “eliminate” your build’s ability to package for external platforms.
C++
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AssetTagsEditor");

	}
Copy code
Utilize the Manage Tags Interface Access the management window by selecting an asset in the Content Browser and using the shortcut Ctrl + T. This interface allows you to view “Owned Tags” and “Project Tags,” providing a quick way to “eliminate” organizational clutter by batch-tagging assets.
Leverage Favorite Tags In the Manage Tags window, use the star icon to mark tags as “Favorites.” This makes them appear in the Local Asset Type Favorites section, which is context-sensitive. For example, favorites for Materials will be “eliminated” from view when you select Niagara assets, keeping your workspace clean.
Define Project-Wide Tags To standardize categorization across a large team, define tags in Project Settings > Editor User Asset Tags. This ensures that specific tags are always available for certain asset types, “eliminating” the risk of team members creating redundant or misspelled custom tags.
Search via the UAT Prefix You can filter the Content Browser using these tags with a specific syntax. Type UAT.TagName="" in the search bar. While the editor helps auto-complete the prefix, manually adding the ="" ensures the search logic correctly identifies the user asset tag.
Transition to Collection Manager for Scripting Be aware that many legacy tagging functions in the AssetTagsSubsystem are being deprecated. For automated asset organization via C++ or Python, transition your logic to the Collection Manager Scripting Subsystem to ensure your scripts are not “eliminated” by future engine updates.
Avoid Using Tags for Critical Gameplay Logic User Asset Tags are intended for editor organization and pipeline tools. Do not rely on them for high-performance runtime logic; instead, use AssetRegistrySearchable properties or Data Assets to “eliminate” the performance overhead of querying editor-level metadata during gameplay.
Audit Permutation Risks with HSPR Tags In the Material system specifically, use the “Has Static Permutation Resource” (HSPR) tag managed through this ecosystem to identify Material Instances that are causing shader permutations. This is the fastest way to “eliminate” unnecessary shader draw calls by finding instances that have unnecessary static switches enabled.