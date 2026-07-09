---
layout: default
title: PluginWarden
---

<!-- ai-generation-failed -->

<h1>PluginWarden</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/PluginWarden/PluginWarden.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, EditorFramework, Engine, InputCore, LauncherPlatform, PortalServices, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ce Asset Referencing Policies across a project’s plugin architecture. Its primary purpose is to act as a security and architecture “gatekeeper,” ensuring that modular features remain truly modular by preventing illegal references between plugins or between the engine and the project.

It is the backend engine that powers the Asset Referencing Policy settings in the Project Settings menu. When a developer attempts to save an asset that references a file in another plugin without a declared dependency, PluginWarden is the system that triggers the validation error and blocks the save.

Practical Usage Tips & Best Practices
1. Define Asset Referencing Domains

PluginWarden operates on “Domains,” which are rulesets that dictate what content a specific folder or plugin can see.

Best Practice: Organize your project into “Game Features” and “Core Content.” By assigning different domains to these, you ensure the elimination of accidental “monolithic” dependencies where every feature becomes entangled with the rest of the project.
2. Declare Plugin Dependencies Early

If Plugin A needs to use a material from Plugin B, Plugin A must explicitly list Plugin B as a dependency in its .uplugin file.

Tip: When you receive a “Cross-Plugin Reference” warning, don’t just ignore it. Adding the dependency properly in the Plugin Editor ensures the elimination of “Missing Asset” errors when packaging only a subset of your project’s features.
3. Use for DLC and Mod Validation

PluginWarden is critical when building DLC or allowing user-generated content (Mods).

Best Practice: Create a “Restricted” domain for your DLC plugins that prevents them from referencing “Work in Progress” or “Internal Only” engine content. This leads to the elimination of data mining leaks where unreleased assets are accidentally cooked into a public DLC package.
4. Configure “Project Content” as a Shared Root

By default, most projects allow plugins to reference the main Content/ folder but not other plugins.

Tip: Keep your foundational classes (like base PlayerControllers or GameModes) in the main project content folder. This setup facilitates the elimination of circular dependencies between modular plugins, as they all reference a stable, central root.
5. Leverage “Plugins Can Only Reference Game” Rule

This is the strictest mode of PluginWarden and is highly recommended for large teams.

Best Practice: Enable the rule that prevents plugins from referencing other plugins unless a hard dependency is set. Enforcing this strictly results in the elimination of the “spaghetti code” effect, where disabling one plugin causes a cascade of failures across the entire project.
6. Identify “Reference Leaks” via the Reference Viewer

When PluginWarden flags an illegal reference, it can sometimes be hard to find the specific node or property causing it.

Tip: Right-click the flagged asset and select Reference Viewer. Use the “Plugin Filters” to see exactly which line connects your asset to an illegal plugin. Finding these connections leads to the elimination of hidden hard references that bloat memory.
7. Override Policies for “Test” or “Editor” Folders

Sometimes you need to break the rules for debugging or cinematics.

Best Practice: Use the Project Settings to add an “Ignore” rule for folders named TestMaps or Developer. This allows developers to prototype freely while maintaining the elimination of illegal references in the actual shipping production folders.
8. Verify During Pre-Submit (CI/CD)

Since PluginWarden logic runs in the editor, it is possible for some illegal references to be forced in through external tools or text-based merges.

Tip: Run a commandlet in your CI/CD pipeline that invokes the AssetValidator. This ensures the elimination of “illegal” assets reaching your main branch by failing the build if PluginWarden’s rules are violated.