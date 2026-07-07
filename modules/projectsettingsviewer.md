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

he core user interface and navigation framework for the Project Settings window in Unreal Engine.

Description and Purpose

This module acts as the UI bridge between the engine’s internal configuration files (.ini) and the developer. It implements the ISettingsViewer interface to create the searchable, categorized list of settings found under Edit > Project Settings. Its primary purpose is to dynamically generate settings categories based on registered classes and provide a unified interface for modifying everything from input mappings to rendering features. By centralizing these controls, the module helps eliminate the need for developers to manually edit text-based configuration files, reducing the risk of syntax errors or invalid property values.

Practical Usage Tips and Best Practices
Register Custom Settings Classes
If you are developing a plugin, you can add your own section to the Project Settings by using the ISettingsModule. Registering your custom UObject allows the ProjectSettingsViewer to automatically generate a UI for your plugin, helping you eliminate the work of building custom Slate windows for configuration.
Use the Search Filter for Faster Navigation
The viewer includes a robust search bar. Instead of clicking through categories, type the specific CVar or property name (e.g., “Lumen” or “Allow Static Lighting”). This is the best way to eliminate time wasted searching through the dozens of available categories and sub-sections.
Utilize the “Export/Import” Feature
In the top-right of the window, you can export your current settings to a .ini file. This is a best practice to eliminate the manual effort of replicating complex project configurations (like custom Collision Channels or Input Actions) when starting a new project.
Identify Modified Settings (Yellow Bar)
The viewer displays a yellow vertical bar next to any setting that has been changed from its default value. Use this visual cue to eliminate confusion when debugging; if a project is behaving unexpectedly, look for these indicators to see what has been modified from the engine’s factory defaults.
Understand the “Restart Required” Prompt
Some settings require a full editor restart to take effect (indicated by a prompt at the bottom). Do not ignore these; attempting to work without restarting can cause the viewer to display incorrect data, which is a common way to eliminate hours of productivity due to “ghost” bugs.
Leverage Per-Platform Overrides
For mobile or console projects, look for the “plus” or “platform” icons next to specific settings. The viewer allows you to set different values for different hardware targets. Properly configuring these overrides helps you eliminate performance issues on weaker platforms while maintaining high quality on PC.
Reset to Default via the “Arrow” Icon
If you have experimented with settings and caused visual issues, click the small “yellow arrow” icon next to a modified property. This will immediately eliminate the custom value and revert it to the engine default, providing a safe “undo” mechanism for project-wide configurations.
Verify Source Control Status
The Project Settings window integrates with the Perforce and Git modules. If your configuration files are not checked out, a warning will appear. Ensure your settings files are writable to eliminate the frustration of losing changes because the viewer could not save to a read-only .ini file.