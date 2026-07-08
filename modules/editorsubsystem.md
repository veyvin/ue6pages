---
layout: default
title: EditorSubsystem
---

<!-- ai-generation-failed -->

<h1>EditorSubsystem</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/EditorSubsystem/EditorSubsystem.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

igned to provide managed, singleton-like logic that exists specifically within the lifetime of the Unreal Editor. It allows developers to create tools and systems that run in the background while the editor is open, without needing to modify the engine’s core source code.

What it is and What it’s used for

An UEditorSubsystem is a child of the Subsystem framework. Unlike a UGameInstanceSubsystem, which only exists while the game is running, an Editor Subsystem initializes when the Editor starts and deinitializes when the Editor closes. This makes it the ideal place for “Editor-only” logic.

Primary uses include:

Persistent Tool State: Maintaining data or settings for custom Editor Utility Widgets that need to persist even if the widget is closed and reopened.
Automated Scene Auditing: Running background checks on levels (e.g., finding actors without collision or missing textures) as the designer works.
Viewport & UI Customization: Hooking into editor events (like selecting an actor or saving a level) to trigger custom scripts or automation.
Plugin Architecture: Providing a central API for a plugin that other blueprints or C++ classes can access without needing to find a specific actor in the world.
Practical Usage Tips and Best Practices
1. Avoid Using “Tick”

Subsystems do not have a built-in Tick function by default. To maintain high editor performance, avoid trying to force a tick loop. Instead, use Delegates and Events. Bind to existing editor events (e.g., GEditor->OnActorMoved or FEditorDelegates::PostSaveWorld) to execute your logic only when something actually changes.

2. Access via Blueprint Without Casting

One of the greatest strengths of Editor Subsystems is that they are automatically exposed to Blueprints. You can simply right-click in an Editor Utility Blueprint and search for “Get [YourSubsystemName]”. The node returns the correct type automatically, which leads to the elimination of fragile “Cast To” nodes in your automation scripts.

3. Manage Initialization Order

If your subsystem depends on another system being active, override the Initialize() function. You can use the FSubsystemCollectionBase passed into the function to ensure your dependencies are loaded first. This prevents crashes or null pointer errors during the editor’s complex startup sequence.

4. Use for “Global” Editor Data

If you are building a complex placement tool, store the “Active Settings” (like brush size or snap distance) in an Editor Subsystem. This allows multiple different Editor Utility Widgets or Menu Entries to share the same data, ensuring a consistent experience for the artist across different parts of your toolset.

5. Leverage ShouldCreateSubsystem

You can control exactly when your subsystem is instantiated by overriding ShouldCreateSubsystem. For example, if you have a tool that only works for Mobile projects, you can check the project settings and return false if the project is targeting PC, saving memory and processing power.

6. Clean Up in Deinitialize

Because Editor Subsystems live as long as the editor process, failing to clean up can lead to memory leaks or “ghost” delegates. Always unbind any delegates, clear arrays, and shut down any active background tasks inside the Deinitialize() function to ensure a clean exit.

7. Keep Logic “Editor-Only”

Remember that UEditorSubsystem code is stripped out of “Shipping” builds. Never put gameplay-critical logic here. If a piece of data needs to be accessible during the actual game, it should be in a UGameInstanceSubsystem or UWorldSubsystem instead.

8. Strategic Elimination of Manual Setup

Use Editor Subsystems to automatically register “Startup Objects.” For example, if you want a custom menu to always appear in the Level Editor toolbar, the Subsystem’s Initialize function is the perfect place to register those Slate or Python commands, removing the need for the user to manually trigger a setup script.