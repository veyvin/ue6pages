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

for the legacy AssetTypeActions system. It provides a C++ framework to define how custom asset types appear, are categorized, and behave within the Content Browser and the wider Unreal Editor ecosystem.

What it is and What it’s used for

The UAssetDefinition class serves as the “identity” of a custom UObject-based asset in the editor. While the object itself holds the data, the Asset Definition tells the editor how to handle it.

Primary uses include:

Editor Visuals: Setting the asset’s display name, icon, and color coding in the Content Browser.
Organization: Assigning assets to specific categories or sub-categories in the “Create New Asset” (Right-click) menu.
Discovery: Providing the Asset Registry with metadata needed to filter and identify specific asset types without loading them.
Workflow Entry Points: Defining which editor opens when an asset is double-clicked and adding custom right-click context menu actions.
Practical Usage Tips and Best Practices
1. Inherit from UAssetDefinitionDefault

For most custom assets, inherit from UAssetDefinitionDefault. This provides standard implementations for common behaviors like opening the default Details-based editor, allowing you to focus only on visual overrides.

2. Leverage Automatic Registration

Unlike the legacy system, you do not need to manually register UAssetDefinition classes in your module’s StartupModule. The UAssetDefinitionRegistry automatically scans for all classes derived from UAssetDefinition and registers them during editor startup.

3. Use FAssetCategoryPath for Better Menus

UE5’s AssetDefinition supports hierarchical categories. Instead of a single bitmask, GetAssetCategories returns an array of paths. Use this to keep your studio’s assets organized: FAssetCategoryPath(INVTEXT("Systems"), INVTEXT("SubsystemName"))

4. Define Custom Context Actions

To add specific functionality to the right-click menu (e.g., “Export to JSON” or “Bake Data”), override GetContextMenuActions. This is more modular and performant than the old FAssetTypeActions approach.

5. Control Asset Activation

If your asset requires a specialized editor (like a Graph Editor or a custom Viewport), override GetAssetOpenSupport. You can return EAssetActivationMethod::Open to launch your custom FAssetEditorToolkit.

6. Support Source File Tracking

If your asset is generated from external data (like an FBX or CSV), use GetSourceFiles to inform the editor of the relationship. This enables the “Reimport” functionality and allows the editor to watch those files for external changes.

7. Performance: Avoid Asset Loading

The virtual functions in UAssetDefinition are called frequently by the Content Browser. Ensure your implementations are fast. If you need to check asset state, use the FAssetData provided in some overrides rather than calling GetAsset(), which would force a slow load of the object.

8. Module Placement

Always place your UAssetDefinition classes in an Editor Module. These classes rely on Developer and UnrealEd modules that are stripped out of shipping builds. Attempting to include them in a Runtime module will cause packaging failures and eliminate your ability to compile a shipping build.