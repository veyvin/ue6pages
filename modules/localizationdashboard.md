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

es the Unreal Editor with a centralized interface for managing the end-to-end localization pipeline. It is designed to replace manual commandlet workflows, allowing developers to define Localization Targets, gather text from source code and assets, manage translations, and compile binary localization resources (.locres).

Its primary role is to streamline the “Author-at-Source” approach, where the engine automatically tracks FText properties and LOCTEXT macros, ensuring that every piece of user-facing content can be translated without altering the original source.

Practical Usage Tips & Best Practices
1. Define Explicit Loading Policies

Every Localization Target has a “Loading Policy” (e.g., Game, Engine, Editor, or Always).

Best Practice: Ensure your primary game target is set to Game. If this is not set correctly, the compiled translations will not be loaded in a standalone build. Correct policy management leads to the elimination of “missing translation” bugs in the final packaged product.
2. Utilize the PO Export/Import Workflow

While the dashboard includes a built-in Translation Editor, it lacks advanced features like translation memory.

Tip: Use the Export Text function to generate .po files for use in professional external tools like Poedit, OneSky, or XLOC. Re-importing these files via the dashboard ensures the elimination of formatting errors often introduced by manual text entry.
3. Implement String Tables for High-Frequency Text

Gathering text from thousands of individual Blueprints is resource-intensive because the engine must load each asset into memory.

Best Practice: Use String Tables for common UI elements and dialogue. Since these are treated as a single source of truth, they facilitate the elimination of long “Gather Text” wait times and reduce the performance overhead of the asset-scanning process.
4. Configure Culture Remapping for Regional Variants

Some languages have many regional dialects (e.g., Spanish in Mexico vs. Spain) that might share the same translation.

Tip: Use the Culture Mappings settings in your DefaultGame.ini to point multiple regional codes to a single translation folder (e.g., mapping es-MX to es-419). This results in the elimination of redundant translation files and reduces the overall package size.
5. Leverage the Gather Cache

To speed up localization, Unreal generates a “gather cache” in asset headers when they are saved, preventing the need to load the entire asset during a gather.

Best Practice: If your gather process is slow, run the ReportStaleGatherCache commandlet. Fixing missing or stale caches results in the elimination of unnecessary disk I/O, significantly speeding up the localization iteration loop.
6. Segregate Expansion Content into Separate Targets

Large projects with DLC or expansions shouldn’t keep all text in a single target.

Tip: Create separate Localization Targets for your base game and each expansion. This allows for the elimination of bloated manifest files and ensures that players only download the localization data relevant to the content they own.
7. Proactive “Elimination” of Non-Localizable Text

By default, the engine may gather text you don’t intend to translate, such as debug strings or internal names.

Best Practice: Use the FText::ShouldGatherForLocalization check and set text to Culture Invariant in the Details panel for any strings that should remain universal. This ensures the elimination of “junk” entries in your translation archives, reducing costs for external translation services.
8. Verify with the Translation Editor “Needs Review” Tab

When source text is changed in C++ or a Blueprint, the existing translation is marked as stale.

Tip: Regularly check the Needs Review tab in the Translation Editor. This identifies translations that no longer match the current source text, leading to the elimination of outdated or misleading information being shown to the player.