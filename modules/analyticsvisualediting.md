---
layout: default
title: AnalyticsVisualEditing
---

<!-- ai-generation-failed -->

<h1>AnalyticsVisualEditing</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Runtime/Analytics/AnalyticsVisualEditing/AnalyticsVisualEditing.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Analytics, Core, CoreUObject, DeveloperSettings, Engine</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

hat provides the user interface and visual configuration logic for the Analytics system. While the core analytics modules handle the background transmission of data, this module bridges the gap by allowing developers to manage analytics providers, view session metadata, and configure project-level analytics settings through the Unreal Editor UI.

Practical Usage Tips & Best Practices
1. Manage Provider Configurations via Project Settings

The primary role of this module is to populate the Project Settings > Engine > Analytics menu. Instead of manually editing .ini files for every provider, use this visual interface to set your API keys and select your default “Development” and “Release” providers.

2. Dependency Management in Build.cs

Because this module contains Editor-specific UI code, it must never be included in a runtime module. Always place it within an Editor module or wrap it in an Editor target check in your Build.cs to prevent packaging errors.

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AnalyticsVisualEditing");

	}
Copy code
3. Custom Analytics Provider UI

If you are developing a custom analytics provider plugin (e.g., for a proprietary backend), you will use this module to register your provider’s configuration settings. This ensures your custom settings appear natively alongside the built-in providers in the Editor.

4. Verification of Property Metadata

When exposing analytics variables to the Editor, this module respects standard UProperty metadata. Ensure your analytics configuration properties are marked with Config and EditAnywhere so the visual editing system can correctly display and save them to the project’s configuration files.

5. Debugging Session Transitions

Use the visual tools provided by this module to verify how the Editor transitions between “Editor Sessions” and “Game Sessions.” This is critical for ensuring that data like a player’s elimination count is being attributed to the correct session type during Play-In-Editor (PIE) testing.

6. Coordinate with UAnalyticsSettings

The module works closely with the UAnalyticsSettings class. When modifying analytics behavior in C++, use the visual editing menu to verify that your GetMutableDefault<UAnalyticsSettings>() calls are pulling the correct values that you see on screen.

7. Validating Event Flow without Code

For designers, this module provides the necessary UI hooks to ensure that analytics are “Opt-In” or “Opt-Out” according to privacy requirements. Use the Project Settings provided by this module to toggle the bIsAnonymized flags and see how they affect event structure during local testing.

8. Visualizing Elimination Events in Logs

While the module handles configuration, it often interfaces with the Output Log. Use the visual settings to enable “Verbose” logging for analytics. This allows you to see a clear text representation of every event—such as a player elimination—directly in the Editor as it is fired, confirming that the visual configuration is working as intended.