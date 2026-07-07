---
layout: default
title: DeveloperSettings
---

<!-- ai-generation-failed -->

<h1>DeveloperSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/DeveloperSettings/DeveloperSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, Projects</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

plify the creation of project-wide settings. It centers around the UDeveloperSettings class, which provides a high-level wrapper for the Unreal configuration (.ini) system.

Unlike standard classes, any class inheriting from UDeveloperSettings is automatically discovered and registered by the editor. This allows developers to expose global variables, toggles, and constants to the Project Settings menu without writing custom Slate UI code or manual registration logic.

Practical Usage Tips and Best Practices
1. Always Use ‘defaultconfig’

When declaring your settings class in C++, use the defaultconfig class specifier: UCLASS(Config=Game, defaultconfig).

Best Practice: This ensures that when a designer changes a setting in the editor, the value is written to the project’s DefaultGame.ini rather than a local user file. This allows the change to be committed to source control, eliminating desynchronization issues across the team.
2. Access via the Class Default Object (CDO)

Because UDeveloperSettings act as singletons backed by the config system, you should never instantiate them using NewObject.

Tip: Always access your settings using the GetDefault<T>() function. It is highly optimized and ensures you are reading the current configuration state directly from the CDO, which helps eliminate unnecessary memory allocations.
3. Organize with Category and Section Names

You can control exactly where your settings appear in the Project Settings menu by overriding three virtual functions: GetContainerName(), GetCategoryName(), and GetSectionName().

Action: Use these to group related settings (e.g., “Combat,” “UI,” “Networking”). Proper organization makes it easier for team members to find what they need, eliminating time wasted searching through a flat list of variables.
4. Leverage DisplayName and Tooltips

The UI for DeveloperSettings is generated automatically from your code.

Best Practice: Use the meta=(DisplayName="Readable Name") tag for the class and its properties. Combined with descriptive C++ tooltips, this eliminates the need for external documentation, as the instructions are built directly into the editor interface.
5. Implement Validation in ‘PostEditChangeProperty’

Since settings often drive critical systems, invalid values (like a negative “Gravity Multiplier”) can cause crashes.

Tip: Override PostEditChangeProperty to validate user input. You can clamp values or trigger warnings if a setting is set to an unsafe state. This helps eliminate logic errors before the game is even launched.
6. Use ‘ConfigHierarchyEditable’ for Platform Overrides

For settings that need to be different on Mobile versus PC:

Action: Add meta=(ConfigHierarchyEditable) to your properties. This allows the Project Settings UI to display a “per-platform” override icon, helping you eliminate the need for complex runtime “if-platform” checks in your gameplay code.
7. Keep Logic Out of the Settings Class

The UDeveloperSettings class should strictly be a data container.

Best Practice: Do not include complex gameplay logic or state inside this class. It should only hold the variables. Use your Managers or Subsystems to read these values and perform the actual work. This approach helps eliminate circular dependencies between your core logic and your configuration data.
8. Link to Console Variables (CVars)

You can link a developer setting directly to a CVar using the ConsoleVariable metadata.

Tip: Use UPROPERTY(Config, meta=(ConsoleVariable="MyProject.FeatureEnabled")). This allows the setting to be changed via the ~ console at runtime while remaining visible and editable in the Project Settings menu, eliminating the need for redundant boilerplate code.