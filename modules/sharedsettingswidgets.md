---
layout: default
title: SharedSettingsWidgets
---


<h1>SharedSettingsWidgets</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/SharedSettingsWidgets/SharedSettingsWidgets.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, ExternalImagePicker, InputCore, RHI, Slate, SlateCore, SourceControl, TargetPlatform</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

provides standardized components for building project settings and editor preference panels. It is primarily used to create consistent, high-quality user interfaces for complex settings that require more than just a simple text box or checkbox, such as external file path pickers or project summaries.

By utilizing these shared components, you can eliminate the need to reinvent common UI patterns, ensuring that your custom plugin or project settings feel like a native part of the Unreal Engine ecosystem.

Practical Usage Tips and Best Practices
Implement ‘SExternalImageReference’ for Icon Pickers
If your settings require a user to select an external image (like a project logo or splash screen), use the SExternalImageReference widget. This component handles the file path selection and provides a thumbnail preview, helping you eliminate the risk of users providing invalid file formats or missing assets.
Standardize with ‘SProjectSettingDetailSummary’
For complex settings pages, use the summary widget to provide a high-level overview of the configuration. This allows you to present the most critical variables at the top of the panel, helping you eliminate “information overload” for users navigating deep settings hierarchies.
Include the Module in Editor-Only Modules
Since this module relies on Slate and is intended for editor UI, you should add "SharedSettingsWidgets" to your PrivateDependencyModuleNames inside an Editor-only module. This helps you eliminate compilation errors when packaging the final game, as these widgets are not included in shipping builds.
Use for Standardized Path Management
Many widgets in this module are designed to handle FDirectoryPath and FFilePath types specifically for settings. They include built-in logic for relative vs. absolute paths, which helps you eliminate bugs related to hard-coded file paths when sharing projects across different machines.
Leverage for UDeveloperSettings Integration
When creating a class that inherits from UDeveloperSettings, you can use the widgets from this module in your DetailCustomization. This allows you to replace a standard property row with a specialized shared widget, helping you eliminate clunky, generic UI for specialized data types.
Maintain Visual Consistency
Always use these widgets for standard tasks like picking build targets or platform-specific icons. Reusing the engine’s internal UI components ensures that your tools follow the same spacing, font, and interaction rules as the rest of the editor, which helps you eliminate UX friction for other developers.
Handle Variable Elimination Gracefully
If you update your settings structure and a variable is removed (the “elimination” of a setting), ensure that the associated SharedSettingsWidget is properly unbound from the data source. Failing to refresh the UI can lead to “stale” widgets showing data that no longer exists in the configuration files.
Utilize Searchable Metadata
Widgets in this module are often designed to work with the settings search bar. Ensure your properties have proper DisplayName and ToolTip metadata in C++. This helps you eliminate the difficulty users face when trying to find a specific toggle in a large list of project configurations.