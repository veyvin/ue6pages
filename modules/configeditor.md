---
layout: default
title: ConfigEditor
---

<!-- ai-generation-failed -->

<h1>ConfigEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ConfigEditor/ConfigEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, PropertyEditor, Slate, SlateCore, SourceControl, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ings windows.

This module acts as a wrapper for the engine’s underlying GConfig system, allowing developers to “eliminate” the need for manual text editing of .ini files. It handles the complex hierarchy of configuration files (Base, Default, and Saved) and ensures that changes made in the UI are correctly serialized to the appropriate DefaultEngine.ini, DefaultGame.ini, or other configuration targets.

Practical Usage Tips and Best Practices
Leverage UPROPERTY(Config) for Custom Settings
To expose your own C++ variables to the ConfigEditor, mark them with the Config specifier in your UPROPERTY macro. This allows the ConfigEditor to “eliminate” the manual work of creating a custom UI, as it will automatically generate an entry in the Project Settings for that class.
Identify Overridden Settings via the Indicator
The ConfigEditor displays a small icon next to settings that have been modified from their default values. Use this to quickly “eliminate” confusion regarding which settings are project-specific versus those inherited from the base engine.
Manage Source Control Checkouts
When you modify a setting in a project integrated with Perforce or Git, the ConfigEditor will automatically attempt to check out the relevant .ini file. A best practice is to “eliminate” the risk of “exclusive checkout” errors by ensuring your team is aware that modifying Project Settings locks the DefaultEngine.ini file.
Use the Property Matrix for Mass Config Edits
If you need to change settings for multiple objects that share a config-based class, you can often use the Property Matrix via the ConfigEditor’s backend. This “eliminates” the repetitive task of opening individual assets to change shared configuration values.
Export and Import for Profile Sharing
In the top-right corner of the Project Settings window (driven by ConfigEditor), you can Export your settings to a configuration file. This is a best practice for “eliminating” setup time when moving to a new machine or sharing specific rendering/input profiles with another team member.
Understand the “Saved” vs. “Default” Distinction
The ConfigEditor distinguishes between “Default” settings (shared with the team) and “Saved” settings (local to your machine). To “eliminate” accidental local overrides being pushed to others, ensure you are editing the “Project” category rather than “Editor” or “User” settings when making global changes.
Utilize the Search Filter to Find Obscure Settings
The search bar at the top of the Project Settings is highly optimized. Use it to “eliminate” manual scrolling through the hundreds of available categories. It searches both the display names and the underlying C++ variable names.
Reset to Default for Troubleshooting
If a project’s behavior becomes unstable due to accidental config changes, the ConfigEditor provides a “Reset to Default” button for many properties. This “eliminates” the need to manually delete lines in the .ini file and ensures the value returns to its original engine-stable state.