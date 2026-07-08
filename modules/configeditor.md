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

sed by developers and pipeline engineers to inspect how various settings are being merged across different layers of the config hierarchy. It provides a visual way to “eliminate” confusion regarding which specific .ini file is providing a value for a given property at runtime.

Practical Usage Tips and Best Practices
Editor-Only Module Dependency
The ConfigEditor is strictly for use within the Unreal Editor. When referencing it in your Build.cs, ensure it is wrapped in a check for Target.Type == TargetType.Editor. This ensures the dependency is “eliminated” during the packaging process for your shipping game.
Understand the Hierarchy Visualization
Use the Config Editor tool to see the “final” value of a property alongside the source file it originated from. This is the most effective way to “eliminate” bugs where a DefaultEngine.ini setting in your project is being unexpectedly overridden by a UserEngine.ini or a platform-specific config.
Leverage for Custom Project Settings
If you are creating custom classes that use the config and GlobalConfig UPROPERTY metadata, the ConfigEditor system automatically identifies these reflected properties. You can use it to verify that your custom settings are being correctly serialized to the intended .ini category (e.g., Game, Engine, or Input).
Differentiate Between User and Default Settings
A best practice is to use the ConfigEditor to ensure that team-wide settings are saved in Default*.ini (stored in the Config/ folder) while personal overrides are kept in User*.ini (stored in Saved/Config/). This helps “eliminate” merge conflicts in source control like Perforce or Git.
Use for Debugging Config “Bleed”
Sometimes settings from a plugin can “bleed” into the main project config. Use the ConfigEditor’s search functionality to find specific keys and “eliminate” redundant entries that might be bloating your configuration files and increasing engine initialization time.
Utilize Property Change Notifications
When a setting is changed through the ConfigEditor UI, the engine triggers PostEditChangeProperty. In your C++ classes, override this function to react to config changes in real-time. This allows you to “eliminate” the need to restart the editor to see the effects of a setting adjustment.
Check for Read-Only Status
If your project is under strict source control, configuration files may be marked as read-only. The ConfigEditor UI will typically indicate if a file is locked. Always ensure your .ini files are checked out before attempting to save changes through the editor to “eliminate” data loss.
Combine with Developer Settings
For a more polished experience, inherit your settings class from UDeveloperSettings. This integrates your configuration properties into the Project Settings menu, which utilizes the underlying logic of the ConfigEditor to provide a clean, searchable interface for your team.