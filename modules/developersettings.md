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

ne designed to expose C++ configuration properties to the Project Settings menu in the Editor. It provides a highly streamlined way to create globally accessible, data-driven settings that are automatically saved to and loaded from .ini configuration files.

Its primary purpose is to allow programmers to create “set and forget” variables—such as API keys, default gameplay constants, or plugin configurations—that designers can easily modify without touching code. By inheriting from UDeveloperSettings, a class automatically handles its own registration with the Editor UI, helping to eliminate the boilerplate code usually required for custom settings menus.

Practical Usage Tips and Best Practices
Inherit from UDeveloperSettings
To create your own settings, derive your class from UDeveloperSettings. This base class includes the necessary logic to map your UPROPERTY members directly to the Project Settings window and the underlying config system, eliminating the need for manual Slate UI coding.
Define the Config Category
Use the config=Game (or Engine, Input, etc.) specifier in the UCLASS macro. This determines which .ini file will store your variables (e.g., DefaultGame.ini). Properly categorizing your settings helps eliminate confusion by keeping gameplay-specific values separate from engine-level configurations.
Organize with GetCategoryName and GetSectionName
Override these virtual functions to control where your settings appear in the Project Settings sidebar. Grouping related settings under a custom category (like your project name) helps developers eliminate time wasted searching through the long list of default engine sections.
Access Data via GetDefault
To retrieve your settings in code, use the GetDefault<UMySettingsClass>() function. This provides a read-only pointer to the “Class Default Object” (CDO) which holds the current configuration, helping to eliminate the overhead of spawning or searching for a settings actor in the world.
Use EditAnywhere for Visibility
Only properties marked with EditAnywhere or EditDefaultsOnly will appear in the Project Settings menu. Ensure your variables are properly decorated with these macros to eliminate the possibility of settings being “hidden” from designers in the Editor.
Leverage Property Metadata
Use metadata like DisplayName, Tooltip, and ConfigRestartRequired=true. The latter is particularly important; it tells the user the editor must be restarted for changes to take effect, helping to eliminate bugs where a developer thinks a setting change didn’t work.
Implement PostEditChangeProperty for Validation
Override this function to validate settings as they are changed in the Editor. For example, if a designer enters an invalid range for a value, you can reset it or show a warning. This proactive validation helps eliminate runtime crashes caused by “bad data” being saved to the config files.
Restrict to Editor/Developer Modules
While the settings themselves can be read at runtime, the registration and UI logic belong in the Developer or Editor modules. Use the DeveloperSettings module dependency in your Build.cs to ensure that setting definitions are correctly handled and eliminated or optimized appropriately during the final packaging process.