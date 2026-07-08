---
layout: default
title: EditorSettingsViewer
---

<!-- ai-generation-failed -->

<h1>EditorSettingsViewer</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/EditorSettingsViewer/EditorSettingsViewer.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, BlueprintGraph, Core, CoreUObject, CurveEditor, DeveloperToolSettings, EditorFramework, Engine, GraphEditor, InputBindingEditor, InternationalizationSettings, MessageLog, SettingsEditor, Slate, SlateCore, ToolMenus, UnrealEd, VREditor</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

the Slate-based user interface, allowing developers to navigate and modify the properties of UDeveloperSettings or UObject classes within a structured, searchable menu.

This module is essential for making your custom tool configurations accessible to the rest of the team, facilitating the elimination of hard-coded variables by exposing them through a user-friendly interface.

Practical Usage Tips and Best Practices
1. Register Sections via ISettingsModule

To make your settings appear in the viewer, use the ISettingsModule found in the Settings module. You must specify the container name (e.g., “Project” or “Editor”), the category, and the section. This registration is the standard path for the elimination of manual UI coding for your tool’s configuration pages.

2. Use “Show Only Modified” for Debugging

The viewer includes a “Show Only Modified” checkbox. When troubleshooting why a project is behaving differently on two machines, use this filter to see only settings that differ from the defaults. This assists in the elimination of time spent hunting through hundreds of unchanged variables.

3. Leverage the Search Filter for Faster Navigation

The search bar in the EditorSettingsViewer supports metadata filtering. You can search for specific property names or tooltips. Instructing your team to use this feature leads to the elimination of friction when finding deep-nested settings like “Virtual Shadow Maps” or “Lumen Ray Tracing” toggles.

4. Support “Restart Required” Metadata

If your custom setting requires an engine restart to take effect (such as an RHI change), use the ConfigRestartRequired = true metadata in your C++ UPROPERTY. The viewer will automatically display a notification to the user, facilitating the elimination of “silent” configuration failures where the user thinks the change has applied when it hasn’t.

5. Organize with Sub-Categories

When registering your section, use the dot notation in the category name (e.g., “MyTool.Advanced”). The viewer will intelligently group these under a common header. Proper organization in the viewer leads to the elimination of a cluttered, unreadable root settings list for your project.

6. Utilize the “Reset to Default” Button

Every property in the EditorSettingsViewer has a yellow “Reset to Default” arrow. If a developer accidentally breaks a tool’s configuration, using this button restores the value defined in the BaseEditor.ini or C++ constructor, aiding in the elimination of “corrupt” settings-related bugs.

7. Secure Shared Settings in DefaultEngine.ini

Properties displayed in the viewer that are marked as Config but not GlobalConfig may save to a user’s local Optional.ini. If a setting must be the same for all developers, ensure it is registered to save in DefaultEngine.ini. This practice ensures the elimination of “it works on my machine” issues within the team.

8. Implement Custom Detail Rows

If your settings page requires more than just basic checkboxes or text fields, you can use the FDetailCustomization system alongside the viewer. This allows you to inject custom Slate widgets (like a “Generate Keys” button) into the settings row, leading to the elimination of secondary, redundant setup windows for your tools.