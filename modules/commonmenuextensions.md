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

ypically used in conjunction with CommonUI and the UI Extension system to enable modular, data-driven menu injection.

Description and Purpose

This module serves as a bridge between the CommonUI framework and the Modular Gameplay architecture (often seen in the Lyra Starter Game). It provides specialized Game Feature Actions that allow developers to dynamically “inject” UI elements—such as buttons, tabs, or widgets—into existing menu screens without modifying the base menu’s Blueprint or C++ code. Its primary purpose is to support extensible UI design, allowing different Game Feature Plugins to add their own unique settings, shop tabs, or inventory categories to a centralized “Frontend” or “Pause” menu automatically when the plugin is activated.

Practical Usage Tips and Best Practices
Use for “Add Widget” Game Feature Actions
The core strength of this module is the UGameFeatureAction_AddWidgets class. Use it to specify a UI Extension Point (a named slot in your menu) and the widget class you want to spawn there. This allows you to eliminate hard-coded references to specific DLC or feature-specific UI in your main menu.
Define Unique UI Extension Tags
This module relies heavily on FGameplayTag to identify “Extension Points.” Define a clear hierarchy for your tags (e.g., UI.ExtensionPoint.PauseMenu.SideBar). Using specific tags ensures that your injected widgets appear in exactly the right layout container and helps eliminate positioning errors.
Leverage Modular Data Assets
Combine this module with Primary Data Assets to define your menu entries. When a new gameplay feature is added, you simply create a new Data Asset and a Game Feature Action. This architecture ensures that when a feature is disabled, all associated menu buttons are automatically eliminated from the UI.
De-couple UI from Game Logic
Use the UI Extension Point system to keep your “Frontend” module clean. Your main menu shouldn’t know about the “Crafting System” or “Battle Pass.” By using CommonMenuExtensions, the “Crafting” plugin “tells” the menu to add a button, keeping your codebases completely decoupled and easier to maintain.
Manage Widget Lifecycle with Actions
The Game Feature Actions in this module handle the “Teardown” phase automatically. When a Game Feature is deactivated, the action will eliminate the injected widgets from the viewport or parent container. This is critical for preventing “ghost” buttons that point to deactivated code.
Dynamic Elimination Screen Customization
If you have a modular “Elimination Summary” screen, use this module to inject specific stats based on the active game mode. For example, a “Capture the Flag” plugin can inject a “Flag Captures” row into the standard elimination report UI only when that specific game mode is running.
Prioritize Injected Widgets
When multiple plugins inject widgets into the same slot, use the “Priority” or “Order” fields in the action settings. This ensures your “Quit Game” button stays at the bottom while “New Game” and “Load Game” remain at the top, helping you eliminate chaotic or unpredictable UI layouts.
Test with Modular Plugin Toggling
While the game is running in PIE, use the GFA.Toggle console command to activate and deactivate Game Features. Observe the menu in real-time to verify that injected widgets appear and are eliminated correctly without causing layout “pops” or focus issues.