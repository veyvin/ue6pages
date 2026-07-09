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

ch as a Pause Menu that can open a Sub-Menu or a Confirmation Popup) by handling focus management, input routing, and the “Back” button behavior automatically.

Practical Usage Tips & Best Practices
1. Use the Common Activatable Widget Stack

The core of this module is the CommonActivatableWidgetStack. Instead of manually adding or removing widgets from the viewport, push your menus onto this stack.

Best Practice: When you push a new menu (like an Options screen) onto the stack, the module automatically handles the elimination of input focus from the underlying menu, preventing accidental clicks on background elements.
2. Define Clear Input Action Data

The module relies heavily on Common Input Data assets.

Tip: Ensure your “Back” and “Confirm” actions are correctly mapped in your Data Table. The CommonMenuExtensions logic uses these to automatically close the top-most widget on the stack when the “Back” button is pressed, saving you from writing custom “On Key Down” logic in every Blueprint.
3. Leverage “Auto-Activate” for Sub-Menus

When a widget is added to a menu stack managed by this module, it can be set to “Auto-Activate.”

Best Practice: Set your main menu screens to Auto-Activate so that they immediately seize input focus when they appear. This ensures a seamless transition for gamepad users who need immediate cardinal navigation.
4. Implement Proper “Close” Logic

To remove a menu from the stack, call the Deactivate function on the widget rather than RemoveFromParent.

Tip: The module waits for any transition animations to finish before the final elimination of the widget from the stack. This prevents visual “popping” and ensures that the focus returns smoothly to the previous menu in the history.
5. Use Bound Actions for Contextual UI

One of the most powerful features is the ability to bind UI actions to specific buttons that only exist while the menu is active.

Best Practice: Use the BindAction nodes to create “Prompt” icons (e.g., “Press [X] to Save”). The module handles the visibility and interactivity of these prompts, ensuring they are automatically cleaned up when the user exits the menu.
6. Handle Character Elimination in the UI

If your game features a “Death Screen” or “Respawn Menu,” use an Activatable Widget for this purpose.

Tip: When a character elimination event occurs, push the “Eliminated” widget onto the stack. By setting its Input Config to All, you can block all gameplay inputs (like movement or shooting) while the player is interacting with the respawn menu.
7. Optimize Performance with “Hidden” vs “Deactivated”

The CommonMenuExtensions logic allows background menus to remain in memory but stop ticking or responding to input.

Best Practice: Don’t destroy menus that the player toggles frequently (like a Map). Instead, keep them in the stack and let the module manage their activation state. This results in the elimination of loading hitches when the player rapidly opens and closes the UI.
8. Debug Focus with “CommonUI.Debug.Trace”

If you find that your gamepad navigation isn’t working or the “Back” button isn’t responding, use the console command CommonUI.Debug.Trace 1. This provides a visual overlay showing exactly which widget currently holds the “Activation” and which stack is routing the input, making it easy to spot where the focus was lost.