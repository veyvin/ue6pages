---
layout: default
title: InputBindingEditor
---

<!-- ai-generation-failed -->

<h1>InputBindingEditor</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/InputBindingEditor/InputBindingEditor.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DeveloperSettings, EditorFramework, Engine, InputCore, PropertyEditor, Settings, SettingsEditor, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

igger commands within the Unreal Editor environment.

What it is and What it’s used for

Located in Engine/Source/Editor/InputBindingEditor, this module provides the functional area within the Editor Preferences window where users can view and modify shortcut mappings. It interfaces directly with the engine’s FUICommandRegistry to discover all registerable actions across the engine and loaded plugins.

Primary uses include:

Shortcut Customization: Providing the UI for users to search, rebind, or clear keyboard shortcuts for editor actions.
Conflict Detection: Identifying and alerting the user when a newly assigned key combination overlaps with an existing command.
Binding Persistence: Managing the serialization of custom user bindings into the EditorKeyBindings.ini configuration file.
Import/Export Logic: Enabling the migration of shortcut profiles between different team members or engine installations.
Practical Usage Tips and Best Practices
1. Register Commands via FUICommandList

When creating custom editor tools or plugins, do not hardcode key checks in your input logic. Instead, register your actions as FUICommands. This allows the InputBindingEditor to automatically “see” your commands, giving users the freedom to customize them to their own workflow.

2. Utilize the Search Filter for Discovery

The Keyboard Shortcuts window can be overwhelming due to the thousands of commands available. Use the search bar at the top of the window to filter by specific plugins or categories (e.g., “Sequencer” or “Modeling”). This is a best practice for the elimination of time wasted scrolling through irrelevant categories.

3. Export Shortcuts for Team Consistency

In a professional studio environment, it is often helpful to have a “Standard Studio Layout” for shortcuts. Use the Export button in the Keyboard Shortcuts editor to create an .ini file. This file can be checked into version control (like Perforce or Git) so that all developers can import the same bindings, ensuring a unified workflow.

4. Handle Binding Conflicts Gracefully

If you attempt to bind a key that is already in use, the editor will show a warning. Unless the existing command is one you never use, it is a best practice to choose a different combination rather than clicking Override. Overriding critical engine shortcuts can lead to the elimination of access to essential editor features like “Save” or “Compile.”

5. Understand Contextual Bindings

Shortcuts are often context-sensitive. A key bound to an action in the Level Editor might perform a different action in the Material Editor. When rebinding, check the “Context” column in the editor to ensure you aren’t accidentally breaking a shortcut in a different sub-editor where you might need it.

6. Use the “Reset to Default” for Troubleshooting

If your editor starts behaving strangely (e.g., keys no longer trigger expected actions), use the Reset to Default button at the top of the Keyboard Shortcuts panel. This is a primary troubleshooting step for the elimination of issues caused by accidental misconfigurations or corrupted local .ini files.

7. Define User-Friendly Command Names

If you are a developer exposing commands to this module, ensure your UI_COMMAND macros use clear, descriptive names and descriptions. The text you provide in the C++ macro is exactly what appears in the InputBindingEditor UI; clear descriptions help users understand what the shortcut actually does.

8. Strategic Elimination of Unused Bindings

If you find yourself accidentally triggering commands via “fat-fingering” keys, use the X (Delete) button next to the binding in the editor. Removing unused or intrusive shortcuts is a best practice for maintaining a clean and intentional development environment, leading to the elimination of accidental deletions or unintended tool activations.