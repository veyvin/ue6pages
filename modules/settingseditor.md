---
layout: default
title: SettingsEditor
---

<!-- ai-generation-failed -->

<h1>SettingsEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/SettingsEditor/SettingsEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, DesktopPlatform, DeveloperSettings, EditorWidgets, Engine, InputCore, PropertyEditor, SharedSettingsWidgets, Slate, SlateCore, SourceControl, ToolMenus, ToolWidgets</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

graphical interface for viewing, searching, and modifying configuration settings within Unreal Engine.

Description and Purpose

While the Settings module handles the underlying data and registration of settings, the SettingsEditor module provides the Slate-based front-end (specifically the SSettingsEditor widget) used in the Project Settings and Editor Preferences windows. Its primary purpose is to automatically generate a user-friendly interface based on the properties of a UObject. It handles categories, search filtering, and the “Modified” indicators (the yellow bars). By utilizing this module, developers can eliminate the need to write custom Slate code for every configuration menu, as the module dynamically builds the UI by reflecting the UPROPERTY macros defined in C++ or Data Assets.

Practical Usage Tips and Best Practices
Utilize the ISettingsEditorModule Interface
To open a specific settings category via code, access the ISettingsEditorModule. You can use the ShowSettings function to programmatically navigate the user to a specific section, which is a best practice to eliminate confusion when a user needs to find a plugin’s configuration quickly.
Group Properties with Categories
Use the Category specifier in your UPROPERTY macros (e.g., UPROPERTY(Config, EditAnywhere, Category="General|Performance")). The SettingsEditor uses the pipe | symbol to create sub-sections in the UI, helping you eliminate cluttered, flat lists of variables.
Add Tooltips for Clarity
The module automatically pulls the C++ comment above a property and displays it as a tooltip in the editor. Always write descriptive comments to eliminate the need for external documentation; the user can simply hover over the setting to understand its impact.
Use Config and GlobalConfig Flags
For a variable to appear and persist through the SettingsEditor, it must be marked with the Config or GlobalConfig keyword. This ensures that when a user changes a value in the UI, the module knows which .ini file to update, helping you eliminate manual file-handling errors.
Leverage Console Variable Integration
You can link settings directly to Console Variables (CVars) using the ConsoleVariable="r.MyCVar" metadata. This allows the SettingsEditor to update the engine’s state in real-time when the slider is moved, which helps you eliminate the need for a manual “Apply” button or a restart.
Implement PostEditChangeProperty for Validation
If changing a setting requires an engine refresh (like reloading a texture), override PostEditChangeProperty in your settings class. The SettingsEditor will trigger this event, allowing you to eliminate invalid states by clamping values or restarting dependent subsystems immediately.
Support Search with Metadata
If a setting has a non-obvious name, use the Keywords="alias, nickname" metadata. The SettingsEditor search bar scans these keywords, which is a great way to eliminate friction for users who might use different terminology to find a specific feature.
Use EditCondition for Contextual Settings
Hide advanced or irrelevant settings using EditCondition. By making certain properties visible only when a specific boolean is true, the SettingsEditor stays clean and organized, which helps to eliminate user errors caused by modifying settings that have no current effect.