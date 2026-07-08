---
layout: default
title: DeveloperToolSettings
---

<!-- ai-generation-failed -->

<h1>DeveloperToolSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/DeveloperToolSettings/DeveloperToolSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, DeveloperSettings, InputCore, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

to handle the persistence and categorization of settings for internal developer tools and editor extensions. It provides a standardized way to define how various engine utilities (such as the Project Launcher, Device Manager, and Automation tools) store their configurations, ensuring that developer preferences remain consistent across sessions.

It acts as the backend for many of the “Developer” sub-menus in the Editor Preferences, facilitating the elimination of hard-coded tool configurations and allowing for modular, user-specific settings.

Practical Usage Tips and Best Practices
1. Inherit from UDeveloperSettings for Custom Tools

When building a custom editor tool, create a class that inherits from UDeveloperSettings. This automatically integrates your tool’s configuration into the Editor Preferences menu. This is a best practice for the elimination of custom, fragile .ini parsing logic for your tool’s settings.

2. Utilize the “Developer” Category

When defining your settings class, use the Category metadata (e.g., Category="Developer"). This ensures your tool’s options appear in the dedicated Developer section of the settings menu, aiding in the elimination of UI clutter by grouping technical tools away from general artist settings.

3. Leverage Automatic Persistence

Properties marked with UPROPERTY(Config) within a UDeveloperSettings class are automatically saved to the DefaultEditorPerProjectUserSettings.ini. This ensures the elimination of manual “Save” buttons, as the module handles writing the data to disk whenever the user modifies a value in the UI.

4. Use Per-User vs. Per-Project Scopes

Be careful when choosing your Config hierarchy. If a setting is personal (like a preferred debug IP), keep it in the “EditorPerProjectUserSettings” scope. This leads to the elimination of source control conflicts, as individual developer preferences won’t be committed to the shared project repository.

5. Implement OnSettingChanged Callbacks

Override the PostEditChangeProperty function in your settings class to respond immediately when a developer tweaks a value. This allows your tool to update its state in real-time (e.g., changing a debug draw color), facilitating the elimination of the need to restart the tool to see changes.

6. Support Backwards Compatibility

The module includes the UDeveloperSettingsBackwardsCompatibility utility. If you rename a setting or move it to a different class, use this system to migrate old values. This is essential for the elimination of “lost” settings when you update your internal pipeline tools.

7. Define Global Project Settings via Data Assets

For settings that must be shared across the entire team (like naming convention rules), derive from UDeveloperSettings but save them to DefaultEngine.ini. This ensures the elimination of “drift” between different team members’ environments by enforcing a single source of truth.

8. Modularize Tool UI with SectionNames

Use unique SectionName strings for each tool. This allows multiple different utilities within the same module to have their own distinct pages in the settings menu, leading to the elimination of giant, unreadable settings lists and improving navigation for your development team.