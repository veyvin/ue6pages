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

er interface for managing asset lifecycles during critical operations. It is the system responsible for the “Save Content,” “Checkout from Source Control,” and “Delete Assets” dialog boxes that appear when a user attempts to save their work or close the editor.

This module acts as a centralized manager that aggregates a list of modified or targeted packages, checks their status against source control, and presents the user with a unified interface to decide which files should be committed to disk or the repository.

Practical Usage Tips & Best Practices
1. Access via the Module Manager

If you are building custom editor tools or automation scripts that need to trigger a save prompt for specific assets, you must access the module through the FModuleManager.

Best Practice: Use FModuleManager::LoadModuleChecked<IPackagesDialogModule>("PackagesDialog") to retrieve the interface. This ensures the elimination of crashes caused by calling dialog functions before the module is fully initialized in the editor environment.
2. Utilize FSavePackageArgs for Batch Operations

When programmatically calling the Save Packages dialog, you can pass a struct of arguments to define how the dialog behaves.

Tip: Use the FSavePackageArgs to toggle options like bAllowTooManyPackagesDialog. Setting these parameters correctly leads to the elimination of redundant confirmation popups when dealing with large batch operations (e.g., updating 100+ assets via a script).
3. Handle Source Control States Gracefully

The module automatically detects if a file is “Read-Only” or “Out-of-Date” and adds appropriate icons/checkboxes to the dialog.

Best Practice: Before invoking a save dialog from C++, ensure your source control provider is connected. Properly initializing the source control state results in the elimination of “Failed to Save” errors that occur when the user tries to save a file that is locked by another developer.
4. Customize Columns for Data Auditing

The Save Packages dialog is essentially a list view that can display more than just the asset name.

Tip: You can extend the dialog to show extra columns like “Size on Disk” or “Plugin Origin.” Providing this context facilitates the elimination of accidental saves to restricted plugins or large assets that might bloat the project’s repository.
5. Implement Validation Logic Before Saving

The PackagesDialog provides hooks to validate the list of packages before the user clicks “OK.”

Best Practice: Use an OnPostSaveWorld or similar delegate in conjunction with the dialog to check for naming convention violations. Automated checking leads to the elimination of “dirty” data being committed to the project by forcing a fix-up before the save is finalized.
6. Use for “Unsaved Changes” Trackers

This module is used by the engine to track which assets are currently “dirty” in memory compared to the version on disk.

Tip: If you are building a custom “Project Health” dashboard, you can query the same package state logic used by this module. This results in the elimination of data loss by alerting users to unsaved changes in hidden assets (like Data Assets or Curves) that they might have forgotten.
7. Differentiate Between “Save” and “Save As”

The module handles different logic flows for overwriting existing files versus creating new ones.

Best Practice: When creating custom save logic for a new asset type, ensure you use the PromptForAfterPackagesAreSaved flags. This ensures the elimination of logic loops where the editor keeps asking to save the same file repeatedly.
8. Verify User Cancellation

The functions in this module return a boolean or an enum indicating if the user clicked “Save Selected,” “Don’t Save,” or “Cancel.”

Tip: Always check the return value of CreateAndShowPackagesDialog. Failing to handle a “Cancel” result can lead to the elimination of your tool’s state consistency, as the code might proceed as if the save was successful when the user actually aborted the process.