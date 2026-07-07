---
layout: default
title: ToolMenusEditor
---

<!-- ai-generation-failed -->

<h1>ToolMenusEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/ToolMenusEditor/ToolMenusEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, InputCore, Slate, SlateCore, ToolMenus, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

terface and specialized tools for customizing, extending, and debugging the ToolMenus framework within the Unreal Engine.

Description and Purpose

While the base ToolMenus module handles the logic of creating menus and toolbars, ToolMenusEditor provides the “visual” side and developer utilities. Its primary purpose is to power the Menu Editor (an interactive UI for rearranging menu items) and to provide the Slate widgets and commands needed to modify the Unreal Editor’s interface. By utilizing this module, developers can eliminate the complexity of manually searching for menu paths, allowing them to visually identify and inject new buttons or submenus into existing layouts like the Level Editor toolbar or the Content Browser context menu.

Practical Usage Tips and Best Practices
Toggle the Visual Menu Editor via CVar
You can enable the interactive menu editing mode by entering ToolMenus.Edit 1 in the console. This adds gear icons next to every toolbar and menu in the editor, allowing you to eliminate guesswork when trying to find the exact internal name of a specific menu section.
Use the “Copy Name” Feature for Customization
When the Menu Editor is active, clicking the gear icon allows you to “Copy Name” of a menu or entry. Use this name in your C++ or Blueprint code to eliminate path errors when calling ExtendMenu or AddMenuEntry.
Initialize in a Dedicated Editor Module
Always place your menu customization logic within an editor-specific module (Type: Editor in your .uplugin or .uproject). This ensures your menu extensions are only loaded when the editor is active, helping you eliminate linker errors in standalone or shipping builds.
Leverage Metadata for Icons and Styling
The ToolMenusEditor respects Slate Style metadata. When adding entries, ensure you provide a valid FSlateIcon and Style Set. This is a best practice to eliminate the default “white square” icon, ensuring your custom tools look native to the Unreal interface.
Filter and Organize with Section Names
When extending a menu, don’t just add an entry to the end. Use AddSection to create a named category for your tools. This helps the editor’s search and organization logic, allowing users to eliminate visual clutter when looking for specific plugin commands.
Use Startup Objects for Automatic Registration
For Blueprint-based editor tools, you can add your EditorUtilityToolMenuEntry assets to the Startup Objects list in the Editor Utility Subsystem settings. This ensures the ToolMenusEditor registers your buttons every time the engine starts, helping you eliminate the need to manually run a script to see your UI.
Refresh Menus after Dynamic Changes
If your code adds menu items based on a runtime condition (like a project setting), call UToolMenus::Get()->RefreshAllWidgets(). This forces the editor to rebuild the UI, which will eliminate instances where new buttons fail to appear until the editor is restarted.
Debug with the “Menu Name” Search
If you are unsure where a menu exists, use the Widget Reflector (Tools > Debug > Widget Reflector). By hovering over a menu, you can see the underlying Slate structure, which helps the ToolMenusEditor logic eliminate target ambiguity for deeply nested submenus.