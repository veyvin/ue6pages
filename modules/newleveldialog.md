---
layout: default
title: NewLevelDialog
---

<!-- ai-generation-failed -->

<h1>NewLevelDialog</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/NewLevelDialog/NewLevelDialog.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, Slate, SlateCore, ToolWidgets, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rface and logic for the “New Level” window (typically accessed via File > New Level or Ctrl+N). It provides the framework for displaying level templates, handling user selection, and initializing the creation of new world assets based on specific configurations.

This module acts as a gatekeeper for level creation, ensuring that new maps are instantiated with the correct default actors (such as lighting, sky atmosphere, or world partition settings). By standardizing how templates are presented and loaded, it facilitates the elimination of manual level setup tasks, allowing developers to start with a consistent, functional environment.

Practical Usage Tips and Best Practices
1. Add Custom Templates via Configuration

You can expand the list of available templates by adding entries to your project’s DefaultEditor.ini. Specifying custom map paths here leads to the elimination of the need for developers to manually browse for “starting point” levels, as they will appear directly in the New Level dialog.

2. Utilize the /Engine/Maps Directory

The module is hardcoded to look for several default engine templates. If you are building a custom engine fork, placing your base templates in the Engine/Content/Maps/Templates directory ensures they are automatically discovered. This practice facilitates the elimination of broken template links when sharing the engine across a large team.

3. Programmatic Invocation in C++

If you are building a custom editor extension or a project wizard, you can trigger the dialog by calling FNewLevelDialogModule::CreateAndShowNewLevelDialog. This ensures that your custom workflow remains consistent with the standard Unreal Engine UX, leading to the elimination of confusing, non-standard level creation popups.

4. Handle World Partition Initialization

The New Level dialog provides specific options for “Open World” vs. “Basic” levels. The module contains logic to initialize the World Partition system if the user selects an Open World template. Ensuring your custom templates have the correct bEnableWorldPartition flag set in their WorldSettings assists in the elimination of manual partition setup after the level is created.

5. Include in Editor-Only Dependencies

The NewLevelDialog module is part of the Editor’s private API. When referencing it in your code, you must include it in the PrivateDependencyModuleNames section of your Editor.Build.cs. This is essential for the elimination of compilation errors, as this module is not available in runtime or non-editor builds.

6. Leverage for Project-Specific Workflows

For large-scale productions, you can modify the module logic to force certain templates based on the current project branch. Implementing logic that filters the available templates leads to the elimination of “illegal” level configurations that don’t adhere to your project’s technical requirements (e.g., forcing a specific lighting setup).

7. Verify Template Asset Validity

Before showing a template in the dialog, the module checks if the map asset exists and is loadable. Regularly auditing your template directory leads to the elimination of “Missing Asset” errors that can occur if a template level was renamed or moved without updating the editor configuration files.

8. Use for “Elimination” of Empty Level Overhead

Encourage your team to use the “Empty Level” option in the dialog when starting technical tests. This template is designed for the elimination of all default actors, providing a clean slate that prevents performance data from being skewed by unnecessary atmospheric actors or default lighting setups.