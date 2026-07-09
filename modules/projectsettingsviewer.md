---
layout: default
title: ProjectSettingsViewer
---

<!-- ai-generation-failed -->

<h1>ProjectSettingsViewer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ProjectSettingsViewer/ProjectSettingsViewer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AIModule, Core, CoreUObject, DeveloperToolSettings, EditorFramework, Engine, EngineSettings, MoviePlayer, NavigationSystem, ProjectTargetPlatformEditor, SettingsEditor, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

user interface and management of the Project Settings window. It provides the framework for organizing setting categories (e.g., Engine, Project, Platforms) and handles the registration of custom settings classes so they appear in the searchable editor sidebar.

This module acts as the “front-end” for data stored in UDeveloperSettings or UConfig objects, ensuring that when a developer modifies a value in the UI, it is correctly serialized into the project’s .ini files.

Practical Usage Tips & Best Practices
1. Register Custom Settings via UDeveloperSettings

The most efficient way to utilize this module’s functionality is to derive your C++ settings classes from UDeveloperSettings.

Best Practice: By inheriting from UDeveloperSettings, your class is automatically discovered by the ProjectSettingsViewer. This ensures the elimination of manual registration code while providing a dedicated section for your plugin or game-specific configurations.
2. Use the Search Filter for Hidden Options

The Project Settings window contains thousands of properties, many of which are nested deep within sub-menus.

Tip: Use the search bar at the top of the window to find specific console variables or features (e.g., “Lumen” or “Nanite”). Utilizing the search results leads to the elimination of wasted time spent clicking through category tabs.
3. Leverage “Set as Default” for Team Sync

Changes made in the Project Settings are often stored in your local Saved/Config folder until explicitly saved to the project.

Best Practice: Click the Set as Default button at the top of a settings category to write those values into the DefaultEngine.ini or DefaultGame.ini in the Config/ folder. This facilitates the elimination of configuration discrepancies between different team members’ machines.
4. Export and Import Settings for Backups

The module provides a way to transfer settings between different projects or engine versions.

Tip: Use the Export… and Import… buttons to save a .ini snippet of your customized settings. This results in the elimination of manual re-entry when migrating complex rendering or input configurations to a new project.
5. Reveal Advanced Properties

To keep the UI clean, many technical properties are hidden behind a small “Advanced” arrow (a downward-facing chevron).

Best Practice: If you cannot find a specific low-level setting, click the “Advanced” toggle at the bottom of a section. Checking these hidden areas leads to the elimination of confusion when a feature appears to be missing from the UI.
6. Utilize the “Reset to Default” Yellow Arrow

Whenever a setting differs from the engine’s hardcoded default or the project’s config file, a small yellow arrow appears next to it.

Tip: Click this arrow to instantly revert a single property to its original state. This systematic revert process ensures the elimination of accidental performance degradation caused by experimental setting changes.
7. Organize Custom Categories with “CategoryName”

When writing a plugin, you don’t want your settings to be buried under a generic “Plugins” tab.

Best Practice: In your UCLASS macro for your settings, use the CategoryName="MyCategory" specifier. Properly categorizing your settings results in the elimination of UI clutter and makes your tools much more user-friendly for other designers.
8. Verify Permissions for Read-Only Configs

In a source-controlled environment (like Perforce), the ProjectSettingsViewer may be unable to save changes if the .ini files are not checked out.

Tip: Check the status bar at the bottom of the window. If it indicates the file is “Read-Only,” check out the Config/ folder files. Ensuring the files are writable leads to the elimination of “Failed to Save” errors and prevents the loss of your configuration changes.