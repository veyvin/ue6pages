---
layout: default
title: LocalizationDashboard
---

<!-- ai-generation-failed -->

<h1>LocalizationDashboard</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/LocalizationDashboard/LocalizationDashboard.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">Core, CoreUObject, DesktopPlatform, EditorFramework, Engine, InputCore, InternationalizationSettings, Localization, LocalizationCommandletExecution, LocalizationService, MainFrame, PropertyEditor, SharedSettingsWidgets, Slate, SlateCore, SourceControl, ToolMenus, TranslationEditor, UnrealEd, WorkspaceMenuStructure</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

primary interface for managing a project’s localization pipeline.

Description and Purpose

The module implements the Localization Dashboard tool, accessible via the “Tools” menu. Its primary purpose is to automate the complex workflow of “Gathering” localizable text from source code and assets, “Exporting” that text for translation, and “Compiling” it back into binary .locres files. It provides a centralized hub to define Localization Targets, manage supported cultures (languages), and monitor word counts. By using this dashboard, developers can eliminate the need to manually run commandlets or write custom scripts to synchronize their game’s text with external translation services.

Practical Usage Tips and Best Practices
Organize with Multiple Targets
For large projects, split your text into multiple targets (e.g., “Game,” “Inventory,” “Dialogue”). This allows you to gather and export only the specific sections currently being updated, which helps you eliminate long processing times associated with scanning the entire project.
Set an Accurate Native Culture
The “Native Culture” is the language you author your content in (usually English). Setting this correctly in the dashboard is vital to eliminate “source text” mismatches where the engine cannot determine which version of the text is the original reference.
Automate via Commandlets for CI/CD
While the dashboard is a GUI, it actually generates .ini configurations. Use these files with the GatherText commandlet in your build server (Jenkins/GitHub Actions). Automating this process helps you eliminate human error and ensures translations are always up to date in every build.
Use Portable Object (.po) for External Translation
The dashboard supports exporting to the industry-standard .po format. Use this to send text to professional translation tools (like Poedit or Crowdin). This workflow helps you eliminate the risk of translators accidentally breaking game logic or formatting during the translation process.
Monitor the “Needs Review” Tab
In the Translation Editor (accessed via the Dashboard), pay close attention to the “Needs Review” category. This flag appears when source text has changed but the translation remains old. Checking this regularly helps you eliminate outdated or incorrect translations from appearing in-game.
Validate Loading Policy
Ensure your Localization Target has an appropriate “Loading Policy” (typically set to Game). If this is not configured correctly, the engine will eliminate the translated text from the packaged build, resulting in your game defaulting back to the native language regardless of user settings.
Prefer String Tables for Frequent Changes
For text that changes often, use String Tables alongside the dashboard. The dashboard can gather from String Tables more efficiently than from deep within Blueprint bytecode, helping you eliminate “uncached asset” warnings during the gather phase.
Run “Report Stale Gather Cache”
Periodically run the gather process with the stale cache report enabled. This identifies assets that need to be re-saved to update their localization headers, helping you eliminate “missing text” bugs that occur when the dashboard cannot find text in older assets.