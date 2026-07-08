---
layout: default
title: EngineSettings
---

<!-- ai-generation-failed -->

<h1>EngineSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/EngineSettings/EngineSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

rlying data structures and logic for global engine-level configurations. It defines the classes responsible for managing how the engine behaves at a fundamental level, including settings for maps and sets, game-specific user data, and general project metadata.

It acts as the programmatic interface for several major categories in the Project Settings menu, allowing developers to query or modify engine-wide defaults (like the startup map or the default game mode) via C++ or Blueprints. This module is essential for the elimination of hard-coded references to global assets and system behaviors.

Practical Usage Tips and Best Practices
1. Use UGameMapsSettings for Level Logic

Use the UGameMapsSettings class to programmatically get or set the default map names (Transition Map, Editor Startup Map, etc.). Accessing these values through the module rather than hard-coded strings leads to the elimination of “Map Not Found” errors when levels are renamed or moved during development.

2. Subclass UGameUserSettings for Player Options

The module provides the base UGameUserSettings class. By creating a custom subclass, you can add game-specific variables (like “Difficulty” or “Colorblind Mode”) that are automatically saved to GameUserSettings.ini. This facilitates the elimination of custom save-system boilerplate for simple player preferences.

3. Access UGeneralProjectSettings for Metadata

If you need to display your game’s version number, project name, or company info in the UI (e.g., in a “Credits” or “About” screen), query the UGeneralProjectSettings. This ensures the elimination of data duplication by pulling directly from the settings defined in the Editor.

4. Configure Default Classes Correctly

Use this module to define default classes for critical systems like the GameSession, ServerStatReplicator, and GameNetworkManager. Properly setting these via the EngineSettings module assists in the elimination of runtime casting errors by ensuring the engine always spawns your specific project overrides.

5. Leverage UConsoleSettings for Developer Tools

The UConsoleSettings class allows you to define auto-complete suggestions and colors for the in-game tilde (~) console. Customizing these for your team leads to the elimination of time wasted typing long, complex console commands during debugging sessions.

6. Optimize Scalability with GameUserSettings

The UGameUserSettings class within this module handles the “Quality Levels” (Resolution Quality, View Distance, etc.). Use the ApplySettings and SaveSettings functions to commit changes to the user’s hardware profile, which is a best practice for the elimination of performance hitches on lower-end devices.

7. Control “Can Tick by Default” Logic

The module contains settings that control whether Blueprint subclasses of Actors or Components can tick by default. Setting these to false at a project-wide level (and enabling them only when needed) is a vital best practice for the elimination of unnecessary CPU overhead and performance bloat.

8. Verify Module Dependencies in Build.cs

When accessing these classes in C++, you must include "EngineSettings" in your PublicDependencyModuleNames. Failing to do so will cause linker errors. Ensuring proper dependency management leads to the elimination of “Unresolved External Symbol” errors during the compilation of your project’s core systems.