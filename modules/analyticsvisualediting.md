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

designed to bridge the gap between analytics data structures and the Unreal Editor UI. It provides specialized Detail Customizations and property visualizers that make it easier for designers to configure and inspect analytics-related assets without digging into raw code or complex JSON strings.

Description

This module is primarily used to enhance the user experience of the Analytics Blueprint Library. It provides the custom UI logic for the “Analytics Attribute” picker and specialized property panels. By using this module, developers can ensure that the attributes and event names sent to analytics providers are consistent, valid, and easily selectable from dropdown menus rather than being prone to manual typing errors.

Practical Usage Tips and Best Practices
1. Dependency Management

Since this is an editor module, it should never be included in your runtime or shipping builds. Ensure it is added to your project’s *.Build.cs only when the target is the Editor:

C#
	if (Target.Type == TargetType.Editor)

	{

	    PrivateDependencyModuleNames.Add("AnalyticsVisualEditing");

	}
Copy code
2. Utilize the Attribute Picker

One of the core features of this module is providing a visual picker for analytics attributes. When creating custom Data Assets for your game’s telemetry, this module allows you to select predefined attribute keys from a list, which helps eliminate typos that could lead to fragmented data in your analytics dashboard.

3. Leverage Detail Customizations

If you are writing a custom C++ class that handles event tracking, the AnalyticsVisualEditing module can be used to register a IDetailCustomization. This allows you to hide complex raw data structures and instead present a clean, organized UI for designers to input event parameters.

4. Validate Event Names in Editor

Use the visual editing tools to enforce naming conventions. The module provides hooks to validate strings in the editor, ensuring that every event name (such as an event triggered upon a player’s elimination) follows a strict format before the project is even compiled or run.

5. Pair with AnalyticsBlueprintLibrary

This module works best when the Analytics Blueprint Library plugin is enabled. While the library provides the “nodes” to record events, AnalyticsVisualEditing provides the “look and feel” of those nodes in the Details panel, making the workflow much more intuitive for non-programmers.

6. Debugging Event Payload Structures

When an analytics event is structured incorrectly, it can be difficult to diagnose. Use the visual inspectors provided by this module to “peek” into the structured data of an analytics object. This helps you verify that the keys and values are paired correctly before they are sent to the provider.

7. Standardize Metadata

Use the module’s UI capabilities to create standardized metadata templates. By providing a visual interface for “Common Attributes” (like Map Name or Build Version), you ensure that every event—from opening a chest to a player elimination—is tagged with the same essential context.

8. Improve Iteration Time

By moving analytics configuration from hard-coded C++ strings to visually editable properties, you allow your design and QA teams to tweak what data is collected during a playtest without requiring a code recompile. This is a best practice for live-service games that need to adapt their telemetry on the fly.