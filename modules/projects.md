---
layout: default
title: Projects
---

<!-- ai-generation-failed -->

<h1>Projects</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Projects/Projects.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, DesktopPlatform, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ng descriptor files for both projects (.uproject) and plugins (.uplugin). It provides the low-level API needed to query metadata about the currently loaded project, discover installed plugins, and determine module loading phases.

This module acts as the “source of truth” for the engine’s structure at startup. By using its interfaces, developers can programmatically check version numbers, find file paths for active plugins, or identify which modules are enabled. This facilitates the elimination of hard-coded paths and manual file-searching logic within your C++ tools and systems.

Practical Usage Tips and Best Practices
1. Access Project Metadata via IProjectManager

Use IProjectManager::Get().GetCurrentProject() to retrieve a FProjectDescriptor. This allows you to programmatically access information defined in the .uproject file, such as the ProjectName, EngineAssociation, or custom attributes. This leads to the elimination of manual string-parsing for project-wide settings.

2. Query Plugins with IPluginManager

The IPluginManager is the most common interface used from this module. Use IPluginManager::Get().FindPlugin(TEXT("PluginName")) to get a pointer to a IPlugin object. This is essential for the elimination of “Missing Plugin” errors when your code depends on another plugin being present and enabled.

3. Locate Plugin Content via GetContentDir

Once you have an IPlugin reference, use GetContentDir() to find the absolute disk path to that plugin’s assets. This practice assists in the elimination of broken file references in C++ code that needs to load specific loose files or configuration data stored within a plugin’s folder.

4. Check for Content Availability

Before attempting to load assets from a plugin, check IPlugin::CanContainContent(). The Projects module stores this flag based on the .uplugin descriptor. Verifying this leads to the elimination of runtime crashes when code attempts to mount a content path for a “code-only” plugin that does not support assets.

5. Filter Plugins by Type or Group

You can use GetDiscoveredPlugins() to iterate through all plugins and filter them by their Descriptor.Category or Type (Engine vs. Project). This facilitates the elimination of manual plugin lists when building custom editor tools that need to act on specific classes of plugins (e.g., all “Localization” plugins).

6. Identify the Main Project Module

The FProjectDescriptor contains a list of modules defined for the project. Querying this list allows you to find the “Primary” module name dynamically. This is useful for the elimination of hard-coded module strings in systems that need to perform reflection or class-loading tasks based on the project’s own code.

7. Verify Module Dependencies in Build.cs

While the Projects module handles the descriptors, you must ensure your Build.cs includes "Projects" in its dependencies to use these C++ interfaces. Including it correctly leads to the elimination of linker errors when trying to access IPluginManager or IProjectManager from your game or editor module.

8. Use for Version Checking

The .uplugin file often contains a VersionName and Version integer. Use the Projects module to compare these values at startup. This assists in the elimination of compatibility issues by allowing your code to warn the user or disable features if a required plugin version is too old for the current project state.