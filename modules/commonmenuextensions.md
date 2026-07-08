---
layout: default
title: CommonMenuExtensions
---

<!-- ai-generation-failed -->

<h1>CommonMenuExtensions</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/CommonMenuExtensions/CommonMenuExtensions.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, Engine, InputCore, Slate, SlateCore, ToolMenus</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

on top of the ToolMenus system.

Description

In modern Unreal Engine versions (5.0+), the editor moved away from legacy Slate-only menu extensions toward the UToolMenus system. CommonMenuExtensions provides pre-configured logic for common UI extension tasks, such as adding entries to the Level Editor toolbar, the Content Browser context menu, or the Main Menu bar. It is used to ensure that custom plugins and editor tools can inject their functionality into the editor’s UI in a way that is consistent with Epic’s own internal tools, handling the “boilerplate” of menu registration and command binding.

Practical Usage Tips and Best Practices
1. Prefer ToolMenus over Legacy Delegates

Instead of manually finding extension points via the older FLevelEditorModule delegates, use the patterns found in this module. CommonMenuExtensions leverages the UToolMenus system, which allows menus to be dynamically rebuilt and modified via Python, Blueprints, or C++ without needing to restart the editor.

2. Use “Menu Context” for Dynamic Content

When extending a menu, always check the FToolMenuContext. This structure allows your menu extension to see what is currently selected (e.g., which Actors are selected in the viewport or which Assets are selected in the Content Browser). This is a best practice for eliminating irrelevant menu options—only show your “Fix Textures” button if the user actually has textures selected.

3. Register Extensions in StartupModule

To ensure your custom menu items appear as soon as the editor loads, place your registration logic inside the StartupModule() of your editor module. Use UToolMenus::RegisterStartupCallback to ensure the menu system is fully initialized before you attempt to inject your custom entries.

4. Leverage “Section” and “Entry” Hierarchy

Menus are organized into “Sections.” When adding an entry, don’t just add it to the bottom. Use the AddMenuEntry function to specify a Section Name. If you want your tool to appear near existing engine tools, look up the engine’s internal section names (like “FileProject” or “AssetContext”) to ensure your tool feels like a native part of the engine.

5. Debug with “ToolMenus.Edit 1”

If you are unsure where to inject your menu item, use the console command ToolMenus.Edit 1. This puts the editor into a special mode where you can click on any menu or toolbar to see its internal name and the names of its sections. This eliminates the guesswork involved in finding the correct “Hook” for your extension.

6. Use Icons from the Editor Style Set

To make your menu entries look professional, pull icons from the FAppStyle. When creating a FToolMenuEntry, specify the icon name (e.g., Default or Icons.Settings). This ensures your buttons match the visual language of the editor and scale correctly on high-DPI displays.

7. Safety Checks on Actor Elimination

If your menu extension performs actions on actors (such as a “Bulk Rename” tool), always verify that the actors are still valid and have not been eliminated or marked for destruction while the menu was open. Use IsValid(Actor) and check Actor->IsPendingKillPending() before executing your logic to eliminate potential crashes during batch operations.

8. Keep Callbacks Fast

Menu callbacks (the functions that run when you click a button) run on the Main Thread. If your tool needs to perform a heavy operation (like re-cooking assets or processing a large landscape), do not run it directly in the callback. Instead, trigger a background task or a notification with a progress bar. This prevents the editor UI from freezing, which is a key best practice for a smooth developer experience.