---
layout: default
title: PackagesDialog
---

<!-- ai-generation-failed -->

<h1>PackagesDialog</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/PackagesDialog/PackagesDialog.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, AssetRegistry, Core, CoreUObject, InputCore, Slate, SlateCore, SourceControl, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the standard user interface for managing multiple assets during critical operations like saving, checking out from source control, or deleting content.

Description and Purpose

This module is responsible for the “Save Content” and “Packages to Save” dialog boxes that appear when you close the editor or manually trigger a save. Its primary purpose is to provide a centralized, filtered list of modified or unsaved assets, allowing the user to select exactly which files should be committed to disk or source control. By using this module, the engine can eliminate the risk of accidental data loss by ensuring developers are explicitly aware of which “dirty” (modified) packages are currently in memory before a major operation occurs.

Practical Usage Tips and Best Practices
Access via IPackagesDialogModule
To trigger a custom save or checkout prompt in an editor plugin, load this module using FModuleManager::LoadModuleChecked<IPackagesDialogModule>("PackagesDialog"). This is the best way to eliminate the need to build a custom Slate list for asset management tasks.
Utilize for Custom Save Workflows
When creating a tool that modifies many assets at once (like a bulk renamer), use the CreatePackagesDialogConfig struct. This allows you to define exactly which assets are shown in the window, helping you eliminate confusion by only presenting the relevant modified files to the user.
Integrate with Source Control
The module automatically handles status icons for Source Control (e.g., Perforce or Git). If an asset is not checked out, the dialog will offer a “Check Out” button. Using this built-in logic is a best practice to eliminate “File is Read-Only” errors during the saving process.
Handle User Cancellation Gracefully
The dialog returns an ERefusedToSaveAction or a boolean result. Always check this return value in your code. If a user clicks “Cancel,” your script should stop immediately to eliminate the risk of continuing an operation on data that the user chose not to preserve.
Apply Filters to Large Asset Sets
If your operation affects hundreds of assets, use the configuration options to enable the “Filter” bar within the dialog. This allows users to search for specific assets by name or type, helping them eliminate the frustration of scrolling through a massive list to find a single important file.
Use for “Delete” Confirmation Logic
While primarily for saving, the underlying Slate widgets in this module are often used to show dependencies before an elimination of an asset. Use these dialogs to warn users if the asset they are trying to eliminate is still being referenced by other packages.
Set Clear Dialog Descriptions
When invoking the dialog through C++, you can set the Message and Title properties. Use clear, actionable language (e.g., “The following assets were modified by the cleanup script”) to eliminate ambiguity so the developer knows exactly why they are being prompted to save.
Avoid Frequent Pop-ups
To maintain a good developer experience, batch your asset modifications and trigger the PackagesDialog only once at the end of the process. This helps you eliminate “pop-up fatigue,” where users might reflexively click “Save All” without reviewing the changes due to too many interruptions.