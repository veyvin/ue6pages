---
layout: default
title: SourceControlWindows
---

<!-- ai-generation-failed -->

<h1>SourceControlWindows</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/SourceControlWindows/SourceControlWindows.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AssetDefinition, AssetTools, Core, CoreUObject, DeveloperToolSettings, EditorFramework, Engine, InputCore, Projects, PropertyEditor, Slate, SlateCore, SourceControl, ToolMenus, ToolWidgets, UncontrolledChangelists, UnrealEd, UnsavedAssetsTracker, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

nd dialogs used for version control operations within the Unreal Editor. While the core SourceControl module handles the backend logic (communicating with Perforce, Git, or Subversion), this module handles the visual representation, including the Submit Files Dialog, the Changelist Manager, and the History View.

It is primarily used by tools developers to integrate revision control workflows into custom editor windows. By leveraging these existing UI classes, you can eliminate the need to build complex submission or file-locking interfaces from scratch, ensuring your custom tools maintain a consistent look and feel with the rest of the editor.

Practical Usage Tips and Best Practices
Invoke the Global ‘Submit Files’ Dialog
If your custom tool generates multiple new assets (like a batch processor), use this module to trigger the standard SSubmitFilesDialog. This allows the user to review their changes and write a description in a familiar interface, helping you eliminate accidental “ghost” commits that lack proper documentation.
Integrate with the Changelist Manager
Use the components in this module to display “Uncontrolled Changelists” within your custom tool. This is particularly useful for world-building tools where you want to show which actors are currently modified, helping you eliminate confusion over which files are ready for check-in.
Utilize ‘SRevisionControlStatusWidget’
Instead of writing custom logic to show if a file is “checked out” or “out of date,” use the standard status widgets. These automatically update based on the state of the revision control provider, which helps you eliminate UI synchronization bugs in your custom asset browsers.
Leverage Submit Validation Logic
This module interfaces with the Data Validation plugin. Before allowing a submission, the dialog can trigger validation scripts to check for naming conventions or performance budgets. Using this built-in flow helps you eliminate broken assets from entering the main project branch.
Implement Custom ‘Check-In’ Filters
When calling the submission dialog from C++, you can pass a list of files to be filtered or pre-selected. Providing a focused list to the user helps them eliminate irrelevant files from their current task’s changelist, streamlining the collaboration process.
Use the History Window for Diffing
If your tool manages complex data assets, you can programmatically open the Revision History window from this module. This allows users to compare different versions of an asset, helping them eliminate regressions by identifying exactly when a specific change was made.
Handle Login Prompts Gracefully
The module includes the UI for the “Login” and “Connection Settings” dialogs. If your tool detects that the source control connection is lost, triggering these standard prompts helps you eliminate technical barriers for artists who may not realize they have been disconnected from the server.
Unbind Delegates on Widget Elimination
When your custom editor tab is closed (the “elimination” of your tool’s UI), ensure you unregister any delegates that listen for source control state changes. Failing to clean up these listeners can cause the editor to try and update a non-existent widget, which you must eliminate to prevent memory leaks and crashes.