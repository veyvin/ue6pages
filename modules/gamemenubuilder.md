---
layout: default
title: GameMenuBuilder
---

<!-- ai-generation-failed -->

<h1>GameMenuBuilder</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/GameMenuBuilder/GameMenuBuilder.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine, InputCore, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

tion of menu items, sub-menus, and navigation logic, ensuring that menus are consistent and respond correctly to keyboard, mouse, and gamepad inputs without manual focus management for every widget.

Primary uses include:

Hierarchical Menus: Creating nested menu structures (e.g., Main Menu > Options > Video Settings) through a clean C++ API.
Controller Support: Automating the “up/down/select” navigation logic essential for console and gamepad-driven interfaces.
Settings Menus: Generating lists of toggleable options, sliders, and multi-choice buttons for game configurations.
Rapid Prototyping: Building functional, navigable debug or utility menus in C++ before a final UMG design is implemented.
Practical Usage Tips and Best Practices
1. Implement via FGameMenuPage

When using this system, the core of your logic should reside in classes derived from FGameMenuPage. This class allows you to define the title and the collection of items. Use the AddMenuItem and AddSubMenu functions to populate the page, which leads to the elimination of manual coordinate-based widget placement.

2. Centralize Styles in FGameMenuStyle

The visual appearance of the menu is driven by an FGameMenuStyle struct. Instead of styling every button individually, define your colors, fonts, and textures in a single Slate Style Set. This ensures that changing a “Pressed” color in one location updates every menu in your game.

3. Leverage “Multi-Choice” for Settings

For settings like Resolution or Graphics Quality, use the built-in “Multi-Choice” menu items. This item type handles the cycling of options automatically, ensuring that when a player presses “Right” on the d-pad, the value increments and triggers a callback to your settings manager.

4. Handle Controller “Back” Navigation

The module is designed to handle the “Back” action (typically the B or Circle button) automatically if you have configured your sub-menus correctly. Always ensure your root menu page is set up to “Exit” the menu, while sub-pages are configured to “Return” to their parent, providing a seamless navigation flow.

5. Use Delegated Callbacks

Instead of hard-coding logic into the menu widgets, use FOnMenuStateChanged or custom delegates. When a menu item is clicked, it should fire an event that your PlayerController or GameInstance listens to. This separation of concerns ensures the elimination of tightly coupled UI and gameplay code.

6. Optimize for Performance

Since GameMenuBuilder is built on Slate, it is highly performant. However, avoid rebuilding the entire menu tree every frame. Build the menu hierarchy once during initialization and simply toggle visibility. This approach maintains a low CPU footprint even during complex screen transitions.

7. Combine with UMG for Visual Polish

While the logic is handled in C++ by the builder, you can still wrap these Slate widgets inside a UMG Widget using the SObjectWidget. This allows you to use the builder’s robust navigation logic while utilizing UMG for high-level layout, animations, and decorative elements.

8. Strategic Elimination of Focus Issues

One of the primary benefits of this module is its focus management. To ensure it works correctly, always use the FSlateApplication::Get().SetUserFocus or the SetInputModeGameAndUI nodes in tandem with the menu’s activation. This prevents the “mouse cursor disappears” or “gamepad doesn’t move” issues common in custom-built UI systems.