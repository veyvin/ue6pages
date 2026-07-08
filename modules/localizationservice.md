---
layout: default
title: LocalizationService
---

<!-- ai-generation-failed -->

<h1>LocalizationService</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Developer/LocalizationService/LocalizationService.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, EditorFramework, Engine, InputCore, MessageLog, PropertyEditor, Slate, SlateCore, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

ified interface for interacting with external translation providers and managing localization workflows. It functions similarly to the SourceControl module, but specifically handles text and translation assets rather than file versions.

What it is and What it’s used for

Located in Engine/Source/Editor/LocalizationService, this module acts as an abstraction layer between the Unreal Editor and external localization platforms (such as XLOC or OneSky). It allows developers to upload text for translation, check the status of pending translations, and download completed strings directly within the editor.

Primary uses include:

External Provider Integration: Connecting the Localization Dashboard to professional translation services via APIs.
Translation State Tracking: Managing the status of localized text (e.g., New, In-Progress, Completed) across different languages.
Task Automation: Providing a backend for commandlets that automate the export/import of translation data for CI/CD pipelines.
Conflict Resolution: Handling discrepancies between local text changes and remote translations received from external vendors.
Practical Usage Tips and Best Practices
1. Configure via the Localization Dashboard

While the module handles the logic, you should manage your settings via Tools > Localization Dashboard. Select your target and look for the “Localization Service” section. Correct configuration here is essential for the elimination of manual CSV/PO file shuffling between your team and the translators.

2. Utilize String Tables for Stability

The Localization Service works most reliably with String Tables. By centralizing your text into String Table assets, you provide the service with a stable “Key/Namespace” structure. This practice leads to the elimination of “orphan” translations that often occur when text is embedded directly inside rapidly changing Blueprints or levels.

3. Use Commandlets for Nightly Updates

Automate your localization sync using the Localize commandlet via the Unreal Automation Tool (UAT). By scheduling this to run nightly, you ensure the elimination of “translation lag,” where developers are forced to wait for manual imports to see updated text in-game.

4. Verify Culture Codes

The LocalizationService is strict about ISO culture codes (e.g., en-US vs en-GB). Ensure your project cultures match exactly what your external provider expects. Mismatched codes are a leading cause of import failures, and standardizing them early ensures the elimination of data mapping errors.

5. Check “Should Gather” Settings

Not all text needs to be sent to a localization service. In your assets, use the FText::ShouldGatherForLocalization check or the “Culture Invariant” flag for technical strings. This ensures the elimination of unnecessary translation costs by preventing non-user-facing strings from being sent to external vendors.

6. Monitor Translation Status in PIE

Use the Translation Picker (found in the Window menu) while the game is running in the editor. If the LocalizationService is correctly synced, you can inspect UI elements to see their translation status. This is a best practice for the elimination of “untranslated” UI bugs before a build is finalized.

7. Handle Bytecode Assets with Caution

Assets containing bytecode (like Blueprints) can be difficult for localization services to interrogate if not cached correctly. If the service fails to find text, try a “Full Recompile” and “Save All.” This ensures the elimination of stale gather caches, allowing the service to see the most recent text data.

8. Strategic Elimination of Local Overrides

When importing translations from a service, the module may flag conflicts if a local developer has changed the “Source” text. Always treat the localization service as the “Source of Truth” for non-native languages to ensure the elimination of inconsistent translations across different branches of the project.