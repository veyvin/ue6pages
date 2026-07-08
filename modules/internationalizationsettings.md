---
layout: default
title: InternationalizationSettings
---

<!-- ai-generation-failed -->

<h1>InternationalizationSettings</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/InternationalizationSettings/InternationalizationSettings.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">AppFramework, Core, CoreUObject, Engine, InputCore, Localization, PropertyEditor, Slate, SlateCore</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

at manages the configuration and persistent state of a project’s localization and internationalization preferences. It acts as the bridge between the Localization Dashboard UI and the underlying configuration files (like BaseEditor.ini and DefaultGame.ini).

This module is primarily used to define how the engine handles different languages, regions, and asset groups. It allows developers to specify which cultures are supported, which one is the “native” (development) language, and how internationalization data (ICU) should be packaged. Proper use of this module helps eliminate inconsistencies between developer settings and the final localized player experience.

Practical Usage Tips and Best Practices
Define Asset Group Cultures
Use this module to set up Asset Groups. For example, you can create a group for “Audio” and another for “UI”. This allows a player to play with French text but Japanese audio, helping you eliminate the limitation of forcing a single language across all asset types.
Manage ICU Data Packaging
In the project settings (driven by this module), ensure you select the correct Internationalization Support level (e.g., EFIGS, CJK). Choosing only the necessary regions helps you eliminate megabytes of unused data from your final build, optimizing the installation size.
Set the Native Culture Early
Always define your Native Culture (usually en) at the start of production. This module uses this setting as the “source of truth” for all translations. Changing this late in development can cause the localization gatherer to fail or eliminate existing translation links.
Utilize the ‘Preview Game Language’
The module provides the logic for the “Preview Game Language” setting in the Editor. Use this to quickly swap the editor’s viewport strings to another language. This practice helps you eliminate UI clipping or font-rendering issues before you ever run a standalone build.
Coordinate with the Localization Dashboard
While you can modify these settings via C++ or .ini files, it is best practice to use the Localization Dashboard (which uses this module under the hood). This ensures that your DefaultGame.ini is updated correctly and helps eliminate manual syntax errors in your configuration files.
Configure Font Fallbacks
Use the internationalization settings to define fallback fonts for specific regions (like Chinese or Arabic). This ensures that if your primary font is missing a character, the engine can find a suitable replacement, helping you eliminate the “empty box” or “tofu” characters in your UI.
Automate Settings via Editor Utility Blueprints
You can access internationalization settings through Editor Utility Blueprints to automate project setup for multi-studio collaborations. This ensures that every developer is working with the same culture settings, which helps eliminate “it works on my machine” issues related to text rendering.
Validate Culture Codes
When adding new languages, always use the standard IETF language tags (e.g., es-MX for Mexican Spanish vs. es-ES for Spain). The module relies on these specific codes to map to the correct ICU data; using non-standard codes will eliminate the engine’s ability to format numbers and dates correctly.