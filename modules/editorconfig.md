---
layout: default
title: EditorConfig
---

<!-- ai-generation-failed -->

<h1>EditorConfig</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/EditorConfig/EditorConfig.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorSubsystem, Engine, Json</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

maintain consistency in both the User Interface state and the underlying C++ source code. It ensures that the editor “remembers” your preferences and that your code adheres to Epic’s rigorous standards.

What it is and What it’s used for

The module operates in two distinct areas. First, it provides a metadata framework (EditorConfig) that allows specific UProperties to persist across different engine versions and project streams by saving data to the user’s local AppData. Second, it integrates support for .editorconfig files, which define coding styles (like indentation and naming conventions) that IDEs like Visual Studio or Rider use to format Unreal C++ code.

Primary uses include:

UI State Persistence: Saving “per-user” settings such as favorite properties in the Details panel, folder colors, and view settings in the Content Browser.
Coding Standard Enforcement: Defining rules for PascalCase, indentation, and brace placement so that all developers on a team write code that looks identical.
Cross-Version Migration: Ensuring that your custom editor layouts and “favorited” items remain intact even after upgrading the engine or switching branches.
Metadata Tagging: Allowing C++ developers to mark specific variables for automatic serialization to the local editor config file.
Practical Usage Tips and Best Practices
1. Use the EditorConfig Metadata Flag

If you are building a custom tool or Actor and want a specific property to be “remembered” for the user (even if they don’t save the asset), add the EditorConfig flag to your UPROPERTY. This is ideal for toggle states or preferred default values in custom Editor Utility Widgets.

C++
	UPROPERTY(EditAnywhere, Category="Settings", meta=(EditorConfig))

	bool bShowAdvancedDebugTools;
Copy code
2. Commit a .editorconfig to Source Control

Always include a .editorconfig file in your project’s root directory. This ensures that every developer—regardless of whether they use Visual Studio, Rider, or VS Code—automatically inherits the same tab sizes (usually 4 spaces) and line ending rules. This leads to the elimination of “white-space only” merge conflicts.

3. Standardize Naming Conventions

Use the .editorconfig to enforce Unreal’s naming prefixes (A for Actors, U for Objects, b for Booleans). Modern IDEs will read these rules and provide “Quick Fix” suggestions if a developer forgets a prefix, maintaining the project’s professional standard.

4. Favor Favorites for Complex Actors

The EditorConfig module powers the “Favorites” (star icon) in the Details panel. Encourage your team to favorite deeply nested properties they use frequently. These favorites are stored via the EditorConfig system, meaning they will persist even if the project’s Saved folder is deleted.

5. Keep Local Configs out of Source Control

While you should check in the .editorconfig (the rules), you must never check in the actual generated .ini files that store the user’s personal preferences (usually found in Saved/Config). These are machine-specific and can cause conflicts if shared between different users’ environments.

6. Synchronize View Settings

If you prefer the “Column View” in the Content Browser or specific “Show” flags in the Viewport, the EditorConfig module manages their persistence. If your editor settings feel like they are resetting every time you restart, verify that your user account has write permissions to the Engine’s config directory in Local/UnrealEngine.

7. Leverage for Custom Plugin Settings

When developing plugins for Fab or internal use, use the EditorConfig system to store “Global” plugin states that shouldn’t be saved into the project’s .uproject or .ini files. This keeps the project file clean while allowing the user to have a personalized plugin experience across multiple projects.

8. Strategic Elimination of Config Bloat

Over time, the local editor config can become bloated with settings for deleted assets or old plugins. Periodically cleaning your Local/UnrealEngine/Common/EditorConfig directory can resolve rare UI glitches or sluggishness in the Details panel caused by searching through thousands of stale “favorited” entries.