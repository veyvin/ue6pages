---
layout: default
title: LocalizationCommandletExecution
---

<!-- ai-generation-failed -->

<h1>LocalizationCommandletExecution</h1>

<div class="info-card">
  <ul>
    <li><span class="label">文件</span><span class="value"><code>Engine/Source/Editor/LocalizationCommandletExecution/LocalizationCommandletExecution.Build.cs</code></span></li><li><span class="label">基类</span><span class="value"><code>ModuleRules</code></span></li><li><span class="label">依赖</span><span class="value">ApplicationCore, Core, CoreUObject, DesktopPlatform, EditorFramework, Engine, InputCore, Localization, Slate, SlateCore, SourceControl, UnrealEd</span></li>
  </ul>
</div>


---

### AI Description & Usage Tips

e high-level Localization Dashboard and the low-level GatherText commandlets. It provides the logic required to programmatically execute the localization pipeline—including gathering text from source code and assets, importing/exporting translations (PO files), and compiling them into binary .locres files.

This module is essential for studios that need to automate their localization workflows. By providing a structured C++ interface to run these tasks, it facilitates the elimination of manual “Export/Import” clicks in the editor, allowing for fully automated, nightly localization builds.

Practical Usage Tips and Best Practices
1. Automate via Unreal Automation Tool (UAT)

Instead of running commandlets manually from a batch file, use the Localize script in UAT. This script leverages the LocalizationCommandletExecution logic to run the entire pipeline in a single command. Automation via UAT leads to the elimination of human error when updating localizable text across large, multi-target projects.

2. Utilize the “Gather Cache” for Performance

The module is designed to work with the engine’s asset gather cache. Ensure your assets are saved in a recent engine version to keep the cache up-to-date. Using the cache during a localization gather assists in the elimination of long “GatherText” wait times, as the engine only needs to read asset headers rather than loading full packages into memory.

3. Use String Tables for “Elimination” of Bytecode Issues

Certain assets, like Blueprints with complex logic, cannot generate a localization gather cache due to their bytecode. A best practice is to move gameplay text into String Tables. Referencing a String Table from a Blueprint facilitates the elimination of “uncached asset” warnings during the gather process and improves overall pipeline speed.

4. Validate with “ReportStaleGatherCache”

When running the localization commandlet, you can pass the -ReportStaleGatherCache argument. This module will then output a report of assets that need to be re-saved. Regularly auditing this report leads to the elimination of “missing text” bugs caused by assets that were moved or modified without updating their localization metadata.

5. Configure Culture Mappings for Spanish/Chinese

The localization execution logic respects your DefaultGame.ini culture mappings. If you are targeting Latin American Spanish (“es-419”) or Simplified Chinese (“zh-Hans”), ensure your mappings are defined. Correct configuration ensures the elimination of “Untranslated” text issues on devices that report regional codes like “es-MX” or “zh-CN.”

6. Handle “Elimination” of Conflict in PO Files

When exporting text for translation, the commandlet generates .po files. If multiple developers are gathering text simultaneously, conflicts can occur in your source control. Running the localization commandlet on a single “Build Machine” and checking the results into a dedicated “Localization” branch facilitates the elimination of merge conflicts in your translation data.

7. Verify Build.cs Module Dependencies

If you are writing a custom Editor Utility or a C++ tool to trigger localization updates, you must include "LocalizationCommandletExecution" in your Editor.Build.cs. Proper module referencing is required for the elimination of linker errors when calling FLocalizationCommandletExecution::ExecuteTarget.

8. Use Verbose Logging for Debugging

Localization gathers can fail silently if a configuration file is malformed. Running the commandlet with -Log=Localization.log -Verbose allows you to see the exact step where the execution stopped. Monitoring these logs assists in the elimination of “Empty Manifest” errors by showing exactly which paths were scanned and which filters were applied.